var app = angular.module('home', ['ngMaterial', 'ngMessages']);
app.controller('homeController', function($http, $scope) {
	var self = this;
    
    self.displayJournal = function(journal) {
        return journal.name + ' (' + journal.short + ')';
    };
    
    self.findOr = function(query, field1, field2) {
        var lowerQuery = angular.lowercase(query);
        return function(item) {
            var target1 = field1 in item ? item[field1].toLowerCase().includes(lowerQuery) : false;
            var target2 = field2 in item ? item[field2].toLowerCase().includes(lowerQuery) : false;
            return target1 || target2;
        }
    };

    self.searchJournals = function(query) {
        return query ? self.journals.filter(self.findOr(query, 'name', 'short')) : self.journals;
    };
    
    $http.get('/journals').then(function(data) {
        self.journals = data.data;
    });
});