function addNewElement() {
  const div = document.getElementById("myDiv");

  const button = document.createElement("button");

  const textNode = document.createTextNode("დაამატე ახალი ელემენტი");
  button.appendChild(textNode);

  div.appendChild(button);
}

window.onload = addNewElement;
