//  While loop

/*let count = 3
 while (count > 0) {
    console.log(count --)
} */

//  For x in range - 3 part for loop
/*
for (let i=0; i <10; i++) {
    console.log(i)
}
*/

// const numbers = [1,2,3,21,44,37]
// for (let i=0; i < numbers.length; i++) {
//     console.log(numbers[i])
// }

//  Printing as an array
/*
const anumbers = [1, 2, 5, 21, 44, 37];
const resultArray = [];

for (let i = 0; i < anumbers.length; i++) {
    resultArray.push(anumbers[i]);
}

console.log(resultArray);
*/

// Fibonnaci Sequence
/*
for (let prev = 1, next = 1; next <= 1000; tmp= next, next=prev+next, prev=tmp) {
    console.log(next)
}
*/
// Printing index number and element
/*
favFoods = ['pizza', 'pasta', 'tacos']
for (let index in favFoods) {
    console.log(`${parseInt(index)+1}. ${favFoods[index]}`)
}
*/

favFoods = ['pizza', 'pasta', 'tacos']
favFoods.forEach((food, index) => {
    console.log(`${index+1}. ${food}`)
})

favFoods.forEach(food => console.log(food))

