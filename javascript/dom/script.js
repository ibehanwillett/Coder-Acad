// const newDiv = document.createElement('div');
// // document.body.appendChild(newDiv);
// newDiv.innerHTML = '<h3>Awesome content</h3>';
// document.body.insertBefore(newDiv, document.querySelector('ul'));
// newDiv.id = 'spam'
// newDiv.style.color = 'blue'
// document.body.insertBefore(newDiv, document.querySelector('ul')

// const myColor = 'blue'
// document.body.innerHTML = `<div id="spam" style="color:${myColor}"><h3>Awesome content</h></div>`

const items = [
'Adding to DOM',
'Querying the DOM',
'Changing the DOM',
'Event Listeners'
]

const ul = document.querySelector('ul')

// for (let item of items) {
    
//     ul.innerHTML += `<li> ${item}</li>`
//     // const newLi = document.createElement('li')
//     // newLi.innerHTML = item
//     // ul.appendChild(newLi)
// }

const lis = items.map(item => `<li> ${item} </li>`)
ul.innerHTML = lis.join('')

//  Handle a mouse click on the H1 element
document.querySelector('h1').addEventListener('click', event => event.target.innerHTML += "!")

const newItem = document.querySelector('#newItem')
const btn = document.querySelector('button')

btn.addEventListener('click', () => {
    ul.innerHTML += `<li> ${newItem.value} </li>`
    newItem.value = ''
})
