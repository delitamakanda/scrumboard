(function () {
    'use strict';

    angular.module('scrumboard')
        .service('Signup', ['$http', '$location', Signup]);

    function Signup($http, $location) {
        this.signup = signup;

        function signup(credentials) {
            return $http.post('/auth_api/signup/', credentials)
                .then(function(response){
                    localStorage.currentUser = JSON.stringify(response.data);
                });
        }

    }
})();
