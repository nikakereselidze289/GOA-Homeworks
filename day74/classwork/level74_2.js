const link = document.getElementById("myLink");

link.addEventListener("pointerover", function (e) {
  const target = e.target;

  for (let attr of target.attributes) {
    console.log(`${attr.name} = ${attr.value}`);
  }

  console.log(target);
});
