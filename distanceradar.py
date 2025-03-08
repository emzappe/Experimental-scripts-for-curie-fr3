import uhd
import time
import numpy as np

usrp = uhd.usrp.MultiUSRP("")  
freq = 1e9  
samp_rate = 10e6 
gain = 0
usrp.set_rx_freq(freq)
usrp.set_tx_freq(freq)
usrp.set_rx_rate(samp_rate)
usrp.set_tx_rate(samp_rate)
usrp.set_rx_gain(gain)
usrp.set_tx_gain(gain)

t_end = time.time()
while time.time() < t_end:

