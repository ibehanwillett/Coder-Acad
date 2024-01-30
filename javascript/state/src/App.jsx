import React, { useState } from 'react'

function App() {
  // let count = 0
  let [count, setCount] = useState(0)

  return (
    <>
    <h1>State</h1>
    <p>You have clicked {count} times.</p>
    <button onClick={() => setCount(count+1)}>Click me!</button>
    </>
  )
}

export default App