#include <Arduino.h>

#if SERVER_MODE
    #include "ble_server.hpp"
#elif CLIENT_MODE
    #include "ble_client.hpp"
#endif

/****************************************************************
 * Function Definitions
 ***************************************************************/

void setup() {

    Serial.begin(115200);

#if SERVER_MODE
    Serial.print("Starting BLE server...");
    start_bluetooth_server();
    Serial.print("BLE server started...");
#elif CLIENT_MODE
    Serial.print("Setting up BLE client...");
    start_bluetooth_client();
    Serial.print("BLE client started...");
#endif
}

void loop() {

#if SERVER_MODE
    /**Nothing to do here */
#elif CLIENT_MODE
    do_client_tasks();
    publish_rssi();
#endif

}

