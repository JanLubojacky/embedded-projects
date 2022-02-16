import serial
from time import sleep
import string
import threading

port = "/dev/ttyACM0" # linux
# port = "COM11" # windows

channel = serial.Serial(port, baudrate = 9600, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE,timeout=None)

class KeyboardThread(threading.Thread):

    def __init__(self, input_cbk = None, name='keyboard-input-thread'):
        self.input_cbk = input_cbk
        super(KeyboardThread, self).__init__(name=name)
        self.start()

    def run(self):
        while True:
            self.input_cbk(input()) #waits to get input + Return

def my_callback(inp):
    #evaluate the keyboard input
    print('Sending message: ', inp)
    message_bytes = inp.encode('utf-8')
    channel.write(message_bytes)

#start the Keyboard thread
kthread = KeyboardThread(my_callback)

mess = '12345'
message_bytes_2 = mess.encode('utf-8')


while True:
    data = channel.readline()

    data_recieved = data.decode('utf-8')

    print(data_recieved)
