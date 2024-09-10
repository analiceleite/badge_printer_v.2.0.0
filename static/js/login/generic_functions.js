import { limitDigits } from "../utils/limit_digits.js";

$(document).ready(function () {
  var fields = {
    edv: 8,
    token: 5,
  };
  limitDigits(fields);
});

const openEye = "/static/assets/images/open_eye.png";
const closeEye = "/static/assets/images/close_eye.png";

function togglePasswordVisibility(element) {
  const passwordContainer = element.parentElement; 
  const passwordInput = passwordContainer.querySelector("input");
  const togglePasswordIcon = element.querySelector("img");

  const type = passwordInput.getAttribute("type") === "password" ? "text" : "password";
  passwordInput.setAttribute("type", type);

  const newIcon = type === "password" ? closeEye : openEye;
  togglePasswordIcon.setAttribute("src", newIcon);
}

//* Colocando a função em um escopo global
window.togglePasswordVisibility = togglePasswordVisibility;
