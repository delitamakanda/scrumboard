(function() {
    'use strict';

    angular
        .module('scrumboard')
        .controller('LoginController', ['$scope', '$http', '$location', 'Login', LoginController]);

    function LoginController($scope, $http, $location, Login) {
        $scope.login = function () {
            Login.login($scope.user)
                .then(function() {
                    $location.url('/')
                },
                function() {
                    $scope.login_error="Invalid username/password combination";
                });
        }

        $scope.signup = function() {

            var data = {
                username: $scope.username,
                password: $scope.password
            };

            $http.post('/auth_api/register/', data)
                .then(function(response) {
                    $location.url('/login')
                }, function(){
                    //console.log('error');
                    $scope.signup_error="An error occurred or username already taken.";
                });

        }

        if (Login.isLoggedIn()) {
            $location.url('/');
        }
    }
})();
