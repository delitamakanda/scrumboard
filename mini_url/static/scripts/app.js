(function(){
    'use strict';

    angular.module('scrumboard', [])
        .controller('ScrumboardController', ScrumboardController,
        ['$scope', '$http', ScrumboardController]);

        function ScrumboardController($scope, $http){
            $scope.add = function(list, title) {
                var card = {
                    title: title
                };

                list.cards.push(card);
            };

            $scope.data = [];
            $http.get('/lists').then(function(response){
                $scope.data = response.data;
            });

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
