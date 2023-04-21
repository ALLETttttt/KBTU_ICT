import numpy as np

import sklearn.linear_model as skmod

#Our data: the goats and the altitude
alt = [3.25, 0.816, 4.376, 1.314, 3.982, 2.957, 2.482, 3.7]
n_goats = [21, 22, 13, 25, 17, 23, 23, 27]

#Reorder your arrays
arrx = np.array(alt).reshape(-1, 1)
print(arrx)
arry = np.array(n_goats).reshape(-1, 1)
print(arry)


#Plot your data first
import matplotlib.pyplot as plt
plt.scatter(arrx, arry)
# plt.show()



#Create a linear regression model: LinearRegression()
model = skmod.LinearRegression()

#some parameters than you can change:
#fit_intercept (consider b=0 if False, default is True)


model_trained = model.fit(arrx, arry)


#get the result: the intercept (b)(.intercept_), the coeff (w1)(.coef_) 
#and the R2 (.score(x, y))
print(model_trained.intercept_)
print(model_trained.coef_)
#Equation is: y' = -1.83*x + 26.6
print(model_trained.score(arrx, arry))



#draw your model on the graph
plt.scatter(arrx, arry)
plt.plot([0, 5], [-1.83 * 0 + 26.6, -1.83 * 5 + 26.6])
# plt.show()

#Now use your model to predict data (.predict(x))
predictarr = np.array([[0], [2.5], [5]])
print(predictarr)
print(model.predict(predictarr))


#Predict the result without predict but with intercept and coeff
print(model.coef_*2.5 + model.intercept_)


feature1 = np.array([25, 100, 30, 5, 85]).reshape(-1, 1)
label = np.array([80, 254, 152, 4, 271]).reshape(-1, 1)
model = skmod.LinearRegression().fit(feature1, label)
print(model.coef_[0])
print(model.intercept_[0])
print(model.score(feature1, label))


plt.scatter(feature1, label)
plt.plot([0, 100], model.predict(np.array([[0], [100]])))
# plt.show()

#Our datas: the students work
x1 = [9, 10, 16, 22, 17, 7, 10, 24, 15] #homework hours
x2 = [14, 18, 1, 22, 6, 12, 4, 28, 22] #nb of classes attended
y = [42.8, 48.8, 36.8, 81.1, 44.8, 32.4, 28.8, 100, 73.1] #average final score

plt.scatter(x1, x2, c = y, cmap = 'Reds')
# plt.show()


#Draw in 3D
# ax = plt.subplot(projection = '3d')
# ax.scatter(x1, x2, y)
# plt.show()

arrx1 = np.array(x1).reshape(-1, 1)
arrx2 = np.array(x2).reshape(-1, 1)
arry = np.array(y).reshape(-1, 1)
arrx1x2 = np.hstack([arrx1, arrx2])
print(arry)
print(arrx1x2)


model = skmod.LinearRegression().fit(arrx1x2, arry)
print(model.coef_)
print(model.intercept_)

#Equation is: y' = 2.213*x1 + 1.689*x2 -1.507

print(model.predict(np.array([[2, 10], 
                              [30, 10], 
                              [2, 30]])))


#YOUR TURN (15 minutes)
#Here is your data
#x1 = [7, 0, 3, 3, 5]
#x2 = [2, 0, 7, 3, 9]
#y = [44, 0, 25, 21, 39]
#Make the linear regression between these datas.
#What are the weights and the bias? Write the final equation of your model.
#What would be the prediction for x1 = 5 and x2 = 6
x1 = np.array([7, 0, 3, 3, 5]).reshape(-1, 1)
x2 = np.array([2, 0, 7, 3, 9]).reshape(-1, 1)
y = np.array([44, 0, 25, 21, 39]).reshape(-1, 1)
x2x1 = np.hstack([x1, x2])
model = skmod.LinearRegression().fit(x2x1, y)
print(model.coef_)
print(model.intercept_)
#Equation is: y' = 2.213*x1 + 1.689*x2 -1.507
print(model.predict(np.array([[5, 6]])))
# print(model.predict(np.array([[2, 10], 
#                               [30, 10], 
#                               [2, 30]])))



#Our data: the number of goats
alt = [3.25, 0.816, 4.376, 1.314, 3.982, 2.957, 2.482, 3.7]
n_goats = [21, 22, 13, 25, 17, 23, 23, 27]


all = []
for i in alt:
    all.append(i**2)

x1 = np.array(alt).reshape(-1, 1)
x2 = np.array(all).reshape(-1, 1)
y = np.array(n_goats).reshape(-1, 1)
x1x2 = np.hstack([x1, x2])
print(len(x1x2))
print(len(y))

model = skmod.LinearRegression().fit(x1x2, y)
print(model.coef_)
print(model.intercept_)

#Equation is: y' = 8.23*x1 + -1.97*x2 + 16.66
#Equation is: y' = 8.23*x1 + -1.97*x1^2 + 16.66
plt.scatter(x1, y)
xforplot = np.arange(0, 5, 0.1)
x2forplot = xforplot*xforplot
xfinal = np.hstack([xforplot.reshape(-1, 1), x2forplot.reshape(-1, 1)])

