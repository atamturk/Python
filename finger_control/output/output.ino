#include <cvzone.h>

SerialData serialData(2,1); //(numOfValsRec,digitsPerValRec)

/*0 or 1 - 1 digit
0 to 99 -  2 digits 
0 to 999 - 3 digits 
 */

int valsRec[1];

void setup() {
  serialData.begin(); 
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(12,OUTPUT); 
}

void loop() {
  
  serialData.Get(valsRec);
  if(valsRec[0]== 0){
  digitalWrite(8,0);
  digitalWrite(9,0);
  digitalWrite(10,0);
  digitalWrite(11,0);
  digitalWrite(12,0);
  }
  else if(valsRec[0]== 1){
  digitalWrite(8,1);
  digitalWrite(9,0);
  digitalWrite(10,0);
  digitalWrite(11,0);
  digitalWrite(12,0);
  } 
  else if(valsRec[0]== 2){
  digitalWrite(8,1);
  digitalWrite(9,2);
  digitalWrite(10,0);
  digitalWrite(11,0);
  digitalWrite(12,0);
  } 
  else if(valsRec[0]== 3){
  digitalWrite(8,1);
  digitalWrite(9,1);
  digitalWrite(10,1);
  digitalWrite(11,0);
  digitalWrite(12,0);
  } 
  else if(valsRec[0]== 4){
  digitalWrite(8,1);
  digitalWrite(9,1);
  digitalWrite(10,1);
  digitalWrite(11,1);
  digitalWrite(12,0);
  }
  else if(valsRec[0]== 5){
  digitalWrite(8,1);
  digitalWrite(9,1);
  digitalWrite(10,1);
  digitalWrite(11,1);
  digitalWrite(12,1);
  } 
  else {
  digitalWrite(8,0);
  digitalWrite(9,0);
  digitalWrite(10,0);
  digitalWrite(11,0);
  digitalWrite(12,0);
  }  
}
