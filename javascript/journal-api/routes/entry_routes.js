import { EntryModel } from "../db.js";
import { Router } from "express"

 const router = Router()

// Entries
router.get('/', async (req, res) => res.send(await EntryModel.find().populate('category')))
// Gets single entry
router.get('/entries/:id', async (req, res) => {
    const entry = await EntryModel.findById(req.params.id); 
    if (entry) {
        res.status(200).send(entry)
    } else {
        res.status(404).send({error: "Entry not found!"})
    }
})

router.post('/', async (req, res) => {
    try {
        const insertedEntry = await (await EntryModel.create(req.body)).populate('category')
        res.status(201).send(insertedEntry)
    } catch (err) {
    res.status(400).send({error: err.message})}
})

router.put('/:id', async (req, res) => {
    try {
        const updatedEntry = await EntryModel.findByIdAndUpdate(req.params.id, req.body, {new: true})
        if (updatedEntry) {
            res.send(updatedEntry).populate('category')
        } else {
            res.status(404).send({error: err.message})
        }
    } 
    catch (err) {
    res.status(400).send({error: err.message})}
})

router.delete('/:id', async (req, res) => {
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


export default router