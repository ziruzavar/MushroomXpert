const url = '/mushroom/'
export async function getMush(id) {
    let response = await fetch(url + id);
    let result = await response.json();
    return result
}
export async function getMushes() {
    let response = await fetch(url);
    let result = await response.json();
    return result
}