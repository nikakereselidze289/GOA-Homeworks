// Task 2: Log numbers from 1 to 5 every second, then stop.
let counter = 1;
const counterInterval = setInterval(() => {
  console.log(counter);
  counter++;
  if (counter > 5) clearInterval(counterInterval);
}, 1000);

// Task 3: Log a message every 2 seconds, stop after 10 seconds.
let messageCount = 0;
const messageInterval = setInterval(() => {
  console.log("This message is logged every 2 seconds.");
  messageCount++;
  if (messageCount >= 5) clearInterval(messageInterval); // Stop after 10 seconds (5 * 2 = 10)
}, 2000);

// Task 4: Change background color every 3 seconds, stop after 5 changes.
const colors = [
  "lightblue",
  "lightgreen",
  "lightcoral",
  "lightyellow",
  "lightpink",
];
let colorChangeCount = 0;
const colorInterval = setInterval(() => {
  document.body.style.backgroundColor = colors[colorChangeCount];
  colorChangeCount++;
  if (colorChangeCount >= 5) clearInterval(colorInterval);
}, 3000);

// Task 5: Display the current time every second, stop after 15 seconds.
let timeCount = 0;
const timeInterval = setInterval(() => {
  const now = new Date();
  console.log(now.toLocaleTimeString());
  timeCount++;
  if (timeCount >= 15) clearInterval(timeInterval); // Stop after 15 seconds
}, 1000);

// Task 6: Simple timer that counts up to 10 seconds.
let timer = 0;
const timerInterval = setInterval(() => {
  console.log(`Timer: ${timer} seconds`);
  timer++;
  if (timer >= 10) clearInterval(timerInterval); // Stop after 10 seconds
}, 1000);

// Task 7: Create an array of 4 numbers and log the value of the second element.
const numbersArray = [10, 20, 30, 40];
console.log("Second element:", numbersArray[1]); // Logs: 20

// Task 8: Change the value of the first element in an array to 100 and log the entire array.
numbersArray[0] = 100;
console.log("Updated array:", numbersArray); // Logs: [100, 20, 30, 40]

// Task 9: Create an array of 3 strings and log each one using individual console.log().
const stringArray = ["apple", "banana", "cherry"];
console.log("First element:", stringArray[0]); // Logs: apple
console.log("Second element:", stringArray[1]); // Logs: banana
console.log("Third element:", stringArray[2]); // Logs: cherry

// Task 10: Create an array of 5 numbers and find the sum of the first and last elements.
const numArray = [5, 10, 15, 20, 25];
const sum = numArray[0] + numArray[numArray.length - 1];
console.log("Sum of first and last element:", sum); // Logs: 30 (5 + 25)
