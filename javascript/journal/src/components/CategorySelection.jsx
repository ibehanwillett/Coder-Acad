import React from 'react'
import { Link } from 'react-router-dom'

const CategorySelection = ({ categories }) => {


  return (
    <>
    <h3>Please select a category:</h3>
      <ul>
        {
          categories.map((cat, index) => (
            <li key={index} >
              <Link to={`/entry/new/${index}`}>{cat.name}</Link>
            </li>
          ))
        }
      </ul>
    </>
  )
}

export default CategorySelection