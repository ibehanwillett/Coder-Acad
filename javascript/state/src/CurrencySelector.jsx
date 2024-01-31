import React, { useEffect, useState } from 'react'

const CurrencySelector = ( { setCurrency }) => {
    const [selectValue, setSelectValue] = useState("AUD")
    const [currencies, setCurrencies] = useState([])

    useEffect(() => setCurrency(selectValue), [selectValue])
    useEffect(() => {
        fetch('https://api.coindesk.com/v1/bpi/supported-currencies.json')
        .then(res => res.json())
        .then(data => setCurrencies(data))
    }, [])

  return (
    <select onChange= {(event) => setSelectValue(event.target.value)} value={selectValue}>
        {currencies.map(cur => <option key={cur.currency} value={cur.currency}>{cur.country}</option>)}
    </select>
  )
}

export default CurrencySelector