#include <Arduino.h>

#include "ble.hpp"

/****************************************************************
 * Function Definitions
 ***************************************************************/

void setup() {

    Serial.begin(115200);

#if SERVER_MODE
    Serial.print("Starting BLE server...");
    start_bluetooth_server();
    Serial.print("BLE server started...");
#endif
}

void loop() {

    /**Nothing to do here for now */

}

