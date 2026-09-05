void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  analogReadResolution(14);
  Serial.println("timestamp_ms,value");
}

void loop() {
  // put your main code here, to run repeatedly:
  unsigned long t = millis();
  int value = analogRead(A0);
  Serial.print(t);
  Serial.print(",");
  Serial.println(value);
  delay(2);
}
