#include <Adafruit_ICM20649.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
#include <Servo.h>
#include <Arduino.h>
#include "Adafruit_ZeroTimer.h"

#if defined(LED_BUILTIN)
#define pin  LED_BUILTIN
#else
#define pin  D2
#endif

#define SPEED_MAX 2000

#define motorPin 10

Adafruit_ICM20649 icm;
uint16_t measurement_delay_us = 65535; // Delay between measurements for testing
// For SPI mode, we need a CS pin
#define ICM_CS 10
// For software-SPI mode we need SCK/MOSI/MISO pins
#define ICM_SCK 13
#define ICM_MISO 12
#define ICM_MOSI 11

// timer tester
Adafruit_ZeroTimer zt3 = Adafruit_ZeroTimer(3);
//   Timer3: channel 0 on D2 or D10, channel 1 on D5 or D12

void setup() {
  Serial.begin(115200);
  while (!Serial)
    delay(10); // will pause Zero, Leonardo, etc until serial console opens
  pinMode(motorPin, OUTPUT);

  configureD21PWM();
} 

#define BUFFER_MAX 8
#define PACKET_MAX 2

void loop() {
  int buffer[BUFFER_MAX];
  int buf_ind = 0;
  while (Serial.available()) {
    write_to_buffer(buffer, &buf_ind);
    int packet[2];
    if (has_packet(buffer)) {
      if (has_valid_packet(buffer)) {
        buffer_to_packet(buffer, packet);
      }
      flush_buffer(buffer, &buf_ind);
    }
  }
}

void write_to_buffer(int* buffer, int* buf_ind) {
  int buf_byte = Serial.read();
  if (buf_byte == -1) {
    return;
  }
  buffer[*buf_ind] = buf_byte;
  (*buf_ind)++;
}

bool has_packet(int* buffer) {
  for (int ind = 0; ind < BUFFER_MAX; ind++) {
    if ((int)(buffer[ind]) == 255) {
      return true;
    }
  }
  return false;
}

bool has_valid_packet(int* buffer) {
  for (int ind = 0; ind < BUFFER_MAX; ind++) {
    if ((int)(buffer[ind]) == 255 && ind == PACKET_MAX + 1) {
      return true;
    }
    return false;
  }
}

void buffer_to_packet(int* buffer, int* packet) {
  for (int ind = 0; ind < PACKET_MAX; ind++) {
    packet[ind] = buffer[ind];
  }
}

void flush_buffer(int* buffer, int* buf_ind) {
  for (int ind = 0; ind < BUFFER_MAX; ind++) {
    buffer[ind] = 0;
  }
  (*buf_ind) = 0;
}

void execute_packet(int* packet) {
  int cmd_byte = packet[0];
  int arg_byte = packet[1];

  switch (cmd_byte) {
    case (int)('0'):
      break;
    case (int)('1'):
      break;
    case (int)('2'):
      break;
    case (int)('3'):
      break;
    case (int)('4'):
      break;
    case (int)('5'):
      break;
    case (int)('6'):
      break;
    case (int)('7'):
      break;
    case (int)('8'):
      break;
    case (int)('9'):
      break;
    default:
      break;
  }
}

void configureD21PWM() {
 zt3.configure(TC_CLOCK_PRESCALER_DIV1, // prescaler
                TC_COUNTER_SIZE_16BIT,   // bit width of timer/counter
                TC_WAVE_GENERATION_NORMAL_PWM // frequency or PWM mode
                );
  if (! zt3.PWMout(true, 0, 10)) {
    Serial.println("Failed to configure PWM output");
  }
  if (! zt3.PWMout(true, 1, 12)) {
    Serial.println("Failed to configure PWM output");
  }
  zt3.setPeriodMatch(SPEED_MAX, 0, 0);
  zt3.setPeriodMatch(SPEED_MAX, 0, 1);
  zt3.enable(true);
}
