#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 08:27:40 2020

@author: otrjcmadigan
"""

import vin
import pandas as pd
from vin_decoder import VinDecoder
vd = VinDecoder()
#vd.decode(vin.getRandomVin())
#vd.decode('1GTGK241remain4D5C3REM')
#vd.decode('WAUPEAFMremainA38Y7J8Y')
x = vin.getNRandomVin(500)
vinTable = []
for v in x:
	mapVin = vd.decode(v)
	if mapVin['vehicle type']=='TRUCK ':
		vinTable.append(mapVin)

vindf = pd.DataFrame(vinTable)
vinTruck = vindf[vindf['vehicle type']=='TRUCK ']
vinTruck.to_csv('vintrucks.csv')

