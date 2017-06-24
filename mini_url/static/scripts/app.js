(function(){
    'use strict';

    angular.module('scrumboard', [])
        .controller('ScrumboardController', ScrumboardController, ['$scope', ScrumboardController]);

        function ScrumboardController($scope){
            $scope.add = function(list, title) {
                var card = {
                    title: title
                };

                list.cards.push(card);
            };
            
            $scope.data = [
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

        ];
        }
}());
