
// The following code produceswave train of approximately 10% duty cycle at 1KHz


// Connect oscilloscope between pin 13 and ground.
void setup()
{
pinMode(13, OUTPUT);
}
void loop()
{
  digitalWrite(13, HIGH);
  delayMicroseconds(100); // Approximately 10% duty cycle @ 1KHz
  digitalWrite(13, LOW);
  delayMicroseconds(1000 - 100);
}