import {render} from 'https://unpkg.com/lit-html?module';
import {mushroomTemplate} from "./templates/mushroomTemplate.js"
import {paginationTemplate} from "./templates/pagination.js"
import {getMushes} from "./utils/getShroom.js"

const page = window.location.search.split("=")[1] || 1
const mushrooms = await getMushes()

const main = document.querySelector(".mushrooms")
const paginator = document.querySelector(".pagination")

const pages = Array.from({length: Math.ceil(mushrooms.length / 9)}, (v, i) => i + 1)
render(mushroomTemplate(mushrooms.splice((page - 1) * 9, 9)), main)
render(paginationTemplate(pages, page), paginator)