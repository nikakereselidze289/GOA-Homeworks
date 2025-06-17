// 1. Create a <p> element and add it to the body
const p = document.createElement("p");
p.textContent = "This is a new paragraph.";
document.body.appendChild(p);

// 2. Create an <h1> element with text and append it to a <div>
const h1 = document.createElement("h1");
h1.textContent = "Welcome to My Page";
const div = document.querySelector("div");
div.appendChild(h1);

// 3. Create an <img> element, set its src, and add it to the page
const img = document.createElement("img");
img.src = "https://wallpapercat.com/w/full/0/f/3/5815630-3840x2160-desktop-hd-4k-wallpaper-image.jpg";
img.alt = "Placeholder Image";
document.body.appendChild(img);

// 4. Create a <button> element with text and add it to the body
const button = document.createElement("button");
button.textContent = "Click me";
document.body.appendChild(button);

// 5. Create a <ul> element and add three <li> items to it
const ul = document.createElement("ul");
["Item 1", "Item 2", "Item 3"].forEach((text) => {
  const li = document.createElement("li");
  li.textContent = text;
  ul.appendChild(li);
});
document.body.appendChild(ul);

// 6. Select a <div> with id content and remove its first child element
const content = document.getElementById("content");
const firstChild = content.firstElementChild;
content.removeChild(firstChild);

// 7. Create a <ul> with three <li> items, then remove the last <li>
const newUl = document.createElement("ul");
["Item A", "Item B", "Item C"].forEach((text) => {
  const li = document.createElement("li");
  li.textContent = text;
  newUl.appendChild(li);
});
document.body.appendChild(newUl);
const lastLi = newUl.lastElementChild;
newUl.removeChild(lastLi);

// 8. Create a new <p> element and replace an existing <p> inside a <div> with id textContainer
const textContainer = document.getElementById("textContainer");
const oldP = textContainer.querySelector("p");
const newP = document.createElement("p");
newP.textContent = "This is the new paragraph.";
textContainer.replaceChild(newP, oldP);

// 9. Replace a <button> inside a <div> with a new <span> element
const oldButton = textContainer.querySelector("button");
const newSpan = document.createElement("span");
newSpan.textContent = "This is a span.";
textContainer.replaceChild(newSpan, oldButton);

// 10. Find a <ul> with one <li> and replace that <li> with a new one
const ulToReplace = document.querySelector("ul");
const oldLi = ulToReplace.querySelector("li");
const newLi = document.createElement("li");
newLi.textContent = "This is a new list item.";
ulToReplace.replaceChild(newLi, oldLi);

// 11. Replace an <h2> element with a new <h1> element
const h2 = document.querySelector("h2");
if (h2) {
  const newH1 = document.createElement("h1");
  newH1.textContent = "This is a new heading.";
  h2.parentNode.replaceChild(newH1, h2);
}
