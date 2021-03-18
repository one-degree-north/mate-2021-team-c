import serial

class Sensor:
    def __init__(ID):
        ser = serial.Serial(ID, 115200)
    
    def run():
        while True:
            self.line = self.ser.readline()
            if(self.line[1] == 'o'):
                self.ori = self.line[4:].split()
            elif(self.line[1] == 'g'):
                sel.vel = self.line[4:].split()