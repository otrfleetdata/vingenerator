#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 08:27:40 2020

@author: otrjcmadigan
"""

import vin
from vin_decoder import VinDecoder
vd = VinDecoder()
print(vd.decode(vin.getRandomVin()))
