$(document).ready(function () {
  verifyLocalStorage();
});

function verifyLocalStorage() {
  const statusData = JSON.parse(localStorage.getItem("statusData"));
  if (statusData != null) {
    $("#statusMessage .message__text").text(statusData.message);
    $("#statusMessage").addClass(`message--${statusData.status} message--show`);

    setTimeout(function () {
      $("#statusMessage").removeClass("message--show");
    }, 4000);
    localStorage.removeItem("statusData");
  }
}
