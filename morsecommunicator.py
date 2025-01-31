import time
import sys
import importurllib.request
import uhd
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    ' ': ' ' 
}
usrp = uhd.usrp.MultiUSRP("type=n210")
freq1 = input("Enter Freqency 6-24Ghz ")
freq2 = "1000000000"
freq4 = "000000000"
message = input("What would you like to say ")
base_ur = "http://10.42.0.10:5111/high_lo?freq="
base_url = "http://10.42.0.10:511/low_lo?freq="
freq3 = f"{freq1}{freq4}"
url = f"{base_ur}{freq3}"
u1l = f"{base_url}{freq2}"
def text_to_morse(message):
    morse = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse.append(MORSE_CODE_DICT[char])
    return ' '.join(morse)
for symbol in morse_code:
        if symbol == '.':
            usrp.send_waveform(np.ones(int(tx_rate * 0.1)), tx_time)
        elif symbol == '-':
            usrp.send_waveform(np.ones(int(tx_rate * 0.3)), tx_time)
        usrp.send_waveform(np.zeros(int(tx_rate * 0.1)), tx_time)
if __name__ == "__main__":
    text = "message"
    morse_code = text_to_morse(text)
    print(morse_code)
with urllib.request.urlopen(url) as response:
    ht4l = response.read().decode('utf-8')
    print(ht4l)
with urlib.request.urlopen(u1l) as response:
    ht3l = response.read().decode('utf-8')
    print(ht3l)
  def transmit_morse(morse_code, tx_rate, tx_freq, tx_gain, tx_time):
    usrp.set_tx_rate(1e6)
    usrp.set_tx_freq(1e9)
    usrp.set_tx_gain(-20)
  

