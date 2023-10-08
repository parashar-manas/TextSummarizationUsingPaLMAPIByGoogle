// You can add custom JavaScript code here if needed for client-side interactions.
// Add a click event listener to a button with the ID "myButton."
document.addEventListener("DOMContentLoaded", function () {
  const myButton = document.getElementById("myButton");
  if (myButton) {
    myButton.addEventListener("click", function () {
      // Perform some action when the button is clicked.
      alert("Button clicked!");
    });
  }
});
