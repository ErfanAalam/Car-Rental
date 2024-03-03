const hamburger = document.querySelector(".hamburger");
const features = document.querySelector(".features");
const close = document.querySelector(".close")

hamburger.addEventListener("click",()=>{
    if (features.classList.contains("-translate-x-96")) {
        features.classList.remove("-translate-x-96");
    }
})
hamburger.addEventListener("click",()=>{
    hamburger.classList.add("hidden")
})
close.addEventListener("click",()=>{
    hamburger.classList.remove("hidden")
})

close.addEventListener("click",() =>{
    features.classList.add("-translate-x-96")
})

// image slider component


const slides = document.querySelectorAll('.slide');
        let currentSlide = 0;

        function showSlide(n) {
            slides.forEach((slide) => {
                slide.style.display = 'none';
            });
            slides[n].style.display = 'block';
        }

        function nextSlide() {
            currentSlide = (currentSlide + 1) % slides.length;
            showSlide(currentSlide);
        }

        function prevSlide() {
            currentSlide = (currentSlide - 1 + slides.length) % slides.length;
            showSlide(currentSlide);
        }

        function autoSlide() {
            nextSlide();
        }

        showSlide(currentSlide);
        setInterval(autoSlide, 2000);
