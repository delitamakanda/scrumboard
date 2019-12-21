(function(){
    'use strict';

    angular.module('scrumboard')
        .controller('TodoController', TodoController,
        ['$scope', '$http', '$location', '$window', 'Login', 'Todos', TodoController]);

        function TodoController($scope, $http, $location, $window, Login, Todos) {

            // modelOptions
            $scope.modelOptions = {
                debounce: 500
            };

            // show dropdown menu
            $scope.showDropdown = function() {
                $scope.dropDownOpen = true;
            }

            $scope.hideDropdown = function() {
                $scope.dropDownOpen = false;
            }

            // show user settings
            $scope.showUserBoard = function() {
                $scope.userBoard = true;
            }

            $scope.hideUserBoard = function() {
                $scope.userBoard = false;
                $scope.dropDownOpen = false;
            }
            
            Login.redirectedIfNotLoggedIn();
            $scope.userData = [];
            $scope.logout = Login.logout;
            $scope.sidebarOpen = true;
            $scope.dropDownOpen = false;
            $scope.userBoard = false;
            $scope.currentUser = JSON.parse(localStorage.currentUser);

            // fetch user by id
            $http.get('/kanbanboard/users/' + $scope.currentUser.id).then(function(response){
                $scope.userData = response.data;
            });


            // update User
            $scope.updateUser = function() {

                return $http.patch(
                    '/kanbanboard/users/' + $scope.currentUser.id + '/',
                    $scope.userData
                );
            }

            // Todos
            $scope.newTodo = {};
            $scope.todoCompleted = [];

            $scope.addTodo = function() {
                Todos.createTodo($scope.newTodo)
                    .then(function(res) {
                        $scope.todos.push(res.data);
                        $scope.newTodo.name = '';
                        $scope.newTodo.text = '';
                    }, function(error) {
                        console.log('error', error);
                    });
            };

            $scope.toggleCompleted = function(todo) {
                if (todo.complete) {
                    $scope.todoCompleted.push(todo);
                } else {
                    $scope.todoCompleted.pop(todo)
                }
                Todos.updateTodo(todo);
            }

            $scope.deletedTodo = function(id) {
                Todos.deleteTodo(id);
                $scope.todoCompleted.splice(-1, 1);
                $scope.todos = $scope.todos.filter(function(todo) {
                    return todo.id !== id;
                })
            }

            Todos.getTodos().then(function(res) {
                res.data.find(r => {
                    if (r.complete) {
                        $scope.todoCompleted.push(r); 
                    }
                });
                return $scope.todos = res.data;
            });
        }
}());
