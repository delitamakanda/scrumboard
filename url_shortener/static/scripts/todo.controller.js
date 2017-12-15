(function(){
    'use strict';

    angular.module('scrumboard')
        .controller('TodoController', TodoController,
        ['$scope', '$http', '$location', '$window', 'Login', TodoController]);

        function TodoController($scope, $http, $location, $window, Login){
            
            $scope.createTask = function() {
                var todo = {
                    name: $scope.name,
                    text: $scope.text,
                };
                
                $http.post('/scrumboard/todos/', todo)
                    .then(function(response) {
                        $location.url('/todo');
                        $window.location.reload();
                    }, function(){
                        console.log('error');
                    });
            };
            
            // modelOptions
            $scope.modelOptions = {
                debounce: 500
            };
            
            Login.redirectedIfNotLoggedIn();
            $scope.data = [];

            // fetch all of your lists and cards
            $http.get('/scrumboard/todos').then(function(response){
                $scope.data = response.data;
                console.log($scope.data);
            });

        }
}());
