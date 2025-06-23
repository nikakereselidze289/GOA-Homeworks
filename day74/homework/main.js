// 1. Click Alert
document.getElementById("alertButton").addEventListener("click", function() {
  alert("Hello, this is an alert!");
});

// 2. Change Text on Hover
document.getElementById("hoverText").addEventListener("mouseover", function() {
  this.innerText = "Text has been changed!";
});

document.getElementById("hoverText").addEventListener("mouseout", function() {
  this.innerText = "Hover over me to change my text!";
});

// 3. Toggle Background Color
document.getElementById("toggleDiv").addEventListener("click", function() {
  if (this.style.backgroundColor === "lightblue") {
    this.style.backgroundColor = "lightcoral";
  } else {
    this.style.backgroundColor = "lightblue";
  }
});

// 4. Log Input Value on Click
document.getElementById("inputField").addEventListener("click", function() {
  console.log("Current input value: " + this.value);
});

// 5. Show/Hide Image on Button Click
document.getElementById("toggleButton").addEventListener("click", function() {
  var img = document.getElementById("image");
  if (img.style.display === "none") {
    img.style.display = "block";
  } else {
    img.style.display = "none";
  }
});
