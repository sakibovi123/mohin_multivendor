$('.img__slider').slick({
    dots: true,
    infinite: true,
    autoplay: true,
    autoplaySpeed: 2000,
    speed: 300,
    slidesToShow: 1,
    slidesToScroll: 1,
});

$(document).ready(function() {
    const hamburger = document.querySelector(".tab__hamburgerMenu");
    const crossIcon = document.querySelector(".cross__icon");
    const navSidebarBG = document.querySelector(".nav__sidebarBG");
    const sidebarNav = document.querySelector(".sidebar__nav");

    hamburger.addEventListener("click", function() {
        navSidebarBG.classList.add("activeNavSidebarBG");
        sidebarNav.classList.add("activeSidebarNav");
    });

    crossIcon.addEventListener("click", function() {
        navSidebarBG.classList.remove("activeNavSidebarBG");
        sidebarNav.classList.remove("activeSidebarNav");
    })

});