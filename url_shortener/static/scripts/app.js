(function(){
    'use strict';

    angular.module('scrumboard', ['ngRoute'])
        .controller('ScrumboardController', ScrumboardController,
        ['$scope', '$http', '$location', ScrumboardController]);

        function ScrumboardController($scope, $http, $location){
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

            $scope.logout = function() {
                $http.get('/auth_api/logout/')
                    .then(function() {
                        $location.url('/login');
                    });
            }

            $scope.data = [];
            $http.get('/scrumboard/lists').then(function(response){
                $scope.data = response.data;
            });

            $scope.sortBy='story_points';
            $scope.reverse=true;
            $scope.showFilters=false;


            /*$scope.data = [
                {
                    name: 'Django',
                    cards: [
                    {
                        title: 'models'
                    },
                    {
                        title: 'views'
                    },
                    {
                        title: 'controllers'
                    }
                ]
            },
            {
                name: 'angular',
                cards : [
                    {
                        title: 'html'
                    },
                    {
                        title: 'binding'
                    }
                ]
            }

        ];*/
        }
}());
