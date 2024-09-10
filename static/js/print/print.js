$(document).ready(function () {
  setupEventListeners();
});

function setupEventListeners() {
  setupSelectAllCheckboxes();
  setupSearchFilter();
  setupCheckNoResults();
}

function setupSelectAllCheckboxes() {
  $("#selectAllButton").click(function () {
    const checkboxes = $(".ticketCheckbox");
    const allChecked = checkboxes.length === checkboxes.filter(":checked").length; 

    checkboxes.prop("checked", !allChecked);
  });
}

function setupSearchFilter() {
  $("#searchInput").on("input", function () {
    const searchTerm = $(this).val().toLowerCase();
    let hasResults = false;

    $(".table tbody .table__row").each(function () {
      const rowText = $(this).text().toLowerCase();
      if (rowText.includes(searchTerm)) {
        $(this).show();
        hasResults = true;
      } else {
        $(this).hide();
      }
    });

    toggleNoResultsMessage(hasResults);
  });
}

function setupCheckNoResults() {
  const hasResults = $(".table tbody .table__row:visible").length > 0;
  toggleNoResultsMessage(hasResults);
}

function toggleNoResultsMessage(hasResults) {
  if (hasResults) {
    $(".no__results").hide();
  } else {
    $(".no__results").show();
  }
}
