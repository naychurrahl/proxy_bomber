import threading
import requests
from time import sleep
import random

def append_file(filename, text):
  try:
    with open(filename, 'a') as f:
      f.write(text)
  except IOError:
    print("Error: could not append to file " + filename)

def num(n = 0, x = 1000):
  return random.randint(n, x)

def pow(x, p):
  n = x
  for _ in range(p-1):
    n = n * x
  return n

def proxie():
  return str(num())+"."+str(num())+"."+str(num())+"."+str(num())

def prox():
  print("Started")
  while True:
    proy = proxie()
    for x in range(100000):
      proxy = proy+":"+str(x)
      if ((x % 100) == (random.randint(100, 1000)) % 100):
        print ("Trying: "+proxy)
      try:
        res = requests.get("http://ipinfo.io/json", proxies={"http": proxy, "https":proxy})
      except:
        continue

      if res.status_code == 200:
        append_file("proxy_list.txt", proxy)
        print(proxy)
  

for _ in range(10):
  threading.Thread(target=prox).start()

 