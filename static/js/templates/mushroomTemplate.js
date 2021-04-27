import {html} from 'https://unpkg.com/lit-html?module';

export function detailsTemplate(data) {
    return html`
        <div class="row">
            <div class="col-xl-4 col-lg-4 col-md-6 col-sm-12">
                <div class="plants-box">
                    <figure><img
                            src="${data["image_url"]}"
                            alt="img"/></figure>
                    <h3>${data.name}</h3>
                    <p>${data.description}</p>
                    <p>${data["edible_choices"]}</p>
                    <a href="/mushrooms/${data.name}" class="btn btn-success">See
                        More</a>
                </div>
            </div>
        </div>`
}

export function mushroomTemplate(data) {
    return html`
        ${data.map((mushroom) => html`
            <div class="col-xl-4 col-lg-4 col-md-6 col-sm-12">
            <div class="plants-box">
                <figure><img src="${mushroom["image_url"]}" alt="img"/></figure>
                <h3>${mushroom.name}</h3>
                <p>${mushroom["edible_choices"]}</p>
                <a href="/details/${mushroom.name}" class="btn btn-success">See More</a>
            </div>
        </div>`)}`
}

