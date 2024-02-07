import { useState, useEffect } from 'react'
import Home from './Home.jsx'
import NewEntry from './NewEntry.jsx'
import CategorySelection from './CategorySelection.jsx'
import NavBar from './NavBar.jsx'
import { BrowserRouter, Route, Routes, useParams } from 'react-router-dom'
import ShowEntry from './ShowEntry.jsx'

function App() {
  const[categories, setCategories] = useState(['Food', 'Gaming', 'Coding'])
  const [entries, setEntries] = useState([{category: 0, content: "Soup"}])
  const params = useParams()

  useEffect(() => {
    fetch('http://localhost:4002/categories')
    .then(res => res.json())
    .then(data => setCategories(data.categories)) 
  }, []
  )

  function addEntry(cat_id, content) {
    const newId = entries.length
    // 1. Create a entry object from user input
    const newEntry = {
        category: cat_id,
        content: content,
    }
    // 2. Add new entry to the entries list
    setEntries([...entries, newEntry])
    return newId
}

function ShowEntryWrapper() {
  const { id } = useParams()
  return <ShowEntry entry={entries[id]} categories={categories}/>
}

  return (
    <>
      
      <BrowserRouter>
      <NavBar />
        <Routes>
          <Route path='/' element={<Home entries={entries} />} />
          <Route path='/category' element={<CategorySelection categories={categories}/>}/>
          <Route path='/entry'>
            <Route path=':id' element={<ShowEntryWrapper />}/>
            <Route path='new/:cat_id' element={<NewEntry categories={categories} addEntry={addEntry}/>}/>
          </Route>
          
          <Route path='*' element={<h2>Page Not Found</h2>}/>
          
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
