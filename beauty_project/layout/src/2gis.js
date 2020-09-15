// 2Gis API Homepage
var DG = require('2gis-maps');


var map = DG.map('section-map__map', {
    'center': [55.754, 37.619],
    'zoom': 10,

    // 'dragging': false,
    // 'touchZoom': false,
    'scrollWheelZoom': false,
    'doubleClickZoom': false,
    'boxZoom': false,
    // 'geoclicker': false,
    // 'zoomControl': false,
    'fullscreenControl': false
});

// DG.marker([55.754271, 37.619255]).addTo(map).bindPopup('Информация о салоне');

fetch('/api/salons/')
    .then(response => response.json())
    // .then(data => console.log(data));
    .then(data => {
        data.forEach(el => {
            DG.marker([el.latitude, el.longitude]).addTo(map).bindPopup(el.description);
        });
    });