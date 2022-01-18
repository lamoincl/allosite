function refreshSuiviData() {$("#updContent").load(document.URL + "?refresh");}
setInterval(refreshSuiviData, 60000);

function copyNumPay() {
    copyText = document.getElementById("numPay");

  /* Select the text field */
  copyText.select();
  copyText.setSelectionRange(0, 99999); /* For mobile devices */

   /* Copy the text inside the text field */
  navigator.clipboard.writeText(copyText.value);
}

function copyCmdId() {
    copyText = document.getElementById("cmdId");

  /* Select the text field */
  copyText.select();
  copyText.setSelectionRange(0, 99999); /* For mobile devices */

   /* Copy the text inside the text field */
  navigator.clipboard.writeText(copyText.value);
}