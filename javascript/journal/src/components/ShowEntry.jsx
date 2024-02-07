import React from 'react'

const ShowEntry = ({ entry, categories }) => {
  return  entry ? (
    <>
    <h3>{entry.content}</h3>
    <p>Posted in {categories[entry.category]}</p>
    </>
  ) : (
    <h3>Entry not found!</h3>
  )
}

export default ShowEntry