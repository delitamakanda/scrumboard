(function () {
    'use strict';

    angular.module('scrumboard')
        .service('Login', ['$http', '$location', Login]);

    function Login($http, $location) {
        this.login = login;
        this.isLoggedIn = isLoggedIn;
        this.logout = logout;
        this.redirectedIfNotLoggedIn = redirectedIfNotLoggedIn;

        function login(credentials) {
            return $http.post('/auth_api/login/', credentials)
                .then(function(response){
                    localStorage.currentUser = JSON.stringify(response.data);
                });
        }

        function isLoggedIn() {
            return !!localStorage.currentUser;
        }

        function logout() {
            delete localStorage.currentUser;
            $http.get('/auth_api/logout/').then(function() {
                $location.url('/login');
            });
        }

        function redirectedIfNotLoggedIn() {
            if ( !isLoggedIn() ) {
                $location.url('/login');
            }
        }
        
    }
})();
