import express, { response } from 'express';

const categories = ['Food', 'Gaming', 'Coding', 'Other']

const entries = [
    {category: 'Food', content: 'Pizza is yummy!'},
    {category: 'Coding', content: 'Coding is fun!'},
    {category: 'Gaming', content: 'I love Inscrption!'},
]

const app = express();

app.use(express.json());
// Runs on every request & looks at request header & content type. if that's application /json it'll ignore the body & move on.
app.get('/', (request, response) => response.send({info: "Journal API"}))

app.get('/categories', (request, response) => response.status(201).send(categories))

// Entries
app.get('/entries', (req, res) => res.send(entries))
app.post('/entries', (req, res) => {
    // Get entry data from request
    console.log(req.body)
    // Validate
    //To do
    // Create new entry object
    // Push new entry into array
    // Respond with 201 & the created resource
    res.status(201).send({})
})

app.listen(4001);

