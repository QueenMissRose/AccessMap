document.addEventListener('DOMContentLoaded', () => {
    const icons = document.querySelectorAll('.icon'); 
    const popup = document.getElementById('popup'); 

    icons.forEach(icon => {
        icon.addEventListener('mouseover', (event) => {
            const message = event.target.getAttribute('data-message');
            showPopup(event, message);
        });

        icon.addEventListener('mouseout', () => {
            hidePopup();
        });
    });

    function showPopup(event, message) {
        popup.innerText = message;
        popup.style.display = 'block';
        popup.style.left = event.clientX + 'px';
        popup.style.top = event.clientY + 'px';
    }

    function hidePopup() {
        popup.style.display = 'none';
    }
});
