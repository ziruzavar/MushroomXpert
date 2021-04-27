import {render} from 'https://unpkg.com/lit-html?module';
import { detailsTemplate } from "./templates/mushroomTemplate.js"
import { getMush } from "./utils/getShroom.js"
const shroom = window.location.search.split("=")[1]
if(shroom) {
    document.getElementById("prediction").style.display="block"
    document.getElementById("static").style.display="none"

    const main = document.querySelector("#prediction")
    const data = shroom.split("_")
    const mushroom = await getMush(data[1] + "_" + data[2])
    render(detailsTemplate(mushroom), main)
}else {
    document.getElementById("prediction").style.display="none"
    document.getElementById("static").style.display="block"
}
Array.from(document.querySelectorAll(".form-detail > label")).map(x=> x.remove())