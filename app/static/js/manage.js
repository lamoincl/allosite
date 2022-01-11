function updateStatus(element, status) {
    let cmdId = element.parentElement.id
    let mainInfo = document.querySelector("#main-info-" + cmdId)
    let statusElement = mainInfo.querySelector(".status")

    $.get("/change-status/" + cmdId + "/" + status, function (){
        $(statusElement).load("/refresh-status/" + cmdId);
    });
}