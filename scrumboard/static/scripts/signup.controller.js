(function() {
    'use strict';

    angular
        .module('scrumboard')
        .controller('SignupController', ['$scope', '$http', '$location', 'Login', SignupController]);

    function SignupController($scope, $http, $location, Login) {
        
        $scope.signup = function() {

            var data = {
                username: $scope.username,
                password: $scope.password
            };

            $http.post('/auth_api/register/', data)
                .then(function(response) {
                    Login.login(data)
                        .then(function() {
                            $location.url('/');
                        });
                }, function(){
                    //console.log('error');
                    $scope.signup_error="An error occurred or username already taken.";
                });

        }
    }
})();
