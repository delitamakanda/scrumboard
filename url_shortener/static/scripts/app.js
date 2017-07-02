(function(){
    'use strict';

    angular.module('scrumboard', ['ngRoute'])
        .controller('ScrumboardController', ScrumboardController,
        ['$scope', '$http', 'Login', ScrumboardController]);

        function ScrumboardController($scope, $http, Login){
            $scope.add = function(list, title) {
                var card = {
                    list: list.id,
                    title: title
                };
                $http.post('/scrumboard/cards/', card)
                    .then(function(response){
                        list.cards.push(response.data);
                    }, function(){
                        console.log('error');
                    });
            };

            Login.redirectedIfNotLoggedIn();
            $scope.data = [];
            $scope.logout = Login.logout;
            $scope.sortBy='story_points';
            $scope.reverse=true;
            $scope.showFilters=false;

            $http.get('/scrumboard/lists').then(function(response){
                $scope.data = response.data;
            });

        }
}());
