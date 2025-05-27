function checkNumber() {
  const number = document.getElementById("numInput").value;
  const resultElement = document.getElementById("numberResult");

  if (number > 0) {
    resultElement.innerText = "The number is positive.";
  } else if (number < 0) {
    resultElement.innerText = "The number is negative.";
  } else {
    resultElement.innerText = "The number is zero.";
  }
}

function checkVotingEligibility() {
  const age = document.getElementById("ageInput").value;
  const resultElement = document.getElementById("ageResult");

  if (age >= 18) {
    resultElement.innerText = "You can vote!";
  } else {
    resultElement.innerText = "You are not eligible to vote.";
  }
}

function compareNumbers() {
  const num1 = parseInt(document.getElementById("num1").value);
  const num2 = parseInt(document.getElementById("num2").value);
  const resultElement = document.getElementById("comparisonResult");

  if (num1 > num2) {
    resultElement.innerText = `The first number (${num1}) is larger.`;
  } else if (num2 > num1) {
    resultElement.innerText = `The second number (${num2}) is larger.`;
  } else {
    resultElement.innerText = "Both numbers are equal.";
  }
}
