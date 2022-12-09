// Swiper
var swiper = new Swiper(".mySwiper", {
  slidesPerView: 1,
  spaceBetween: 30,
  loop: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});

let swiperArea = document.getElementById("swiper");
let nextBtn = document.getElementById("autoClick");

let hover = true;

swiperArea.addEventListener("mouseover", () => {
  hover = true;
  console.log("true");
});
swiperArea.addEventListener("mouseout", () => {
  hover = false;
  console.log("false ");
});
// window.setInterval(() => {
//   if (!hover) {
//     window.setInterval(() => {
//       nextBtn.click();
//     }, 3000);
//   } else {
//     console.log("still");
//   }
// }, 1000);
window.setInterval(() => {
  nextBtn.click();
}, 7000);
