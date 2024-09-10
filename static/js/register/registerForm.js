import { loadingButton, resetButton } from "../utils/loadingButton.js";
import { completeHandler } from "../utils/completeHandler.js";

$(document).ready(function () {
  $("#registerForm").on("submit", function (event) {
    registerSubmit(event);
  });
});

function registerSubmit(event) {
  event.preventDefault();

  loadingButton('registerButton', 'Registrando...')

  var form = $("#registerForm")[0];
  var formData = new FormData(form);
  $.ajax({
    type: "POST",
    url: form.action,
    data: formData,
    dataType: "json",
    processData: false,
    contentType: false,
    complete: function (xhr) {
      resetButton('uploadButton', 'Registrar')
      var data = JSON.parse(xhr.responseText);
      completeHandler(data);
    },
  });
}
