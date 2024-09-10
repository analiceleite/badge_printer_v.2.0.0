import { loadingButton, resetButton } from "../utils/loadingButton.js";
import { completeHandler } from "../utils/completeHandler.js";

$(document).ready(function () {
  $("#importForm").on("submit", function (event) {
    submitImportForm(event);
  });
});

function submitImportForm(event) {
  event.preventDefault();
  loadingButton('uploadButton', 'Enviando...');

  var form = $("#importForm")[0];
  var formData = new FormData(form);

  $.ajax({
    type: "POST",
    url: form.action,
    data: formData,
    dataType: "json",
    processData: false,
    contentType: false,
    complete: function (xhr) {
      resetButton('uploadButton', 'Enviar');
      var data = JSON.parse(xhr.responseText);
      completeHandler(data);
    },
    error: function(error) {
      console.error("Erro ao enviar formulário:", error)
      resetButton('uploadButton', 'Enviar');
    }
  });
}
