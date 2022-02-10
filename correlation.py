from re import X
import numpy as np

def print_as_table(**kwargs):
    
    for key in kwargs.keys():
        print(str(key).ljust(5), end=" | ") 
        # .center(5) is a string method to align values in a particular padding and center them
        # other options are .ljust() which will align to the right
    print() #cause next value to move under

    for key in kwargs.values():
        print(str(key).ljust(5), end=" | ")
    

print_as_table(x =[1,3], y = 30, z = 40, bola = 15)

# x = [1,2,3,4,5,6,7]
# y = [21,31,41,51,13,42,67]


# meanx = ((sum(x))/ (len(x)))
# # print(meanx)
# meany = ((sum(y))/ (len(y)))
# # NUMERATOR
# erxbar = list(map(lambda a: (a - meanx), x))
# erybar = list(map(lambda a: (a - meany), y))
# upper = [num*aw for num,aw in zip(erxbar,erybar)]
# sumupper = sum(upper)
# # DENOMINATOR
# downx = list(map(lambda s: s**2, erxbar))
# downx = sum(downx)
# downy = list(map(lambda s: s**2, erybar))
# downy = sum(downy)
# down = ((downx * downy) ** 0.5)

# r = sumupper / down
# print(r)
# r2 = np.corrcoef(x,y)[0,1]
# print(r2)
