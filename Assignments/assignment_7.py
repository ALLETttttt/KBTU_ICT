'''
For your assignment, please use the code below first and then write your code.
DO NOT DELETE THE FOLLOWING CODE
'''
import sys
try:
    input1 = sys.argv[1]
    input2 = sys.argv[2]
except:
    print("You didn't put any input when you run your code! Please add an input!")
    input1 = ""
    input2 = ""


'''
The objective of this assignment is to print the expected output.
You can find it in the instruction folder.
List of installed and authorized packages :
    - numpy
    - scikit-learn (import sklearn)
You cannot use other packages than the listed ones (except built-in default package in python).
You can write you code after this comment :
'''

#Your code here:
import numpy as np
from sklearn.linear_model import LinearRegression


list1 = [int(i) for i in input1.split(',')]
list2 = [int(i) for i in input2.split(',')]

Ox = np.array(list1).reshape((-1, 1))
Oy = np.array(list2)

moda = LinearRegression().fit(Ox, Oy)
w1 = float(moda.coef_)
b = float(moda.intercept_)


#use this printing (where "w1" is the weight and "b" the bias)
print("The most accurate linear regression has the following equation: y' = {:0.2f}*x + {:0.2f}".format(w1, b))