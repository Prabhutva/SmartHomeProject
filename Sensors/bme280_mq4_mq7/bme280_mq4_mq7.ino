int i=0;
#include "MQ7.h"
MQ7 mq7(A0,5.0);

#include <Wire.h>
#include "SparkFunBME280.h"
BME280 mySensor;

#include <SPI.h>   //Library for SPI interface 
#include <Wire.h>  //Library for I2C interface 
int gas_sensor = A1;                             //Sensor pin
float m = -0.318;                                //Slope
float b = 1.133;                                 //Y-Intercept
float R0 = 11.820;  


void setup() {  
  
Serial.begin(9600);
pinMode(10,OUTPUT); //FOR MQ7

Wire.begin();//for bme
while (mySensor.beginI2C() == false) //Begin communication over I2C
{
   Serial.println("#Error:BME280 did not respond");
   //while(1); //Freeze
}

}

void loop() {
  
if(i<60){
  analogWrite(9,255);
  Serial.print("@MQ7.CO.PPM:+" );
  Serial.print((float)i);
//  Serial.println();
}
else if (i<150){
  analogWrite(9,72);
  Serial.print("@MQ7.CO.PPM:-" );
  Serial.print((float)i);
//  Serial.println();
}
else if(i=150){ 
  Serial.print("@MQ7.CO.PPM:");
  digitalWrite(9,HIGH);
  delay(50);
  Serial.print(mq7.getPPM());
//  Serial.println();
  i=0;
} 
i++;
  //BME
  Serial.print("@BME.Humidity:");
  Serial.print(mySensor.readFloatHumidity(), 0);
//  Serial.println();

  Serial.print("@BME.Pressure:");
  Serial.print(mySensor.readFloatPressure(), 0);
//  Serial.println();

  Serial.print("@BME.Altitude:");
  //Serial.print(mySensor.readFloatAltitudeMeters(), 1);
  Serial.print(mySensor.readFloatAltitudeMeters(), 1);
//  Serial.println();

  Serial.print("@BME.Temperature:");
  //Serial.print(mySensor.readTempC(), 2);
  Serial.print(mySensor.readTempC(), 2);
//  Serial.println();

//mq4
float sensor_volt;                             //Define variable for sensor voltage
  float RS_gas;                                  //Define variable for sensor resistance
  float ratio;                                   //Define variable for ratio
  float sensorValue = analogRead(gas_sensor);    //Read analog values of sensor
  sensor_volt = sensorValue * (4.4 / 1023.0);    //Convert analog values to voltage
  RS_gas = ((4.4 * 10.0) / sensor_volt) - 10.0;  //Get value of RS in a gas
  ratio = RS_gas / R0;                           // Get ratio RS_gas/RS_air
  double ppm_log = (log10(ratio) - b) / m;       //Get ppm value in linear scale according to the the ratio value
  double ppm = pow(10, ppm_log);                 //Convert ppm value to log scale
  double percentage = ppm / 10000;               //Convert to percentage
  Serial.print("@MQ4.CH4.PPM:");
  
  Serial.println(ppm);
//  Serial.println();
delay(1000);
    
}
