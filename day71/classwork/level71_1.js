let randomNumber = Math.floor(Math.random() * 100) + 1;

function checkGuess() {
  const userGuess = parseInt(document.getElementById("guess").value);
  const message = document.getElementById("message");

  if (userGuess < randomNumber) {
    message.textContent = "თქვენი რიცხვი ნაკლებია!";
  } else if (userGuess > randomNumber) {
    message.textContent = "თქვენი რიცხვი მეტია!";
  } else {
    alert("გილოცავ, თქვენ მოიგეთ!");
    message.textContent = "";
    randomNumber = Math.floor(Math.random() * 100) + 1;
  }
}
