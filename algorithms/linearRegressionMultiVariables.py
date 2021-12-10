import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('house_data.csv')

dataset.insert(0,'ones',1)

x = dataset.iloc[:,[0,12,5,18,6,10]]
y = dataset.iloc[:,3]

minValue = x.iloc[:,[1,2,3,4,5]].min()
maxValue = x.iloc[:,[1,2,3,4,5]].max()

x.iloc[:,[1,2,3,4,5]] = (x.iloc[:,[1,2,3,4,5]] - minValue)/(maxValue - minValue)

dataSize =  (int)(0.8 * len(x))
trainDataX = x[:dataSize]
testDataX = x[dataSize:]
trainDataY = y[:dataSize]
testDataY = y[dataSize:]

arrX = np.array(trainDataX)
arrY = np.array(trainDataY).flatten()
theta = np.array([-50000,50000,50000,50000,50000,50000])

m = len(arrY)

def cost_function(x,y,theta,m):
    j = np.sum((x.dot(theta) - y) **2)/(2*m)
    return j

iterations = 10000
alpha = 0.8

def gradient_descent(x,y,theta,alpha,iterations,m):
    history = [0] * iterations
    for iter in range(iterations):
        hyp = x.dot(theta)
        loss = hyp - y
        gradient = x.T.dot(loss)/m
        theta = theta - (alpha * gradient)
        cost = cost_function(x,y,theta,m)
        #print(cost)
        history[iter] = cost
    return theta,history

(t,h) = gradient_descent(arrX,arrY,theta,alpha,iterations,m)

print(cost_function(testDataX,testDataY,t,len(testDataX)))
print(cost_function(x,y,t,len(x)))

#24687131259.3546
#24687125769.73265
plt.title('Cost Function J')
plt.xlabel('No. of iterations')
plt.ylabel('Cost')
plt.plot(h)
plt.show()
