// const person = {
//     name: 'Matt',
//     age: 51
// }

// function Person(name, age) {
// }

// const person = new Person ('Matt', 51)

// console.log(person)

class Rectangle {
    #width
    #height
    constructor(width, height) {
        this.#width = width;
        this.#height = height;
    }
    get width() { return this.width; }
    set width(value) {
        if (typeof value === 'number') {
             this.width = value; } else {
                // raise an exception
             }}
    // Changes the widith into a read only property
    get area() { return this.#width * this.#height; }

}

const rect = new Rectangle(10,20)

console.log(rect.area)

class Square extends Rectangle {

    constructor(size) {
        super(size, size)
    }
}