export function limitDigits(fields) {
  $(document).ready(function() {
    $.each(fields, function(inputId, maxDigits) {
      var $inputField = $('#' + inputId);
      // Verifica se o inputField foi encontrado no DOM
      if ($inputField.length) {
        $inputField.on('input', function() {
          if ($inputField.val().length > maxDigits) {
            $inputField.val($inputField.val().slice(0, maxDigits)); 
          }
        });
      }
    });
  });
}