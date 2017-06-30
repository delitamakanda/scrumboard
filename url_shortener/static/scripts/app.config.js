(function() {
    'use strict';

    angular.module('scrumboard').run(['$http', run]);

    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }
})();
