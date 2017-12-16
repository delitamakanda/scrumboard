(function(){
    'use strict';

    angular
        .module('scrumboard')
        .controller('TodoController', ['$scope', '$http', '$location', '$window', 'Login', 'Todos', TodoController]);

    function TodoController($scope, $http, $location, $window, Login, Todos){
        $scope.newTodo = {};

        $scope.addTodo = function() {
            Todos.createTodo($scope.newTodo)
                .then(function(res) {
                    $location.url('/todo');
                }, function() {
                    console.log('error');
                });
        };

        $scope.toggleCompleted = function(todo) {
            Todos.updateTodo(todo);
        }

        $scope.deletedTodo = function(id) {
            Todos.deleteTodo(id);
            $scope.todos = $scope.todos.filter(function(todo) {
                return todo.id !== id;
            })
        }

        Todos.getTodos().then(function(res) {
            return $scope.todos = res.data;
        });

        Login.redirectedIfNotLoggedIn();
    }
}());
