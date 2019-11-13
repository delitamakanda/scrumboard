(function(){
    'use strict';

    angular.module('scrumboard', ['ngRoute'])
        .controller('ScrumboardController', ScrumboardController,
        ['$scope', '$http', '$location', '$window', 'Login', 'Todos', ScrumboardController]);

        function ScrumboardController($scope, $http, $location, $window, Login, Todos){

            // add card to the list
            $scope.add = function(list, title) {
                var card = {
                    list: list.id,
                    title: title,
                };
                $http.post('/kanbanboard/cards/', card)
                    .then(function(response){
                        list.cards.push(response.data);
                    }, function(){
                        console.log('error');
                    });
            };

            // create a new list
            $scope.create = function() {
                var data = {
                    name: $scope.name,
                };

                $http.post('/kanbanboard/lists/', data)
                    .then(function(response) {
                        $scope.data.push(response.data)
                    }, function(){
                        console.log('error');
                    });
            };

            // delete a list
            $scope.confirmDelete = function(list) {
                var r = confirm('Are you sure to delete this list ?');
                if (r == true) {
                    $http.delete('/kanbanboard/lists/' + list.id)
                        .then(function(){
                            $scope.data.splice(list, 1)
                        });
                }
            };

            // modelOptions
            $scope.modelOptions = {
                debounce: 500
            };


            //show hide popin
            $scope.addBoard = function(key, index) {
                $scope.showAddBoard=true;
            }

            $scope.hideBoard = function() {
                $scope.showAddBoard=false;
            }

            Login.redirectedIfNotLoggedIn();
            $scope.data = [];
            $scope.userData = [];
            $scope.logout = Login.logout;
            $scope.sortBy='story_points';
            $scope.reverse=true;
            $scope.showFilters=false;
            $scope.showAddBoard=false;
            $scope.currentUser = JSON.parse(localStorage.currentUser);

            // fetch all of your lists and cards
            $http.get('/kanbanboard/lists').then(function(response){
                $scope.data = response.data;
            });

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
        }
}());
