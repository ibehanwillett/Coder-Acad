import React, { useState } from 'react'
import { Link } from 'react-router-dom'

const CategorySelection = () => {
 const[categories, setCatergories] = useState(['Food', 'Gaming', 'Coding'])

  return (
    <>
    <h1>Please select a category:</h1>
      <ul>
        {
          categories.map((cat, index) => (
            <li key={index} >
              <Link to={`/entry/new/${index}`}>{cat}</Link>
            </li>
          ))
        }
      </ul>
    </>
  )
}

export default CategorySelection