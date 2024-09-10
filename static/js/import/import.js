import { handleMessage } from "../utils/handleMessage.js";

$(document).ready(function () {
  const spreadsheetInput = document.getElementById("spreadsheet");
  const pictureInput = document.getElementById("picture");
  const uploadButton = document.getElementById("uploadButton");

  function isValidFileFormat(input, validExtensions) {
    const fileName = input.value.toLowerCase();
    return validExtensions.some((ext) => fileName.endsWith(ext));
  }

  function updateButtonState() {
    const isSpreadsheetFilled =
      spreadsheetInput.files.length > 0 &&
      isValidFileFormat(spreadsheetInput, [".xlsx"]);
    const isPictureFilled =
      pictureInput.files.length > 0 &&
      isValidFileFormat(pictureInput, [".zip"]);

    if (isSpreadsheetFilled && isPictureFilled) {
      uploadButton.disabled = false;
      uploadButton.style.backgroundColor = "#56b0ff";
    } else {
      uploadButton.disabled = true;
      uploadButton.style.backgroundColor = "#4E5256";
    }
  }

  function updateInputState(input) {
    const isValid =
      input.files.length > 0 &&
      isValidFileFormat(
        input,
        input === spreadsheetInput ? [".xlsx"] : [".zip"]
      );
    if (input.nextElementSibling) {
      input.nextElementSibling.style.backgroundColor = isValid ? "#449571" : "";
    }
    return isValid;
  }

  function validateInputs() {
    let isValid = true;
    if (!isValidFileFormat(spreadsheetInput, [".xlsx"])) {
      handleMessage(
        "statusMessage",
        "error",
        "Por favor, envie um arquivo de colaboradores no formato .xlsx."
      );
      isValid = false;
    }
    if (!isValidFileFormat(pictureInput, [".zip"])) {
      handleMessage(
        "statusMessage",
        "error",
        "Por favor, envie um arquivo de imagens no formato .zip."
      );
      isValid = false;
    }
    return isValid;
  }

  spreadsheetInput.addEventListener("change", function () {
    const isSpreadsheetValid = updateInputState(spreadsheetInput);
    updateButtonState();
    if (!isSpreadsheetValid) {
      handleMessage(
        "statusMessage",
        "error",
        "Por favor, envie um arquivo de colaboradores no formato .xlsx."
      );
    }
  });

  pictureInput.addEventListener("change", function () {
    const isPictureValid = updateInputState(pictureInput);
    updateButtonState();
    if (!isPictureValid) {
      handleMessage(
        "statusMessage",
        "error",
        "Por favor, envie um arquivo de imagens no formato .zip."
      );
    }
  });

  uploadButton.addEventListener("click", function (event) {
    if (!validateInputs()) {
      event.preventDefault();
      handleMessage(
        "statusMessage",
        "error",
        "Por favor, envie os arquivos antes de tentar enviar o formulário."
      );
    }
  });

  updateButtonState();
});
