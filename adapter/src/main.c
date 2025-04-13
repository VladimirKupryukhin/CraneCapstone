#include "pico/stdlib.h"
#include <stdio.h>
#include <stdlib.h>
#include "../include/myADC.h"
#include "../include/constants.h"



void initPins(){
    
    gpio_init(PIN_V_ADC_CS);
    gpio_init(PIN_DUT1_RTD_ADC_CS);
    gpio_init(PIN_DUT2_RTD_ADC_CS);
    gpio_init(PIN_DUT3_RTD_ADC_CS);

}


int main () {
    stdio_init_all();

    gpio_init(25);
    gpio_set_dir(25, GPIO_OUT);

    for (int index = 0; index < 10; index++) {
        gpio_put(25,index % 2);
        sleep_ms(1000);
        printf("%d \n", index);
    }

    


    return 0;
}