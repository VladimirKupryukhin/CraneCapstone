#include "pico/stdlib.h"
#include <stdio.h>
#include <stdlib.h>
#include "hardware/gpio.h"
#include "hardware/adc.h"
#include <tusb.h>

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

float getVoltageAsADC(){
    float conversion_factor = 3.3f / (1 << 12);
    float adc_value = adc_read();
    return adc_value;
}


void sendSTART(){
    printf("start\n");
}

void sendSMRT1Temp(){

    //select 1
    gpio_put(PIN_S0, 1);
    gpio_put(PIN_S1, 0);
    short dut1V = getVoltageAsADC();

    if (dut1V == 0) {
        printf("smrt1t0000\n");
    }
    else{
        printf("smrt1t%hu\n", dut1V);
    }

}

void sendSMRT1A(){
    short temp = 2910;
    printf("smrt13%hu\n", temp);
}

void sendSMRT1BPOS(){
    short temp = 2910;
    printf("smrt1+%hu\n", temp);
}

void sendSMRT1BNEG(){
    short temp = 2910;
    printf("smrt1-%hu\n", temp);
}

//asdsa

void sendSMRT2Temp(){
    //select 2
    gpio_put(PIN_S0, 0);
    gpio_put(PIN_S1, 1);
    short dut2V = getVoltageAsADC();

    if (dut2V == 0) {
        printf("smrt2t0000\n");
    }
    else{
        printf("smrt2t%hu\n", dut2V);
    }
}

void sendSMRT2A(){
    short temp = 2910;
    printf("smrt23%hu\n", temp);
}

void sendSMRT2BPOS(){
    short temp = 2910;
    printf("smrt2+%hu\n", temp);
}

void sendSMRT2BNEG(){
    short temp = 2910;
    printf("smrt2-%hu\n", temp);
}

//asdasdas

void sendSMRT3Temp(){
    //select 3
    gpio_put(PIN_S0, 1);
    gpio_put(PIN_S1, 1);
    short dut3V = getVoltageAsADC();

    if (dut3V == 0) {
        printf("smrt3t0000\n");
    }
    else{
        printf("smrt3t%hu\n", dut3V);
    }
}

void sendSMRT3A(){
    short temp = 2910;
    printf("smrt33%hu\n", temp);
}

void sendSMRT3BPOS(){
    short temp = 2910;
    printf("smrt3+%hu\n", temp);
}

void sendSMRT3BNEG(){
    short temp = 2910;
    printf("smrt3+%hu\n", temp);
}

void sendEND(){
    printf("end\n");
}

void mainloop(){

    char inputBuffer[10];//"get\n"
    fgets(inputBuffer, 10, stdin);
    //printf("RAW DATA: %s\n", inputBuffer);
    tud_cdc_read_flush();

    if (inputBuffer[0] == 'g') {
        //printf("69420\n");
        sendSTART();

        sendSMRT1Temp();
        sendSMRT1A();
        sendSMRT1BPOS();
        sendSMRT1BNEG();

        sendSMRT2Temp();
        sendSMRT2A();
        sendSMRT2BPOS();
        sendSMRT2BNEG();

        sendSMRT3Temp();
        sendSMRT3A();
        sendSMRT3BPOS();
        sendSMRT3BNEG();

        sendEND();

    }




    




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