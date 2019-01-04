window.addEventListener('scroll', () => {
    const scrolled = window.scrollY;
    
    if (scrolled > 100){
        document.getElementById('header').classList.add('black');
    }

    if (scrolled < 100){
        document.getElementById('header').classList.remove('black');
    }
});