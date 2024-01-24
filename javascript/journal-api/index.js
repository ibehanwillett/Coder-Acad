import express from 'express';
import { EntryModel, CategoryModel, closeConnection } from './db.js'


const categories = ['Food', 'Gaming', 'Coding', 'Other']

const app = express();

app.use(express.json());
// Runs on every request & looks at request header & content type. if that's application /json it'll ignore the body & move on.
app.get('/', (request, response) => response.send({info: "Journal API"}))

app.get('/categories', async (request, response) => response.status(201).send(await CategoryModel.find()))

// Entries
app.get('/entries', async (req, res) => res.send(await EntryModel.find()))
// Gets single entry
app.get('/entries/:id', async (req, res) => {
    const entry = await EntryModel.findById(req.params.id); 
    if (entry) {
        res.status(200).send(entry)
    } else {
        res.status(404).send({error: "Entry not found!"})
    }
})
app.post('/entries', async (req, res) => {
    try {
    // Get entry data from request
    console.log(req.body)
    // Validate
    //To do
    // Create new entry object
    // Push new entry into array
    // entries.push(req.body)
    const insertedEntry = await EntryModel.create(req.body)

    // Respond with 201 & the created resource
    res.status(201).send(insertedEntry)
    } catch (err) {
    res.status(400).send({error: err.message})}
})

app.put('/entries/:id', async (req, res) => {
    try {
        const updatedEntry = await EntryModel.findByIdAndUpdate(req.params.id, req.body, {new: true})
        if (updatedEntry) {
            res.status(204).send(updatedEntry)
        } else {
            res.status(404).send({error: err.message})
        }
    } 
    catch (err) {
    res.status(400).send({error: err.message})}
})

app.delete('/entries/:id', async (req, res) => {
    try {
        const deletedEntry = await EntryModel.findByIdAndDelete(req.params.id)
        if (deletedEntry) {
            res.sendStatus(204)
        } else {
            res.status(404).send({error: err.message})
        }
    } 
    catch (err) {
    res.status(400).send({error: err.message})}
})



app.listen(4002);

