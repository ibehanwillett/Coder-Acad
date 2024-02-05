import { useState } from 'react'
import reactLogo from '../assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Home from './Home.jsx'
import NewEntry from './NewEntry.jsx'
import CategorySelection from './CategorySelection.jsx'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1>Journal</h1>
      <Home />
      <NewEntry />
      <CategorySelection />
    </>
  )
}

export default App
