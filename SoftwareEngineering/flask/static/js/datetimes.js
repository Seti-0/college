setupDatetimeSelectors();


// Uses functions below to create lists of dates and times used later to update drop-down menus.
// Adds on-click event to date drop-down to update time drop-down.
function setupDatetimeSelectors() {

    const dateTimes = getDateTimes();

    const dateInputs = document.getElementsByClassName("future-date");
    for (let dateElement of dateInputs) {

        renderDateOptions(dateTimes, dateElement);

        const timeID = dateElement.getAttribute("data-time-id");
        const timeElement = document.getElementById(timeID);

        function updateTimeElement() {
            updateTimes(dateTimes, dateElement, timeElement);
        }

        updateTimeElement();
        dateElement.addEventListener("click", updateTimeElement);

    }

}

function renderDateOptions(dateTimes, dateElement) {

    let html = "";
    for (let sqlDate in dateTimes) {
        const label = dateTimes[sqlDate].label
        html += `<option value="${sqlDate}">${label}</option>`
    }

    dateElement.innerHTML = html;

}

function updateTimes(dateTimes, dateElement, timeElement) {

    const sqlTime = dateElement.value;
    const times = dateTimes[sqlTime].times;

    let html = "";
    for (let value of times) {
        const label = value + ":00";
        html += `<option value="${value}">${label}</option>`
    }

    timeElement.innerHTML = html;

}


// Generates an object keyed by date, with lists of times for each date.
// Dates/times correspond to four day window for which there are reliably forecasts available to use for predictions.
// (Using a five-day window means that the times rendered here for the fifth day do not always sync up with the
// times for which there are weather forecasts in the database.)
function getDateTimes() {

    const result = {};

    // Start at the beginning of the next hour.
    const start = new Date();
    start.setHours(start.getHours() + 1);
    start.setMinutes(0);
    start.setSeconds(0);

    // End 4 days from now.
    const end = new Date();
    end.setDate(end.getDate() + 4);

    // Store hourly times in the form of
    // lists of hours, keyed by the date in sql format.
    let current = new Date(start.getTime());
    while (current <= end) {

        // It is important that this the sql value be
        // in UTC time! That is what the database is running as.
        const sqlDate = [
            current.getUTCFullYear(),
            current.getUTCMonth() + 1,
            current.getUTCDate()
        ].join("-");

        // For each sql date, store an object with a display
        // label and the times for that date.
        if (!(sqlDate in result))
            result[sqlDate] = {
                label: current.toLocaleDateString(),
                times: []
            }

        // For each hour, push that hour to the list
        // of times for the relevant date.
        result[sqlDate].times.push(current.getHours())

        current.setHours(current.getHours() + 1)

    }

    return result;

}