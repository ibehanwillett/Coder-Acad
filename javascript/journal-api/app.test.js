import app from './app.js'
import request from 'supertest'

describe("app test", () => {
    test('GET /', async () => {
        const res = await request(app).get('/')
        expect(res.status).toBe(200)
        expect(res.header['content-type']).toContain('json')
        expect(res.body.info).toBeDefined()
        expect(res.body.info).toBe('Journal API')
    })

    describe('POST /entries', () => {
        let cats, res
    
        beforeAll(async () => {
          cats = await request(app).get('/categories')
          res = await request(app).post('/entries').send({
            category: cats.body[0]._id,
            content: 'Jest test content'
          })
        })
    
        test('Returns JSON with 201 status', () => {
          expect(res.status).toBe(201)
          expect(res.header['content-type']).toContain('json')
        })
    
        test('Body has _id, category and content fields', () => {
          expect(res.body._id).toBeDefined()
          expect(res.body.category).toBeDefined()
          expect(res.body.content).toBeDefined()
        })
    
        test('Category is an object with _id and name fields', () => {
          expect(res.body.category).toBeInstanceOf(Object)
          expect(res.body.category._id).toBeDefined()
          expect(res.body.category.name).toBeDefined()
        })
    
        test('Correct category and content are returned', () => {
          expect(res.body.category._id).toBe(cats.body[0]._id)
          expect(res.body.content).toBe('Jest test content')
        })
    
        afterAll(() => {
          // Cleanup
          request(app).delete(`/entries/${res.body._id}`)
        })
      })

    describe('GET /categories' , () => {
        let res 

        beforeEach(async () => {
            res = await request(app).get('/categories')
        })

        test ('return JSON content', async () => {
            expect(res.status).toBe(201)
            expect(res.header['content-type']).toContain('json')
        })

        test ('return an array', async () => {
            expect(res.body).toBeInstanceOf(Array)
        })

        test ('array has three elements', async () => {
            expect(res.body).toHaveLength(3)
            expect(res.body).toEqual(expect.arrayContaining([expect.objectContaining({ name: "Food" })]))
        })

        test ('array contains food cat', async () => {
            expect(res.body).toEqual(expect.arrayContaining([expect.objectContaining({ name: "Food" })]))
        })
    })
    
})