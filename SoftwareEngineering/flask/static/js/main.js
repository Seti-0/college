let map;

function initMap() {

    // Set up charting
    google.charts.load('current', {packages: ['corechart', 'bar']});

    const element = document.getElementById("map");

    map = new google.maps.Map(element, {
        center: { lat: 53.35, lng: -6.26  },
        zoom: 14,
    });

    // pull station data and assign to global variable before creating station markers
    fetch("stations/latest")
        .then(response => response.json())
        .then(data => createStationMarkers(data));

    setupRoutePlanner(map);
}


function drawChart(station_num) {
    /*
    Call functions that draw the google chart elements based on the station number chosen.
    The average historical for today's day of the week and the current average per hour for today are generated.
     */
    drawAverage(station_num);
    drawToday(station_num);
}

function drawAverage(station) {
    // Pull data from flask generated endpoint (json) for the required station
    $.ajax({
        url: "charts/average/" + station,
        dataType: "json",
        success: function(jsonData) {

            // Create google DataTable data element
            let data = new google.visualization.DataTable();

            // Add required columns that we will be using
            data.addColumn('string', 'Time');
            data.addColumn('number', 'Available Bikes');
            data.addColumn('number', 'Available Spaces');

            // Get the day of week used in the title
            let DayOfWeek = jsonData[1].weekday;

            // Populate the rows of data in the data table
            for (let i = 0; i < jsonData.length; i++) {
                data.addRow([
                    jsonData[i].hour + ":00",
                    jsonData[i].avg_avail_bikes,
                    jsonData[i].avg_avail_spaces
                ]);
            }

            // Set up options like title and size for the chart
            let options = {
                title: 'Average Bike Availability: ' + DayOfWeek,
                height: "100%",
                width: "100%",
                legend: {
                    position: 'bottom'
                },
                isStacked: true
            };

            // Create chart element and draw it
            let chart = new google.visualization.BarChart(document.getElementById('chart_div_average'));
            chart.draw(data, options);
        }
    });
}


function drawToday(station) {
    // Pull data from flask generated endpoint (json) for the required station
    $.ajax({
        url: "charts/today/" + station,
        dataType: "json",
        success: function(jsonData) {

            // Create google DataTable data element
            let data = new google.visualization.DataTable();

            // Add required columns that we will be using
            data.addColumn('string', 'Time');
            data.addColumn('number', 'Available Bikes');
            data.addColumn('number', 'Available Spaces');

            // Populate the rows of data in the data table
            for (let i = 0; i < jsonData.length; i++) {
                data.addRow([
                    jsonData[i].hour + ":00",
                    jsonData[i].avg_avail_bikes,
                    jsonData[i].avg_avail_spaces]);
            }

            // Set up options like title and size for the chart
            let options = {
                title: 'Average Bike Availability Today',
                width: '75%',
                height: '10px',
                legend: {
                    position: 'bottom'
                },
                isStacked: true
            };

            // Create chart element and draw it
            let chart = new google.visualization.BarChart(document.getElementById('chart_div_today'));
            chart.draw(data, options);
        }
    });

}


function showCharts() {

    // Set elements used in function
    let chartButton = document.getElementById("show-chart-button");
    let chartContent = document.getElementById("charts-content");

    // If div is hidden, show it and button text
    if (chartButton.textContent === "Show Charts") {
        chartContent.style.display = "block";
        chartButton.textContent = 'Hide Charts';
    } else {

    // If div is visible, hide it and change button text
        chartContent.style.display = "none";
        chartButton.textContent = "Show Charts";
    }
}