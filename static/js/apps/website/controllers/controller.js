var controllers = {};

controllers.websiteController = function($scope, $http, userUrl){
    $scope.login = function(username, password){
        var url = userUrl.loginUrl;
        var data = {
          username: username,
          password: password
        };

        return $http.post(url, data).success(function(response, status){
            if(status == 200){

            }
        });
    };
    $scope.signup = function(username, email, password){
        var url = userUrl.signupUrl;
        var data = {
          username: username,
          email: email,
          password: password
        };

        return $http.post(url, data).success(function(response, status){
            if(status == 200){

            }
        });
    };
    $scope.logout = function(){
        var url = userUrl.logoutUrl;

        return $http.get(url).success(function(response, status){
            if(status == 200){

            }
        });
    };

};

websiteapp.controller(controllers);