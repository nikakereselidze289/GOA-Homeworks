document.getElementById("myForm").onsubmit = function (event) {
  event.preventDefault();
  console.log(document.getElementById("userInput").value);
};
