"""
Exer 11

Given a string, verify whether it is a valid credit card number from ABCD Bank
or not. The verifier function is_valid_credit_card_number should be written as a separate function

A valid credit card from ABCD Bank has the following characteristics:

- It must start with 4,5,6 
- It must contain exactly 16 digits 
- It must only consist of digits (0-9)
- It may have digits in groups of 4, separated by one hyphen "-"
- It must NOT use any separator like ''.'_'. etc
- It must NOT have 4 or more consecutive repeated digits

"""
import re

def is_valid_credit_card_number(card_number):
    pattern = r'^[456](?!.*(\d)(?:-?\1){4})\d{3}(?:-?\d{4}){3}$'

    if not re.match(pattern, card_number):
        return False
    
    else:
        return True
    
print(is_valid_credit_card_number('4567-1234-5678-9123'))

#4567-1234-5678-9123
#4567123456789123
#4567-1234-4442-9123

