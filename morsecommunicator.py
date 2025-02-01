import time
import sys
import urllib.request
import uhd
import numpy as np
import uhd.usrp
from uhd import types
from uhd import usrp

MORSE_CODE_DICT = {
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
samp_rate = 1e7
gain = 10
usrp = uhd.usrp.MultiUSRP(uhd_args)
transmission = 1
usrp.set_tx_freq(center_freq)
usrp.set_tx_rate(samp_rate)
usrp.set_tx_gain(gain)
usrp.set_tx_bandwidth(100, 0)


dration = int(samp_rate * 0.1 * 2)
duation = int(samp_rate * 0.3 * 2)

def generate_morse_signal(text, samp_rate, freq):
    morse_code = ""
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + " "
        elif char == ' ':
            morse_code += "/ "
        else:
            print(f"Character '{char}' not found in Morse code dictionary.")
            return None
    signal = []
    for symbol in morse_code:
        pause_duration = int(samp_rate * 0.1)  
        if symbol == '.':
            duration = int(samp_rate * 0.1)
            sine_wave = np.sin(2 * np.pi * freq * np.arange(duration) / samp_rate)
            signal.extend(sine_wave)
            signal.extend(np.zeros(pause_duration))  
            print(f"Generated dot with length {len(sine_wave)} and pause with length {pause_duration}")
        elif symbol == '-':
            duation = int(samp_rate * 0.3 * 2)
            sine_wave = np.sin(2 * np.pi * freq * np.arange(duation) / samp_rate)
            signal.extend(sine_wave)
            signal.extend(np.zeros(pause_duration))  
            print(f"Generated dash with length {len(sine_wave)} and pause with length {pause_duration}")
        elif symbol == ' ': 
            pause = np.zeros(pause_duration * 3)
            signal.extend(pause)  
            print(f"Generated space with length {len(pause)}")
        elif symbol == '/':
            pause = np.zeros(pause_duration * 7)  
            signal.extend(pause)  
            print(f"Generated word space with length {len(pause)}")
        return np.array(signal, dtype=np.complex64), morse_code

def main():
    print("Starting Morse code transmission...")
    try:
        morse_signal, morse_code = generate_morse_signal(sentence, samp_rate, freq)
        if not morse_signal.any() or not morse_code:
             return

        dot_duration = 0.1 * 2
        dash_duration = 0.3 * 2
        letter_space_duration = dot_duration
        word_space_duration = 7 * dot_duration

        stream_args = uhd.stream_args_t("fc32", "out") 
        tx_stream = usrp.get_tx_stream(stream_args)
        chunk_size = tx_stream.get_max_num_samps()


        symbol_index = 0
        for i in range(0, len(morse_signal), chunk_size):
            chunk = morse_signal[i:i + chunk_size]
            tx_stream.send(chunk, uhd.stream_cmd_t.STREAM_NOW)

            current_symbol = morse_code[symbol_index]

            if current_symbol == '.':
                time.sleep(dot_duration)
            elif current_symbol == '-':
                time.sleep(dash_duration)
            elif current_symbol == ' ':
                time.sleep(letter_space_duration)
            elif current_symbol == '/':
                time.sleep(word_space_duration)

            symbol_index += 1  

        print("Transmission complete.")

    except RuntimeError as e:  
        print(f"Error: {e}")

if __name__ == "__main__":  
    main()
