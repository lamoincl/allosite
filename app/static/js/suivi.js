function refreshSuiviData() {
    $.getJSON(
        document.URL + '?refresh',
        {},
        function (data) {
            $("#updContent").innerHTML(data.result);
        }
    );
}

setInterval(refreshSuiviData, 500);