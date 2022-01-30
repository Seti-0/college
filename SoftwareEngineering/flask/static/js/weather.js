fetch("/weather/data")
    .then(response => response.json())
    .then(displayWeather);


/* Calls weather/data endpoint in flask app to get current weather and forecast. Loops through records, and adds
* icon and temperature to weather div. */
function displayWeather(data) {

    const days = [];

    for (const key in data) {
        if (!data.hasOwnProperty(key))
            continue;

        let date;
        if (key === "0")
            date = "Now";
        else
            date = data[key]["date"].toString().slice(0,3); // Extract Three-letter abbreviation of name of day

        const src = `/weather/icons/${data[key]["description"]}`; // get corresponding icon for description
        const temp = `${data[key]["temp"]}`;

        const current = `${date}: <img src="${src}">${temp}C`;
        days.push(current);
    }

    document.getElementById("weather-box")
        .innerHTML = days.join(" | ");
}