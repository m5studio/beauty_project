const api_cities_url = "/api/cities/";
const api_services_url = "/api/services/";

document.getElementById('search-tile-input__date').valueAsDate = new Date();

// const searchInputPlaces = document.getElementsByClassName('search-tile-input__place');
const searchInputPlaces = document.getElementById('search-tile-input__place');
// const searchInputServices = document.getElementsByClassName('search-tile-input__services');
const searchInputServices = document.getElementById('search-tile-input__services');

let citiesArr = [];
let servicesArr = [];

function fetchCitiesData() {
    return fetch(api_cities_url)
                .then(response => response.json());
}

function fetchServicesData() {
    return fetch(api_services_url)
                .then(response => response.json());
}


fetchCitiesData().then(citiesArr => {
    // console.log(citiesArr);
    for (let i = 0; i < citiesArr.length; i++) {
        let search_option = document.createElement("option");
        search_option.value = citiesArr[i].id;
        search_option.text = citiesArr[i].name;
        // searchInputPlaces[i].add(search_option);
        searchInputPlaces.add(search_option);
    }
});

fetchServicesData().then(servicesArr => {
    // console.log(servicesArr);
    for (let i = 0; i < servicesArr.length; i++) {
        let search_option = document.createElement("option");
        search_option.value = servicesArr[i].id;
        search_option.text = servicesArr[i].name;
        // searchInputServices[i].add(search_option);
        searchInputServices.add(search_option);
    }
});


// TODO: Clone .st-4 .st-5
