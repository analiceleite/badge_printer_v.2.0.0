$(document).ready(function () {
  $("#password-form").on("submit", function (event) {

    var newPassword = $("#newPassword").val();
    var confirmPassword = $("#confirmPassword").val();
    var errorMessage = $(".errorMessage");

    if (newPassword !== confirmPassword) {
      errorMessage.show();
      event.preventDefault();
    } else {
      errorMessage.hide();
    }
  });
});
