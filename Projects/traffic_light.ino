// Section 1: Define Pins
#define RED 11
#define YELLOW 12
#define GREEN 13
#define buttonPin 5

// Section 2: Setup 
void setup() 
{
  pinMode(RED, OUTPUT);
  pinMode(YELLOW, OUTPUT);
  pinMode(GREEN, OUTPUT);

  pinMode(buttonPin, INPUT_PULLUP);  
}

// Section 3: Starting light values
int redValue = 1;
int yellowValue = 0;
int greenValue = 0;

// Section 4: main program
void loop() 
{
  // Section 4.1: Button
  if (digitalRead(buttonPin) == LOW)
  {
    if (greenValue == 1)
    {
      greenValue = 0;
      yellowValue = 1;
      redValue = 0;
    }
    else if (yellowValue == 1)
    {
      greenValue = 0;
      yellowValue = 0;
      redValue = 1;
    }
    else if (redValue == 1)
    {
      greenValue = 1;
      yellowValue = 0;
      redValue = 0;
    }

    delay(200);
  }
  
  // Section 4.2: Update lights
  digitalWrite(RED, redValue);
  digitalWrite(YELLOW, yellowValue);
  digitalWrite(GREEN, greenValue);
}
