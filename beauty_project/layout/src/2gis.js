// 2Gis API Homepage
var DG = require('2gis-maps');

/*
DG.then(function() {
    const api_url = '/api/salons/';

    const map = DG.map('section-map__map', {
        'center': [55.754, 37.619],
        'zoom': 10,

        'dragging': true,
        'touchZoom': true,
        'scrollWheelZoom': true,
        'doubleClickZoom': true,
        'boxZoom': true,
        'geoclicker': true,
        'zoomControl': true,
        'fullscreenControl': false
    });


    // Add markers to map on page load
    const getSalonsArray = [];

    fetch(api_url)
        .then(response => response.json())
        .then(data => {
            getSalonsArray.push(...data);

            getSalonsArray.forEach(el => {
                DG.marker([el.latitude, el.longitude]).addTo(map).bindPopup(el.name);
            });
        });

    document.querySelector("#section-map__legend--show-opened").addEventListener("click", function(e) {
        e.preventDefault();
        console.log('show-opened');
    }, false);

    document.querySelector("#section-map__legend--show-actions").addEventListener("click", function(e) {
        e.preventDefault();
        console.log('actions');
    }, false);

    document.querySelector("#section-map__legend--show-all").addEventListener("click", function(e) {
        e.preventDefault();
        console.log('show-all');
    }, false);
});
*/


DG.then(function() {
    const api_url = '/api/salons/';

    var map,
        markers = DG.featureGroup(),
        markers_actions = DG.featureGroup(),
        coordinates = [];

    map = DG.map('section-map__map', {
        'center': [55.754, 37.619],
        'zoom': 10,

        'dragging': true,
        'touchZoom': true,
        'scrollWheelZoom': true,
        'doubleClickZoom': true,
        'boxZoom': true,
        'geoclicker': true,
        'zoomControl': true,
        'fullscreenControl': false
    });

    // Add markers to map on page load
    // var salonsArray = [];

    fetch(api_url)
        .then(response => response.json())
        .then(data => {
            // salonsArray.push(...data);

            for (var i = 0; i < data.length; i++) {
                coordinates[0] = data[i].latitude;
                coordinates[1] = data[i].longitude;
                DG.marker(coordinates).addTo(markers).bindPopup(data[i].name);

                if (data[i].action === true) {
                    DG.marker(coordinates).addTo(markers_actions).bindPopup(data[i].name);
                }
            }

            // return salonsArray.push(...data);
        })
        .catch(err => console.error(err))

    showMarkers();


    document.getElementById('hide').onclick = hideMarkers;
    // document.getElementById('show').onclick = showMarkers;

    document.getElementById('section-map__legend--show-all').onclick = showMarkers;
    document.getElementById('section-map__legend--show-actions').onclick = showActionMarkers;

    function showMarkers() {
        markers.addTo(map);
        // map.fitBounds(markers.getBounds());
    };

    function showActionMarkers() {
        hideMarkers();

        markers_actions.addTo(map);
        map.fitBounds(markers.getBounds());
    };

    function hideMarkers() {
        markers.removeFrom(map);
        markers_actions.removeFrom(map);
    };

    function showSanonsActions() {
        // hideMarkers();
        // markers_actions.removeFrom(map);

        salonsArray.forEach(el => {
            if (el.action === true) {
                coordinates[0] = el.latitude;
                coordinates[1] = el.longitude;
                DG.marker(coordinates).addTo(markers_actions).bindPopup(el.name);
            }
        });

        markers_actions.addTo(map);

        /*
        fetch(api_url)
            .then(response => response.json())
            .then(data => {
                for (var i = 0; i < data.length; i++) {
                    if (data[i].action === true) {
                        coordinates[0] = data[i].latitude;
                        coordinates[1] = data[i].longitude;
                        DG.marker(coordinates).addTo(markers_actions).bindPopup(data[i].name);
                    }
                }
                // showMarkers();
                markers_actions.addTo(map);
                // map.fitBounds(markers_actions.getBounds());
            })
            .catch(err => console.error(err));
        */
    };
});

/*
DG.then(function() {
    var map,
        markers = DG.featureGroup(),
        coordinates = [];

    map = DG.map('map', {
        center: [54.98, 82.89],
        zoom: 13
    });

    for (var i = 0; i < 100; i++) {
        coordinates[0] = 54.98 + Math.random();
        coordinates[1] = 82.89 + Math.random();
        DG.marker(coordinates).addTo(markers);
    }

    document.getElementById('hide').onclick = hideMarkers;
    document.getElementById('show').onclick = showMarkers;

    function showMarkers() {
        markers.addTo(map);
        map.fitBounds(markers.getBounds());
    };

    function hideMarkers() {
        markers.removeFrom(map);
    };
});
*/