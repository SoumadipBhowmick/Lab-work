// Generate a low frequency near sine wane signal. 

// Add an electrolytic cap & oscilloscope btw pin 10 and GND


int F = 1;
int Fs = 500;
int n = 500;
float t;
int sampling_interval;
byte samples[1000];

void setup() {
  pinMode(10, OUTPUT);
  for (int n = 0; n < 500; n++)
  {
    t = (float) n / Fs;
    samples[n] = (byte) (127.0 * sin(2 * 3.14 * t) + 127.0 );
  }
  sampling_interval = 10000000 / (F * n);

}
void loop() {
  for (int j = 0; j < 500; j++) {
    analogWrite(10, samples[j]);
    delayMicroseconds(sampling_interval);
  }
}