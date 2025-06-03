// userLoop ფუნქციის შექმნა
function userLoop() {
  const firstNumber = parseInt(prompt("შეიყვანეთ პირველი რიცხვი:"));
  const secondNumber = parseInt(prompt("შეიყვანეთ მეორე რიცხვი:"));

  if (isNaN(firstNumber) || isNaN(secondNumber)) {
    alert("გთხოვთ შეიყვანოთ მხოლოდ რიცხვები.");
    return;
  }

  if (firstNumber > secondNumber) {
    alert("პირველი რიცხვი უნდა იყოს ნაკლები ან თანაბარი მეორეს.");
    return;
  }

  for (let i = firstNumber; i <= secondNumber; i++) {
    console.log(i);
  }
}

window.onload = function () {
  userLoop();
};
