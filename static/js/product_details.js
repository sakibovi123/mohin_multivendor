$(document).ready(function() {
    // Zoom image on hover(image magnifier)
    let e = window.innerWidth;

    if (e >= 991) {
        $(".main__img").imagezoomsl({
            zoomrange: [3, 3]
        });
    }

    const descriptionButton = document.querySelector(".description__button");

    descriptionButton.addEventListener("click", function() {
        $(".description").addClass("activeResource");
        $(".reviews").removeClass("activeResource");
        $(".description__text").show();
        $(".reviews__text").hide();
    });

    const reviewsButton = document.querySelector(".reviews__button");

    reviewsButton.addEventListener("click", function() {
        $(".description").removeClass("activeResource");
        $(".reviews").addClass("activeResource");
        $(".description__text").hide();
        $(".reviews__text").show();
    });
});