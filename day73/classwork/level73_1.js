function modifyContent() {
  const div = document.getElementById("myDiv");
  const button = document.getElementById("myButton");
  const paragraph = document.getElementById("myParagraph");

  div.removeChild(button);

  const italicElement = document.createElement("i");
  italicElement.textContent = "ეს არის ახალი ტექსტი <i> ტეგში.";

  div.replaceChild(italicElement, paragraph);
}

window.onload = modifyContent;
