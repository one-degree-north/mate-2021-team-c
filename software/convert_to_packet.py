
key = 'w' #imported from control subsystem
secKey = 'q'#imported from control subsystem
ind = ''
allKeys= ['w', 'a', 'up', 'down', 'a', 'd', 'right', 'left', 'spacebar', 'command+w']


class Convert_To_Packet:
    
    def __init__():
        key = 'w'

    def pack(keyPressed):
        if (keyPressed == 'w'):
        ind = '0'  + chr(50)+ chr(255) # moveForward
        elif (keyPressed == 's'):
            ind = '1' + chr(50)+ chr(255) # moveBack
        elif (keyPressed == 'up'):
            ind = '2' + chr(50)+ chr(255) # moveUp
        elif (keyPressed == 'down'):
            ind = '3' + chr(50)+ chr(255) # moveBack
        elif (keyPressed == 'a'):
            ind = '4' +  chr(50)+ chr(255) # moveLeft
        elif (keyPressed == 'd'):
            ind = '5' + chr(50)+ chr(255) # turnRight
        elif (keyPressed == 'right'):
            ind = '6' + chr('left')+ chr(255) # turnLeft
        elif (keyPressed = 'spacebar'):
            ind = '8' + '0' + chr(255) #Take screenshot 

            #if (secKey == '1'):
                #ind = '7' + chr(0) + chr(255)# StartAccelerometer
            '''
            if (secKey == '1'):
                ind = '7' + chr(0) + chr(255) # CollectXPos
            elif (secKey == '2'):
                ind = '7' + chr(1) + chr(255) # CollectYPos
            elif (secKey == '3'):
                ind = '7' + chr(2)  + chr(255) # CollectZPos
            elif (secKey == '4'):
                ind = '7' + chr(3) + chr(255) # CollectXVelocity
            elif (secKey == '5'):
                ind = '7' + chr(4) + chr(255) # CollectYVelocity
            elif (secKey == '6'):
                ind = '7' + chr(5) + chr(255) # CollectZVelocity
            elif (secKey == '7'):
                ind = '7' + chr(6) + chr(255) # CollectXAcceleration
            elif (secKey = '8'):
                ind = '7' + chr(7)+ chr(255) # CollectYAcceleration
            elif (secKey = '9'):
                ind = '7' + chr(8) + chr(255) # CollectZAcceleration
            elif (secKey = '['):
                ind = '7' + chr(9) + chr(10) + chr(255) # CollectXGyroscope
            elif (secKey = ']'):
                ind = '7' + chr(10) + chr(255) # CollectYGyroscope
            elif (secKey = '\'):
                ind = '7' + chr(11) + chr(255) # CollectXGyroscope 
            elif (secKey = 'spacebar'):
                ind = '8' + chr(0) + chr(255) # Take Screenshot
                '''
        elif (keyPressed = 'command+w'):
            ind = '9' + chr(254) + chr(255) # StopTasks

        return ind
