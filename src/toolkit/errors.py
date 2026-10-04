class CalcError(ValueError):
    pass

class ConvertError(ValueError):
    pass

class NegativeLengthError(ConvertError):
    def __init__(self):
        super().__init__("Cannot convert negative length")

class BellowAbsoluteZeroError(ConvertError):
    def __init__(self, from_unit, value):

        if from_unit == 'k' or from_unit == 'K':
            super().__init__(f"Cannot convert value bellow absolute zero: {value} < 0 in kelvin")
        
        if from_unit == 'f' or from_unit == 'F':
            super().__init__(f"Cannot convert value bellow absolute zero: {value} < -459.67 in fahrenheit")

        if from_unit == 'c' or from_unit == 'C':
            super().__init__(f"Cannot convert value bellow absolute zero: {value} < -273.15 in celcius")

class DiffirentGroupsError(ConvertError):
    def __init__(self, from_unit, to_unit):
        super().__init__(f"Cannot convert '{from_unit}' to '{to_unit}'")

class UnknownUnitError(ConvertError):
    def __init__(self):
        super().__init__("Unknown unit type")

class NotSupportedCharacter(CalcError):
    def __init__(self, character):
        super().__init__(f"'{character}' is not supported")

class ZeroDisivionError(CalcError):
    def __init__(self):
        super().__init__("Cannot divide by 0")

class NothingError(CalcError):
    def __init__(self):
        super().__init__(f'No expression is given')
