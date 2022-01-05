const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  let numPrimes=0
  for (let i=2;i<250001;i++) {
      numPrimes+=isPrime(i)
  }
  console.log(numPrimes)
  res.send(""+numPrimes)
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

function isPrime(n) {
    for (let i=2; i<n/2;i++) {
        if(!(n%i)) {
            return 0
        }
    }
    return 1
}
