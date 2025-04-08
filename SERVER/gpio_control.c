#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>

void control_led(int pin, int estado) {
    pinMode(pin, OUTPUT);
    digitalWrite(pin, estado);
}

int leer_boton(int pin) {
    pinMode(pin, INPUT);
    return digitalRead(pin);
}