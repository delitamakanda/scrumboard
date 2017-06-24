(function(){
    'use strict';

    angular.module('scrumboard', [])
        .controller('ScrumboardController', ScrumboardController, ['$scope', ScrumboardController]);

        function ScrumboardController($scope){
            $scope.person = {
                name:'Delita',
                age: 29
            };
        }
}());
