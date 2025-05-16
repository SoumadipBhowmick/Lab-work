
/*
Analog input reads an analog input on analog in 0, prints the value out.
created 24 March 2006 by Tom Igoe
*/
int analogValue = 0;
// variable to hold the analog value
void setup() {
// open the serial port at 9600 bps:
Serial.begin(9600);
}
void loop() {
// read the analog input on pin 0:
analogValue = analogRead(0);
// print it out in many formats:
Serial.println(analogValue);
Serial.println(analogValue, DEC);
Serial.println(analogValue, HEX);
Serial.println(analogValue, OCT);
Serial.println(analogValue, BIN);
// print as an ASCII-encoded decimal
// print as an ASCII-encoded decimal
// print as an ASCII-encoded hexadecimal
// print as an ASCII-encoded octal
// print as an ASCII-encoded binary
// delay 10 milliseconds before the next reading:
delay(10);
}