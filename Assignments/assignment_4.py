
'''
The objective of this assignment is to print the csv file as a dataframe.
When you upoad your code, the path to the csv file should be "airbus_price.csv"
You can find it in the instruction folder.
List of installed and authorized packages :
    - csv
    - pandas
You cannot use other packages than the listed ones (except built-in default package in python).
You can write you code after this comment :
'''

#Your code here:

import pandas as pd
df = pd.read_csv("airbus_price.csv")
print(df)