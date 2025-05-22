document.getElementById("navbar").innerHTML = await (
  await fetch("level66.html")
).text();
document.getElementById("header").innerHTML = await (
  await fetch("level66.html")
).text();
document.getElementById("footer").innerHTML = await (
  await fetch("level66.html")
).text();ml

const num1 = 5,
  num2 = 10;
document.getElementById("comparison-result").innerHTML = `
  num1 == num2: ${num1 == num2}<br>
  num1 > num2: ${num1 > num2}<br>
  num1 <= num2: ${num1 <= num2}<br>
  num1 != num2: ${num1 != num2}<br>
  num1 >= 100: ${num1 >= 100}
`;

document.getElementById("confirm-btn").addEventListener("click", () => {
  const result = confirm("Do you want to proceed?");
  document.getElementById(
    "confirm-result"
  ).textContent = `User confirmed: ${result}`;
});

document.getElementById("user-form").addEventListener("submit", (event) => {
  event.preventDefault();
  console.log("Username:", event.target.username.value);
});

document.getElementById("clear-email").addEventListener("click", () => {
  document.getElementById("email").value = "";
});

document.getElementById("alert-phone").addEventListener("click", () => {
  alert("Phone number: " + document.getElementById("phone").value);
});
