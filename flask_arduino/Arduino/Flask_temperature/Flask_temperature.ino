#include <DHT.h>
#include <SoftPWM_RGB.h>

#define DHT_PIN 13
#define DHT_Type DHT11
#define REDPIN 8
#define GREENPIN 9
#define BLUEPIN 10

float temperature;
float humidity;

DHT dht(DHT_PIN, DHT_Type);
RGB rgb(REDPIN, GREENPIN, BLUEPIN);

void setup() {
    Serial.begin(9600);
    dht.begin();
    rgb.init();
    blink(3);
}

void loop() {
    char var = Serial.read();

    switch (var) {
        case 'm':
            measure_tempereture();
            break;
        case 'r':
            RGB();
            break;
        case 'b':
            blink(5);
            break;
        case 'h':
            rgb.on(1);
            break;
        case 'l':
            rgb.off(1);
            break;
    }
}

void measure_tempereture() {
    temperature = dht.readTemperature();
    humidity = dht.readHumidity();
    Serial.println(temperature);
    Serial.println(humidity);
    blink(3);
}

void RGB() {
    int max = 255;
    for (int i = 0; i < max; i++) {
        rgb.RGB_LED(i, max - i, 0, 5);
    }
    for (int i = 0; i < max; i++) {
        rgb.RGB_LED(max - i, 0, i, 5);
    }
    for (int i = 0; i < max; i++) {
        rgb.RGB_LED(0, i, max - i, 5);
    }
}

void blink(int num) {
    int delayTime = 100;
    while (num--) {
        rgb.off(delayTime);
        rgb.on(delayTime);
    }
}