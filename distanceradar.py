import uhd
import time
import numpy as np

usrp = uhd.usrp.MultiUSRP("")  
freq = 1e9  # 1 GHz
samp_rate = 10e6 # 10 
gain = 0
usrp.set_rx_freq(freq)
usrp.set_tx_freq(freq)
usrp.set_rx_rate(samp_rate)
usrp.set_tx_rate(samp_rate)
usrp.set_rx_gain(gain)
usrp.set_tx_gain(gain)


pulse_duration = 1e-6  # 1 microsecond pulse
num_samps = int(pulse_duration * samp_rate)
pulse = np.ones(num_samps, dtype=np.complex64) # create a pulse of ones.


def measure_distance():
    # Send the pulse
    tx_stream = usrp.get_tx_stream(uhd.stream_args("fc32"))
    tx_stream.send(pulse, uhd.stream_metadata())

    rx_stream = usrp.get_rx_stream(uhd.stream_args("fc32"))
    rx_buffer = np.zeros(num_samps * 10, dtype=np.complex64) # create a buffer to recieve data.
    start_time = time.time()
    rx_stream.recv(rx_buffer, uhd.stream_metadata())
    end_time = time.time()

    
  
    round_trip_time = end_time - start_time 

  
    speed_of_light = 299792458  # meters per second
    distance = (round_trip_time * speed_of_light) / 2 # divide by 2 for round trip.

    return distance
distance = measure_distance()
print(f"Estimated distance: {distance:.2f} meters")
