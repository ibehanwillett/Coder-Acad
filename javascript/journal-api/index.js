import express, { response } from 'express';

const categories = ['Food', 'Gaming', 'Coding', 'Other']

const entries = [
    {category: 'Food', content: 'Pizza is yummy!'},
    {category: 'Coding', content: 'Coding is fun!'},
    {category: 'Gaming', content: 'I love Inscrption!'},
]
// Using array index as id during development

const app = express();

app.use(express.json());
// Runs on every request & looks at request header & content type. if that's application /json it'll ignore the body & move on.
app.get('/', (request, response) => response.send({info: "Journal API"}))

app.get('/categories', (request, response) => response.status(201).send(categories))

// Entries
app.get('/entries', (req, res) => res.send(entries))
// Gets single entry
app.get('/entries/:id', (req, res) => {
    const entry = entries[req.params.id - 1];
    if (entry) {
        res.status(200).send(entry)
    } else {
        res.status(404).send({error: "Entry not found!"})
    }
})
app.post('/entries', (req, res) => {
    // Get entry data from request
    console.log(req.body)
    // Validate
    //To do
    // Create new entry object
    // Push new entry into array
    entries.push(req.body)
    // Respond with 201 & the created resource
    res.status(201).send(entries[entries.length - 1])
})

app.listen(4001);

