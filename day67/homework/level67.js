// 1. Object Manipulation
const person = {
  name: "John",
  age: 30,
  city: "New York",
};

person.country = "USA";
person.address = { street: "123 Main St", city: "New York" }; // Nested object
person.age = 31;

document.getElementById("object-demo").innerHTML = `
  <strong>Original Object:</strong> ${JSON.stringify(person, null, 2)}
`;

const a = 15,
  b = 20;
document.getElementById("logic-demo").innerHTML = `
  <strong>Logical AND (a > 10 && b > 10):</strong> ${a > 10 && b > 10}<br>
  <strong>Logical OR (a > 10 || b > 10):</strong> ${a > 10 || b > 10}<br>
  <strong>Logical NOT (!true):</strong> ${!true}<br>
  <strong>Combined Expression (a > 10 && b > 10 || !false):</strong> ${
    (a > 10 && b > 10) || !false
  }
`;

const num = 123;
const bool = true;
const strNum = "456";
const nonNumericStr = "Hello";

document.getElementById("type-conversion-demo").innerHTML = `
  <strong>Number to String:</strong> ${String(num)}<br>
  <strong>Boolean to String:</strong> ${String(bool)}<br>
  <strong>String to Number:</strong> ${Number(strNum)}<br>
  <strong>Boolean to Number:</strong> ${Number(bool)}<br>
  <strong>Non-numeric String to Number:</strong> ${Number(nonNumericStr)}
`;
