#!/usr/local/opt/python/bin/python2.7
"""Decode VINs from the NHTSA API as of 6/16/28."""
#import urllib2
from urllib.request import urlopen
import json


class VinDecoder():
    """Super simple module to decode VINs using the NHTSA API."""

    def __init__(self):
        """Initialize the decoder."""
        return None

    def decode(self, vin):
        """Decode the given VIN."""
        url = 'https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/\
            %s?format=json&vehicletype=truck' % vin

        url = url.strip()
        url = url.replace(" ", "")
        res = urlopen(url).read()
        print(str(res))
        obj = json.loads(res)
        ctry=""
        if 'Results' in obj:
            o = obj['Results']
            for i in o:
                if 'Variable' not in i:
                    return None
                if i['Variable'] == 'Model Year':
                    year = i['Value']
                if i['Variable'] == 'Make':
                    make = i['Value']
                if i['Variable'] == 'Model':
                    model = i['Value']
                if i['Variable'] == 'Displacement (L)':
                    disp = i['Value']
                if i['Variable'] == 'Engine Number of Cylinders':
                    cyl = i['Value']
                if i['Variable'] == 'Plant Country':
                    ctry = i['Value']
                if i['Variable'] == 'Vehicle Type':
                    vhcl = i['Value']
#            print ("vin: %s %s %s %s, Disp: %s Cyl: %s Country:%s Vehicle type %s" , (vin, year, make, model, disp, cyl,ctry,vhcl))
            return {'vin': vin, 'year': year, 'make': make,
                    'model': model, 'disp': disp, 'cyl': cyl,'country':ctry,'vehicle type':vhcl}
    def formatArrayJson(self,vinArray):
         vinArray = str(vinArray)
         vinArray = vinArray.replace('\'',"").replace(', ',";").replace(']',"").replace('[',"")
         return vinArray
    def decodeBatch(self, vinArray):
         """Decode the given VIN."""
         print("in decode batch")
         vinArray = self.formatArrayJson(vinArray)
#         vinArray = str(vinArray)
#         vinArray = vinArray.replace('\'',"").replace(', ',";").replace(']',"").replace('[',"")
         url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/%s?format=json' % vinArray

         resultMap = {}
#         return resultMap
         url = url.strip()
         url = url.replace(" ", "")
#         print(url)
#         print(url)
         res = urlopen(url).read()
         obj = json.loads(res)
         ctry=""
         resultMap = {}
         count = 0
         if 'Results' in obj:
             o = obj['Results']
             for j in o:

                 for i in j:
                     if 'Variable' not in i:
                         return None
                     if i['Variable'] == 'Model Year':
                        year = i['Value']
                     if i['Variable'] == 'Make':
                        make = i['Value']
                     if i['Variable'] == 'Model':
                        model = i['Value']
                     if i['Variable'] == 'Displacement (L)':
                        disp = i['Value']
                     if i['Variable'] == 'Engine Number of Cylinders':
                        cyl = i['Value']
                     if i['Variable'] == 'Plant Country':
                        ctry = i['Value']
                     if i['Variable'] == 'Vehicle Type':
                        vhcl = i['Value']
#                 print ("vin: %s %s %s %s, Disp: %s Cyl: %s Country:%s Vehicle type %s" , (vin, year, make, model, disp, cyl,ctry,vhcl))
                 resultMap.update({count:{'vin': vin, 'year': year, 'make': make,
                    'model': model, 'disp': disp, 'cyl': cyl,'country':ctry,'vehicle type':vhcl}})
                 count = count + 1
         return resultMap




if __name__ == "__main__":
    vd = VinDecoder()
    vin = '1GNGK56K19R227051'
    d = vd.decode(vin)
    print (d)
