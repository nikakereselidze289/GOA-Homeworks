function centerText() {
  let paragraph = document.getElementById("myParagraph");
  paragraph.style.textAlign = "center";
}

let paragraph = document.getElementById("myParagraph");
paragraph.onmouseover = centerText;
