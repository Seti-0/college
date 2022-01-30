// This will be used later as template for the station popups.
const infoTemplate = fetch("/stations/template")
    .then(response => response.text());

// Current data is fetched once at the beginning and never updated.
// It includes current available bikes. Predicted data is fetched when
// the user requests a prediction, and ONLY includes available bikes.
let currentData;
let predictedAvailableBikes;

// The map markers are created after map initialization
// and then never removed. Their labels and icons are
// updated as needed.
const markers = [];

// There is a single popup window, which appears by one
// station at most at any given time.
let popupWindow;
let popupWindowStationNumber = -1;

// At any given time, station markers are all displaying
// either the number of free bikes, or free bike stands.
const DisplayType = {
    FREE_BIKES: 0,
    FREE_STANDS: 1,
}
let displayType = DisplayType.FREE_BIKES;

// At any given time, station markers are all displaying
// either the current number of available items, or a future
// prediction of available items.
let showPredictions = false;

// The prediction lock is greater than 0 while one
// (or more) predictions are in progress. Else it is zero.
// While a prediction request is being processed, a loading
// symbol is visible, and the markers do not display information.
let predictionLock = 0;

// At any given time, one or more stations may be highlighted
// a different color.
let highlightedStations = new Set();


function createStationMarkers(initialData) {

    currentData = initialData;

    // I don't think the content here is ever visible.
    popupWindow = new google.maps.InfoWindow({
        content: "Loading..."
    });

    for (const station_number in currentData) {

        // currentData is a plain old object, but is being treated as a dictionary.
        // Hence, hasOwnProperty() checks are used throughout this file.
        if (!currentData.hasOwnProperty(station_number))
            continue;

        const station = currentData[station_number];

        const marker = new google.maps.Marker({
            position: {
                lat: station["latitude"],
                lng: station["longitude"]
            },
            map: map,
            title: station["name"],   // gives marker a tooltip
        });

        function display() {
            popupWindow.open(map, marker);
        }

        function onclick() {
            popupWindowStationNumber = station_number;
            updatePopupWindow()
                .then(display);
            drawChart(station_number);
        }

        marker.addListener("click", onclick);

        markers[station_number] = marker;

    }

    updateStationMarkers();
}

async function updatePopupWindow() {

    if (popupWindowStationNumber === -1)
        // No station has been selected.
        return;

    const station_number = popupWindowStationNumber;
    const station = currentData[station_number];

    let available_bikes;
    if (showPredictions)
        available_bikes = predictedAvailableBikes[station_number];
    else
        available_bikes = station["available_bikes"];

    /*
    A little javascript library called "Mustache" is used
    here for templating.

    Note: The library has been included directly in the project
    as a source file (called "mustache.js"), rather than being installed
    or referenced in some way.

    More info: https://github.com/janl/mustache.js
    Template syntax: http://mustache.github.io/mustache.5.html
    */

    const view = {
        name: station["name"],
        open: station["status"] === "OPEN",
        available_bikes: available_bikes,
        free_spaces: station["bike_stands"] - available_bikes,
        bank: station["banking"]
    }

    const template = await infoTemplate;
    const content = Mustache.render(template, view);

    popupWindow.setContent(content);

}

function updateStationMarkers() {

    for (const stationNumber in currentData) {

        if (!currentData.hasOwnProperty(stationNumber))
            continue;

        updateMarkerLabel(stationNumber);
        updateMarkerColor(stationNumber);

    }

    updatePopupWindow();

}

function updateMarkerLabel(stationNumber) {

    if (!currentData.hasOwnProperty(stationNumber))
        return;

    let label;

    // Clear the marker while an update is progress.
    if (predictionLock > 0)
        label = "";

    else label = getMarkerNumber(stationNumber).toString();

    markers[stationNumber].setLabel(label);

}

function getMarkerNumber(stationNumber) {

    let available;

    if (showPredictions)
        available = predictedAvailableBikes[stationNumber];
    else
        available = currentData[stationNumber]["available_bikes"];

    if (displayType === DisplayType.FREE_STANDS)
    {
        const total_stands = currentData[stationNumber]["bike_stands"];
        available = total_stands - available;
    }

    return available;

}

function updateMarkerColor(stationNumber) {

    if (!markers.hasOwnProperty(stationNumber))
        return;

    let color;

    // Clear the marker color while an update is in progress
    if (predictionLock > 0)
        color = "green";

    else if (highlightedStations.has(stationNumber))
        color = "purple";

    else {

        const available = getMarkerNumber(stationNumber)
        const stands = currentData[stationNumber]["bike_stands"];

        const proportion = available / stands;
        if (proportion < 0.2)
            color = "red";

        else if (proportion < 0.3)
            color = "amber";

        else color = "green";

    }

    markers[stationNumber].setIcon(getMarkerIcon(color));

}

function getMarkerIcon(color, type="empty", size=50) {

    let url = `static/icons/marker-${color}`;
    if (type !== "empty")
        url += "-" + type;
    url += ".svg";

    // The icon sizes and proportions here
    // were in part determined by experimentation,
    // I'm not sure if they will hold in all scenarios.

    return {
        url: url,
        anchor: new google.maps.Point(size * 0.5, size),
        scaledSize: new google.maps.Size(size, size),
        labelOrigin: new google.maps.Point(size * 0.5, size * 0.34)
    };

}

function setHighlightStation(stationNumber, highlight) {

    if (!currentData.hasOwnProperty(stationNumber))
        return;

    if (highlight)
        highlightedStations.add(stationNumber);
    else
        highlightedStations.delete(stationNumber);

    updateMarkerColor(stationNumber);

}

function displayPredictions() {

    // Clear markers
    predictionLock += 1;
    updateStationMarkers();

    // Display loading box
    document.getElementById("loader").style.display = "block";

    let date = document.getElementById("date").value;
    let time = document.getElementById("time").value;

    // Start request
    fetch(`stations/prediction?date=${date}&hour=${time}`)
        .then(response => response.json())
        .then(data => {

            predictedAvailableBikes = data;
            showPredictions = true;

            // Apply update, and hide the loading box, but
            // only if no more updates are in progress.

            predictionLock -= 1;
            updateStationMarkers();

            if (predictionLock === 0)
                document.getElementById("loader").style.display = "none";

        });

}

function resetMarkersToCurrent() {

    showPredictions = false;
    updateStationMarkers();

}

function toggleLabels(source) {

    if (source === "stands")
        displayType = DisplayType.FREE_STANDS;

    else displayType = DisplayType.FREE_BIKES;

    updateStationMarkers();

    /*
        Swap the toggle button visuals.

        This is more verbose than I'd like, but it
        is just swapping which button holds the "active" class.
     */

    let activeId;
    let inactiveId;

    if (source === 'stands') {
        activeId = "show-bikes";
        inactiveId = "show-stands";
    } else {
        activeId = "show-stands";
        inactiveId = "show-bikes";
    }

    const activeElement = document.getElementById(activeId);
    const inactiveElement = document.getElementById(inactiveId);

    activeElement.classList.remove("marker-button-active");
    activeElement.classList.add("marker-button-inactive");

    inactiveElement.classList.remove("marker-button-inactive");
    inactiveElement.classList.add("marker-button-active");

}

function findNearestStation(lat, lon) {

    // Minimizing the distance is the same as minimizing
    // the distance squared.

    // I'm treating lat/lon like x/y when finding the distance
    // here, which would give weird results in some parts of the
    // world (such as the North Pole), but I think it should be
    // fine in Ireland.

    let minDistanceSquared = 1000000;
    let result = -1;

    for (const number in currentData) {

        if (!currentData.hasOwnProperty(number))
            continue;

        const lat2 = currentData[number]["latitude"];
        const lon2 = currentData[number]["longitude"];

        const distanceSquared = Math.pow(lat - lat2, 2)
            + Math.pow(lon - lon2, 2);

        if (distanceSquared < minDistanceSquared)
        {
            minDistanceSquared = distanceSquared;
            result = number;
        }

    }

    return result;

}