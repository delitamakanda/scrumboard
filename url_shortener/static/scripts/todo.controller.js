(function(){
    'use strict';

    angular
        .module('scrumboard')
        .controller('TodoController', ['$scope', '$http', '$location', '$window', 'Login', TodoController]);

    function TodoController($scope, $http, $location, $window, Login){
        $scope.createTask = function() {
            var data = {
                name: $scope.name,
                text: $scope.text,
                user: $scope.currentUser.id,

            };

            $http.post('/scrumboard/todos/', data)
                .then(function(response) {
                    $location.url('/todo');
                    $window.location.reload();
                }, function(){
                    console.log('error');
                });
        };

        Login.redirectedIfNotLoggedIn();
        $scope.data = [];
        $scope.currentUser = JSON.parse(localStorage.currentUser);


        // fetch all of your lists and cards
        $http.get('/scrumboard/todos').then(function(response){
            $scope.data = response.data;
        });

    }
}());
