"""
Exer 6-2

Create a recursive function that would sort out a list of integers of undefined length.

"""

def sorter(given):
    if len(given)<=1:
        return given
    
     #quicksort algorithm

    shift=given[0]
    left=[]                
    right=[]

    for i in range(1, len(given)):
        if given[i]<shift:
            left.append(given[i])
        else:
            right.append(given[i])
    return sorter(left) + [shift] + sorter(right)

num_list=[1,20,56,78,33,2,90]
print(sorter(num_list))