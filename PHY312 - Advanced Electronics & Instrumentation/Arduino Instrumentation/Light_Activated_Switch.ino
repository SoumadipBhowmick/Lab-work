const int ledPin = 12;   
const int   ldrPin = A0; 


void setup() {

  Serial.begin(9600);
   pinMode(ledPin, OUTPUT);
  pinMode(ldrPin,   INPUT);  
}

void loop() {
  int   ldrStatus = analogRead(ldrPin); 

Serial.println(ldrStatus);

   if (ldrStatus <=80) {
    digitalWrite(ledPin,   HIGH);            
   }
  else {
    digitalWrite(ledPin,   LOW);      
  }
}
