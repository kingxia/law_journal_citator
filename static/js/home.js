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
        'orderBy': 'year',
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
        'case': self.fieldSort('case'),
        'jurisdiction': self.fieldSort(self.generateJurisdictionFunction()),
        'year': self.fieldSort('year'),
        '-cite': self.fieldSort(self.generateCiteFunction(), false),
        '-case': self.fieldSort('case', false),
        '-jurisdiction': self.fieldSort(self.generateJurisdictionFunction(), false),
        '-year': self.fieldSort('year', false),
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
    
    self.search = function() {
        searchOptions = {};
        if (self.journal) searchOptions['journalId'] = [self.journal.id];
        if (self.jurisdiction) searchOptions['jurisdiction'] = [self.jurisdiction.id];
        if (self.minYear) searchOptions['yearMin'] = self.minYear;
        if (self.maxYear) searchOptions['yearMax'] = self.maxYear;
        
        $http.post('/cites', searchOptions).then(function(data) {
            self.searchResults = data.data.map(function(arr) {
                return {
                    'id': arr[0],
                    'journal': arr[1],
                    'volume': arr[2],
                    'page': arr[3],
                    'case': arr[4],
                    'jurisdiction': arr[5],
                    'year': arr[6],
                    'startPos': arr[7],
                    'endPos': arr[8],
                };
            });
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
});