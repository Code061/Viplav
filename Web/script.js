let currentSlide = 0;
const slides = document.querySelectorAll('.slide');

function showSlide(index) {
    slides.forEach((slide, i) => {
        slide.classList.remove('active');
        if (i === index) {
            slide.classList.add('active');
        }
    });
}

function changeSlide(direction) {
    currentSlide += direction;
    if (currentSlide < 0) {
        currentSlide = slides.length - 1; // Loop to last slide
    } else if (currentSlide >= slides.length) {
        currentSlide = 0; // Loop to first slide
    }
    showSlide(currentSlide);
}

// Initialize the first slide
showSlide(currentSlide);