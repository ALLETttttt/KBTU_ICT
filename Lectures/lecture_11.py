#!/usr/bin/env python
# coding: utf-8

# # Correction of practice 10

# In[1]:


import numpy as np
import sklearn.linear_model as skmod


# In[6]:


x1 = [6, 10, 2, 3, 4, 0, 7, 8, 9, 1]
y = [130, 21, 43, 76, 105, 3, 167, 162, 91, 15]
arr_x1 = np.array(x1).reshape(-1,1)
print(arr_x1)
arr_y = np.array(y).reshape(-1,1)
print(arr_y)
arr_x2 = arr_x1**2
arr_x3 = arr_x1**3
print(arr_x2)
print(arr_x3)


# In[18]:


model = skmod.LinearRegression()
model = model.fit(arr_x1, arr_y)
print("Eq: {:.2f}*x + {:.2f}".format(model.coef_[0][0], model.intercept_[0]) )
print("score is : {:.2f}".format(model.score(arr_x1, arr_y)))


# In[19]:


#degree2
arr_x12 = np.hstack([arr_x1, arr_x2])
model2 = skmod.LinearRegression().fit(arr_x12, arr_y)
print("Eq: {:.2f}*x + {:.2f}*x**2 + {:.2f}".format(model2.coef_[0][0],
                                                   model2.coef_[0][1], 
                                                   model2.intercept_[0]))
print("score is : {:.2f}".format(model2.score(arr_x12, arr_y)))


# In[20]:


#degree3
arr_x123 = np.hstack([arr_x1, arr_x2, arr_x3])
model3 = skmod.LinearRegression().fit(arr_x123, arr_y)
print("Eq: {:.2f}*x + {:.2f}*x**2 +{:.2f}*x**3 + {:.2f}".format(
                                                    model3.coef_[0][0],
                                                   model3.coef_[0][1],
                                                   model3.coef_[0][2],
                                                   model3.intercept_[0]))
print("score is : {:.2f}".format(model3.score(arr_x123, arr_y)))


# In[32]:


import matplotlib.pyplot as plt
plt.scatter(arr_x1, arr_y)
plt.plot([0,10], model.predict(np.array([[0], [10]])))
x_for_plot = np.arange(0,10,0.1).reshape(-1,1) #like range
x2_for_plot = x_for_plot**2
plt.plot(x_for_plot, model2.predict(np.hstack([x_for_plot, x2_for_plot])))
x3_for_plot = x_for_plot**3
plt.plot(x_for_plot, model3.predict(np.hstack([x_for_plot, x2_for_plot, x3_for_plot])))
plt.show()


# # Lecture 11: Machine Learning III

# In[33]:


#import some package
import numpy as np
import sklearn.linear_model as skmod
import sklearn.preprocessing as skprepro
import sklearn.model_selection as sksel
import matplotlib.pyplot as plt


# ## The polynomial features object

# In[35]:


#Create data and reshape it
x1 = [6, 10, 2, 3, 4, 0, 7, 8, 9, 1]
arr_x1 = np.array(x1).reshape(-1,1)
print(arr_x1)


# In[46]:


#Create the polynomial feature object from the preprocessing module
#PolynomialFeatures() function
#choose the degree and don't include bias
poly2 = skprepro.PolynomialFeatures(degree = 2, include_bias = False)


# In[47]:


#Transform your data into fetaures of degree two, fit_transform() function
arr_x_poly = poly2.fit_transform(arr_x1)
print(arr_x_poly)


# In[51]:


#Your turn (10 minutes)
#From the data of practice, make a polynomial regression of degree 8
#print the coef of the model
#degree2
# arr_x12 = np.hstack([arr_x1, arr_x2]) #replace this line
#create polynomial object
poly8 = skprepro.PolynomialFeatures(8, include_bias = False)
#model:
model = skmod.LinearRegression().fit(poly8.fit_transform(arr_x1), arr_y)
#print coef
print(model.coef_)


# ## Train and test set

# In[70]:


#let's create data, you can check this code at home
data_x = np.random.normal(9, 4, 100)
data_y = np.random.randint(70,130, size = (len(data_x)))/100*(data_x*data_x*8 + 2*data_x + 5)
plt.scatter(data_x, data_y)
data_x = data_x.reshape(-1,1)
data_y = data_y.reshape(-1,1)
# print(data_x)
# print(data_y)


# In[125]:


#Let's keep 20 % of our data aside
data_x_train = data_x[:80]
data_x_test = data_x[80:]
data_y_train = data_y[:80]
data_y_test = data_y[80:]
plt.scatter(data_x_train, data_y_train)
plt.scatter(data_x_test, data_y_test)


# In[133]:


#choose a test and train set with scikit-learn:
#import sklearn.model_selection and use the train_test_split() function
#The order is train/test, train/test
import sklearn.model_selection as sksel
data_x_train, data_x_test, data_y_train, data_y_test =                         sksel.train_test_split(data_x, 
                                               data_y, 
                                               train_size = 0.75, 
                                               shuffle = True)

plt.scatter(data_x_train, data_y_train)
plt.scatter(data_x_test, data_y_test)


# In[134]:


#Let's use the Polynomial transform of the sklearn.preprocessing module
poly2 = skprepro.PolynomialFeatures(2, include_bias = False)
data_x_train_poly2 = poly2.fit_transform(data_x_train)
data_x_test_poly2 = poly2.fit_transform(data_x_test)


# In[135]:


#let's make our regression of degree 2
model2 = skmod.LinearRegression().fit(data_x_train_poly2, data_y_train)


# In[136]:


#Let's plot our result
plt.scatter(data_x_train, data_y_train)
plt.scatter(data_x_test, data_y_test)
plt.plot(np.arange(0,18,0.1), model2.predict(poly2.fit_transform(np.arange(0,18,0.1).reshape(-1,1))))


# In[137]:


#Let's do for all regression for degree 8
poly8 = skprepro.PolynomialFeatures(8, include_bias = False)
data_x_train_poly8 = poly8.fit_transform(data_x_train)
data_x_test_poly8 = poly8.fit_transform(data_x_test)
model8 = skmod.LinearRegression().fit(data_x_train_poly8, data_y_train)
plt.scatter(data_x_train, data_y_train)
plt.scatter(data_x_test, data_y_test)
plt.plot(np.arange(0,18,0.1), model2.predict(poly2.fit_transform(np.arange(0,18,0.1).reshape(-1,1))))
plt.plot(np.arange(0,18,0.1), model8.predict(poly8.fit_transform(np.arange(0,18,0.1).reshape(-1,1))))


# In[138]:


#Result of our model of the training set: the score function 
#(1 = perfect fitting, 0 = no fitting at all)
print("Training :", model2.score(data_x_train_poly2, data_y_train))
print("Testing :", model2.score(data_x_test_poly2, data_y_test))
print('-'*20)
print("Training :", model8.score(data_x_train_poly8, data_y_train))
print("Testing :", model8.score(data_x_test_poly8, data_y_test))


# In[139]:


'''
Result of several runs

'''


# ## Values scaling

# ### The logic behind scaling

# In[152]:


#Create two features with different size with random (use function np.random.randint())
data_x1 = np.random.randint(10000, 20000, size = (20))
data_x2 = np.random.randint(0, 10, size = (20))
print(data_x1)
print(data_x2)


# In[141]:


#Let's try to plot it together
plt.scatter(range(20), data_x1)
plt.scatter(range(20), data_x2)


# In[142]:


#We can scale our data with normalization ((x - xmin)/(xmax - xmin))
data_x1_norm = (data_x1 - min(data_x1))/(max(data_x1)- min(data_x1))
data_x2_norm = (data_x2 - min(data_x2))/(max(data_x2)- min(data_x2))


# In[144]:


#Let's plot it again

plt.scatter(range(20), data_x1_norm)
plt.scatter(range(20), data_x2_norm)


# In[146]:


#We can scale our data with standardization
data_x1_stan = (data_x1 - np.mean(data_x1))/np.std(data_x1)
data_x2_stan = (data_x2 - np.mean(data_x2))/np.std(data_x2)


# In[147]:


#we can now plot our data
plt.scatter(range(20), data_x1_stan)
plt.scatter(range(20), data_x2_stan)


# In[150]:


#The difference between normalisation and standardization when there is outliers
#Let's plot it
data_x1[0] = -100_000
data_x1_norm = (data_x1 - min(data_x1))/(max(data_x1)- min(data_x1))
data_x2_norm = (data_x2 - min(data_x2))/(max(data_x2)- min(data_x2))
plt.scatter(range(20), data_x1_norm)
plt.scatter(range(20), data_x2_norm)
plt.show()
data_x1_stan = (data_x1 - np.mean(data_x1))/np.std(data_x1)
data_x2_stan = (data_x2 - np.mean(data_x2))/np.std(data_x2)
plt.scatter(range(20), data_x1_stan)
plt.scatter(range(20), data_x2_stan)
plt.ylim(-1.1,1.1)


# ### The scikit-learn object

# In[151]:


#Create the scaler object StandardScaler() object
scaler = skprepro.StandardScaler()


# In[154]:


#prepare our data: 2 columns because 2 features
data_x = np.hstack([data_x1.reshape(-1,1), data_x2.reshape(-1,1)])
print(data_x)


# In[164]:


#use it on your data with the fit(), transform(), fit_transform()
scaler_f = scaler.fit(data_x)
data_x_stan = scaler_f.transform(data_x)
# print(data_x_stan)
print(scaler_f.transform([[5, 5]]))


# In[168]:


#Use inverse_transform method to come back for standardized data to real data
print(scaler.inverse_transform([[0.01, 0.01]]))


# In[185]:


#YOUR TURN (10 minutes)
#On the file in Teams (use copy past to transfer it in python), 
#tranform the three lists in a 10*3 matrix of standardized features
l1 = np.array([22, 85, 96, 81, 68, 97, 29, 61, 73, 86])
l2 = np.array([1489022, 1073767, 1975250, 1493073, 1063635, 1017921, 1206827, 1217274, 1933018, 1325618])
l3 = np.array([-99.67, -99.37, -99.08, -99.54, -99.8, -99.21, -99.73, -99.78, -99.6, -99.48])
l = np.hstack([l1.reshape(-1,1), l2.reshape(-1,1), l3.reshape(-1,1) ])
scaler_f = skprepro.StandardScaler()
# scaler_f = scaler.fit(l)
# l_stan = scaler.transform(l)
l_stan = scaler_f.fit_transform(l)
print(l_stan)


# In[186]:


#YOUR TURN (10 minutes)
#Make a linear regression with the three features (l1, l2 and l3) and the label (l4)
#with standardized and non-standardized features
# what is the prediction of both model for fatures: [30, 1600000, -99.5]
l4 = np.array([-182, -254.3,  -71  , -172, -261 , -262, -237, -231, -85, -204])
l4 = l4.reshape(-1,1)
scaler_l = skprepro.StandardScaler()
l4_stan = scaler_l.fit_transform(l4)
print(l4_stan)


# In[187]:


model = skmod.LinearRegression().fit(l_stan, l4_stan)
x_predict =  [30, 1600000, -99.5]


# In[193]:


# x_predict =  np.array([30, 1600000, -99.5]).reshape(-1,1)
x_predict_stan = scaler_f.transform(np.array([[30, 1600000, -99.5]]))
print(x_predict_stan)
y_predict_stan = model.predict(x_predict_stan)
print(scaler_l.inverse_transform(y_predict_stan))


# In[ ]:




