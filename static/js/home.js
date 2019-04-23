var app = angular.module('home', ['ngMaterial', 'ngMessages']);
app.controller('homeController', function($http, $scope) {
	var self = this;
    
    self.displayJournal = function(journal) {
        return journal.name + ' (' + journal.short + ')';
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
        if (self.minYear) searchOptions['minYear'] = self.minYear;
        if (self.maxYear) searchOptions['maxYear'] = self.maxYear;
        
        $http.post('/cites', searchOptions).then(function(data) {
            self.queryResults = data.data;
        }, function(error) {
            self.queryError = error;
        });
    };
    
    $http.get('/journals').then(function(data) {
        self.journals = data.data;
    });
    
    const CASELAW_API = 'https://api.case.law/v1/';
    $http.get(CASELAW_API + 'jurisdictions/').then(function(data) {
        self.jurisdictions = data.data.results;
    });
});