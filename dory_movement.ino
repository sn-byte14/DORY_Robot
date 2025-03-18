#define trigPin 9
#define echoPin 10
#define motorLeft 5
#define motorRight 6

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(motorLeft, OUTPUT);
  pinMode(motorRight, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  long duration, distance;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;

  if (distance < 20) {
    Serial.println("Obstacle Detected!");
    digitalWrite(motorLeft, LOW);
    digitalWrite(motorRight, LOW);
    delay(500);
  } else {
    digitalWrite(motorLeft, HIGH);
    digitalWrite(motorRight, HIGH);
  }
}
