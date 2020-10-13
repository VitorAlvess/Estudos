const options = {
    dragging:false,
    touchZoom:false,
    doubleClickZoom:false,
    scrollWheelZoom:false,
    zoomControl:false
}


const map = L.map('mapid', options).setView([-23.5707501,-46.6810928], 15);


//create and add tileLayer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

//create icon
const icon = L.icon({
    iconUrl: "./public/images/map-marker.svg",
    iconSize: [58, 68],
    iconAnchor: [29, 68],
    popupAnchors:[170, 2]
})




L.marker([-23.5707501,-46.6810928], {icon}).addTo(map)
    
/*img galeria */

function selectImage(event){
    const button = event.currentTarget

    //remover todas as classes active
    const buttons = document.querySelectorAll(".images button")
    buttons.forEach (removeActiveClass)

    function removeActiveClass(button){
        button.classList.remove("active")
    }

    //selecionar as image clicada
    const image = button.children[0]
    const imageContainer = document.querySelector(".orphanage-datails > img")

    //atualizar containe de imagen
    imageContainer.src = image.src
    //adicionar a classe .active para este botão
    button.classList.add("active")
}