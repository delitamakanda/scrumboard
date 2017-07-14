(function() {
    'use strict';

    angular
        .module('scrumboard')
        .controller('SignupController', ['$scope', '$location', 'Signup', SignupController]);

    function SignupController($scope, $location, Signup) {
        $scope.signup = function () {
            Signup.signup($scope.user)
                .then(function() {
                    $location.url('/')
                },
                function() {
                    $scope.signup_error="Username already taken!";
                });
        }

    }
})();
