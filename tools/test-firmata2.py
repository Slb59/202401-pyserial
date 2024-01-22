from pyfirmata2 import Arduino, util
# INPUT
import time

port = 'COM5'
board = Arduino(port)

it = util.Iterator(board)
it.start()

# board.digital[10].mode = INPUT

digital_input = board.get_pin('d:10:i')
led = board.get_pin('d:13:o')

# board.digital[13].write(1)
# time.sleep(1)
# board.digital[13].write(0)


while True:
    # sw = board.digital[10].read()
    sw = digital_input.read()

    if sw is True:
        # print(sw)
        # board.digital[13].write(1)
        led.write(1)
    else:
        # board.digital[13].write(0)
        led.write(0)
    time.sleep(0.1)
