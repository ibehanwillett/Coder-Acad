import React, { useEffect, useState } from 'react'

const CurrencySelector = ( { setCurrency }) => {
    const [selectValue, setSelectValue] = useState("AUD")

    useEffect(() => setCurrency(selectValue), [selectValue])

  return (
    <select onChange= {(event) => setSelectValue(event.target.value)} value={selectValue}>
        <option value="AUD">Australian Dollar</option>
        <option value="USD">US Dollar</option>
        <option value="EUR">Euro</option>
    </select>
  )
}

export default CurrencySelector