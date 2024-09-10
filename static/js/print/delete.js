import { showModal, hideModal } from "../utils/modal_controller.js";
import { completeHandler } from "../utils/completeHandler.js";

$(document).ready(function () {
  setupDeleteButtons();
  $("#deleteCollaboratorForm").on("submit", function (event) {
    submitDeleteForm(event);
  });
});

function submitDeleteForm(event) {
  event.preventDefault();
  var form = $("#deleteCollaboratorForm")[0];
  var formData = new FormData(form);
  $.ajax({
    type: "POST",
    url: form.action,
    data: formData,
    dataType: "json",
    processData: false,
    contentType: false,
    complete: function (xhr) {
      var data;
      data = JSON.parse(xhr.responseText);
      completeHandler(data);
    },
  });
}

function setupDeleteButtons() {
  $(".table").on("click", ".delete-btn", function () {
    var collaboratorID = $(this).data("collaborator-id");
    $("#deleteCollaboratorID").val(collaboratorID);
    showModal("confirmDeleteModal");
  });
  $("#cancelDeleteBtn").on("click", function () {
    hideModal("confirmDeleteModal");
  });
}
