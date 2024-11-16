import time
import urllib.request
url = "http://10.42.0.10:5111/high_lo"
for i in range(10000):
  with urllib.request.urlopen('http://10.42.0.10:5111/high_lo?freq=7e9') as response:
   ht4l = response.read().decode('utf-8')
   print(ht4l)
   time.sleep(1)
  with urllib.request.urlopen('http://10.42.0.10:5111/high_lo?freq=10e9') as response:
   ht3l = response.read().decode('utf-8')
   print(ht3l)
   time.sleep(1)
  with urllib.request.urlopen('http://10.42.0.10:5111/high_lo?freq=15e9') as response:
   ht2l = response.read().decode('utf-8')
   print(ht2l)
   time.sleep(1)
  with urllib.request.urlopen('http://10.42.0.10:5111/high_lo?freq=20e9') as response:
   html = response.read().decode('utf-8')
   print(html)
   time.sleep(1)
