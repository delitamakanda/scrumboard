(function(){
    'use strict';

    angular.module('scrumboard', ['ngRoute'])
        .controller('ScrumboardController', ScrumboardController,
        ['$scope', '$http', '$location', '$window', 'Login', ScrumboardController]);

        function ScrumboardController($scope, $http, $location, $window, Login){
            //add card to the list
            $scope.add = function(list, title) {
                var card = {
                    list: list.id,
                    title: title,
                };
                $http.post('/scrumboard/cards/', card)
                    .then(function(response){
                        list.cards.push(response.data);
                    }, function(){
                        console.log('error');
                    });
            };

            //update User
            $scope.updateUser = function() {
                localStorage.setItem('currentUser', JSON.stringify({
                    username: document.getElementById("username").value,
                    first_name: document.getElementById("first_name").value,
                    last_name: document.getElementById("last_name").value,
                    email: document.getElementById("email").value,
                 }));

                 $scope.currentUser = JSON.parse(localStorage.getItem('currentUser'));

                return $http.patch(
                    '/scrumboard/users/' + $scope.currentUser.id + '/',
                    $scope.currentUser
                );
            }

            //create a new list
            $scope.create = function() {
                var data = {
                    name: $scope.name,
                };

                $http.post('/scrumboard/lists/', data)
                    .then(function(response) {
                        $location.url('/');
                        $window.location.reload();
                    }, function(){
                        console.log('error');
                    });
            };


            //delete list
            $scope.confirmDelete = function(list) {
                var r = confirm('Are you sure to delete this card ?');
                if (r == true) {
                    $http.delete('/scrumboard/lists/' + list.id)
                        .then(function(response, status, headers, config){
                            var index = $scope.data.indexOf(list);
                            $scope.data.splice(index, 1);
                            $window.location.reload();
                        }, function(response, error) {
                            console.log(error);
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
            $scope.logout = Login.logout;
            $scope.sortBy='story_points';
            $scope.reverse=true;
            $scope.showFilters=false;
            $scope.showAddBoard=false;
            $scope.currentUser = JSON.parse(localStorage.currentUser);

            // fetch all of your lists and cards
            $http.get('/scrumboard/lists').then(function(response){
                $scope.data = response.data;
            });


        }
}());
