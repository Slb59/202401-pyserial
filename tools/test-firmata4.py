from pyfirmata2 import Arduino, util
import time
import smtplib
import ssl


def send_email():
    port = 25  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "osynia.devapps@gmail.com"
    receiver_email = "brioman@neuf.fr"
    password = "12345"
    message = """Subject: Arduino Notification\n The switch was turned on."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        print("Sending email")
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


port = 'COM5'
board = Arduino(port)

it = util.Iterator(board)
it.start()

digital_input = board.get_pin('d:10:i')

while True:
    sw = digital_input.read()
    if sw is True:
        send_email()
        time.sleep(0.1)
