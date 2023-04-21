'''
-------------------------ENDTERM EXAM-----------------
DO NOT DELETE THE FOLLOWING CODE
'''
import sys
try:
    input1 = sys.argv[1]
except:
    pass
'''
In the following file, do not delete anything (comments, code, ...). Just add you code in every part (one per exercise).
Use my variable for input (if there is any), use my printing for output (if there is any).
You can upload your code to codepost.io to check the tests. A sucess in one test doesn't always mean than your exercise is correct,
a fail doesn't always mean that your exercise is wrong. I will check all codes.
At the end of exam, you should upload the last version of your code to codepost.io or to the online folder on Teams.
The only authorized packages are:
- pandas
- pyarrow
- fastparquet
- numpy
- sklearn
- matplotlib
- datetime

'''

if input1 == '1':
    # ----------------------EXERCISE 1 - Data Cleaning--------------------------------------
    # Instructions:
    # Open the dataframe (Ex_1_price_to_clean_v6.parquet) with the read_parquet() function of the pandas package.
    # If you upload your code to codepost use the the following path in the read_parquet() function : "Ex_1_price_to_clean_v6.parquet".
    # Remove the line or lines with the data under the wrong format from the dataframe, reset the indexes, sort it by the date column and print it.
    # Keep the same format for the date column and be sure than the other columns are in float format.
        import pandas as pd 
        predictions = pd.read_parquet(r"C:\Users\user\Downloads\Ex_1_price_to_clean_v6.parquet")

        arr = ['Date', 'Open', 'Hgih', 'Close', 'Adj Close', 'Volume']
        for i in arr:
            predictions.dropna(subset=[i], inplace = True)

        predictions = predictions.reset_index()   

        predictions['Date'] = pd.to_datetime(predictions['Date'])
        predictions.index = predictions['Date']
        del predictions['Date']
        predictions.sort_index()


    # Here is the command to print the final data (where predictions is all the predictions of your model.)
        print(np.around(predictions,3))
    # ---------------------End of EXERCISE 1 --------------------------------------

elif input1 == '4':
# ----------------------EXERCISE 4 - Machine Learning II--------------------------------------
# Instructions:
# You have a model (linear regression) trained with two features and a label : feature1, feature2 and label.
# What is the prediction of this model for three samples : 
#	- feature 1 : -1 and feature 2 : 145
#	- feature 1 : 3 and feature 2 : 183
#	- feature 1 : -4 and feature 2 : 166
# You can find the wanted predictions in the file named Ex_4_predictions_V6.txt

    import sklearn.linear_model as skmod
    import numpy as np
    feature1 = np.array([-3, 9, -8, 1, 8, -1, -9, 9, 9, -3, 2, 9, 2, 7, 8, -10, -3, 0, -1, -4])
    feature2 = np.array([118, 174, 173, 150, 156, 181, 137, 173, 151, 197, 149, 198, 164, 147, 189, 108, 103, 130, 119, 165])
    label = np.array([19.0, -44.0, 32.0, 5.0, -28.0, 14.0, 38.0, -38.0, -41.0, 24.0, 1.0, -33.0, 1.0, -17.0, -35.0, 70.0, 25.0, 8.0, 19.0, 29.0])
    model = skmod.LinearRegression().fit(np.hstack([feature1.reshape(-1,1), feature2.reshape(-1,1)]), label.reshape(-1,1))


    predictions = model.predict(np.array([[12.982]
                                        [-8.975]
                                        [24.911]]))








    # Here is the command to print the final data (where predictions is all the predictions of your model.)
    print(predictions)
# ----------------------End of EXERCISE 4 --------------------------------------

