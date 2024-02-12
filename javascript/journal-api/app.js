import express from 'express';
import { EntryModel, CategoryModel, closeConnection } from './db.js'
import entryRoutes from './routes/entry_routes.js'
import cors from 'cors'

const app = express();

app.use(cors())

app.use(express.json());
// Runs on every request & looks at request header & content type. if that's application /json it'll ignore the body & move on.

app.get('/', (request, response) => response.send({info: "Journal API"}))

app.get('/categories', async (request, response) => response.status(201).send(await CategoryModel.find()))

app.use("/entries",entryRoutes)

export default app

