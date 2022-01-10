function updatePage(data) {
    $("#updContent").innerHTML(data.result);
}

function refreshSuiviData() {
    $.getJSON(
        document.URL + '?refresh',
        {},
        updatePage(data)
    );
}

setInterval(refreshSuiviData, 500);