#ifndef MYADC_H
#define MYADC_H

#include "../include/constants.h"
#include "pico/stdlib.h"
#include <stdlib.h>


struct ADC_RESULT {
    int adcID;
    short adcValue;
};


/**
 * DUT1_RTD_ADC = 0,
 * DUT2_RTD_ADC = 1,
 * DUT3_RTD_ADC = 2,
 * VOLTAGE_ADC = 3
 * 
 * 
 */
struct ADC_RESULT* readADC(int target);

void adcIdleBus();
void adcInitConvo();
void adcConversion();
short readADCBits(int target);





#endif