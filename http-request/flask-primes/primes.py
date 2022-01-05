from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)

def isPrime(n):
    for i in range(2,n//2+1):
        if (not (n%i)):
            return 0
    return 1

@app.route("/")
def hello_world():
    numPrimes = 0
    for i in range(2,250001):
        numPrimes += isPrime(i)
    print(str(numPrimes))

    return str(numPrimes)
