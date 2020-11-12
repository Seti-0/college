/*eslint-env es6,browser*/

window.onload = loadData;

function loadData() {

    const loadinginfo = document.getElementById("loading-info");
    loadinginfo.style.visibility = "visible";

    const progressDisplay = document.getElementById("data-load-progress");

    const client = new XMLHttpRequest();
    client.open("GET", "scheduling.json");

    client.onprogress = function(event) {
        updateProgress(event.loaded/event.total);
    }

    client.onload = function() {
        showInitialSelection(client, loadinginfo);    
    }

    client.send();

    function updateProgress(p) {
        progressDisplay.innerHTML = (p*100).toFixed(2);
    }

}

function showInitialSelection(client, loadinginfo) {

    const data = JSON.parse(client.responseText);

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
          - remote show button
          - update timetable on select box change
          - show filter radio set
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

function updateDatepicker(datepicker, data) {

    var content = "";

    // I only noticed on re-reading the assignment that this
    // isn't supposed to be an option.
    //content += "<option value=any>Any</option>";

    for (const dayID in data) {

        content += '<option value="';
        content += dayID;
        content += '">' + new Date(data[dayID].date).toDateString();
        content += "</option>";

    }

    datepicker.innerHTML = content;
}

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

function createDay(data, slotID, filter) {

    var content = "<li class=day>";

    content += "<h2 class=day-title>";
    content += data.date + " - " + data.day;
    content += "</h2>";

    if (slotID === "any") {
        for (const slotID in data.slots) {
            const slot = data.slots[slotID];
            content += createSlot(slot, filter);   
        }   
    } else {
        const slot = data.slots[slotID];
        content += createSlot(slot, filter);
    }

    content += "</li>";
    return content;

}

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

function createSubmission(submission) {

    var content = "<li class=submission>";
    content += "<h5 class=submission-title>" + submission.title + "</h5>";
    content += "<p class=submission-info>";
    content += "<a class=submission-doi target=_blank href=\"" + submission.doiUrl + "\">" + submission.doi + "</a>";
    content += "</p>";
    content += "</li>";
    return content;

}

var lastOpen = null;

/* eslint-disable no-unused-vars */
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