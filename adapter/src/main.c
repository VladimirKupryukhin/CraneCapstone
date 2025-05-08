#include "pico/stdlib.h"
#include <stdio.h>
#include <stdlib.h>
#include "hardware/gpio.h"
#include "hardware/adc.h"

#define PIN_S0 16
#define PIN_S1 17
#define PIN_SIG 26


void initPins(){
    gpio_init(PIN_S0);
    gpio_init(PIN_S1);
    gpio_init(PIN_SIG);

    gpio_set_dir(PIN_S0, GPIO_OUT);
    gpio_set_dir(PIN_S1, GPIO_OUT);
    adc_select_input(0);//adc0 gp26

    // Onboard LED 
    gpio_init(25);
    gpio_set_dir(25, GPIO_OUT);

}

float getVoltageFromADC(){
    float conversion_factor = 3.3f / (1 << 12);
    float adc_value = adc_read();
    float voltage = adc_value * conversion_factor;
    printf("%f\n", adc_value);

    return voltage;
}

void mainloop(){
    //select 0
    //gpio_put(PIN_S0, 0);
    //gpio_put(PIN_S1, 0);
    //float dut1V = getVoltageFromADC();

    //select 1
    //gpio_put(PIN_S0, 1);
    //gpio_put(PIN_S1, 0);
    //float dut2V = getVoltageFromADC();

    //select 2
    //gpio_put(PIN_S0, 0);
    //gpio_put(PIN_S1, 1);
    
    //select 3
    gpio_put(PIN_S0, 1);
    gpio_put(PIN_S1, 1);
    float dut3V = getVoltageFromADC();
    //float inputV = getVoltageFromADC();

    //printf("\n----\ndut1V: %f\n", dut1V);
    // printf("dut2V: %f\n", dut2V);
    printf("dut3V: %f\n", dut3V);
    // printf("inputV: %f\n", inputV);

    sleep_ms(100);



}



int main(){
    stdio_init_all();
    adc_init();
    initPins();

    
    // For debugging purposes
    for (int index = 0; index < 10; index++) {
        gpio_put(25,index % 2);
        //gpio_put(PIN_MY_SCK,index % 2);
        sleep_ms(1000);
        printf("%d \n", index);
    }

    while (true) {
        mainloop();
    }

    return 0;
}