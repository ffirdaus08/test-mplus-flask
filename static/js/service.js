'use strict';

angular.module('booksApp', ['ngResource']).controller('booksController', ['$http', '$scope',
    function ($http, $scope) {

        var txTitle = document.getElementById('tx-title');
        var txAuthor = document.getElementById('tx-author');
        var txPublish = document.getElementById('dt-publish');
        var txPages = document.getElementById('in-pages');
        var txTypes = document.getElementById('cb-type');

        var btSave = document.getElementById('bt-save');
        var btDelete = document.getElementById('bt-delete');
        var btCancel = document.getElementById('bt-cancel');
        var tbBook = document.getElementById('tb-book');

        $scope.selectedBook = null;


        $scope.init = function () {

            btDelete.style.display = 'none';    // hide
            tbBook.style.display = 'none';    // hide

            $http({
                url: '/api/get-types',
                method: 'POST',
                data: {}
            }).success(function (data, status, headers, config) {
                var response = data;
                if(response.status.code === 0){
                    $scope.types = response.data;
                }
                else{
                    alert('Something wrong!');
                }
            }).error(function (data, status, headers, config) {
                alert('Error when request to server. Check your connection.');
            });

            $http({
                url: '/api/get-books',
                method: 'POST',
                data: {}
            }).success(function (data, status, headers, config) {
                var response = data;
                if(response.status.code === 0){
                    $scope.books = response.data;

                    if(response.data.length > 0){
                         tbBook.style.display = '';    // show
                    }
                }
                else{
                    alert('Something wrong!');
                }
            }).error(function (data, status, headers, config) {
                alert('Error when request to server. Check your connection.');
            });

        }



        $scope.delete = function() {

            var yes = confirm('Are you fucking sure?');
            if(!yes){
                return;
            }

            $http({
                url: '/api/book/drop',
                method: 'POST',
                data: {id : $scope.selectedBook.id}
            }).success(function (data) {
                var response = data;

                if(response.status.code === 0){
                    alert('Success!');
                }
                window.location = '/';

            }).error(function (data, status, headers, config) {
                alert('Error when request to server. Check your connection.');
            });

        }


        $scope.save = function () {

            if(txTitle.value === ''){
                alert('Please input title!');
                return;
            }
            if(txAuthor.value === ''){
                alert('Please input author!');
                return;
            }

            var bookId = null;
            if($scope.selectedBook !== null){
                bookId = $scope.selectedBook.id;
            }

            var input = {
                id: bookId,
                title: txTitle.value,
                author: txAuthor.value,
                date: txPublish.value,
                pages: txPages.value,
                type_id: txTypes.value
            }

            $http({
                url: '/api/book/save',
                method: 'POST',
                data: input
            }).success(function (data, status, headers, config) {
                var response = data;
                if(response.status.code === 0){
                    alert('Success');
                    window.location = '/';
                }
                else{
                    alert('Something wrong!');
                }
            }).error(function (data, status, headers, config) {
                alert('Error when request to server. Check your connection.');
            });
        }

        $scope.edit = function(index){
            var sb = $scope.books[index];
            $scope.selectedBook = sb;

            txTitle.value = sb.title;
            txAuthor.value = sb.author;
            txPublish.value = sb.date;
            txPages.value = sb.pages;

            btDelete.style.display = '';    // show

            for(var i=0;i < $scope.types.length;i++){
                var t = $scope.types[i];
                if(t.id === sb.type_id){
                    txTypes.selectedIndex = i;
                    break;
                }
            }
        }

        $scope.getTypeLabel = function(typeId){
            for(var i=0;i < $scope.types.length;i++){
                var t = $scope.types[i];
                if(t.id === typeId){
                    return t.title
                }
            }

            return '-';
        }


        $scope.clear = function(){
            txTitle.value = '';
            txAuthor.value = '';
            txPublish.value = null;
            txPages.value = '';
            txTypes.selectedIndex = 0;
            $scope.selectedBook = null;

            btDelete.style.display = 'none';    // hide
        }

    }]
 );