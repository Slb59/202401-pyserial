from pyfirmata2 import Arduino
import time

port = 'COM5'
board = Arduino(port)

while True:
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)
