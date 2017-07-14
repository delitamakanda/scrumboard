(function(){
    'use strict';

    angular.module('scrumboard', ['ngRoute'])
        .controller('ScrumboardController', ScrumboardController,
        ['$scope', '$http', 'Login', ScrumboardController]);

        function ScrumboardController($scope, $http, Login){
            $scope.add = function(list, title) {
                var card = {
                    list: list.id,
                    title: title,
                };
                $http.post('/scrumboard/cards/', card)
                    .then(function(response){
                        $location.url('/')
                    }, function(){
                        console.log('error');
                    });
            };

            $scope.create = function() {
                var data = {
                    name: $scope.name,
                    user: $scope.user
                };
                $http.post('/scrumboard/lists/', data)
                    .then(function(response) {
                        console.log(response,'yes')
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
