// Preloader
window.addEventListener('load', () => {
    //after window is loaded completely 
    let preloader = document.querySelector('.preloader')

    setTimeout(function () {
        preloader.classList.add('disappear')
    }, 2000)

})

//Setting up the map
function initMap() {
    //Starting point
    const center = { lat: 35.773650, lng: -78.641260 }; // Raleigh Convention Center

    // Initialize the map
    const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 35.7796, lng: -78.6382 }, // Raleigh, NC
        zoom: 10,
    })

    // URL to the KML file (use the direct download link)
    const kmlUrl = 'https://drive.google.com/uc?export=download&id=1XhY-IMbfdguWv9ROXQ18A2W_CLmDtWPL'

    
    // Load the KML Layer
    const kmlLayer = new google.maps.KmlLayer({
        url: kmlUrl,
        map: map,
        suppressInfoWindows: false, // Disable default info windows
        preserveViewport: true,    // Keep the map from zooming out
    })

    // Add error handling
    google.maps.event.addListener(kmlLayer, "status_changed", () => {
        if (kmlLayer.getStatus() !== "OK") {
            console.error("KML Layer failed to load: ", kmlLayer.getStatus());
        } else {
            console.log('it is ok')
        }
    })
}

// Checked items in AccessibilityNeeds html
// set variable for all checkbox items
const items = document.querySelectorAll('.item');

//add event listeners to each checkbox element
items.forEach(item => {
    item.addEventListener('click', (event) => {
        const isChecked = item.getAttribute('aria-checked') === 'true';
        item.setAttribute('aria-checked', !isChecked);
    });
})

