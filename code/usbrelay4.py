#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time
import sys

import usb.core
import usb.util

VENDOR_ID = 0x16c0
DEVICE_ID = 0x05df

MANUFACTURER_NAME = "www.dcttech.com"
PRODUCT_NAME = "USBRelay2"


def check_manufacturer_and_product(dev):
    return dev.manufacturer == MANUFACTURER_NAME and dev.product == PRODUCT_NAME


def find_device_handle():
    return usb.core.find(idVendor=VENDOR_ID, idProduct=DEVICE_ID,
                         custom_match=check_manufacturer_and_product)


dev_handle = find_device_handle()

if dev_handle.is_kernel_driver_active(0):
    try:
        dev_handle.detach_kernel_driver(0)
        print("kernel driver detached")
    except usb.core.USBError as e:
        sys.exit("Could not detach kernel driver: %s" % str(e))

requestType = usb.util.build_request_type(usb.util.CTRL_OUT,
                                          usb.util.CTRL_TYPE_CLASS,
                                          usb.util.CTRL_RECIPIENT_INTERFACE)


def set_relay(relay_number, enabled: bool):
    b1 = 0xff if enabled else 0xfd
    dev_handle.ctrl_transfer(requestType, 9, 0x0300, 0, (b1, relay_number, 0, 0, 0, 0, 0, 0))


while True:
    set_relay(1, True)
    time.sleep(1)
    set_relay(1, False)
    time.sleep(1)
    set_relay(2, True)
    time.sleep(1)
    set_relay(2, False)
    time.sleep(1)
