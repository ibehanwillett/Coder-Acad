import React from 'react'
import { useParams } from 'react-router-dom'

const NewEntry = () => {
  const params= useParams()

  return (
    <h3>New Entry in category {params.cat_id}</h3>
  )
}

export default NewEntry