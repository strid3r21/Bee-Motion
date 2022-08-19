
#define PIR 5  //defining the PIR

void setup() {
  Serial.begin(115200);

  pinMode(PIR, INPUT);   //Setting the PIR as an Input
 
    WiFi.begin(WLAN_SSID, WLAN_PASS);
  delay(2000);
}


void loop() {
 

  if(digitalRead(PIR) == HIGH){   //if the PIR reads HIGH, then its detecting motion.
   Serial.println("Motion Detected!!!");   
  delay(500); 
  }else{    //if its not reading HIGH (ie, its LOW) then there is no motion detected.
    Serial.println("No Motion");
    delay(500); 
  }

               
}
