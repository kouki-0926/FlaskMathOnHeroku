#include <DHT.h>

#define DHT_PIN 13
#define DHT_Type DHT11

float temperature;
float humidity;

DHT dht(DHT_PIN,DHT_Type);

void setup(){
  Serial.begin(9600);
  dht.begin();
}

void loop(){
  char var=Serial.read();
  if(var=='m'){
    measure_tempereture();
  }
}

void measure_tempereture(){
  temperature=dht.readTemperature();
  humidity=dht.readHumidity();
  Serial.println(temperature);
  Serial.println(humidity);
}
