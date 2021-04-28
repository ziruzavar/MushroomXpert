import {render} from 'https://unpkg.com/lit-html?module';
import {detailsTemplate} from "./templates/mushroomTemplate.js"
import {getMush} from "./utils/getShroom.js"

const shroom = window.location.search.split("=")[1]
const main = document.getElementById("prediction")
const staticPng = document.getElementById("static")
if (shroom) {
    main.style.display = "block"
    staticPng.style.display = "none"

    const data = shroom.split("_")
    const mushroom = await getMush(data[1] + "_" + data[2])
    render(detailsTemplate(mushroom), main)
} else {
    main.style.display = "none"
    staticPng.style.display = "block"
}
Array.from(document.querySelectorAll(".form-detail > label")).map(x => x.remove())