RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${RED}C/C++${NC}"
gcc primes.c -o primes.o && time ./primes.o

echo -e "${RED}Java${NC}"
javac Primes.java && time java Primes

echo -e "${RED}Python${NC}"
time python3 primes.py

echo -e "${RED}NodeJS${NC}"
time node primes.js

