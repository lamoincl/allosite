function continuer() {
    let spec_div = document.getElementById("spec");
    let common_div = document.getElementById("common");
    let hideString = 'display: none !important';

    common_div.removeAttribute("style");
    spec_div.setAttribute("style", hideString);
}

function retour() {
    let spec_div = document.getElementById("spec");
    let common_div = document.getElementById("common");
    let hideString = 'display: none !important';

    spec_div.removeAttribute("style");
    common_div.setAttribute("style", hideString);
}