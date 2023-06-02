#include <Servo.h>

Servo servo1;  // create servo object to control a servo
Servo servo2;

String angle_str;
int angle;
String recieved;

void setup() {
  servo1.attach(6);  // attaches the servo on pin 9 to the servo object
  servo2.attach(5);

  Serial.begin(9600);
  pinMode(8, INPUT);
  pinMode(9, OUTPUT);
}

void loop() {
       // scale it for use with the servo (value between 0 and 180)
  if (Serial.available()) { // S’il y a des nouvelles données à lire
    String recieved = Serial.readStringUntil('\n'); // On lit entièrement la ligne reçue ('\n' <=> Nouvelle ligne)
    if (recieved[0] == 'S') {
      Serial.println("Dans S");
      if (recieved[1] == '1') {
        Serial.println("Dans S1");
        angle_str = "";
        angle_str += recieved[3];
        angle_str += recieved[4];
        angle_str += recieved[5];
        angle = angle_str.toInt();
        Serial.println(angle_str);
        servo1.write(angle);
        delay(10);
      } else if (recieved[1] == '2') {
        Serial.println("Dans S2");

        angle_str = "";
        angle_str += recieved[3];
        angle_str += recieved[4];
        angle_str += recieved[5];
        angle = angle_str.toInt();
        Serial.println(angle_str);
        servo2.write(angle);
        delay(10);
      }
    }
  }

  digitalWrite(9, HIGH); // On demande une mesure
  delayMicroseconds(10); // en allumant le pin
  digitalWrite(9, LOW); // trigger pendant 10 ms.
  long duration = pulseIn(8, HIGH); // On lit le résultat de la mesure (durée pendant laquelle le pin reste HIGH)
  int distance = duration * 0.034 / 2; // On calcul la distance = durée * vitesse du son en ms / 2 (distance mesurer = aller-retour => / 2)
  Serial.print("distance="); // On affiche le résultat
  Serial.println(distance);

  delay(500);
}
