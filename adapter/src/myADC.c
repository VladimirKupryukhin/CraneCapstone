#include "../include/myADC.h"



struct ADC_RESULT* readADC(int target){
    struct ADC_RESULT* result = malloc(sizeof(struct ADC_RESULT));
    result->adcID = target;
    // result->adcValue = 12345;
    //gpio_set_dir(PIN_MY_MISO, GPIO_OUT);
    //gpio_put(PIN_MY_MISO, 1);
    
    adcInitConvo();
    adcConversion();
    short ADCvalue = readADCBits(PIN_DUT1_RTD_ADC_CS);
    result->adcValue = ADCvalue;
    
    printf("\n---RAW ADC%u\n---", (unsigned short)ADCvalue);
    adcIdleBus();
    sleep_ms(100);
    
    return NULL;
}

void adcIdleBus(){
    gpio_put(PIN_CONVERT, 0);

    // Set the MISO/SDO to LOW
    //gpio_set_dir(PIN_MY_MISO, GPIO_OUT);
    //gpio_put(PIN_MY_MISO, 0);

    // All chip selects are high (active low)
    // This means that currently all CS are deselected
    gpio_put(PIN_V_ADC_CS, 1);
    gpio_put(PIN_DUT1_RTD_ADC_CS, 1);
    gpio_put(PIN_DUT2_RTD_ADC_CS, 1);
    gpio_put(PIN_DUT3_RTD_ADC_CS, 1);

    // Put the clock pin to LOW
    gpio_put(PIN_MY_SCK, 0);
}

void adcInitConvo(){
    // Rising edge on CNV
    sleep_ms(5);
    gpio_put(PIN_CONVERT, 1);

}

void adcConversion(){
    sleep_ms(5);
}

short readADCBits(int target){
    //gpio_put(PIN_CONVERT, 1);
    gpio_set_dir(PIN_MY_MISO, GPIO_IN);
    // Pull CS to LOW
    gpio_put(PIN_DUT1_RTD_ADC_CS, 0);

    short result = 0;

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(10);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(10);
    result = result | ((gpio_get(PIN_MY_MISO)) << 15);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(10);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(10);
    result = result | ((gpio_get(PIN_MY_MISO)) << 14);
    
    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(10);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(10);
    result = result | ((gpio_get(PIN_MY_MISO)) << 13);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(10);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(10);
    result = result | ((gpio_get(PIN_MY_MISO)) << 12);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(10);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(10);
    result = result | ((gpio_get(PIN_MY_MISO)) << 11);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(10);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(10);
    result = result | ((gpio_get(PIN_MY_MISO)) << 10);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(10);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(10);
    result = result | ((gpio_get(PIN_MY_MISO)) << 9);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(10);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(10);
    result = result | ((gpio_get(PIN_MY_MISO)) << 8);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(10);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(10);
    result = result | ((gpio_get(PIN_MY_MISO)) << 7);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(10);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(10);
    result = result | ((gpio_get(PIN_MY_MISO)) << 6);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(10);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(10);
    result = result | ((gpio_get(PIN_MY_MISO)) << 5);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(10);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(10);
    result = result | ((gpio_get(PIN_MY_MISO)) << 4);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(10);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(10);
    result = result | ((gpio_get(PIN_MY_MISO)) << 3);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(10);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(10);
    result = result | ((gpio_get(PIN_MY_MISO)) << 2);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(10);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(10);
    result = result | ((gpio_get(PIN_MY_MISO)) << 1);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(10);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(10);
    result = result | ((gpio_get(PIN_MY_MISO)) << 0);

    return result;
}

