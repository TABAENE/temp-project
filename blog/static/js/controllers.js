var  blogControllers = angular.module('blogControllers', []);

blogControllers.controller('blogListController', ['$scope', '$routeParams', '$http', 'Blog', 'popupService', '$window',
    function($scope, $routeParams, $http, Blog, popupService, $window){
    $scope.blogs=Blog.query();
}]).controller('blogCreateController',['$scope', '$http', 'Blog', '$location',
	function($scope, $http, Blog, $location){

    $scope.blog=new Blog();
    $scope.blog.author = $("[id='author']").text();
    $scope.addBlog=function(){
    debugger;
        $scope.blog.$save(function(){
            $location.url('/blog');
        });
    }
}]).controller('blogEditController',['$scope', '$routeParams', '$http', 'Blog', '$location',
	function($scope, $routeParams, $http, Blog, $location){

    $scope.updateBlog=function(){
        $scope.blog.$update(function(){
            $location.url('/blog');
        });
    }
    $scope.loadBlog=function(){
        $scope.blog=Blog.get({id:$routeParams.id});
    };
    $scope.loadBlog();
}]);

blogControllers.config(['$resourceProvider', function($resourceProvider) {
  // Don't strip trailing slashes from calculated URLs
  $resourceProvider.defaults.stripTrailingSlashes = false;
}]);