#include <Wire.h>
#include <Servo.h>
#include <Arduino.h>

#define SPEED_MIN 1000
#define SPEED_MID 1500
#define SPEED_MAX 2000

#define FRONT_LEFT_PIN 6
#define FRONT_RIGHT_PIN 9
#define REAR_LEFT_PIN 10
#define REAR_RIGHT_PIN 11
#define FORWARD_LEFT_PIN 12
#define FORWARD_RIGHT_PIN 13

Servo front_left;
Servo front_right;
Servo rear_left;
Servo rear_right;
Servo forward_left;
Servo forward_right;

void setup() {
  setup_motors();
  delay(2000);
  Serial.begin(115200);
  while (!Serial)
    delay(10); // will pause Zero, Leonardo, etc until serial console opens
} 

#define BUFFER_MAX 8
#define PACKET_MAX 2

void loop() {
  int buffer[BUFFER_MAX];
  int packet[PACKET_MAX];
  int buf_ind = 0;
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

void setup_motors() {
  front_left.attach(FRONT_LEFT_PIN);
  front_right.attach(FRONT_RIGHT_PIN);
  rear_left.attach(REAR_LEFT_PIN);
  rear_right.attach(REAR_RIGHT_PIN);
  forward_left.attach(FORWARD_LEFT_PIN);
  forward_right.attach(FORWARD_RIGHT_PIN);
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
    if ((int)(buffer[ind]) == 255 && ind == PACKET_MAX) {
      return true;
    }
  }
  return false;
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
