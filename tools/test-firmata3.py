from pyfirmata2 import Arduino, util
import time
import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

port = 'COM5'
board = Arduino(port)

it = util.Iterator(board)
it.start()

digital_input = board.get_pin('d:10:i')
led = board.get_pin('d:13:o')

while True:
    sw = digital_input.read()
    if sw is True:
        led.write(1)
        messagebox.showinfo("Notification", "Button was pressed")
        root.update()
        led.write(0)
    time.sleep(0.1)
