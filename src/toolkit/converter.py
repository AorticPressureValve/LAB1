import src.toolkit.errors as error

from .constants import *

mm = ['mm', 'Mm', 'mM', 'MM']
cm = ['cm', 'Cm', 'cM', 'CM']
m = ['m', 'M']
km = ['km', 'Km', 'kM', 'KM']
g = ['g', 'G']
kg = ['kg', 'Kg', 'kG', 'KG']
c = ['c', 'C']
f = ['f', 'F']
k = ['k', 'K']
length = mm + cm + m + km
temperature = c + f + k
weight = g + kg
everything = length + temperature + weight


def convert(value: float, from_unit: str, to_unit: str):

    if from_unit in length and to_unit in length:



        if value >  0:

            if from_unit in mm:
                
                if to_unit in cm:
                    return value / 10
                elif to_unit in m:
                    return value / 1000
                elif to_unit in km:
                    return value / 1000000
                if to_unit in mm:
                    return value
            
            elif from_unit in cm:
                
                if to_unit in mm:
                    return value * 10
                elif to_unit in cm:
                    return value
                elif to_unit in m:
                    return value / 100
                elif to_unit in km:
                    return value / 100000
                
            elif from_unit in m:
                
                if to_unit in mm:
                    return value * 1000
                elif to_unit in cm:
                    return value * 100
                elif to_unit in m:
                    return value
                elif to_unit in km:
                    return value / 1000
            
            elif from_unit in km:
                
                if to_unit in mm:
                    return value * 10 * 100 * 1000
                elif to_unit in cm:
                    return value * 100 * 1000
                elif to_unit in m:
                    return value * 1000
                elif to_unit in km:
                    return value
        else:
            raise error.NegativeLengthError()
    
    elif from_unit in temperature and to_unit in temperature:
        


        if from_unit in f and value < FAHRENHEIT_ABSOLUTE_ZERO or from_unit in c and value < CELSIUS_ABSOLUTE_ZERO or from_unit in k and value < KELVIN_ABSOLUTE_ZERO:
            raise error.BellowAbsoluteZeroError(from_unit, value)




        if from_unit in c:

            if to_unit in f:
                return (value * 1.8) + 32
            elif to_unit in k:
                return 273.15 + value
            
        if from_unit in f:

            if to_unit in c:
                return (value - 32) / 1.8
            elif to_unit in k:
                return 273.15 + (value - 32) / 1.8
            
        if from_unit in k:

            if to_unit in c:
                return value - 273.15
            elif to_unit in f:
                return (value - 273.15) * 1.8 + 32



    elif from_unit in weight and to_unit in weight:
        
        if value > 0:

            if from_unit in g:
                return value / 1000
            elif from_unit in kg:
                return value * 1000



    
    elif from_unit not in everything or to_unit not in everything:
        raise error.UnknownUnitError()
    
    else: raise error.DiffirentGroupsError(from_unit, to_unit)