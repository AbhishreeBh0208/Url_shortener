const navBtn = document.querySelector('.toggleNav');
const navBar = document.querySelector('.navbar-responsive')

navBtn.addEventListener('click', () => {
    navBar.classList.toggle('open');
    navBtn.classList.toggle('close');
})