function getJoke(){
    return new Promise ((resolve, reject) => {
        try{
        const req = new XMLHttpRequest()
        req.open('GET', 'https://icanhazdadjoke.com/')
        req.setRequestHeader('Accept', 'application/json')
        req.responseType = 'json'
        req.addEventListener('load', event =>  resolve(event.target.response.joke))
        req.send()
    }
    catch(e) {
        reject(e)
    }
})

}

async function fetchJoke(){
    const res = await fetch('https://icanhazdadjoke.com/', {
        headers: {
            'Accept': 'application/json'
        }
    })
    const data = await res.json()
    return data.joke
}

fetchJoke().then(joke => console.log(joke))
// const jokes = []
// getJoke()
// .then(joke => {
//     jokes.push(joke)
//     return getJoke()})

// const jokePromises = []
// for (let i=0; i <3; i++) {
//     jokePromises.push(getJoke())
// }

// Promise.all(jokePromises)
//     .then(jokes => console.log(jokes))
//     .catch(err => console.error(err))

// console.log(jokePromises)
console.log('Request sent!')
