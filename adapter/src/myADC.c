#include "../include/myADC.h"



struct ADC_RESULT* readADC(int target){
    //struct ADC_RESULT* result = malloc(sizeof(struct ADC_RESULT));
    //result->adcID = target;
    // result->adcValue = 12345;
    //gpio_set_dir(PIN_MY_MISO, GPIO_OUT);
    //gpio_put(PIN_MY_MISO, 1);
    //gpio_put(PIN_MY_SCK, 1);
    

    // gpio_put(PIN_DUT2_RTD_ADC_CS, 1);
    // gpio_put(PIN_MY_SCK, 0);
    // gpio_put(PIN_CONVERT, 0);

    // //conv and init
    // sleep_ms(10);
    // gpio_put(PIN_CONVERT, 1);
    // sleep_ms(10);

    // gpio_put(PIN_DUT2_RTD_ADC_CS, 0);

    // //clock 
    // gpio_put(PIN_MY_SCK, 0);
    // sleep_ms(10);
    // gpio_put(PIN_MY_SCK, 1);
    // sleep_ms(10);

    // gpio_put(PIN_MY_SCK, 0);
    // sleep_ms(10);
    // gpio_put(PIN_MY_SCK, 1);
    // sleep_ms(10);

    // gpio_put(PIN_MY_SCK, 0);
    // sleep_ms(10);
    // gpio_put(PIN_MY_SCK, 1);
    // sleep_ms(10);

    // gpio_put(PIN_MY_SCK, 0);
    // sleep_ms(10);
    // gpio_put(PIN_MY_SCK, 1);
    // sleep_ms(10);

    // gpio_put(PIN_MY_SCK, 0);
    // sleep_ms(10);
    // gpio_put(PIN_MY_SCK, 1);
    // sleep_ms(10);

    // gpio_put(PIN_MY_SCK, 0);
    // sleep_ms(10);
    // gpio_put(PIN_MY_SCK, 1);
    // sleep_ms(10);

    // gpio_put(PIN_MY_SCK, 0);
    // sleep_ms(10);
    // gpio_put(PIN_MY_SCK, 1);
    // sleep_ms(10);

    // gpio_put(PIN_MY_SCK, 0);
    // sleep_ms(10);
    // gpio_put(PIN_MY_SCK, 1);
    // sleep_ms(10);

    // gpio_put(PIN_MY_SCK, 0);
    // sleep_ms(10);
    // gpio_put(PIN_MY_SCK, 1);
    // sleep_ms(10);

    // gpio_put(PIN_MY_SCK, 0);
    // sleep_ms(10);
    // gpio_put(PIN_MY_SCK, 1);
    // sleep_ms(10);

    // gpio_put(PIN_MY_SCK, 0);
    // sleep_ms(10);
    // gpio_put(PIN_MY_SCK, 1);
    // sleep_ms(10);

    // gpio_put(PIN_MY_SCK, 0);
    // sleep_ms(10);
    // gpio_put(PIN_MY_SCK, 1);
    // sleep_ms(10);

    // gpio_put(PIN_MY_SCK, 0);
    // sleep_ms(10);
    // gpio_put(PIN_MY_SCK, 1);
    // sleep_ms(10);

    // gpio_put(PIN_MY_SCK, 0);
    // sleep_ms(10);
    // gpio_put(PIN_MY_SCK, 1);
    // sleep_ms(10);

    // gpio_put(PIN_MY_SCK, 0);
    // sleep_ms(10);
    // gpio_put(PIN_MY_SCK, 1);
    // sleep_ms(10);

    // gpio_put(PIN_MY_SCK, 0);
    // sleep_ms(10);
    // gpio_put(PIN_MY_SCK, 1);
    // sleep_ms(10);


    adcInitConvo();
    adcConversion();
    //short ADCvalue1 = readADCBits(PIN_DUT1_RTD_ADC_CS);
    short ADCvalue2 = readADCBits(PIN_DUT2_RTD_ADC_CS);
    //ADCvalue2 = readADCBits(PIN_DUT2_RTD_ADC_CS);
    //short ADCvalue3 = readADCBits(PIN_DUT3_RTD_ADC_CS);
    //short ADCvalue4 = readADCBits(PIN_V_ADC_CS);



    //result->adcValue = ADCvalue1;
    // result->adcValue = 69;
    
    //printf("\n---RAW ADC 1 %u\n", (unsigned short)ADCvalue1);
    printf("RAW ADC 2 %u\n", (unsigned short)ADCvalue2);
    //printf("RAW ADC 3 %u\n", (unsigned short)ADCvalue3);
    //printf("RAW ADC 4 %u\n---", (unsigned short)ADCvalue4);
    adcIdleBus();
    
    sleep_ms(100);
    
    return NULL;
}

void adcIdleBus(){

    // Put the clock pin to LOW
    gpio_put(PIN_MY_SCK, 0);

    // Set the MISO/SDO to LOW
    //gpio_set_dir(PIN_MY_MISO, GPIO_OUT);
    //gpio_put(PIN_MY_MISO, 0);

    // All chip selects are high (active low)
    // This means that currently all CS are deselected
    gpio_put(PIN_V_ADC_CS, 1);
    gpio_put(PIN_DUT1_RTD_ADC_CS, 1);
    gpio_put(PIN_DUT2_RTD_ADC_CS, 1);
    gpio_put(PIN_DUT3_RTD_ADC_CS, 1);

    sleep_ms(5);
    gpio_put(PIN_CONVERT, 0);


    
}

void adcInitConvo(){
    // Rising edge on CNV
    //sleep_us(1);
    sleep_ms(1);
    gpio_put(PIN_CONVERT, 1);

}

void adcConversion(){
    //sleep_us(1);
    sleep_ms(1);
}

short  readADCBits(int target){
    //gpio_put(PIN_CONVERT, 1);
    // gpio_set_dir(PIN_MY_MISO, GPIO_IN);
    // Pull CS to LOW
    gpio_put(target, 0);
    //gpio_put(PIN_CONVERT, 0);
    sleep_ms(1);
    //sleep_us(1);

    short result = 0;

    // gpio_put(PIN_MY_SCK, 0);
    // sleep_ms(1);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(1);
    result = result | ((gpio_get(PIN_MY_MISO)) << 15);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(1);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(1);
    result = result | ((gpio_get(PIN_MY_MISO)) << 14);
    
    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(1);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(1);
    result = result | ((gpio_get(PIN_MY_MISO)) << 13);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(1);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(1);
    result = result | ((gpio_get(PIN_MY_MISO)) << 12);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(1);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(1);
    result = result | ((gpio_get(PIN_MY_MISO)) << 11);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(1);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(1);
    result = result | ((gpio_get(PIN_MY_MISO)) << 10);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(1);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(1);
    result = result | ((gpio_get(PIN_MY_MISO)) << 9);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(1);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(1);
    result = result | ((gpio_get(PIN_MY_MISO)) << 8);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(1);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(1);
    result = result | ((gpio_get(PIN_MY_MISO)) << 7);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(1);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(1);
    result = result | ((gpio_get(PIN_MY_MISO)) << 6);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(1);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(1);
    result = result | ((gpio_get(PIN_MY_MISO)) << 5);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(1);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(1);
    result = result | ((gpio_get(PIN_MY_MISO)) << 4);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(1);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(1);
    result = result | ((gpio_get(PIN_MY_MISO)) << 3);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(1);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(1);
    result = result | ((gpio_get(PIN_MY_MISO)) << 2);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(1);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(1);
    result = result | ((gpio_get(PIN_MY_MISO)) << 1);

    gpio_put(PIN_MY_SCK, 0);
    sleep_ms(1);
    gpio_put(PIN_MY_SCK, 1);
    sleep_ms(1);
    result = result | ((gpio_get(PIN_MY_MISO)) << 0);

    return result;
}

