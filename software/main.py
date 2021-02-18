import pygame
import serial
import threading
import time

DIMENSIONS: (int, int) = (800, 600)
BACKGROUND: (int, int, int) = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode(DIMENSIONS)
screen.fill(BACKGROUND)

active = True

PORT_NAME = "/dev/ttyACM0"
BAUD_RATE = 115200

ser = serial.Serial(port=PORT_NAME, baudrate=BAUD_RATE)
ser.close()
ser.open()

def read_serial(ser):
    while True:
        print(ser.readline())
        time.sleep(0.01)

t = threading.Thread(target=read_serial, args=(ser))
t.start()

while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.KEYDOWN:
            term_byte = chr(255)
            if event.key == pygame.K_w:
                cmd_byte = chr(0)
                arg_byte = chr(200)
                msg = cmd_byte + arg_byte + term_byte
                ser.write(msg.encode("latin"))
                print("w")
            if event.key == pygame.K_s:
                cmd_byte = chr(1)
                arg_byte = chr(200)
                msg =cmd_byte + arg_byte + term_byte
                ser.write(msg.encode("latin"))
                print("s")
            if event.key == pygame.K_LSHIFT:
                cmd_byte = chr(2)
                arg_byte = chr(200)
                msg =cmd_byte + arg_byte + term_byte
                ser.write(msg.encode("latin"))
                print("shift")
            if event.key == pygame.K_SPACE:
                cmd_byte = chr(3)
                arg_byte = chr(200)
                msg =cmd_byte + arg_byte + term_byte
                ser.write(msg.encode("latin"))
                print("space")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                cmd_byte = chr(0)
                arg_byte = chr(0)
                msg = cmd_byte + arg_byte + term_byte
                ser.write(msg.encode("latin"))
                print("w")
            if event.key == pygame.K_s:
                cmd_byte = chr(1)
                arg_byte = chr(0)
                msg =cmd_byte + arg_byte + term_byte
                ser.write(msg.encode("latin"))
                print("s")
            if event.key == pygame.K_LSHIFT:
                cmd_byte = chr(2)
                arg_byte = chr(0)
                msg =cmd_byte + arg_byte + term_byte
                ser.write(msg.encode("latin"))
                print("shift")
            if event.key == pygame.K_SPACE:
                cmd_byte = chr(3)
                arg_byte = chr(0)
                msg =cmd_byte + arg_byte + term_byte
                ser.write(msg.encode("latin"))
                print("space")

t.join()
ser.close()
