let loader = document.getElementById("preloader");

// window.setTimeout(() => {
//     loader.style.display = "none";
// }, 2000);

window.addEventListener('load', ()=>{
    loader.style.display = "none";
})

let navbarResp = document.getElementById("navbar-resp");
let opacity = document.getElementById("opacity");
let burger = document.getElementById("burger");
let line1 = document.getElementById("line-1");
let line2 = document.getElementById("line-2");
let line3 = document.getElementById("line-3");

burger.addEventListener('click', () =>{
    console.log("visible")
    navbarResp.classList.toggle("visible");
    opacity.classList.toggle("opacity");
});

burger.addEventListener('mouseover', ()=>{
    line1.style.backgroundColor = "rgb(230, 0, 127)";
    line2.style.backgroundColor = "rgb(230, 0, 127)";
    line3.style.backgroundColor = "rgb(230, 0, 127)";
});
burger.addEventListener('mouseout', ()=>{
    line1.style.backgroundColor = "rgb(50, 50, 50)";
    line2.style.backgroundColor = "rgb(50, 50, 50)";
    line3.style.backgroundColor = "rgb(50, 50, 50)";
});

//twitter
let twitter = document.getElementById("twitter");
let twitterIcon = document.getElementById("twitter-icon");

twitter.addEventListener('mouseover', () => {
    twitterIcon.style.color = "white";
})
twitter.addEventListener('mouseout', () => {
    twitterIcon.style.color = "black";
})

//fb
let fb = document.getElementById("fb");
let fbIcon = document.getElementById("fb-icon");

fb.addEventListener('mouseover', () => {
    fbIcon.style.color = "white";
})
fb.addEventListener('mouseout', () => {
    fbIcon.style.color = "black";
})

//insta
let insta = document.getElementById("insta");
let instaIcon = document.getElementById("insta-icon");

insta.addEventListener('mouseover', () => {
    instaIcon.style.color = "white";
})
insta.addEventListener('mouseout', () => {
    instaIcon.style.color = "black";
})

//yt
let yt = document.getElementById("yt");
let ytIcon = document.getElementById("yt-icon");

yt.addEventListener('mouseover', () => {
    ytIcon.style.color = "white";
})
yt.addEventListener('mouseout', () => {
    ytIcon.style.color = "black";
})

//linkedin
let linkedin = document.getElementById("linkedin");
let linkedinIcon = document.getElementById("linkedin-icon");

linkedin.addEventListener('mouseover', () => {
    linkedinIcon.style.color = "white";
})
linkedin.addEventListener('mouseout', () => {
    linkedinIcon.style.color = "black";
})