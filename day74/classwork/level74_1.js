const button = document.getElementById("myButton");

button.addEventListener("click", function (event) {
  console.log(event);

  document.body.style.backgroundColor = "black";

  document.body.style.color = "white";
});
