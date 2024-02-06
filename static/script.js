let navbar = document.querySelector(".navbar");
let prevScrollPos = window.scrollY;
let elements = document.querySelectorAll(".card");

window.onscroll = function() {
    let currentScrollPos = window.scrollY;
    if (prevScrollPos > currentScrollPos) {
        navbar.style.top = "0";
    } else {
        navbar.style.top = "-56px";
    }
    prevScrollPos = currentScrollPos;
}

let observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if(entry.isIntersecting === true) {
            entry.target.classList.add('animate-on-scroll');
        } else {
            entry.target.classList.remove('animate-on-scroll');
        }
    });
}, { threshold: [0] });

elements.forEach(element => {
    observer.observe(element);
});