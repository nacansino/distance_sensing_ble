/**
 * @file ble_server.hpp
 * @author Niel Cansino (nielcansino@gmail.com)
 * @brief   
 * @version 0.1
 * @date 2020-09-13
 * 
 * @copyright Copyright (c) 2020
 * 
 */

#pragma once

#include "ble_common.hpp"

/****************************************************************
 * Definitions and Constants
 ***************************************************************/
static constexpr char DEVICE_NAME[]  = "Distance_Server";

/****************************************************************
 * Function Prototypes
 ***************************************************************/
/**Empty here */

/****************************************************************
 * Global Variables
 ***************************************************************/
/**Empty here */

/****************************************************************
 * Classes
 ***************************************************************/

class peripheralCallback : public BLEServerCallbacks{
  
  void onConnect(BLEServer* pServer){
    // client connected
    Serial.println("Client connected");
  }

  void onDisconnect(BLEServer* pServer){
    // client disconnected
    Serial.println("Client disconnected");
  }

};

/****************************************************************
 * Function Definition
 ***************************************************************/

void start_bluetooth_server()
{
    BLEDevice::init(DEVICE_NAME);

    /**Create bluetooth server (advertiser) */
    BLEServer       *pServer        = BLEDevice::createServer();
    BLEService      *pService       = pServer->createService(SERVICE_UUID);
    BLEAdvertising  *pAdvertising   = BLEDevice::getAdvertising();

    /**Bind server callback */
    pServer ->setCallbacks(new peripheralCallback());
    pAdvertising->addServiceUUID(SERVICE_UUID);

    /**Start service */
    pService->start();

    pAdvertising->setScanResponse(true);
    pAdvertising->setMinPreferred(0x06);  // functions that help with iPhone connections issue
    pAdvertising->setMinPreferred(0x12);

    /**Start advertising */
    BLEDevice::startAdvertising();

}
