(function(){
    'use strict';

    angular.module('scrumboard')
        .directive('scrumboardCard', CardDirective);

    function CardDirective() {
        return {
            templateUrl: '/static/scrumboard/card.html',
            restrict: 'E'
        };
    }
})();
