function compareNums(num1, num2) {
  let result;
  if (num1 > num2) {
    result = num1;
  } else if (num2 > num1) {
    result = num2;
  } else {
    result = "Numbers are equal";
  }
  document.getElementById("output").innerText = result;
}
