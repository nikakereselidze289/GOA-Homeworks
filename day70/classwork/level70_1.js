s; // changeElements ფუნქცია
function changeElements() {
  const inputValue = document.getElementById("inputField").value;
  console.log("input-ის მნიშვნელობა: " + inputValue);

  const button = document.getElementById("changeButton");
  button.style.backgroundColor = "black";
  button.style.color = "white";

  const title = document.getElementById("title");
  title.style.textAlign = "center";

  document.body.style.backgroundColor = "green";
}

document
  .getElementById("changeButton")
  .addEventListener("click", changeElements);
