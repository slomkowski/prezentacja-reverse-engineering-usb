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
    """Filtracja tego urządzenia, które posiada odpowiedni vendor string i product string."""
    return dev.manufacturer == MANUFACTURER_NAME and dev.product == PRODUCT_NAME


def find_device_handle():
    return usb.core.find(idVendor=VENDOR_ID, idProduct=DEVICE_ID,
                         custom_match=check_manufacturer_and_product)


dev_handle = find_device_handle()

print(dev_handle)
