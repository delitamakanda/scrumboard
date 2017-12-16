(function () {
    'use strict';

    angular.module('scrumboard')
        .service('Todos', ['$http', '$location', Todos]);

    function Todos($http, $location) {
        this.getTodos = getTodos;
        this.updateTodo = updateTodo;
        this.deleteTodo = deleteTodo;
        this.createTodo = createTodo;

        function getTodos() {
            return $http.get('/scrumboard/todos');
        }

        function updateTodo(updatedTodo) {
            return $http.put('/scrumboard/todos/' + updatedTodo.id, updatedTodo);
        }

        function deleteTodo(id) {
            return $http.delete('/scrumboard/todos/' + id + '/');
        }

        function createTodo(newTodo) {
            return $http.post('/scrumboard/todos/', newTodo)
        }
    }
})();
