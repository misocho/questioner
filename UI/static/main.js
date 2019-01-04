window.addEventListener('scroll', () => {
    const scrolled = window.scrollY;
    
    if (scrolled > 20){
        document.getElementById('header').classList.add('black');
    }

    if (scrolled < 20){
        document.getElementById('header').classList.remove('black');
    }
});