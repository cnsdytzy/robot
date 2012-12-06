#include <Servo.h>
const int STOP = 1533;
Servo m1, m2, m3;


const int ledPin = 13;
const int buttonPin = 17;


void setup() {
	setupUserInput();
	setupMotors();
	Serial.begin(9600);
} 

void setupUserInput(){
	pinMode(buttonPin, INPUT);
	pinMode(ledPin, OUTPUT);
}

void setupMotors(){
	m1.attach(9);
	
	m2.attach(10);
	m3.attach(11);
}

void loop() { 

		m1.write(STOP);
		m2.write(STOP);
		m3.write(STOP);
		Serial.println(servo0);
		m3.write(servo0);
		delay(100);



}








