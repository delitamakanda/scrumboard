(function() {
    'use strict';

    angular
        .module('scrumboard')
        .controller('SignupController', ['$scope', '$http', '$location', SignupController]);

    function SignupController($scope, $http, $location) {
        
        $scope.signup = function() {

            var data = {
                username: $scope.username,
                password: $scope.password
            };

            $http.post('/auth_api/register/', data)
                .then(function(response) {
                    $location.url('/login');
                }, function(){
                    //console.log('error');
                    $scope.signup_error="An error occurred or username already taken.";
                });

        }
    }
})();
