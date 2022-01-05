function isPrime(n) {
    for (let i=2; i<n/2;i++) {
        if(!(n%i)) {
            return 0
        }
    }
    return 1
}

let numPrimes=0
for (let i=2;i<250001;i++) {
    numPrimes+=isPrime(i)
}
console.log(numPrimes)