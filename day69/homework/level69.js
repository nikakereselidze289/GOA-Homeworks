// 1. Determine if a number is even or odd
let number = 4; // Example number
let evenOddResult = number % 2 === 0 ? "Even" : "Odd";
document.getElementById(
  "even-odd"
).textContent = `Number: ${number} is ${evenOddResult}`;

// 2. Assign a grade based on a score
let score = 85; // Example score
let grade;
if (score >= 90) {
  grade = "A";
} else if (score >= 80) {
  grade = "B";
} else if (score >= 70) {
  grade = "C";
} else if (score >= 60) {
  grade = "D";
} else {
  grade = "Fail";
}
document.getElementById(
  "grade"
).textContent = `Score: ${score} - Grade: ${grade}`;

// 3. Determine the largest among three numbers
let a = 5,
  b = 10,
  c = 7;
let largest = Math.max(a, b, c);
document.getElementById(
  "largest"
).textContent = `Numbers: ${a}, ${b}, ${c} - Largest: ${largest}`;

// 4. Check if a character is a vowel or consonant
let char = "e"; // Example character
let vowelConsonant = ["a", "e", "i", "o", "u"].includes(char.toLowerCase())
  ? "Vowel"
  : "Consonant";
document.getElementById(
  "vowel-consonant"
).textContent = `Character: ${char} is a ${vowelConsonant}`;

// 5. Check if a number is divisible by 3 and 5
let num = 15; // Example number
let divisibleResult;
if (num % 3 === 0 && num % 5 === 0) {
  divisibleResult = "Divisible by both 3 and 5";
} else if (num % 3 === 0) {
  divisibleResult = "Divisible by 3 only";
} else if (num % 5 === 0) {
  divisibleResult = "Divisible by 5 only";
} else {
  divisibleResult = "Not divisible by either";
}
document.getElementById(
  "divisible"
).textContent = `Number: ${num} - ${divisibleResult}`;

// 6. Check if a person is a child, teenager, adult, or senior based on age
let age = 25; // Example age
let ageCategory;
if (age <= 12) {
  ageCategory = "Child";
} else if (age <= 19) {
  ageCategory = "Teenager";
} else if (age <= 59) {
  ageCategory = "Adult";
} else {
  ageCategory = "Senior";
}
document.getElementById(
  "age-category"
).textContent = `Age: ${age} - Category: ${ageCategory}`;

// 7. Print numbers from 1 to 5 using a while loop
let while1to5 = [];
let i = 1;
while (i <= 5) {
  while1to5.push(i);
  i++;
}
document.getElementById("while-1-5").textContent = `Numbers: ${while1to5.join(
  ", "
)}`;

// 8. Print even numbers from 2 to 10 using a while loop
let whileEven2to10 = [];
i = 2;
while (i <= 10) {
  if (i % 2 === 0) {
    whileEven2to10.push(i);
  }
  i++;
}
document.getElementById(
  "while-even-2-10"
).textContent = `Even Numbers: ${whileEven2to10.join(", ")}`;

// 9. Print numbers from 10 down to 1 using a while loop
let while10to1 = [];
i = 10;
while (i >= 1) {
  while10to1.push(i);
  i--;
}
document.getElementById("while-10-1").textContent = `Numbers: ${while10to1.join(
  ", "
)}`;

// 10. Print numbers from 1 to 10 using a for loop
let for1to10 = [];
for (i = 1; i <= 10; i++) {
  for1to10.push(i);
}
document.getElementById("for-1-10").textContent = `Numbers: ${for1to10.join(
  ", "
)}`;

// 11. Print the first 5 multiples of 3 using a for loop
let multiplesOf3 = [];
for (i = 1; i <= 5; i++) {
  multiplesOf3.push(i * 3);
}
document.getElementById(
  "multiples-3"
).textContent = `Multiples of 3: ${multiplesOf3.join(", ")}`;

// 12. Print numbers from 10 to 1 in reverse using a for loop
let reverse10to1 = [];
for (i = 10; i >= 1; i--) {
  reverse10to1.push(i);
}
document.getElementById(
  "for-reverse-10-1"
).textContent = `Numbers: ${reverse10to1.join(", ")}`;

// 13. Print all even numbers between 1 and 20 using a for loop
let evenNumbers1to20 = [];
for (i = 2; i <= 20; i += 2) {
  evenNumbers1to20.push(i);
}
document.getElementById(
  "even-1-20"
).textContent = `Even Numbers: ${evenNumbers1to20.join(", ")}`;

// 14. Print the sum of numbers from 1 to 5 using a for loop
let sum1to5 = 0;
for (i = 1; i <= 5; i++) {
  sum1to5 += i;
}
document.getElementById("sum-1-5").textContent = `Sum: ${sum1to5}`;
