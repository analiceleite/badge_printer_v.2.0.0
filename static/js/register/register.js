import { handleMessage } from '../utils/handleMessage.js';

$(document).ready(function () {
  const photoInput = document.getElementById("photo");
  const photoErrorMessage = document.getElementById("photoErrorMessage");

  photoInput.addEventListener("change", function () {
    const file = photoInput.files[0];
    const validFormats = ["image/png", "image/jpeg"];
    const fileInput = photoInput;

    if (file) {
      if (validFormats.includes(file.type)) {
        const fileName = file.name.toLowerCase();
        const validExtensions = ["png", "jpg", "jpeg"];
        const fileExtension = fileName.split(".").pop();

        if (validExtensions.includes(fileExtension)) {
          fileInput.classList.add("valid");
          fileInput.classList.remove("invalid");
          photoErrorMessage.classList.remove("message--show"); 
        } else {
          fileInput.classList.add("invalid");
          fileInput.classList.remove("valid");
          handleMessage(
            "statusMessage",
            "error",
            "Por favor, selecione um arquivo PNG, JPG ou JPEG."
          );
          fileInput.value = "";
        }
      } else {
        fileInput.classList.add("invalid");
        fileInput.classList.remove("valid");
        handleMessage(
          "statusMessage",
          "error",
          "Por favor, selecione um arquivo PNG, JPG ou JPEG."
        );
        fileInput.value = "";
      }
    } else {
      fileInput.classList.remove("valid", "invalid");
      photoErrorMessage.classList.remove("message--show"); 
    }
  });
});
