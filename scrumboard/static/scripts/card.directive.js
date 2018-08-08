(function(){
    'use strict';

    angular.module('scrumboard')
        .directive('scrumboardCard', CardDirective);

    function CardDirective() {
        return {
            templateUrl: '/static/components/card.html',
            restrict: 'E',
            controller: ['$scope', '$http', function($scope, $http) {
                var url = 'scrumboard/cards/' + $scope.card.id + '/';
                $scope.destList = $scope.list;

                $scope.update = function() {
                    return $http.put(
                        url,
                        $scope.card
                    );
                };


                function removeCardFromList(card, list) {
                    var cards = list.cards;
                    cards.splice(
                        cards.indexOf(card), 1
                    );
                }

                $scope.delete = function() {
                    $http.delete(url).then(
                        function() {
                            removeCardFromList($scope.card, $scope.list)
                        }
                    );
                };

                $scope.modelOptions = {
                    debounce: 500
                };

                $scope.move = function() {
                    if ($scope.destList === undefined) {
                        return;
                    }
                    $scope.card.list = $scope.destList.id;
                    $scope.update().then(function() {
                        {
                            removeCardFromList($scope.card, $scope.list);
                            $scope.destList.cards.push($scope.card);
                        }
                    });
                };
            }]
        };
    }
})();
