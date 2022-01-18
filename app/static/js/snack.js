function preventZero() {
    let kebab = document.getElementById("kebab");
    let burger = document.getElementById("burger");
    let panini = document.getElementById("panini");
    let croque = document.getElementById("croque");
    let FANTA = document.getElementById("FANTA");
    let COCA = document.getElementById("COCA");
    let ICETEA = document.getElementById("ICETEA");
    let TROPICO = document.getElementById("TROPICO");
    let OASIS = document.getElementById("OASIS");
    let SEVENUP = document.getElementById("SEVENUP");
    let SEVENUPMOJITO = document.getElementById("SEVENUPMOJITO");
    let vals = [kebab, burger, panini, croque, FANTA, COCA, ICETEA, TROPICO, OASIS, SEVENUP, SEVENUPMOJITO];

    for (let val of vals) {
        if (val.value === "") {
            val.value = "0";
        }
    }

}

function updateBoisson() {
    let kebab = parseInt(document.getElementById("kebab").value) || 0;
    let burger = parseInt(document.getElementById("burger").value) || 0;
    let panini = parseInt(document.getElementById("panini").value) || 0;
    let croque = parseInt(document.getElementById("croque").value) || 0;
    let FANTA = parseInt(document.getElementById("FANTA").value) || 0;
    let COCA = parseInt(document.getElementById("COCA").value) || 0;
    let ICETEA = parseInt(document.getElementById("ICETEA").value) || 0;
    let TROPICO = parseInt(document.getElementById("TROPICO").value) || 0;
    let OASIS = parseInt(document.getElementById("OASIS").value) || 0;
    let SEVENUP = parseInt(document.getElementById("SEVENUP").value) || 0;
    let SEVENUPMOJITO = parseInt(document.getElementById("SEVENUPMOJITO").value) || 0;

    let menu_number = kebab+ burger + panini + croque;
    let boisson_number = FANTA + COCA + ICETEA + TROPICO + OASIS + SEVENUP + SEVENUPMOJITO;
    let boisson_restante = menu_number - boisson_number;
    let boisson_i = document.getElementById("boisson");

    boisson_i.innerHTML = boisson_restante.toString() + " boisson(s) à choisir";
    preventZero();
}

function updatePrix() {
    let kebab = parseInt(document.getElementById("kebab").value) || 0;
    let burger = parseInt(document.getElementById("burger").value) || 0;
    let panini = parseInt(document.getElementById("panini").value) || 0;
    let croque = parseInt(document.getElementById("croque").value) || 0;
    let prix_kebab = 6.5
    let prix_burger = 6
    let prix_panini = 5
    let prix_croque = 4.5
    let prix_commande = (kebab * prix_kebab) + (burger * prix_burger) + (panini * prix_panini) + (croque * prix_croque);
    let prix_i = document.getElementById("prix");
    let prix_input = document.getElementById("input-prix");

    updateBoisson();
    prix_i.innerHTML = prix_commande.toString();
    prix_input.value = prix_commande;
    preventZero();
}

function continuerSnack() {
    let kebab = parseInt(document.getElementById("kebab").value) || 0;
    let burger = parseInt(document.getElementById("burger").value) || 0;
    let panini = parseInt(document.getElementById("panini").value) || 0;
    let croque = parseInt(document.getElementById("croque").value) || 0;
    let FANTA = parseInt(document.getElementById("FANTA").value) || 0;
    let COCA = parseInt(document.getElementById("COCA").value) || 0;
    let ICETEA = parseInt(document.getElementById("ICETEA").value) || 0;
    let TROPICO = parseInt(document.getElementById("TROPICO").value) || 0;
    let OASIS = parseInt(document.getElementById("OASIS").value) || 0;
    let SEVENUP = parseInt(document.getElementById("SEVENUP").value) || 0;
    let SEVENUPMOJITO = parseInt(document.getElementById("SEVENUPMOJITO").value) || 0;

    let menu_number = kebab+ burger + panini + croque;
    let boisson_number = FANTA + COCA + ICETEA + TROPICO + OASIS + SEVENUP + SEVENUPMOJITO;
    let box_alert = document.getElementById("snack-alert");

    if (menu_number === boisson_number && menu_number !== 0) {
        continuer();
    } else {
        box_alert.removeAttribute("style")
        if (menu_number > boisson_number) {
            box_alert.innerHTML = "Il manque " + (menu_number - boisson_number) + " boisson(s) à prendre !"
        } else if (menu_number < boisson_number) {
            box_alert.innerHTML = "Il y a  " + (boisson_number - menu_number) + " boisson(s) en trop !"
        } else {
            box_alert.innerHTML = "Il ne peut pas avoir 0 menu commandé !"
        }
    }
    preventZero();
}
