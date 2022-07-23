//NOTE! the Serial Monitor debugging does not work when deep sleep is being used as the serial cant initializae with the board going to sleep constantly.
// if you need to debug, remove the deep sleep functionallity and then add it back in once you've locked down your normal code.

#define BUTTON_PIN_BITMASK 0x20 // 2^5 in hex
RTC_DATA_ATTR int bootCount = 0;


void print_wakeup_reason(){
  esp_sleep_wakeup_cause_t wakeup_reason;

  wakeup_reason = esp_sleep_get_wakeup_cause();

  switch(wakeup_reason)
  {
    case ESP_SLEEP_WAKEUP_EXT0 : Serial.println("Wakeup caused by external signal using RTC_IO"); break;
    case ESP_SLEEP_WAKEUP_EXT1 : Serial.println("Wakeup caused by external signal using RTC_CNTL"); break;
    case ESP_SLEEP_WAKEUP_TIMER : Serial.println("Wakeup caused by timer"); break;
    case ESP_SLEEP_WAKEUP_TOUCHPAD : Serial.println("Wakeup caused by touchpad"); break;
    case ESP_SLEEP_WAKEUP_ULP : Serial.println("Wakeup caused by ULP program"); break;
    default : Serial.printf("Wakeup was not caused by deep sleep: %d\n",wakeup_reason); break;
  }
}

void setup() {
  Serial.begin(115200);

  pinMode(5, INPUT);
  pinMode(1, OUTPUT);

    ++bootCount;
  Serial.println("Boot number: " + String(bootCount));


  //Print the wakeup reason for ESP32
  print_wakeup_reason();
    esp_sleep_enable_ext0_wakeup(GPIO_NUM_5, 1); //1 = High, 0 = Low. Setting the PIR sensor to be the wake up source.

/////// your code for whatever you want the board to do once woken up goes here.
  digitalWrite(1, HIGH);   
  delay(100); 
  digitalWrite(1, LOW);      
  delay(100); 

/////

  digitalWrite(5, LOW);  //set the PIR to off. if you dont do this it will seep more current than it should. setting it to LOW before going to sleep will allow the board to sleep at 45uA.
  esp_deep_sleep_start(); //going to sleep 

}

void loop() {
 
            // nothing happens here   
}
