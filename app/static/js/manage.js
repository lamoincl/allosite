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

function iterateMainInfo() {
    let tr = document.getElementsByClassName("main-info")

    for (let i = 0; i < tr.length; i++) {
        dateUpdate(tr.item(i));
    }
}

function dateUpdate(element) {
    let today = new Date();
    let heure = today.getTime();
    let dixminutesavant = new Date(heure - 10 * 60 * 1000);
    let vingtminutesavant = new Date(heure - 20 * 60 * 1000);
    let d = dixminutesavant.toLocaleTimeString();
    let e = vingtminutesavant.toLocaleTimeString();
    let c = element.querySelector('.time');
    if (c < d) {
        element.style.backgroundColor = '#FFE300';
    }
    if (c < e) {
        element.style.backgroundColor = '#FF0000';
    }
}
setInterval(iterateMainInfo, 60000);