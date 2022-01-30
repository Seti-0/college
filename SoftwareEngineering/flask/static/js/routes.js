// Routes are plotted between stations.
// A start and end station number are maintained globally,
// and set by the two selection ui elements.
const route_station_numbers = {
    start: null,
    end: null
}


function setupRoutePlanner(map) {
    // Add google maps API services
    const directionsService = new google.maps.DirectionsService();
    const directionsRenderer = new google.maps.DirectionsRenderer({suppressMarkers: true});

    // Render directions from DirectionService
    directionsRenderer.setMap(map);

    // When dropdown boxes for start and end are chosen/changed the directions are calculated
    const handler = function () {
        calculateAndDisplayRoute(directionsService, directionsRenderer);
    };

    document
        .getElementById("plan-route")
        .addEventListener("click", handler);

    const start = document.getElementById("start-location");
    createRouteInput(start, "start");

    const end = document.getElementById("end-location");
    createRouteInput(end, "end");

}


/* Uses Google Search box functionality to find locations on map, and place markers for search locations.
Then calls findNearestStation(), defined in markers.js to find the closest stations to those points.
The start and end station are stored in the global object defined at the top of this page so that they an be accessed
by the route calculator */
function createRouteInput(input, location_name) {

    // The search box set up bit
    const searchBox = new google.maps.places.SearchBox(input);

    map.addListener("bounds_changed", () => {
        searchBox.setBounds(map.getBounds());
    });

    let marker = null;
    const icon = getMarkerIcon("purple", "dot", 30);
    searchBox.addListener("places_changed", () => {

        const places = searchBox.getPlaces();

        if (marker !== null)
            marker.setMap(null);

        if (places.length === 0)
            return;

        // Not sure what the behaviour for multiple places should
        // be right now, and so am ignoring any extra ones.
        // The more common use case by far is a single place, anyways.
        const place = places[0];

        // Puts marker on map for actual search location
        marker = new google.maps.Marker({
            map,
            icon,
            title: place.name,
            position: place.geometry.location,
        });


        const lat = place.geometry.location.lat();
        const lon = place.geometry.location.lng();
        const stationNumber = findNearestStation(lat, lon);

        // Highlights nearest station, and removes highlight from previous nearest station
        if (route_station_numbers.start !== route_station_numbers.end)
            setHighlightStation(route_station_numbers[location_name], false);

        setHighlightStation(stationNumber, true);
        route_station_numbers[location_name] = stationNumber;

        // Zooms to location
        const bounds = new google.maps.LatLngBounds();

        if (place.geometry.viewport) {
            // Only geocodes have viewport.
            bounds.union(place.geometry.viewport);
        } else {
            bounds.extend(place.geometry.location);
        }

        bounds.extend(new google.maps.LatLng(
            currentData[stationNumber]["latitude"],
            currentData[stationNumber]["longitude"]
        ));

        map.fitBounds(bounds);

    });
}

function showPlanner() {

    const content = document.getElementById("route-content");
    content.style.display = "flex";

    const control = document.getElementById("show-planner-button");
    control.style.display = "none";

    const label = document.getElementById("start-label");
    label.style.display = "inline";

    const start = document.getElementById("start-location");
    start.placeholder = "Start Location";

}

function dismissPlanner() {

    const content = document.getElementById("route-content");
    content.style.display = "none";

    const control = document.getElementById("show-planner-button");
    control.style.display = "inline-block";

    const label = document.getElementById("start-label");
    label.style.display = "none";

    const start = document.getElementById("start-location");
    start.placeholder = "Search";

}

/*
* Uses input values, calls Google API to render route between them.
* */
function calculateAndDisplayRoute(directionsService, directionsRenderer) {

    // Start and end points taken from function above and google id retrieved from corresponding
    // records in currentData global object.
    let start = currentData[route_station_numbers.start]["google_place_id"];
    let end = currentData[route_station_numbers.end]["google_place_id"];

    if (start === null || end === null)
        return;

    directionsService.route(
        {
            // Set start and end points of journey
            origin: {
                placeId: start,
            },
            destination: {
                placeId: end,
            },
            // Choose cycling as the travel mode, default is car
            travelMode: google.maps.TravelMode.BICYCLING,
        },

        // Render if successful, raise error if not
        (response, status) => {
            if (status === "OK") {
                directionsRenderer.setDirections(response);
            } else {
                window.alert("Directions request failed due to " + status);
            }
        }
    );
}