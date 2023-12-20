// Python
// age = 51
// if age >= 16:
//     print("adult")
// else:
//     print("child")

const age = 51

if (age >= 16) {
    console.log("Adult")
} else if (age >= 13) {
    console.log("Teen")
} else {
    console.log("Child")
}

const message = age >= 18 ? "Allowed" : "Denied"

// Match Statement
const favBird = "Crow"

switch (favBird) {
    case 'Crow':
        console.log('You like crows!')
    case 'Robin':
        console.log('You like robins!')
}