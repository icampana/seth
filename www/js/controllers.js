angular.module('seth.controllers', ['seth.services'])

.controller('DashCtrl', function($scope) {})

.controller('MapCtrl', function($scope) {
  var myLatlng = new google.maps.LatLng(43.07493,-89.381388);
        
        var mapOptions = {
          center: myLatlng,
          zoom: 16,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        var map = new google.maps.Map(document.getElementById("map"),
            mapOptions);
        
        $scope.map = map;
})

.controller('CropsCtrl', function($scope, $state, $stateParams) {
  $scope.crops = [
    {id: 0, name: 'Coffee'},
    {id: 1, name: 'Soy'},
    {id: 2, name: 'Banana'},
  ];
  
  $scope.addCrop = function(){
    console.log("Agregando crop");
    $state.transitionTo('tab.register');
  }
  
  $scope.reportIncident = function(){
    $state.transitionTo('tab.register');
  }
})

.controller('RegisterCtrl', function($scope, $stateParams, $ionicLoading, Camera) {
  $scope.cropType = '';
  $scope.gps_position = 'Pending';
  $scope.location = {latitude:'', longitude: ''};
  $scope.cropPhoto = 'img/empty.png';
  
  $scope.cropList = [
      {id: 0, name: 'Coffee'},
      {id: 1, name: 'Banana'},
      {id: 2, name: 'Cotton'},
    ];
  
  $scope.plagueList = [
      {id: 0, name: 'Sigatoka'},
      {id: 1, name: 'KKK'},
      {id: 2, name: 'XXX'},
    ];
  
  $scope.getPhoto = function() {
    Camera.getPicture().then(function(imageURI) {
      //console.log(imageURI);
      $scope.cropPhoto = imageURI;
      //"data:image/jpeg;base64," + 
    }, function(err) {
      console.err(err);
    }, {
      quality: 75,
      targetWidth: 320,
      targetHeight: 320,
      saveToPhotoAlbum: false,
      destinationType: Camera.DestinationType.DATA_URL 
    });
  };
  
  $scope.updateGPS = function (){
    $ionicLoading.show({
        template: 'Obtaining Location..'
    });

    var options = {maximumAge: 0, timeout: 20000, enableHighAccuracy:true};
    
    navigator.geolocation.getCurrentPosition(function(position){

                    $scope.location.latitude = position.coords.latitude;
                    $scope.location.longitude = position.coords.longitude;

                    $scope.gps_position = 'Obtained';
                    $ionicLoading.hide();
            }, function(error) {
                    $log.log('GPS: ', 'code: '    + error.code    + '\n' +
                                            'message: ' + error.message + '\n');
                    $ionicLoading.hide();
    }, options);
    
  };
  
})

.controller('AccountCtrl', function($scope) {
  $scope.settings = {
    enableFriends: true
  };
});
