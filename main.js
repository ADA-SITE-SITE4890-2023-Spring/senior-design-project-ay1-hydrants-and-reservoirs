const links = document.querySelectorAll("nav a");
const pages = document.querySelectorAll("main");

links.forEach(link => {
  link.addEventListener("click", e => {
    e.preventDefault();
    const href = link.getAttribute("href").substr(1);
    pages.forEach(page => {
      if (page.id === href) {
        page.style.display = "block";
      } else {
        page.style.display = "none";
      }
    });

    if (href === "map") {
      initMap();
    }
  });
});

function initMap() {
  const mapContainer = document.getElementById("map-container");
  const mapOptions = {
    center: { lat: 37.7749, lng: -122.4194 },
    zoom: 12
  };
  const map = new google.maps.Map(mapContainer, mapOptions);
}
