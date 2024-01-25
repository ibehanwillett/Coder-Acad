import mongoose from 'mongoose';
import dotenv from 'dotenv'

dotenv.config();
try {
    const m = await mongoose.connect(process.env.DB_URI)
    console.log(m.connection.readyState === 1 ? 'Mongo connected!' : 'Mongo failed to connect')
} catch (err) {
    console.log(err)
}

const closeConnection = () => {
    console.log('Mongoose is disconnecting...')
    mongoose.disconnect()
}

const categoriesSchema = new mongoose.Schema({
    name: { type: String, required: true }
})

const CategoryModel = new mongoose.model('Category', categoriesSchema)

const entriesSchema = new mongoose.Schema({
    category: { type: mongoose.ObjectId, ref: 'Category' },
    content: { type: String, required: true }
})

const EntryModel = new mongoose.model('Entry', entriesSchema)




export { EntryModel, CategoryModel, closeConnection }