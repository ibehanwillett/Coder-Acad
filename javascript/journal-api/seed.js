import { EntryModel, CategoryModel,  closeConnection } from './db.js';


const categories = [
    {
        "name": "Food"
    },

    {
        "name": "Coding"
    },
    
    {
    "name": "Gaming"
    }
]




await CategoryModel.deleteMany()
console.log('Deleted all categories')
const cats = await CategoryModel.insertMany(categories)
console.log('Added categories')

const entries = [
    {category: cats[0], content: 'Pizza is yummy!'},
    {category: cats[1], content: 'Coding is fun!'},
    {category: cats[2], content: 'I love Inscrption!'},
]

await EntryModel.deleteMany()
console.log('Deleted all entries')
await EntryModel.insertMany(entries)
console.log('Added entries')

closeConnection()