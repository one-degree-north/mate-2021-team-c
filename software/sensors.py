import serial

class Sensor:
    def __init__(self, ID):
        self.ser = serial.Serial(ID, 115200)
    
    def run(self):
        while True:
            self.line = self.ser.readline()
            if(self.line[1] == 'o'):
                self.ori = self.line[4:].split()
                print("o")
            elif(self.line[1] == 'g'):
                sel.vel = self.line[4:].split()
                print("g")

if __name__ == "__main__":
    sensor = Sensor("/dev/cu.usbmodem1431")
    sensor.run()
