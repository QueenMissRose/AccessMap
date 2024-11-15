

window.addEventListener('load', () => {
    //after window is loaded completely 
    let preloader = document.querySelector('.preloader')

    setTimeout( function() {
        preloader.classList.add('disappear')
    }, 2000)
    
})