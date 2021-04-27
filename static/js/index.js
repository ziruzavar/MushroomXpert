let url = '/mushroom/Phaeolus_schweinitzii/'

async function mush() {
    let response = await fetch(url);
    let result = await response.json();
    console.log(result)
}

mush()