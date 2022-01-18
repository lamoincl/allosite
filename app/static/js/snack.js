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
}

function continuerSnack() {
    let kebab = parseInt(document.getElementById("kebab").value);
    let burger = parseInt(document.getElementById("burger").value);
    let panini = parseInt(document.getElementById("panini").value);
    let croque = parseInt(document.getElementById("croque").value);
    let FANTA = parseInt(document.getElementById("FANTA").value);
    let COCA = parseInt(document.getElementById("COCA").value);
    let ICETEA = parseInt(document.getElementById("ICETEA").value);
    let TROPICO = parseInt(document.getElementById("TROPICO").value);
    let OASIS = parseInt(document.getElementById("OASIS").value);
    let SEVENUP = parseInt(document.getElementById("SEVENUP").value);
    let SEVENUPMOJITO = parseInt(document.getElementById("SEVENUPMOJITO").value);

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
}
