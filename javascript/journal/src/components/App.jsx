import { useState } from 'react'
import reactLogo from '../assets/react.svg'
import viteLogo from '/vite.svg'
import Home from './Home.jsx'
import NewEntry from './NewEntry.jsx'
import CategorySelection from './CategorySelection.jsx'
import NavBar from './NavBar.jsx'
import { BrowserRouter, Route, Routes } from 'react-router-dom'

function App() {

  return (
    <>
      
      <BrowserRouter>
      <NavBar />
      <h1>Journal</h1>
        <Routes>
          <Route path='/' element={<Home/>} />
          <Route path='/category' element={<CategorySelection/>}/>
          <Route path='/entry'>
            <Route path='new' element={<NewEntry/>}/>
          </Route>
          <Route path='*' element={<h2>Page Not Found</h2>}/>
          
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
