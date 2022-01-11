function refreshSuiviData() {$("#updContent").load(document.URL + "?refresh");}
setInterval(refreshSuiviData, 60000);