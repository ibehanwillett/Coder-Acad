import { useState } from 'react'
import Home from './Home.jsx'
import NewEntry from './NewEntry.jsx'
import CategorySelection from './CategorySelection.jsx'
import NavBar from './NavBar.jsx'
import { BrowserRouter, Route, Routes } from 'react-router-dom'

function App() {
  const[categories, setCatergories] = useState(['Food', 'Gaming', 'Coding'])
  return (
    <>
      
      <BrowserRouter>
      <NavBar />
        <Routes>
          <Route path='/' element={<Home/>} />
          <Route path='/category' element={<CategorySelection categories={categories}/>}/>
          <Route path='/entry'>
            <Route path='new/:cat_id' element={<NewEntry categories={categories}/>}/>
          </Route>
          <Route path='*' element={<h2>Page Not Found</h2>}/>
          
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
