import serial
import pygame
import time

class Sensor:
    def __init__(self, ID):
        self.ser = serial.Serial(ID, 115200)
    
    def run(self):
        while True:
            #time.sleep(0.1)
            try:
                self.line = self.ser.readline()
                #print(self.line)
            except:
                pass


            #if(chr(self.line[1]) == 'o'):
            #self.ori = self.line[4:].split(str = ',')
            #print("o")
            #elif(chr(self.line[1]) == 'g'):
            #self.vel = self.line[4:].split(str = ',')
            #print("g")


if __name__ == "__main__":
    sensor = Sensor("/dev/cu.usbmodem14111")
    sensor.run()
