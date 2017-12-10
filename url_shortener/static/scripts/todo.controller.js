(function(){
    'use strict';

    angular.module('scrumboard')
        .controller('TodoController', TodoController,
        ['$scope', '$http', '$location', 'Login', TodoController]);

        function TodoController($scope, $http, $location, Login){

            Login.redirectedIfNotLoggedIn();
            $scope.data = [];

            // fetch all of your lists and cards
            $http.get('/scrumboard/todos').then(function(response){
                $scope.data = response.data;
                console.log($scope.data);
            });

        }
}());
