// Automatic Slideshow - change image every 4 seconds
var myIndex = 0;
carousel();

function carousel() {
  var i;
  var x = document.getElementsByClassName("mySlides");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  myIndex++;
  if (myIndex > x.length) {myIndex = 1}
  x[myIndex-1].style.display = "block";
  setTimeout(carousel, 4000);
}

// Used to toggle the menu on small screens when clicking on the menu button
function myFunction() {
  var x = document.getElementById("navDemo");
  if (x.className.indexOf("w3-show") === -1) {
    x.className += " w3-show";
  } else {
    x.className = x.className.replace(" w3-show", "");
  }
}

function onClickAppart() {
  onChangeLieu('MEUH');
}

function onClickAdresse() {
  onChangeLieu('EXTE');
}

function onChangeLieu(selectedLieu) {
  let appartInput = document.getElementById("appart");
  let appartCol = appartInput.parentElement;
  let adresseInput = document.getElementById("adresse");
  let adresseCol = adresseInput.parentElement;
  let hideString = 'display: none !important';

  if (selectedLieu === 'EXTE') {
    appartInput.removeAttribute("required");
    adresseInput.setAttribute("required", "");
    appartCol.setAttribute("style", hideString);
    adresseCol.removeAttribute("style");
  } else {
    appartInput.setAttribute("required", "");
    adresseInput.removeAttribute("required");
    appartCol.removeAttribute("style");
    adresseCol.setAttribute("style", hideString);
  }
}

// todo change this function to disapear menu in mobile format
// When the user clicks anywhere outside of the modal, close it
var modal = document.getElementById('navDemo');
window.onclick = function(event) {
  if (event.target === modal) {
    modal.style.display = "none";
  }
}