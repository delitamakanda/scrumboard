(function(){
    'use strict';

    angular.module('scrumboard')
        .controller('TodoController', TodoController,
        ['$scope', '$http', '$location', 'Login', TodoController]);

        function TodoController($scope, $http, $location, Login){
            
            $scope.createTask = function() {
                var data = {
                    name: $scope.name,
                };
                
                $http.post('/scrumboard/todos/', data)
                    .then(function(response) {
                        $location.url('/todos');
                        $window.location.reload();
                    }, function(){
                        console.log('error');
                    });
            }
            
            Login.redirectedIfNotLoggedIn();
            $scope.data = [];

            // fetch all of your lists and cards
            $http.get('/scrumboard/todos').then(function(response){
                $scope.data = response.data;
                console.log($scope.data);
            });

        }
}());
