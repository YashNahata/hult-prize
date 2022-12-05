let loader = document.getElementById("preloader");

window.setTimeout(() => {
    loader.style.display = "none";
}, 700);

let navbarResp = document.getElementById("navbar-resp");
let opacity = document.getElementById("opacity");
let burger = document.getElementById("burger");
let line1 = document.getElementById("line-1");
let line2 = document.getElementById("line-2");
let line3 = document.getElementById("line-3");

burger.addEventListener("click", () => {
  navbarResp.classList.toggle("visible");
  opacity.classList.toggle("opacity");
});

burger.addEventListener("mouseover", () => {
  line1.style.backgroundColor = "rgb(230, 0, 127)";
  line2.style.backgroundColor = "rgb(230, 0, 127)";
  line3.style.backgroundColor = "rgb(230, 0, 127)";
});
burger.addEventListener("mouseout", () => {
  line1.style.backgroundColor = "rgb(50, 50, 50)";
  line2.style.backgroundColor = "rgb(50, 50, 50)";
  line3.style.backgroundColor = "rgb(50, 50, 50)";
});
