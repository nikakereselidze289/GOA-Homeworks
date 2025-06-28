// 1. Countdown Timer
let countdown = 10;
const countdownInterval = setInterval(function () {
  console.log(countdown);
  countdown--;
  if (countdown < 0) {
    clearInterval(countdownInterval);
    console.log("Time's up!");
  }
}, 1000);

// 2. Flashing Title
let isHello = true;
const titleInterval = setInterval(function () {
  document.title = isHello ? "Hello" : "Goodbye";
  isHello = !isHello;
}, 1000);

setTimeout(function () {
  clearInterval(titleInterval);
}, 6000);

// 3. Move a Box (Optional DOM Task)
const box = document.getElementById("box");
box.style.width = "50px";
box.style.height = "50px";
box.style.backgroundColor = "blue";
box.style.position = "absolute";
box.style.left = "0px";

let moveDistance = 0;
const moveBoxInterval = setInterval(function () {
  moveDistance += 10;
  box.style.left = moveDistance + "px";

  if (moveDistance >= 100) {
    clearInterval(moveBoxInterval);
  }
}, 200);

// 4. Random Number Logger
let randomCount = 0;
const randomInterval = setInterval(function () {
  console.log(Math.floor(Math.random() * 10) + 1);
  randomCount++;

  if (randomCount >= 5) {
    clearInterval(randomInterval);
  }
}, 1500);

// 5. Array to Uppercase
const arr = ["apple", "banana", "cherry"];
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i].toUpperCase());
}

// 6. Replace Middle Element
const numbers = [1, 2, 3];
numbers[1] = 0;
console.log(numbers);

// 7. Add and Remove Elements
let arr2 = [1, 2];
arr2.push(3);
arr2.unshift(0);
arr2.pop();
console.log(arr2);

// 8. Average of Array
const numbers2 = [10, 20, 30, 40];
const average = numbers2.reduce((sum, num) => sum + num, 0) / numbers2.length;
console.log(average);

const arr3 = [1, 2, 3];
console.log(arr3[2]);
console.log(arr3[1]);
console.log(arr3[0]);

// 10. Loop with Index
const fruits = ["apple", "banana", "cherry", "date", "elderberry"];

for (let i = 0; i < fruits.length; i++) {
  console.log(`Index ${i}: ${fruits[i]}`);
}
