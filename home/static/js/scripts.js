'use strict';

function initMap() {
  // Google map
  google.maps.event.addDomListener(window, 'load', init);

  var map;
  var location = new google.maps.LatLng(42.684680, 23.318925);
  var MY_MAPTYPE_ID = 'custom_style';
  function init() {
    var featureOpts = [
      {
        stylers: [
          {saturation: -20},
          {lightness: 40},
          {visibility: 'simplified'},
          {gamma: 0.8},
          {weight: 0.4}
        ]
      },
      {
        elementType: 'labels',
        stylers: [{visibility: 'on'}]
      },
      {
        featureType: 'water',
        stylers: [{color: '#dee8ff'}]
      }
    ];
    var mapOptions = {
      zoom: 16,
      scrollwheel: false,
      panControl: false,
      mapTypeControl: false,
      streetViewControl: false,
      center: location,
      mapTypeControlOptions: {
        mapTypeIds: [google.maps.MapTypeId.ROADMAP, MY_MAPTYPE_ID]
      },
      mapTypeId: MY_MAPTYPE_ID
    };
    map = new google.maps.Map(document.getElementById('map'), mapOptions);
    var image = '/static/images/pmarker.png';
    var myLatLng = location;
    var beachMarker = new google.maps.Marker({
      position: myLatLng,
      map: map,
      icon: image
    });
    var styledMapOptions = {
      name: 'Custom Style'
    };
    var customMapType = new google.maps.StyledMapType(
      featureOpts,
      styledMapOptions
    );
    map.mapTypes.set(MY_MAPTYPE_ID, customMapType);
  }
}

(function() {
  $(document).foundation();
})();
//# sourceMappingURL=scripts.js.map
