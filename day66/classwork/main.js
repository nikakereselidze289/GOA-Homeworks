document.getElementById("myForm").addEventListener("submit", function (event) {
  event.preventDefault();
  const inputValue = document.getElementById("inputValue").value;
  alert(inputValue);
});
