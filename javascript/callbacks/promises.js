

function adder(a, b) {
    return a + b
}

async function adderPromise(x, y) {
        if (typeof x === 'number' && typeof y === 'number') {
        const answer = adder(x, y)
        return (answer)
        } else {
            throw('x and y must be a number')
        }
    }


// adderPromise(15,14)
//     .then(value => {
//         adderPromise(value,100)
//         .then(answer=> console.log(answer))
//     })
//     .catch( err =>console.error(err))


value = await adderPromise(15,14)
console.log(value)
    // .then(value => adderPromise(value,100))
    // .then(answer=> console.log(answer))
    // .catch( err =>console.error(err))

console.log('Not waiting!')