function userOperations() {
  let answer1 = confirm("გსურს პირველი ოპერაცია?");
  let answer2 = confirm("გსურს მეორე ოპერაცია?");
  console.log("AND ოპერაცია:", answer1 && answer2);
  console.log("OR ოპერაცია:", answer1 || answer2);
}

window.onload = userOperations;
