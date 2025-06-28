const myDiv = document.getElementById("myDiv");

const paras = myDiv.getElementsByTagName("p");

for (let i = 0; i < paras.length; i++) {
  paras[i].style.color = "green";
  paras[i].style.backgroundColor = "black";
}
