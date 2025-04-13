#ifndef MYADC_H
#define MYADC_H


struct ADC_RESULT {
    int adcID;
    short adcValue;
};

enum ADC_NAME{
    DUT1_RTD_ADC = 0,
    DUT2_RTD_ADC = 1,
    DUT3_RTD_ADC = 2,
    VOLTAGE_ADC = 3
};


struct ADC_RESULT* readADC(enum ADC_NAME target);

void adcInitConvo();
void adcConversion();
short readADCBits();





#endif