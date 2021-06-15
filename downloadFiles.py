#url = 'http://www.africau.edu/images/default/sample.pdf'
url = "https://hips.hearstapps.com/countryliving.cdnds.net/17/47/1511194376-cavachon-puppy-christmas.jpg"
from tqdm import tqdm
import time
import requests
import math
chunk_size = 2000
req = requests.get(url, stream=True)
size=int(req.headers['Content-Length'])

n= math.ceil(size/chunk_size)
#with open("file.jpg","wb") as file:
with open("file.pdf","wb") as file:
    for chunk in tqdm(req.iter_content(chunk_size = chunk_size), total=n):
        #time.sleep(0.5)
        file.write(chunk)