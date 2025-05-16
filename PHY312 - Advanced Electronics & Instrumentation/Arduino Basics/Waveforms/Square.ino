// Connect an oscilloscope between pin 11 and GND

int f_hz = 100;

double delay_time = 1000 / (f_hz * 2);

void setup() { pinMode(11, OUTPUT); }

void loop()
{
  digitalWrite(11, LOW);
  delay(delay_time);
  digitalWrite(11, HIGH);
  delay(delay_time);
}