const unsigned long INTERVAL_US = 1000;
unsigned long lastSample = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(500000);
  analogReadResolution(14);
  lastSample = micros();
}

void loop() {
  // put your main code here, to run repeatedly:
  unsigned long now = micros();
  if (now - lastSample >= INTERVAL_US) {
    lastSample += INTERVAL_US);
    int value = analogRead(A0);
    Serial.print(now);
    Serial.print(",");
    Serial.println(value);
  }
}
