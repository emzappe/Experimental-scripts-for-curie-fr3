import time
import sys
import urllib.request
import uhd
import numpy as np
import uhd.usrp
from uhd import types
from uhd import usrp
usrp = uhd.usrp.MultiUSRP() 
freq1 = input("Enter Freqency 6-24ghz ")
freq2 = "000000000"
base_ur = "http://10.42.0.10:5111/high_lo?freq="
u2l = f"{freq1}{freq2}"
u1l = f"{base_ur}{freq2}"
with urllib.request.urlopen(u1l) as response:
   ht4l = response.read().decode('utf-8')
   print(ht4l)
text_to_send = input("Enter text to transmit: ")
morse_sequence = text_to_morse(text_to_send)


morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    ' ': '///////////////'
}
sentence = input("Enter the sentence: ")
freq = 1000
uhd_args = "addr=192.168.10.2" 
center_freq = 2.41e9 
sample_rate = 1e7
gain = 10
usrp = uhd.usrp.MultiUSRP()
tone_freq = 700 
dot_duration = 0.1  
usrp.set_tx_freq(center_freq)
usrp.set_tx_rate(samp_rate)
usrp.set_tx_gain(gain)
usrp.set_tx_bandwidth(100, 0)



def text_to_morse(text):
    morse_sequence = ""
    for char in text.upper():  # Handle uppercase and lowercase
        if char in morse_code:
            morse_sequence += morse_code[char] + " "  # Add space between characters
        else:
            print(f"Character '{char}' not found in Morse code dictionary.") #Handles unknown characters
    return morse_sequence

def generate_morse_signal(morse_sequence, sample_rate, tone_freq, dot_duration):
    samples = []
    for symbol in morse_sequence:
        if symbol == '.':
            samples.extend(np.sin(2 * np.pi * tone_freq * np.arange(int(sample_rate * dot_duration)) / sample_rate))
        elif symbol == '-':
            samples.extend(np.sin(2 * np.pi * tone_freq * np.arange(int(sample_rate * dot_duration * 3)) / sample_rate)) 
        elif symbol == ' ':
            samples.extend(np.zeros(int(sample_rate * dot_duration))) 
        elif symbol == '/':
            samples.extend(np.zeros(int(sample_rate * dot_duration * 7))) 
    return np.array(samples, dtype=np.complex64)  

def transmit_morse(samples, usrp, tx_stream):
    num_samps = len(samples)
    samps_sent = 0
    while samps_sent < num_samps:
        to_send = min(num_samps - samps_sent, 4096)  # Send in chunks
        tx_stream.send(samples[samps_sent:samps_sent + to_send], uhd.stream_args())
        samps_sent += to_send




def main():
    print("Starting Morse code transmission...")


    print(f"Morse Code: {morse_sequence}")

  
    samples = generate_morse_signal(morse_sequence, sample_rate, tone_freq, dot_duration)

        print("Transmission complete.")

    except RuntimeError as e:  
        print(f"Error: {e}")

if __name__ == "__main__":  
    main()
