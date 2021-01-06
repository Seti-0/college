/*eslint-env es6,browser*/

// This document is way over-commented, because this was for an assignment.

window.onload = loadData;

/** 
* Sends a request for the scheduling data. When the request is
* complete, if it is successful, the timetable will be loaded.
* (If not, an error message will show)
*/
function loadData() {

    const loadinginfo = document.getElementById("loading-info");
    loadinginfo.style.visibility = "visible";

    const progressDisplay = document.getElementById("data-load-progress");

    const client = new XMLHttpRequest();
    client.open("GET", "scheduling.json");

    client.onprogress = function(event) {
        updateProgress(progressDisplay, event.loaded/event.total);
    }

    // Note: onerror is only called for errors where
    // no HTML response made it at all - it is not called
    // when the HTML returns with, say, code 404.
    
    // An error code in the response still needs to be
    // handled in onload.
    
    client.onerror = function() {
        showError(loadinginfo);
    }
    
    client.onload = function() {
        checkResponse(client, loadinginfo);  
    }
    
    client.send();

}

/** 
* Sets the text of a given element to a formatted proportion.
*/
function updateProgress(progressDisplay, p) {
    progressDisplay.innerHTML = (p*100).toFixed(2);
}

/**
* Sets the content of a given element to a styled error message
* with a title, message content, and user suggestion.
*/
function showError(loadinginfo, text) {
    
    var content = "<h4 class=error-title>";
    content += "Failed to load scheduling data.";
    content += "</h4>";
    
    if (text !== undefined) {
        content += "<p class=error-message>";
        content += text;
        content += "</p>";   
    }
    
    content += "<p class=error-suggestion>";
    content += "Reload the page to try again.";
    content += "</p>";
    
    loadinginfo.innerHTML = content;
    
}

/**
* Loads the timetable or displays an error message, depending 
* on the HTTP status of the client.
*/
function checkResponse(client, loadinginfo) {
    
    if (client.status === 200) {
        showInitialSelection(client.responseText, loadinginfo);
    }
    else {
        const message = client.status + " - " + client.statusText;
        showError(loadinginfo, message);
    }
}

/**
* Shows an initial toolbar with date & time selection 
* and a "submit" button. Selecting a day is mandatory, selecting
* a time is not.
*/
function showInitialSelection(text, loadinginfo) {

    const data = JSON.parse(text);

    const datepicker = document.getElementById("datepicker");
    const timepicker = document.getElementById("timepicker");

    updateDatepicker(datepicker, data);
    updateTimePicker(timepicker, datepicker, data); 

    datepicker.onchange = function() { 
        updateTimePicker(timepicker, datepicker, data); 
    }   

    const toolbar = document.getElementById("toolbar")
    toolbar.style.visibility = "visible";

    const showButton = document.getElementById("show-timetable");
    showButton.onclick = function() {
        switchToTimetableView(showButton, datepicker, timepicker, loadinginfo, data);
    }
}

/**
* Switches the layout of the page and shows the timetable.
*
* The submit button is hidden at this point - the timetable is updated directly
* on a change of value in the toolbar elements.
*
* A filter element is configured and added to the toolbar.
*/
function switchToTimetableView(showButton, datepicker, timepicker, loadinginfo, data) {

    /*
        Show the timetable:
            - hide loading info
            - change root layout
            - build timetable
    */

    loadinginfo.style.display = "none";
    document.getElementById("root-container").className = "timetable-container";
    showTimetable(datepicker.value, timepicker.value, data);

    /*
        Change toolbar behaviour:
          - remove show button
          - update timetable on select-box change
          - show filter radio set, update timetable on radio change
    */

    showButton.style.display = "none";

    var filter = filterAll;

    datepicker.onchange = function() {
        updateTimePicker(timepicker, datepicker, data);
        showTimetable(datepicker.value, timepicker.value, data, filter);
    }

    timepicker.onchange = function() {
        showTimetable(datepicker.value, timepicker.value, data, filter);
    }

    function applyFilter() {

        var value = null;
        // Is there an easier way to get the checked radio button than looping?
        for (const item of document.getElementsByName("filter")) {
            if (item.checked) {
                value = item.value;
                break;
            }
        }

        switch(value) {
            case "papers": filter = filterPapers; break;
            case "other": filter = filterOther; break;
            default: filter = filterAll;
        }

        showTimetable(datepicker.value, timepicker.value, data, filter);

    }

    for (const item of document.getElementsByName("filter")) {
        item.onchange = applyFilter;
    }

    const filterSelection = document.getElementById("filter-selection");
    filterSelection.style.display = "block";

}

function filterAll() {
    return true;
}

function filterPapers(session) {
    return session.type === "paper";
}

function filterOther(session) {
    return session.type !== "paper";
}


/** 
* Update the options for the date select using the scheduling data.
*/
function updateDatepicker(datepicker, data) {

    var content = "";

    // I only noticed on re-reading the assignment that this
    // isn't supposed to be an option.
    content += "<option value=any>Any</option>";

    for (const dayID in data) {

        content += '<option value="';
        content += dayID;
        content += '">' + new Date(data[dayID].date).toDateString();
        content += "</option>";

    }

    datepicker.innerHTML = content;
    
}

/** 
* Update the options for the time select using the scheduling data,
* given a date selected.
*/
function updateTimePicker(timepicker, datepicker, data) {

    var content = "<option value=any>Any</option>";

    if (datepicker.value !== "any") {

        const day = data[datepicker.value];

        for (const slotID in day.slots) {
            const slot = day.slots[slotID];

            if (slot.sessions.length > 0){
                content += '<option value="' + slotID + '">';
                content += slot.time + "</option>";
            }
        }

    }

    timepicker.innerHTML = content;

}

/*

    CREATING THE TIMETABLE
    
    (This is done every time a new day/time/filter is selected)

*/

/** 
* Construct the timetable given a day, slot and filter predicate for sessions
* The day or slot can be "any", this will mean all items of that type are shown.
*/
function showTimetable(dayID, slotID, data, filter) {

    var content = "";

    if (dayID === "any") {
        for (const day of data) {
            content += createDay(day, slotID, filter);
        }   
    }
    else {
        content += createDay(data[dayID], slotID, filter);
    }

    const timetable = document.getElementById("timetable");
    
    timetable.innerHTML = content;

}

/**
* Create a html string for a list element corresponding to a day. Optionally
* restrict the output to a specific time and with a filter predicate for the sessions.
*/
function createDay(data, slotID, filter) {

    var content = "<li class=day>";

    content += "<h2 class=day-title>";
    content += data.date + " - " + data.day;
    content += "</h2>";

    var items = "";
    
    if (slotID === "any") {
        for (const slotID in data.slots) {
            const slot = data.slots[slotID];
            items += createSlot(slot, filter);   
        }   
    } else {
        const slot = data.slots[slotID];
        items += createSlot(slot, filter);
    }
    
    if (items === "") {
        content += "<li class=message-slot><p>"
        content += "No sessions found of the requested type."
        content += "</p></li>"
    }
    else {
        content += items;
    }

    content += "</li>";
    return content;

}

/**
* Create a html string for an element corresponding to a slot. 
* Optionally restrict the output with a filter predicate for the sessions.
* If no sessions exist after filtering, and empty string is returned.
*/
function createSlot(slot, filter) {

    var sessions = slot.sessions;
    if (filter !== undefined) {
        sessions = sessions.filter(filter);
    }

    if (sessions.length === 0) {
        // Don't show time slots with no sessions
        return "";
    }

    var content = "<div class=slot><h3 class=time>";
    content += slot.time;
    content += "</h3>";

    content += "<ul class=sessions>";

    for (const session of sessions) {
        content += createSession(session);
    }

    content += "</ul></div>";   
    return content;

}

/**
* Create a html string for a list element corresponding to a single session - 
* this includes both the "title" element that is always displayed, and
* and the "more info" element that is only displayed when the title is clicked on.
*/
function createSession(session) {

    var content = "<li class=session onclick=\"toggleSubmissionDetails(this)\">";

    content += "<div class=session-header>";

    content += "<h4 class=session-title>" + session.title + "</h4>";

    content += "<p class=session-info>"
    content += " - <span class=session-type>" + session.type + "</span> ";
    content += " - <span class=session-time>" + session.time + "</span> ";
    content += " - <span class=session-location>" + session.room + "</span>";
    content += " - </p>";

    content += "</div>";

    content += "<div class=submissions>";

    if (session.submissions.length > 0) {

        content += "<h5 class=submissions-title>Submissions</h5>";
        content += "<ul>";

        for (const submission of session.submissions) {

            content += createSubmission(submission);

        }

        content += "</ul>";

    }
    else {
        content += "<h5 class=submissions-title>(There are no submissions for this session)</h5>";
    }

    content += "</div>";

    content += "</li>";
    return content;

}

/**
* Create a html string for a list element corresponding to a single submission.
*/
function createSubmission(submission) {

    var content = "<li class=submission>";
    content += "<h5 class=submission-title>" + submission.title + "</h5>";
    content += "<p class=submission-info>";
    content += "<a class=submission-doi target=_blank href=\"" + submission.doiUrl + "\">" + submission.doi + "</a>";
    content += "</p>";
    content += "</li>";
    return content;

}

/*

    SHOWING MORE INFO
    
    Each session element has a hidden "submissions" element 
    with more detail on the session.
    
    When the session is clicked on that element should become visible.

*/


// Only one submissions element should be visible at one time.
// This will keep track of the current visible element.
var lastOpen = null;

// eslint does not know that this next function is used in the js-written html above.
/* eslint-disable no-unused-vars */

/**
* Searches for a subelement of the given element
* with the "submissions" class. Toggles that subelement's visibility.
* Hides the previous element made visible using this method, if one exists.
*/
function toggleSubmissionDetails(element) {

/* eslint-enable no-unused-vars */

    const candidates = element.getElementsByClassName("submissions");

    if (candidates.length == 0)
        return;

    const details = candidates[0];

    if (details.style.display == "block") {

        details.style.display = "none";

        const parent = details.parentElement;
        const parentPos = parent.getBoundingClientRect();

        /*
            The behaviour here is a bit subtle: if the block is big and is then collapsed,
            we might want to scroll back to the top after collapsing so that the user isn't
            thrown down the page. However, in the case that the user is already near back,
            we do not want a small disorienting jump.
        */

        if (parentPos.top < 0) {

            /*
                Note that while some browsers do not support
                the object defined specifics, the default fallback they do support
                of scrolling to top is acceptable in this use case.
            */

            details.parentElement.scrollIntoView({
                behaviour: "smooth",
                block: "center",
                inline: "center"
            });

        }

    }
    else {

        if (lastOpen != null) {
            lastOpen.style.display = "none";
        }

        details.style.display = "block";
        lastOpen = details;

    }

}