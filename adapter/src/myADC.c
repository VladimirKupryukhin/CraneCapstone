#include "../include/myADC.h"


struct ADC_RESULT* readADC(int target){
    struct ADC_RESULT* result = malloc(sizeof(struct ADC_RESULT));
    result->adcID = target;
    // result->adcValue = 12345;

    

    return result;
}

void adcInitConvo(){

}

void adcConversion(){


}

short readADCBits(){


}
