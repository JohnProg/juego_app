var websiteapp = angular.module('websiteapp',[], function($httpProvider){
    $httpProvider.defaults.headers.post['content-type'] = 'application/x-www-form-urlencoded;charset-utf-8';
});

websiteapp.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

websiteapp.run(function(csrfToken, $http){
    $http.defaults.headers.post['X-CSRFToken'] = csrfToken.csrfToken;
    $http.defaults.headers.common['X-Requested-with'] = 'XMLHttpRequest';
});