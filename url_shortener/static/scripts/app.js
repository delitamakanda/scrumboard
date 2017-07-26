(function(){
    'use strict';

    angular.module('scrumboard', ['ngRoute'])
        .controller('ScrumboardController', ScrumboardController,
        ['$scope', '$http', '$location', 'Login', ScrumboardController]);

        function ScrumboardController($scope, $http, $location, Login){
            //add card to the list
            $scope.add = function(list, title) {
                var card = {
                    list: list.id,
                    title: title,
                };
                $http.post('/scrumboard/cards/', card)
                    .then(function(response){
                        list.cards.push(response.data);
                    }, function(){
                        console.log('error');
                    });
            };
            
            //create a new list
            $scope.create = function() {
                var data = {
                    name: $scope.name,
                };

                $http.post('/scrumboard/lists/', data)
                    .then(function(response) {
                        $location.url('/success')
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

            // fetch all of your lists and cards
            $http.get('/scrumboard/lists').then(function(response){
                $scope.data = response.data;
            });

        }
}());
