function reset() {
    document.querySelector('#Pokemon').textContent = '';
}

function capitalize(str) {
    const lower = str.toLowerCase()
    return str.charAt(0).toUpperCase() + lower.slice(1)
}

function output(pokemon) {
    reset()
        let pokemonName = document.createElement('h3');
        let body = document.createElement('article');

        fullName = capitalize(pokemon.name);
        pokemonName.textContent = fullName;
        body.appendChild(pokemonName);



        let pokemonStats = document.createElement('ul');
        pokemonStats.textContent = "STATS";

        // Gets the name for the stat and creates a formatted list inthe html
        let pokemonStatsNameHP = document.createElement('li');
        let pokemonStatsNameATK = document.createElement('li');
        let pokemonStatsNameDEF = document.createElement('li');
        let pokemonStatsNameSPATK = document.createElement('li');
        let pokemonStatsNameSPDEF = document.createElement('li');
        let pokemonStatsNameSPEED = document.createElement('li');

        
        pokemonStatsNameHP.textContent = pokemon.stats[0].stat.name + ':    ' + pokemon.stats[0].base_stat;
        pokemonStatsNameATK.textContent = pokemon.stats[1].stat.name + ':    ' + pokemon.stats[1].base_stat;
        pokemonStatsNameDEF.textContent = pokemon.stats[2].stat.name + ':    ' + pokemon.stats[2].base_stat;
        pokemonStatsNameSPATK.textContent = pokemon.stats[3].stat.name + ':    ' + pokemon.stats[3].base_stat;
        pokemonStatsNameSPDEF.textContent = pokemon.stats[4].stat.name + ':    ' + pokemon.stats[4].base_stat;
        pokemonStatsNameSPEED.textContent = pokemon.stats[5].stat.name + ':    ' + pokemon.stats[5].base_stat;
 
        pokemonStats.appendChild(pokemonStatsNameHP)
        pokemonStats.appendChild(pokemonStatsNameATK)
        pokemonStats.appendChild(pokemonStatsNameDEF)
        pokemonStats.appendChild(pokemonStatsNameSPATK)
        pokemonStats.appendChild(pokemonStatsNameSPDEF)
        pokemonStats.appendChild(pokemonStatsNameSPEED)

        body.appendChild(pokemonStats);
        document.querySelector('#Pokemon').appendChild(body);
    };

function dataDownload(url) {
    fetch(url).then(response => response.json()).then(pokemon => {output(pokemon)});
}


function sortBy() {
    input = document.getElementById('choice').value
    switch(input) {
        case "Bulbasaur": 
            url = "https://pokeapi.co/api/v2/pokemon/1/"
            break

        case "Charmander":
            url = "https://pokeapi.co/api/v2/pokemon/4/"
            break

        case "Squirtle":
            url = "https://pokeapi.co/api/v2/pokemon/7/"
            break
    }
    dataDownload(url)
    }

function sortByPhoto() {
    input = document.getElementById('choice').value
    switch(input) {
        case "Bulbasaur": 
        path = "https://github.com/jordankraude/Personal-Projects/blob/master/webpage/Images/001.png?raw=true" + new Date().getTime()
        break

    case "Charmander":
        path = "https://github.com/jordankraude/Personal-Projects/blob/master/webpage/Images/004.png?raw=true" + new Date().getTime()
        break

    case "Squirtle":
        path = "https://github.com/jordankraude/Personal-Projects/blob/master/webpage/Images/007.png?raw=true" + new Date().getTime()
        break
    }
    var image = document.getElementById('PokemonImg')
    image.src = path + new Date().getTime();
    
    
}


document.getElementById('choice').addEventListener('change', sortBy)
document.getElementById('choice').addEventListener('change', sortByPhoto)

