import { EntryModel, closeConnection } from './db.js';

const entries = [
    {category: 'Food', content: 'Pizza is yummy!'},
    {category: 'Coding', content: 'Coding is fun!'},
    {category: 'Gaming', content: 'I love Inscrption!'},
]

await EntryModel.deleteMany()
console.log('Deleted all entries')
await EntryModel.insertMany(entries)
console.log('Added entries')

closeConnection()