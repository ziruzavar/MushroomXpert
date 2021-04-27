import {html} from 'https://unpkg.com/lit-html?module';

export function paginationTemplate(data, page) {
    return html`
        ${page - 1  > 0 ? html`<a href="?page=${Number(page) - 1}">&laquo;</a>` : ""}
            ${data.map(x=> {
                return html`<a href="?page=${x}" class=${x == page ? "active": ""}>${x}</a>`
            })}
        ${page - data.length < 0 ? html`<a href="?page=${Number(page) + 1}">&raquo;</a>` : ""}`
}

