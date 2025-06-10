let numberList1 = [1, 2, 3, 4, 5];
let numberList2 = [6, 7];
console.log("Number List Length:", numberList1.length);
let combinedNumberList = numberList1.concat(numberList2);
console.log("Combined Number List:", combinedNumberList);

let stringList1 = ["apple", "banana", "cherry"];
let stringList2 = ["date", "fig"];
console.log("String List Length:", stringList1.length);
let combinedStringList = stringList1.concat(stringList2);
console.log("Combined String List:", combinedStringList);

let mixedList1 = [1, "hello", 3.14, true];
let mixedList2 = ["world", false];
console.log("Mixed List Length:", mixedList1.length);
let combinedMixedList = mixedList1.concat(mixedList2);
console.log("Combined Mixed List:", combinedMixedList);

console.log("\n🎯 განსხვავებები სიებს შორის:");
console.log("- Number List: შეიცავს მხოლოდ რიცხვებს");
console.log("- String List: შეიცავს მხოლოდ სტრინგებს (ტექსტებს)");
console.log("- Mixed List: შეიცავს სხვადასხვა ტიპის მონაცემებს ერთ სია-ში");
