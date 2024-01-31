import React, { useEffect, useState } from 'react'
import CurrencySelector from './CurrencySelector'

const Bitcoinindex = () => {
  let [price, setPrice] = useState("")
  let [currency, setCurrency] = useState("AUD")

  useEffect(() => {
    fetch(`https://api.coindesk.com/v1/bpi/currentprice/${currency}.json`)
  .then(res => res.json())
  .then(data => setPrice(data.bpi[currency].rate))
}, [currency])

  

  return (
    <>
      <CurrencySelector setCurrency={setCurrency} />
      <p>
        Current Price ({currency}): {price}
      </p>
    </>
  )
}

export default Bitcoinindex