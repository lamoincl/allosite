function updateStatus(element, status) {
    let cmdId = element.parentElement.id
    let mainInfo = document.querySelector("#main-info-" + cmdId)
    let statusElement = mainInfo.querySelector(".status")

    function updateAndRefresh() {
        $.get("/change-status/" + cmdId + "/" + status, function (){
            $(statusElement).load("/refresh-status/" + cmdId);
        });
    }

    if (status === 'LIVRE') {
        if (confirm('Es-tu sur de vouloir mettre la commande en livré ?')) {
            updateAndRefresh();
            refreshSuiviData();
        }
    } else {
        updateAndRefresh();
    }
}