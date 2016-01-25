#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
=========================================================
Linear Regression Example
=========================================================
This example uses the only the first feature of the `diabetes` dataset, in
order to illustrate a two-dimensional plot of this regression technique. The
straight line can be seen in the plot, showing how linear regression attempts
to draw a straight line that will best minimize the residual sum of squares
between the observed responses in the dataset, and the responses predicted by
the linear approximation.

The coefficients, the residual sum of squares and the variance score are also
calculated.

"""
print(__doc__)


# Code source: Jaques Grobler
# License: BSD 3 clause


import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import json
import sys

json_file=sys.argv[1]
json_data=open(json_file)
data = json.load(json_data)
print 'Processing ' + str(len(data)) + ' samples'
json_data.close()

x_axis_data = []
y_axis_data = []
for entry in data:
	#if entry['fr'][3:] != '' and int(entry['fr'][3:]) >= 2008:
	x_axis_data.append([int(float(entry['ma'])*1000)])
		#x_axis_data.append(float(entry['fr'][3:]) + float(entry['fr'][:2]) / 12.0)
	y_axis_data.append(entry['price_raw'])


x_axis_data = np.array(x_axis_data)
y_axis_data = np.array(y_axis_data)

#x_axis_data.reshape(1, -1)

print x_axis_data

print y_axis_data
# Load the diabetes dataset
#diabetes = datasets.load_diabetes()

# Use only one feature
#diabetes_X = diabetes.data[:, np.newaxis, 2]

#print diabetes_X

# Split the data into training/testing sets
#diabetes_X_train = diabetes_X[:-20]
#diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
#diabetes_y_train = diabetes.target[:-20]
#diabetes_y_test = diabetes.target[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(x_axis_data, y_axis_data)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean square error
print("Residual sum of squares: %.2f"
      % np.mean((regr.predict(x_axis_data) - y_axis_data) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(x_axis_data, y_axis_data))

# Plot outputs
plt.scatter(x_axis_data, y_axis_data,  color='black')
plt.plot(x_axis_data, regr.predict(x_axis_data), color='blue',
         linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
