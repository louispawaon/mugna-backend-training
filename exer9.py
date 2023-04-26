'''
Exer 9

Create a function that converts a 4-byte (8 digits) hexadecimal value
as a string parameter, into its decimal equivalent

Create 2 custom exceptions:

HexFormatError: raise if string does not fit with the format for hexadecimal
MemoryError: raise if the string is beyond 4-bytes (8 hex digits)

'''
class HexFormatError(Exception):
    pass

class MemoryError(Exception):
    pass

def hex_to_decimal(string):
    if len(string) > 8:
        raise MemoryError("String is beyond 4-bytes!")
    
    try:
        decimal_val = int(string,16)
    except:
        raise HexFormatError("String does not fit with the format!")
    
    print (f"Decimal value of {string} is {decimal_val}")

hex_to_decimal("1d3f8F1")