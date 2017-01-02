var blog = angular.module('blog', ['ngRoute', 'ngResource', 'blogControllers', 'blog.services']);

blog.config(['$routeProvider',
    function($routeProvider){
    $routeProvider
    .when('/blog', {templateUrl: '/static/templates/blog.html', controller: 'blogListController'})
    .when('/blog/create', {templateUrl: '/static/templates/create_blog.html', controller: 'blogCreateController'})
    .when('/blog/:id/edit', {templateUrl: '/static/templates/edit_blog.html', controller: 'blogEditController'})
    .otherwise( { redirectTo: "/blog" });
}
]);

blog.config(['$httpProvider',
    function($httpProvider){
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/json';
    $httpProvider.defaults.headers.put['Content-Type'] = 'application/json';
}
]);

//blog.config(['$resourceProvider', function($resourceProvider) {
//  // Don't strip trailing slashes from calculated URLs
//  $resourceProvider.defaults.stripTrailingSlashes = false;
//}]);