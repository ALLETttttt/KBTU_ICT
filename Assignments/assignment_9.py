'''
For your assignment, please use the code below first and then write your code.
DO NOT DELETE THE FOLLOWING CODE
'''
import sys
try:
    input1 = sys.argv[1]
    input2 = sys.argv[2]
    input3 = sys.argv[3]
except:
    # print("You didn't put any input when you run your code! Please add an input!")
    input1 = ""
    input2 = ""
    input3 = ""


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
from sklearn.linear_model import LogisticRegression

security = [int(i) for i in input1.split(',')]
kabel = [i for i in input2.split(',')]
securityPredict = [int(i) for i in input3.split(',')]

security = np.array(security)
security = security.reshape(-1,1)
securityPredict = np.array(securityPredict)
securityPredict = securityPredict.reshape(-1,1)

photomodel = LogisticRegression()
photomodel.fit(security, kabel)

predictions = photomodel.predict(securityPredict)
    
probability = photomodel.predict_proba(securityPredict.reshape(-1,1))




#Use this code for your output where:
#        - feature_predict is the list of features given for prediction (=input3)
#        - predictions is the list of predictions made by your model with the feature_predict.
#        - Predictions_proba is the list a probability of each classes for each predictions (shape looks like [[0.2, 0.8], [0.5, 0.5], [0.6, 0.4]…..], it has two items per predictions, we take the maximum one).
 
for i in range(len(predictions)):
    print("For a feature egal to {}, the most probable result is {} with a probability of {:.2f}.".format(securityPredict[i], predictions[i], max(probability[i])))
