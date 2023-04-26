"""
Exer 6-1

Create a function that would create a multiplication table made of nested lists.

- It must accept 1 argument, then create nxn multiplication table
- It must accept 2 arguments, then create nxm, multiplication table
- The function should raise and error if arguments < 1 or > 2
- Function must accept 2 arguments  of different order as long as, 

n = number of cols
m = number of rows
"""

def multiplication_table(*args):

    if len(args) < 1 or len(args) > 2: #Check number of arguments <1 or >2
        raise ValueError("Function must receive one or two integer arguments only")
    elif len(args)==1:
        n,m = args[0], args[0]
    elif len(args)==2:
        n,m = args

    if type(n) != int or (m is not None and type(m) != int): #Check if n and m are according to their type
        raise TypeError ("Enter appropriate n or m")
    
    for i in range(1, m+1):
        row = []
        for j in range(1, n+1):
            row.append(i*j)
        print(row)
        
multiplication_table(5,5)

