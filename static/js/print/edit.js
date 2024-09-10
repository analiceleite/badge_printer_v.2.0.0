import { showModal, hideModal } from "../utils/modal_controller.js";
import { completeHandler } from "../utils/completeHandler.js";
import { loadingButton, resetButton } from '../utils/loadingButton.js'

$(document).ready(function () {
  setupEditButtons();
  $("#editCollaboratorForm").on("submit", function (event) {
    submitEditForm(event);
  });
});

function setupEditButtons() {
  $(".table").on("click", ".edit-btn", function () {
    var collaboratorID = $(this).data("collaborator-id");
    getCollaboratorData(collaboratorID);
  });
  $("#cancelEditBtn").on("click", function () {
    hideModal("editCollaboratorModal");
  });
}

function submitEditForm(event) {
  event.preventDefault();

  loadingButton('saveButton', "Salvando...")

  var form = $("#editCollaboratorForm")[0];
  var formData = new FormData(form);
  $.ajax({
    type: "POST",
    url: form.action,
    data: formData,
    dataType: "json",
    processData: false,
    contentType: false,
    complete: function (xhr) {
      resetButton('saveButton', 'Salvar')
      var data = JSON.parse(xhr.responseText);
      completeHandler(data);
    },
  });
}

function getCollaboratorData(collaboratorID) {
  $.ajax({
    url: `get_collaborator_data/${collaboratorID}`,
    method: "GET",
    success: function (data) {
      $("#editCollaboratorId").val(data.id);
      $("#editName").val(data.name);
      $("#editTreatmentName").val(data.treatment_name);
      $("#editEdv").val(data.edv);
      $("#editCity").val(data.city);
      $("#photo").attr("data-current-photo", data.photo);
      showModal("editCollaboratorModal");
    },
  });
}