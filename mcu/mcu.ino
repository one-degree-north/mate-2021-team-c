//  Copyright (C) 2021  Lucas Sta Maria <lucas.stamaria@gmail.com>
//
//  mcu.ino: SAS MATE Team C's program to run on the microcontroller and
//  interact with Team C's software on an external computer.
//
//  This program is free software: you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation, either version 3 of the License, or
//  (at your option) any later version.
//
//  This program is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details.
//
//  You should have received a copy of the GNU General Public License
//  along with this program.  If not, see <https://www.gnu.org/licenses/>.

#include <Wire.h>
#include <Servo.h>
#include <Arduino.h>

// Motor Output Constants
#define SPEED_MIN 1000
#define SPEED_MID 1500
#define SPEED_MAX 2000

// Motor Pin Constants
#define FRONT_LEFT_PIN 6
#define FRONT_RIGHT_PIN 9
#define REAR_LEFT_PIN 10
#define REAR_RIGHT_PIN 11
#define FORWARD_LEFT_PIN 12
#define FORWARD_RIGHT_PIN 13

// Comms Constants
#define BAUD_RATE 115200
#define BUFFER_MAX 8
#define PACKET_MAX 2

// Motors
Servo front_left;
Servo front_right;
Servo rear_left;
Servo rear_right;
Servo forward_left;
Servo forward_right;

void setup() {
  setup_motors();
  delay(2000);
  Serial.begin(BAUD_RATE);

  while (!Serial)
    delay(10);
} 

void loop() {
  // Incoming bytes received by the microcontroller from the external computer through Serial are
  // stored in `buffer`, with a maximum storage of 8 bytes.
  int buffer[BUFFER_MAX];

  // `buf_ind` keeps track of which index in the buffer to write to.
  int buf_ind = 0;
  
  // Information is received in packets, which have a distinct static size of 3 bytes, with the
  // last byte being a terminating byte (all 1s, 255). `packet` stores the two significant bytes
  // of information.
  int packet[PACKET_MAX];


  while (Serial.available()) {
    write_to_buffer(buffer, &buf_ind);
    if (has_packet(buffer)) {
      if (has_valid_packet(buffer)) {
        buffer_to_packet(buffer, packet);
        execute_packet(packet);
      }
      flush_buffer(buffer, &buf_ind);
    }
  }
}

// Sets up the motors by attaching them to their respective pins.
void setup_motors() {
  front_left.attach(FRONT_LEFT_PIN);
  front_right.attach(FRONT_RIGHT_PIN);
  rear_left.attach(REAR_LEFT_PIN);
  rear_right.attach(REAR_RIGHT_PIN);
  forward_left.attach(FORWARD_LEFT_PIN);
  forward_right.attach(FORWARD_RIGHT_PIN);
}

// Writes an incoming byte into the buffer `buffer` at the current buffer index `buf_ind`.
// `buffer` and `buf_ind` are pointers to their respective variables. `buffer` is modified to
// contain the newly received byte. `buf_ind` is modified so the program knows where in `buffer` to
// write to next.
void write_to_buffer(int* buffer, int* buf_ind) {
  int buf_byte = Serial.read();
  if (buf_byte == -1) {
    return;
  }
  buffer[*buf_ind] = buf_byte;
  (*buf_ind)++;
}

// Returns a boolean representing whether a packet exists in the buffer `buffer`. Checks if there is
// a terminating byte for a packet ('\255', all bits flipped to 1). If there is, then there exists
// an end of a packet, and returns true. Else it will return false.
bool has_packet(int* buffer) {
  for (int ind = 0; ind < BUFFER_MAX; ind++) {
    if ((int)(buffer[ind]) == 255) {
      return true;
    }
  }
  return false;
}

// Returns a boolean representing whether a valid packet exists in the buffer `buffer`. Checks if
// the received packet size is 3 bytes, including the terminating byte. If it is, then the function
// returns true. Else it will return false.
bool has_valid_packet(int* buffer) {
  for (int ind = 0; ind < BUFFER_MAX; ind++) {
    if ((int)(buffer[ind]) == 255 && ind == PACKET_MAX) {
      return true;
    }
  }
  return false;
}

// Copies the buffer contents in `buffer` to the packet `packet`. `buffer` and `packet` are
// pointers to their respective arrays.
void buffer_to_packet(int* buffer, int* packet) {
  for (int ind = 0; ind < PACKET_MAX; ind++) {
    packet[ind] = buffer[ind];
  }
}

// Sets all the bytes in the buffer `buffer` to 0 to empty it of its contents. Resets the buffer
// index `buf_ind` to 0 so it will indicate the program to write at the start of the buffer again.
void flush_buffer(int* buffer, int* buf_ind) {
  for (int ind = 0; ind < BUFFER_MAX; ind++) {
    buffer[ind] = 0;
  }
  (*buf_ind) = 0;
}

// Executes the packet `packet` based on the two significant bytes. The first byte indicates the
// command to be executed, and the second byte indicates the argument for the command.
// Executes the commands based on the following document:
// https://docs.google.com/document/d/1TtKtFwUutYwbIac_FjjTdN0an4Zpzbw5fHmSIN9APws/edit
void execute_packet(int* packet) {
  int cmd_byte = packet[0];
  int arg_byte = packet[1];

  switch (cmd_byte) {
    case 0:
      move_forward(arg_byte);
      break;
    case 1:
      move_backward(arg_byte);
      break;
    case 2:
      move_up(arg_byte);
      break;
    case 3:
      move_down(arg_byte);
      break;
    case 4:
      turn_left(arg_byte);
      break;
    case 5:
      turn_right(arg_byte);
      break;
    case 6:
      break;
    case 7:
      break;
    case 8:
      break;
    case 9:
      break;
    default:
      break;
  }
}

void move_forward(int arg_byte) {
  int power = SPEED_MID + arg_byte;
  forward_left.writeMicroseconds(power);
  forward_right.writeMicroseconds(power);
}

void move_backward(int arg_byte) {
  int power = SPEED_MID - arg_byte;
  forward_left.writeMicroseconds(power);
  forward_right.writeMicroseconds(power);
}

void move_up(int arg_byte) {
  int power = SPEED_MID + arg_byte;
  front_left.writeMicroseconds(power);
  front_right.writeMicroseconds(power);
  rear_left.writeMicroseconds(power);
  rear_right.writeMicroseconds(power);
}

void move_down(int arg_byte) {
  int power = SPEED_MID - arg_byte;
  front_left.writeMicroseconds(power);
  front_right.writeMicroseconds(power);
  rear_left.writeMicroseconds(power);
  rear_right.writeMicroseconds(power);
}

void turn_left(int arg_byte) {
  int power = SPEED_MIN + arg_byte;
  forward_right.writeMicroseconds(power);
}

void turn_right(int arg_byte) {
  int power = SPEED_MIN + arg_byte;
  forward_left.writeMicroseconds(power);
}
