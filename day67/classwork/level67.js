const person = {
  name: "გიორგი",
  surname: "მაკარაშვილი",
  academy: "Tbilisi State University",
  city: "თბილისი",
  role: "Student",
  favColor: "blue",

  fullName: function () {
    console.log(this.name + " " + this.surname);
  },

  getFavColor: function () {
    console.log(this.favColor);
  },
};

console.log(person);

console.log(person.name);

person.fullName();
person.getFavColor();

person.favColor = "red";
console.log(person.favColor);
