//www.elegoo.com
//2016.12.08
// Define Pins
#define BLUE 3
#define GREEN 5
#define RED 6

const int SW_pin = 2; // digital pin connected to switch output
const int X_pin = A0; // analog pin connected to X output
const int Y_pin = A1; // analog pin connected to Y output

int delayTime = 10; // fading time between colors
int shiftValue = 5;
int redValue = 255;
int greenValue = 0;
int blueValue = 0;

int buttonRpin = 8;
int buttonGpin = 9;
int buttonBpin = 10;

int powerOn = 1;

byte leds = 0;

void setup() 
{
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
  digitalWrite(RED, HIGH);
  digitalWrite(GREEN, LOW);
  digitalWrite(BLUE, LOW);

  pinMode(buttonRpin, INPUT_PULLUP);  
  pinMode(buttonGpin, INPUT_PULLUP);  
  pinMode(buttonBpin, INPUT_PULLUP); 

  pinMode(SW_pin, INPUT);
  digitalWrite(SW_pin, HIGH);
  // Serial.begin(9600); 
}

void loop() 
{
  if (digitalRead(SW_pin) == LOW)
  {
    powerOn = 1 - powerOn;
      delay(500);

  }

  if (digitalRead(buttonRpin) == LOW)
  {
    redValue += shiftValue;
    greenValue -= shiftValue;
    blueValue -= shiftValue;
  }
  if (digitalRead(buttonGpin) == LOW)
  {

    redValue -= shiftValue;
    greenValue += shiftValue;
    blueValue -= shiftValue;
  }
  if (digitalRead(buttonBpin) == LOW)
  {
    
    redValue -= shiftValue;
    greenValue -= shiftValue;
    blueValue += shiftValue;
  }
  
  
  redValue = max(min(redValue,255),0);
  greenValue = max(min(greenValue,255),0);
  blueValue = max(min(blueValue,255),0);

  if (powerOn == 1)
  {
    analogWrite(RED, redValue);
    analogWrite(GREEN, greenValue);
    analogWrite(BLUE, blueValue);
  }
  else
  {
    analogWrite(RED, 0);
    analogWrite(GREEN, 0);
    analogWrite(BLUE, 0);
  }
  delay(delayTime);
}
