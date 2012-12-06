#include <Servo.h>
Servo m[3];
const int STOP = 1533;
const int MAX = 1733;
const int MIN = 1333;
const int ledPin = 13;
const int buttonPin = 17;
int incomingByte = 0;


void setup() {
	setupUserInput();
	setupMotors();
	setupSensors();
	Serial.begin(9600);
} 

void setupUserInput(){
	pinMode(buttonPin, INPUT);
	pinMode(ledPin, OUTPUT);
}

void setupMotors(){
	m[0].attach(9);
	m[1].attach(10);
	m[2].attach(11);
}

void setupSensors(){
	pinMode(14, INPUT);
	pinMode(15, INPUT);
	pinMode(16, INPUT);
}

short readSensor(byte sensorNum){
	return analogRead(ledPin+sensorNum);
}

void setMotor(byte motorNum, int speed){
	m[motorNum-1].write(speed);
}

void stopAll(){
	m[0].write(STOP);
	m[1].write(STOP);
	m[2].write(STOP+7);
}

void north(){
	m[0].write(MAX);
	m[1].write(MIN);
	m[2].write(STOP);
}

void south(){
	m[0].write(MIN);
	m[1].write(MAX);
	m[2].write(STOP);
}

void east(){
	m[0].write(1583);
	m[1].write(1583);
	m[2].write(MIN);
}

void west(){
	m[0].write(1486);
	m[1].write(1486);
	m[2].write(MAX);
}

void left(){
	m[0].write(MAX);
	m[1].write(MAX);
	m[2].write(MAX);
}

void right(){
	m[0].write(MIN);
	m[1].write(MIN);
	m[2].write(MIN);

}

void ledOn(bool state){
	if(state){
		digitalWrite(ledPin, HIGH);
	} else {
		digitalWrite(ledPin, LOW);
	}
}

bool isButtonDown(){
	if(analogRead(buttonPin)>1000){
		return true;
	} else {
		return false;
	}
}

void loop(){ 
        stopAll();
        while(true){
          if (Serial.available() > 0) {
                  incomingByte = Serial.read();
                  switch(incomingByte){
                    case 'N':
                      north();
                      break;
                    case 'E':
                      east();
                      break;
                    case 'S':
                      south();
                      break;
                    case 'W':
                      west();
                      break;
                    case 'H':
                      stopAll();
                    break; 
                    case 'L':
                      left();
                    break; 
                    case 'R':
                      right();
                    break; 
                  }
                  delay(3);
          }
        }

}

