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
    // Initialize the map
    const map = new google.maps.Map(document.querySelector('#map'), {
        center: { lat: 35.7796, lng: -78.6382 }, // Raleigh, NC
        zoom: 12,
    })

    // URL to the KML file (use the direct download link)
    const kmlUrl = 'https://drive.google.com/uc?id=1HxHZR1Wb3o9kMyhpPxXI9NNedF3Vsfnz&export=download'

    // Load the KML Layer
    const kmlLayer = new google.maps.KmlLayer({
        url: kmlUrl,
        map: map,
        suppressInfoWindows: false, // Show info windows if any
        preserveViewport: true,    // Keep the map from zooming out
    })

    // Add error handling
    google.maps.event.addListener(kmlLayer, "status_changed", () => {
        if (kmlLayer.getStatus() !== "OK") {
            console.error("KML Layer failed to load: ", kmlLayer.getStatus())
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