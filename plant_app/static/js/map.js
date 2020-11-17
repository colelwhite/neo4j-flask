require([
    "esri/Map",
    "esri/views/MapView",
    "esri/layers/FeatureLayer"
  ],
  function(
    Map,
    MapView,
    FeatureLayer
  ) {

    var map = new Map({
      basemap: "gray"
    });

    var view = new MapView({
      container: "map_intro_div",
      map: map,
      center: [-88.71511,64.09042],
      zoom: 2
    });

    // Add a feature layer to map with all features visible (no filter)
    var featureLayer = new FeatureLayer({
      url: "https://services6.arcgis.com/ugTDxzvMqh4Ev3ta/arcgis/rest/services/province/FeatureServer",
      outFields: ["*"],  // Return all fields to client
      popupTemplate: {  // Enable a popup on client
        title: "{NAME}", // Show field value
        content: "{DESIGNATION}"  // Show field value
      }
    });

    map.add(featureLayer);

    setFeatureLayerViewFilter("NAME = 'Alberta'");

    // Client-side filter
    function setFeatureLayerViewFilter(expression) {
      view.whenLayerView(featureLayer).then(function(featureLayerView) {
        featureLayerView.filter = {
          where: expression
        };

      });
    }


  });
