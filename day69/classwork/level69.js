function discountFunc() {
  let age = document.getElementById("age").value;

  let discount;
  if (age < 18) {
    discount = "20%";
  } else if (age >= 18 && age < 65) {
    discount = "5%";
  } else {
    discount = "10%";
  }

  document.getElementById(
    "result"
  ).textContent = `Your discount is: ${discount}`;
}
