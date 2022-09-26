
#define Red  8
#define Yellow 9 
#define Green 10 
#define Button 11

 uint8_t ControlFlag = 0 ; // control flag 
void Check_flag() ; // function checks the button 
void setup() {

pinMode(Red,OUTPUT)   ; // initialize the pins of the LEDS
pinMode(Yellow,OUTPUT); 
pinMode(Green,OUTPUT) ;
pinMode(Button,INPUT_PULLUP) ;
}

void loop() {
switch (ControlFlag)
{
case 0 :
  digitalWrite(Red,HIGH) ;
  digitalWrite(Green,LOW) ;
  break ;
case 1 :   
  digitalWrite(Yellow,HIGH) ;
  digitalWrite(Red,LOW) ;
  break ;
 case 2 :
 digitalWrite(Green,HIGH) ;
 digitalWrite(Yellow,LOW) ;
 break ;
 default :
  {
    // check error 
  }
}
  Check_flag() ; 
}

void Check_flag()
{ while(1)
{ if (digitalRead(Button)==LOW) 
  {    ControlFlag++ ;
        if (3==ControlFlag)  // reset flag :D
             ControlFlag=0 ;
            delay(300) ; //  to delay the reading of the button
           break ;         
  }
        
}
}
