function compareNums(num1, num2) {
  console.log(`${num1} > ${num2}:`, num1 > num2);
  console.log(`${num1} >= ${num2}:`, num1 >= num2);
  console.log(`${num1} < ${num2}:`, num1 < num2);
  console.log(`${num1} <= ${num2}:`, num1 <= num2);
  console.log(`${num1} == ${num2}:`, num1 == num2);
  console.log(`${num1} === ${num2}:`, num1 === num2);
  console.log(`${num1} != ${num2}:`, num1 != num2);
  console.log(`${num1} !== ${num2}:`, num1 !== num2);
  console.log("---");
}

compareNums(5, 10);
compareNums(20, 20);
compareNums(15, "15");
