#include "pico/stdlib.h"
#include <stdio.h>
#include <stdlib.h>
#include "../include/myADC.h"
#include "../include/constants.h"

enum ADC_NAME;

void initPins(){
    // Chip select pins
    gpio_init(PIN_V_ADC_CS);
    gpio_init(PIN_DUT1_RTD_ADC_CS);
    gpio_init(PIN_DUT2_RTD_ADC_CS);
    gpio_init(PIN_DUT3_RTD_ADC_CS);
    gpio_init(PIN_CONVERT);

    gpio_set_dir(PIN_V_ADC_CS, GPIO_OUT);
    gpio_set_dir(PIN_DUT1_RTD_ADC_CS, GPIO_OUT);
    gpio_set_dir(PIN_DUT2_RTD_ADC_CS, GPIO_OUT);
    gpio_set_dir(PIN_DUT3_RTD_ADC_CS, GPIO_OUT);
    gpio_set_dir(PIN_CONVERT, GPIO_OUT);

    // CLOCK and MISO pins
    gpio_init(PIN_MY_MISO);
    gpio_init(PIN_MY_SCK);

    //gpio_set_dir(PIN_MY_MISO, GPIO_OUT);
    gpio_set_dir(PIN_MY_MISO, GPIO_IN);
    //gpio_put(PIN_MY_MISO, 1);
    gpio_set_dir(PIN_MY_SCK, GPIO_OUT);

    // Onboard LED 
    gpio_init(25);
    gpio_set_dir(25, GPIO_OUT);
}

void writeToUSB(struct ADC_RESULT* adcResult){
    printf("%d", adcResult->adcID);

    // Send integers as ASCII characters since I am lazy
    for (int offset = 15; offset > -1; offset--) {
        printf("%d", ((adcResult->adcValue) & (1<<offset)) >> offset);
    }

    printf("\n");


}

void mainLoop(){
    
    for (int device = 0; device < 1; device++) {
        struct ADC_RESULT* adcResult = readADC(device);
       // writeToUSB(adcResult);
        free(adcResult);
    }
}


int main () {
    stdio_init_all();
    initPins();

    
    // For debugging purposes
    for (int index = 0; index < 10; index++) {
        gpio_put(25,index % 2);
        //gpio_put(PIN_MY_SCK,index % 2);
        sleep_ms(1000);
        printf("%d \n", index);
    }

    // Main loop
    while (true) {
        mainLoop();

    }


    return 0;
}
