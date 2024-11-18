import time
import sys
import urllib.request
freq1 = input("Enter Freqencycy one ")
freq2 = input("Enter Freqency two ")
freq3 = input("Enter Freqency three ")
freq4 = input("Enter Freqency four ")
base_ur = "http://10.42.0.10:5111/high_lo?freq="
u1l = f"{base_ur}{freq1}"
u2l = f"{base_ur}{freq2}"
u3l = f"{base_ur}{freq3}"
u4l = f"{base_ur}{freq4}"
url = "http://10.42.0.10:5111/high_lo"
for i in range(10000):
  with urllib.request.urlopen(u1l) as response:
   ht4l = response.read().decode('utf-8')
   print(ht4l)
   time.sleep(1)
  with urllib.request.urlopen(u2l) as response:
   ht3l = response.read().decode('utf-8')
   print(ht3l)
   time.sleep(1)
  with urllib.request.urlopen(u3l) as response:
   ht2l = response.read().decode('utf-8')
   print(ht2l)
   time.sleep(1)
  with urllib.request.urlopen(u4l) as response:
   html = response.read().decode('utf-8')
   print(html)
   time.sleep(1)
