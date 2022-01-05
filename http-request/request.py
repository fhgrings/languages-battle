import requests, time

from joblib import Parallel, delayed
import multiprocessing

# what are your inputs, and what operation do you want to
# perform on each input. For example...
inputs = range(5)
def make_request(port):
    return requests.get('http://localhost:'+port)

num_cores = multiprocessing.cpu_count()

for port in [("Java Spring","8080"), ("C-socket","8000"), ("Python Flask","5000"),("Node JS","3000")]:
    start = time.time()
    results = Parallel(n_jobs=num_cores)(delayed(make_request)(port[1]) for i in inputs)
    end = time.time()
    total = end - start
    print("Application: "+port[0]+" --- Time "+str(total))
