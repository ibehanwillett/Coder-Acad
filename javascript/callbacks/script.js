function getJoke(cb){
const req = new XMLHttpRequest();
req.open('GET', 'https://icanhazdadjoke.com/')
req.setRequestHeader('Accept', 'application/json')
req.responseType = 'json'
req.addEventListener('load', event =>  cb(event.target.response.joke))
req.send()
}

getJoke(joke => console.log(joke))
