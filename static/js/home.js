var app = angular.module('home', ['ngMaterial', 'ngMessages', 'md.data.table', 'ngRoute']);
app.controller('homeController', function($http, $scope) {
	var self = this;
    
    self.canSearch = function() {
        return self.journal != undefined ||
            self.jurisdiction != undefined ||
            (self.minYear != undefined && self.minYear > 0) ||
            (self.maxYear != undefined && self.maxYear > 0);
    };
    
    self.tableSelected = [];
    self.tableOptions = {
        'rowsPerPage': 10,
        'rowOptions': [10, 20, 50, 100],
        'page': 1,
    };
    
    self.fieldSort = function(s, sortAsc=true) {
        return function(left, right) {
            lElement = sortAsc ? left : right;
            rElement = sortAsc ? right : left;
            
            lValue = typeof s === 'function' ? s(lElement) : lElement[s];
            rValue = typeof s === 'function' ? s(rElement) : rElement[s];
            
            if (typeof lValue === 'string') return lValue.localeCompare(rValue);
            return lValue - rValue;
        };
    };
    
    self.generateJurisdictionFunction = function() {
        return function(r) {
            return self.jurisdictionIdToName(r.jurisdiction);
        };
    };
    
    self.generateCiteFunction = function() {
        return function(r) {
            return self.generateCite(r);
        };
    };
    
    self.tableSorts = {
        'cite': self.fieldSort(self.generateCiteFunction()),
        'case': self.fieldSort('caseName'),
        'jurisdiction': self.fieldSort(self.generateJurisdictionFunction()),
        'year': self.fieldSort('year'),
        'citeCount': self.fieldSort('citeCount'),
        'caseCount': self.fieldSort('caseCount'),
        'jurisdictionCount': self.fieldSort('jurisdictionCount'),
        'journalCount': self.fieldSort('journalCount'),
        'yearCount': self.fieldSort('yearCount'),
        '-cite': self.fieldSort(self.generateCiteFunction(), false),
        '-case': self.fieldSort('caseName', false),
        '-jurisdiction': self.fieldSort(self.generateJurisdictionFunction(), false),
        '-year': self.fieldSort('year', false),
        '-citeCount': self.fieldSort('citeCount', false),
        '-caseCount': self.fieldSort('caseCount', false),
        '-jurisdictionCount': self.fieldSort('jurisdictionCount', false),
        '-journalCount': self.fieldSort('journalCount', false),
        '-yearCount': self.fieldSort('yearCount', false),
    };
    
    self.updateSearchResults = function() {
        self.lastestSearchResults = Array.from(self.searchResults);
        self.lastestSearchResults.sort(self.tableSorts[self.tableOptions.orderBy]);
        self.lastestSearchResults = self.lastestSearchResults.slice(
            self.tableOptions.rowsPerPage * (self.tableOptions.page - 1),
            self.tableOptions.rowsPerPage * self.tableOptions.page);
    };
    
    self.displayJournal = function(journal) {
        return journal.name + ' (' + journal.short + ')';
    };
    
    self.generateCite = function(r) {
        return r.volume + ' ' + self.journalsById[r.journal].short + ' ' + r.page;
    };
    
    self.jurisdictionIdToName = function(id) {
        return self.jurisdictionsById[id].name_long;
    };
    
    self.find = function(query, field) {
        var lowerQuery = angular.lowercase(query);
        return function(item) {
            return field in item ? item[field].toLowerCase().includes(lowerQuery) : false;
        };
    };
    
    self.findOr = function(query, field1, field2) {
        var lowerQuery = angular.lowercase(query);
        return function(item) {
            var target1 = field1 in item ? item[field1].toLowerCase().includes(lowerQuery) : false;
            var target2 = field2 in item ? item[field2].toLowerCase().includes(lowerQuery) : false;
            return target1 || target2;
        };
    };

    self.searchJournals = function(query) {
        return query ? self.journals.filter(self.findOr(query, 'name', 'short')) : self.journals;
    };
    
    self.searchJurisdictions = function(query) {
        return query ? self.jurisdictions.filter(self.find(query, 'name_long')) : self.jurisdictions;
    };
    
    self.searchGroups = function(query) {
        return query ? self.groupOptions.filter(function(s) {
            return s.includes(angular.lowercase(query));
        }) : self.groupOptions;
    };
    
    self.groupBy = null;
    self.groupOptions = ['case', 'cite', 'jurisdiction', 'year'];
    self.toProperCase = function(s) {
        if (s === undefined) return '';
        return s.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
    }
    
    self.search = function() {
        searchOptions = {};
        if (self.journal) searchOptions['journalId'] = [self.journal.id];
        if (self.jurisdiction) searchOptions['jurisdiction'] = [self.jurisdiction.id];
        if (self.volume) searchOptions['volume'] = [self.volume];
        if (self.page) searchOptions['page'] = [self.page];
        if (self.minYear) searchOptions['yearMin'] = self.minYear;
        if (self.maxYear) searchOptions['yearMax'] = self.maxYear;
        if (self.groupBy) searchOptions['groupBy'] = self.groupBy;
        self.searchGroupBy = self.groupBy;
        delete self.searchResults;
        delete self.latestSearchResults;
        delete self.searchError;
        
        $http.post('/cites', searchOptions).then(function(data) {
            self.searchResults = data.data.map(self.resultMapper[self.searchGroupBy]);
            self.lastestSearchResults = self.searchResults;
        }).catch(function(error) {
            self.searchError = error;
        });
    };
    
    $http.get('/journals').then(function(data) {
        self.journals = data.data;
        self.journalsById = {};
        for(i = 0; i < data.data.length; i++) {
            self.journalsById[data.data[i].id] = data.data[i];
        }
    });
    
    const CASELAW_API = 'https://api.case.law/v1/';
    $http.get(CASELAW_API + 'jurisdictions/').then(function(data) {
        self.jurisdictions = data.data.results;
        self.jurisdictionsById = {};
        for(i = 0; i < data.data.results.length; i++) {
            self.jurisdictionsById[data.data.results[i].id] = data.data.results[i];
        }
    });
    
    self.noGroupBy = function(arr) {
        return {
            'id': arr[0],
            'journal': arr[1],
            'volume': arr[2],
            'page': arr[3],
            'caseId': arr[4],
            'caseName': arr[5],
            'jurisdiction': arr[6],
            'year': arr[7],
            'startPos': arr[8],
            'endPos': arr[9],
            'url': arr[10],
        };
    };
    
    self.groupByCase = function(arr) {
        return {
            'caseId': arr[0],
            'caseName': arr[1],
            'jurisdiction': arr[2],
            'year': arr[3],
            'citeCount': arr[4],
            'journalCount': arr[5],
            'url': arr[6],
        };
    };
    
    self.groupByCite = function(arr) {
        return {
            'volume': arr[0],
            'page': arr[1],
            'journal': arr[2],
            'citeCount': arr[3],
            'caseCount': arr[4],
            'jurisdictionCount': arr[5],
            'yearCount': arr[6],
            'url': arr[7],
        };
    };
    
    self.groupByJurisdiction = function(arr) {
        return {
            'jurisdiction': arr[0],
            'citeCount': arr[1],
            'journalCount': arr[2],
            'caseCount': arr[3],
            'yearCount': arr[4],
            'url': arr[5],
        };
    };
    
    self.groupByYear = function(arr) {
        return {
            'year': arr[0],
            'citeCount': arr[1],
            'journalCount': arr[2],
            'caseCount': arr[3],
            'jurisdictionCount': arr[4],
            'url': arr[5],
        };
    };
    
    self.resultMapper = {
        null: self.noGroupBy,
        'case': self.groupByCase,
        'cite': self.groupByCite,
        'jurisdiction': self.groupByJurisdiction,
        'year': self.groupByYear,
    };
    
    self.showColumn = function(s) {
        switch(s) {
            case 'cite':
                return self.searchGroupBy == null || self.searchGroupBy == 'cite';
            case 'case':
                return self.searchGroupBy == null || self.searchGroupBy == 'case';
            case 'jurisdiction':
                return self.searchGroupBy == null || self.searchGroupBy == 'case' || self.searchGroupBy == 'jurisdiction';
            case 'year':
                return self.searchGroupBy == null || self.searchGroupBy == 'case' || self.searchGroupBy == 'year';
            case 'position':
                return self.searchGroupBy == null;
            case 'citeCount':
                return self.searchGroupBy != null;
            case 'journalCount':
                return self.searchGroupBy == 'jurisdiction' || self.searchGroupBy == 'case' || self.searchGroupBy == 'year';
            case 'caseCount':
                return self.searchGroupBy == 'jurisdiction' || self.searchGroupBy == 'cite' || self.searchGroupBy == 'year';
            case 'jurisdictionCount':
                return self.searchGroupBy == 'year' || self.searchGroupBy == 'cite';
            case 'yearCount':
                return self.searchGroupBy == 'jurisdiction' || self.searchGroupBy == 'cite';
        }
    };
});