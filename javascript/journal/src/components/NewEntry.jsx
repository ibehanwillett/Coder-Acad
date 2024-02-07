import React, { useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'

const NewEntry = ({categories=[], addEntry}) => {
  const params= useParams()
  const [entry, setEntry] = useState('')
  const nav = useNavigate()

function createEntry(e) {
  e.preventDefault()
  let newId = addEntry(params.cat_id, entry)
  setEntry('')
  // redirect the browser
  nav(`/entry/${newId}`)
}

  return (
    <>
    <h3>New entry in category: {categories[params.cat_id]?.name}</h3>
    <form className="section" onSubmit={createEntry}>
      <div className="field"> 
        <label className="label">Content</label>
        <div className="control">
          <textarea className="textarea"
          value={entry}
          placeholder='Type your journal entry here'
          onChange={ e => setEntry(e.target.value) }>

          </textarea>
          </div>
        </div>
        <div className='field is-grouped'>
          <div className='control'>
            <button className='button is-link'>Create Entry</button>
          </div>
        </div>
    
        
    </form>
    </>
  )
}

export default NewEntry