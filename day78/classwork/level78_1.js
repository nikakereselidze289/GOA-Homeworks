const container = document.getElementById("container");

for (let i = 1; i <= 5; i++) {
  // შექმენით ახალი <p> ელემენტი
  const p = document.createElement("p");

  p.textContent = `ეს არის ${i}-ე პარაგრაფი.`;

  container.appendChild(p);
}
