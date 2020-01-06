#
def toLowerCase(str: str):
    return str.lower()
print(toLowerCase("ABCCC"))


def reverseWords(s: str):
    StrList =s.split(" ")
    StrR = ""
    for i in StrList:
        Str = ''.join(reversed(i))+" "
        StrR = StrR + " "+ Str
    return StrR
print(reverseWords("Let's take deep learning contest"))


counter=0
from itertools import permutations
for i in permutations([1,2,3,4],3):
    print("{}{}{}".format(i[0],i[1],i[2]),end=" ")
    counter +=1
print("")
print("共{}种组合".format(counter))


import math
import numpy as np
def FirstFactorial(num):
    st = ""
    x = math.factorial(num)
    st = "1"
    for i in range(2,num+1):
        #（4 * 3 * 2 * 1）= 24
       st = st +"*"+ str(i)
    print("("+st+") = ", end='')
    return x
print(FirstFactorial(6))
print(str(100))
print(3779*0.8)