"""
Exer 12

Create an iterator named PrimeNumberDigit that would return the 
prime number (starting with lowest possible value) that contains
a given integer in its digits

div  = PrimeNumberDigit(13)
next(div) -> 13
next(div) -> 113
next(div) -> 131
next(div) -> 137
next(div) -> 139

"""

class PrimeNumberDigit:
    def __init__(self, divisible):
        self.divisible = divisible # 13
        self.current = divisible 

    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            if str(self.divisible) in str(self.current) and self.is_prime(self.current): # if 13 is in currentNum and currentNum is prime
                prime_num = self.current
                self.current += 1
                return prime_num
            else:
                self.current += 1

    def is_prime(self, num):
        if num < 2:
            return False
        for x in range(2, num):
            if num % x == 0:
                return False
        return True

div = PrimeNumberDigit(1)
print(next(div))
print(next(div))
print(next(div))
print(next(div))
print(next(div))
print(next(div))
    











