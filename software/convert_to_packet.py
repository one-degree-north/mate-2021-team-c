key = 'w' #imported from control subsystem
secKey = 'q'#imported from control subsystem
ind = ''
allKeys= ['w', 'a', 'up', 'down', 'd', 'right', 'left', 'spacebar', 'ctrl+w']


class Convert_To_Packet:
    
    def __init__(self):
        self.key = 'w'

    def pack(self, keyPressed):
        
        if (keyPressed == 'w'):
            self.ind = '0'  + chr(50)+ chr(255) # moveForward
        elif (keyPressed == 's'):
            self.ind = '1' + chr(50)+ chr(255) # moveBack
        elif (keyPressed == 'up'):
            self.ind = '2' + chr(50)+ chr(255) # moveUp
        elif (keyPressed == 'down'):
            self.ind = '3' + chr(50)+ chr(255) # moveBack
        elif (keyPressed == 'a'):
            self.ind = '4' +  chr(50)+ chr(255) # moveLeft
        elif (keyPressed == 'd'):
            self.ind = '5' + chr(50)+ chr(255) # moveRight
        elif (keyPressed == 'right'):
            self.ind = '6' + chr(50)+ chr(255) # tiltRight
        elif (keyPressed == 'left'):
            self.ind = '7' + chr(50) + chr(255) # tiltLeft
        elif (keyPressed == 'spacebar'):
            self.ind = '8' + '0' + chr(255) #Take screenshot 

            #if (secKey == '1'):
                #self.ind = '7' + chr(0) + chr(255)# StartAccelerometer
            '''
            if (secKey == '1'):
                self.ind = '7' + chr(0) + chr(255) # CollectXPos
            elif (secKey == '2'):
                self.ind = '7' + chr(1) + chr(255) # CollectYPos
            elif (secKey == '3'):
                self.ind = '7' + chr(2)  + chr(255) # CollectZPos
            elif (secKey == '4'):
                self.ind = '7' + chr(3) + chr(255) # CollectXVelocity
            elif (secKey == '5'):
                self.ind = '7' + chr(4) + chr(255) # CollectYVelocity
            elif (secKey == '6'):
                self.ind = '7' + chr(5) + chr(255) # CollectZVelocity
            elif (secKey == '7'):
                self.ind = '7' + chr(6) + chr(255) # CollectXAcceleration
            elif (secKey = '8'):
                self.ind = '7' + chr(7)+ chr(255) # CollectYAcceleration
            elif (secKey = '9'):
                self.ind = '7' + chr(8) + chr(255) # CollectZAcceleration
            elif (secKey = '['):
                self.ind = '7' + chr(9) + chr(10) + chr(255) # CollectXGyroscope
            elif (secKey = ']'):
                self.ind = '7' + chr(10) + chr(255) # CollectYGyroscope
            elif (secKey = '\'):
                self.ind = '7' + chr(11) + chr(255) # CollectXGyroscope 
            elif (secKey = 'spacebar'):
                self.ind = '8' + chr(0) + chr(255) # Take Screenshot
                '''
        elif (keyPressed == 'command+w'):
            self.ind = '9' + chr(254) + chr(255) # StopTasks

        return self.ind


