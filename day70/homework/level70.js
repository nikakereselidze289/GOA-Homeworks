// Task 1: Print numbers from 1 to 10 using a for loop
console.log("Numbers from 1 to 10:");
for (let i = 1; i <= 10; i++) {
  console.log(i);
}

// Task 2: Print even numbers from 2 to 20 using a while loop
console.log("Even numbers from 2 to 20:");
let j = 2;
while (j <= 20) {
  console.log(j);
  j += 2;
}

// Task 3: Print numbers from 10 down to 1 using a for loop
console.log("Numbers from 10 to 1:");
for (let k = 10; k >= 1; k--) {
  console.log(k);
}

// Task 4: Print the first 5 multiples of 3 using a while loop
console.log("First 5 multiples of 3:");
let count = 1;
while (count <= 5) {
  console.log(count * 3);
  count++;
}

// Task 5: Print each character of a string using a for loop
const sampleString = "Hello";
console.log("Characters in string:");
for (let i = 0; i < sampleString.length; i++) {
  console.log(sampleString[i]);
}

// DOM Manipulation Tasks
function changeText() {
  document.getElementById("myPara").textContent = "Text has been changed!";
}

function changeBackground() {
  document.getElementById("myDiv").style.backgroundColor = "skyblue";
}

function changeFontSize() {
  document.getElementById("myHeading").style.fontSize = "36px";
}

function hideDiv() {
  document.getElementById("hideDiv").style.display = "none";
}

function showAlert() {
  alert("Hello! This is your custom message.");
}
