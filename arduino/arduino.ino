#include <Servo.h>

Servo myservo;  // create servo object to control a servo

String angle_str;
int angle;
String recieved;

void setup() {
  myservo.attach(6);  // attaches the servo on pin 9 to the servo object
  Serial.begin(9600);
  pinMode(8, INPUT);
  pinMode(9, OUTPUT);
}

void loop() {
       // scale it for use with the servo (value between 0 and 180)
  if (Serial.available()) { // S’il y a des nouvelles données à lire
    String recieved = Serial.readStringUntil('\n'); // On lit entièrement la ligne reçue ('\n' <=> Nouvelle ligne)
    if (recieved[0] = 'S') {
      if (recieved[1] = '1') {
        angle_str = "";
        angle_str += recieved[3];
        angle_str += recieved[4];
        angle_str += recieved[5];
        angle = angle_str.toInt();
        Serial.println(angle_str);
        myservo.write(angle);
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
