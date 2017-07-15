(function() {
    'use strict';

    angular.module('scrumboard')
        .config(['$routeProvider', config])
        .run(['$http', run]);

    function config($routeProvider) {

        $routeProvider
            .when('/', {
                templateUrl: '/static/components/scrumboard.html',
                controller: 'ScrumboardController'
            })
            .when('/login', {
                templateUrl: '/static/components/login.html',
                controller: 'LoginController'
            })
            .when('/signup', {
                templateUrl: '/static/components/signup.html',
                controller: 'LoginController'
            })
            .when('/success', {
                templateUrl: '/static/components/success.html',
                controller: 'ScrumboardController'
            })
            .otherwise('/')
    }

    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }
})();
