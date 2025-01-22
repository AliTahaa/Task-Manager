// script.js

document.addEventListener('DOMContentLoaded', function () {
  // Select all checkboxes on the page
  const checkboxes = document.querySelectorAll('input[type="checkbox"]');

  // Event listener for when a checkbox is checked or unchecked
  checkboxes.forEach(function (checkbox) {
    checkbox.addEventListener('change', function () {
      // Submit the form when a checkbox state changes
      document.getElementById('updateForm').submit();
    });
  });
});
