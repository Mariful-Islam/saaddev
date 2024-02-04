
menu = document.querySelector(".menu");
      menu.onclick = function () {
        navBar = document.querySelector(".nav-bar");
        navBar.classList.toggle("active");
        menu = document.querySelector(".menu");
        menu.classList.toggle("bar");
      };



//Active Page
const navBtn = document.querySelectorAll('.nav__list li a')
const activePage = window.location.pathname

navBtn.forEach((link)=>{
  if(link.href.includes(`${activePage}`)){
    document.querySelector('.nav__list li a.active').classList.remove('active')
    link.classList.add('active')
  }
})



// Slider for client section start

let sliderContent = document.querySelectorAll(".client__detail"),
      arrowLeft = document.querySelector("#arrow-left"),
      arrowRight = document.querySelector("#arrow-right"),
      current = 0;


function reset() {
  for(let i=0; i<sliderContent.length; i++){
    sliderContent[i].style.display="none";
  }
}


function startSlide(){
  reset();
  sliderContent[0].style.display="block";
}
startSlide();


function slideLeft(){
  reset();
  sliderContent[current - 1].style.display="block";
  current--;
}

function slideRight(){
  reset();
  sliderContent[current + 1].style.display="block";
  current++;
}
      

arrowLeft.addEventListener('click', function(){
  if (current === 0){
    current=sliderContent.length;
  }
  slideLeft();
});

arrowRight.addEventListener('click', function(){
  if (current === sliderContent.length - 1){
    current = -1;
  }
  slideRight();
});

// Slider for client section End


//Service Page start
