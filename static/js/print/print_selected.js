import { loadingButton, resetButton } from "../utils/loadingButton.js";
import { completeHandler } from "../utils/completeHandler.js";
import { handleMessage } from "../utils/handleMessage.js";

$(document).ready(function () {
  $("#printSelectedBtn").click(function () {
    console.log("Detectou o click");
    $("#printForm").submit();
  });

  $("#printForm").on("submit", function (event) {
    console.log("Detectou");
    printSelectedBadges(event);
  });
});

function printSelectedBadges(event) {
  console.log("Entrou em print");
  event.preventDefault();

  if (!$("input[name='selected_badges']:checked").length) {
    handleMessage(
      "statusMessage",
      "error",
      "Selecione um colaborador para imprimir."
    );
    return;
  }

  loadingButton('printSelectedBtn', 'Imprimindo...');

  setTimeout(function () {
    resetButton('printSelectedBtn', 'Imprimir Selecionados')
  }, 5000)
  var form = $("#printForm")[0];
  var formData = new FormData(form);
  $.ajax({
    type: "POST",
    url: form.action,
    data: formData,
    processData: false,
    contentType: false,
    xhrFields: {
      responseType: "blob",
    },
    success: function (data) {
      console.log("a" + data);
      successHandler(data);
    },
    error: function (xhr) {
      resetButton('printSelectedBtn', 'Imprimir Selecionados');
      var data = JSON.parse(xhr.responseText);
      completeHandler(data);
    },
  });
}

function successHandler(data) {
  var blob = new Blob([data], { type: "application/pdf" });
  var url = window.URL.createObjectURL(blob);
  var iframe = createPrintFrame();
  openPrintWindow(iframe, url);
}

function createPrintFrame() {
  var iframe = document.createElement("iframe");
  iframe.style.display = "none";
  document.body.appendChild(iframe);
  return iframe;
}

function openPrintWindow(iframe, url) {
  iframe.src = url;

  iframe.onload = function () {
    var iframeWindow = iframe.contentWindow;

    if (iframeWindow) {
      iframeWindow.focus();
      iframeWindow.print();


      iframeWindow.onafterprint = function () {
        cleanup();
      };

      iframeWindow.onbeforeprint = function () {
        console.log('Impressão cancelada');
        cleanup();
      };

    } else {
      console.error("iframe.contentWindow não está definido.");
      cleanup();
    }
  };

  function cleanup() {
    window.URL.revokeObjectURL(url);
    document.body.removeChild(iframe);
    resetButton('printSelectedBtn', 'Imprimir Selecionados');
  }
}
