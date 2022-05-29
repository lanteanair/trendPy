import numpy as np

def linReg(x,y):
    a = (np.inner(x,y) - (len(x) * np.mean(x) * np.mean(y))) / (np.inner(x,x) - (len(x) * ((np.mean(x))**2)))
    b = np.mean(y) - a * np.mean(x)
    return [a,b]


def r2(y, y_pred):
        wert = 1-np.sum((y-y_pred)**2)/np.sum((y-np.mean(y))**2)
        return wert


def linreg(x,y):
    check(x,y)
    #initialising calculating variables
    partA = partB = partC = partD = partE = slope = yIntercept = 0.0
    #calculating linear regression
    for i in range(len(x)):
        #splitting and calculating the parts of the formula (linear regression)
        partA += x[i] * y[i]
        partB += x[i]
        partC += y[i]
        partD += (x[i])**2
        partE += x[i]
    #merging the parts into the final constants
    slope = ((len(x) * partA) - (partB * partC)) / ((len(x) * partD) - (partE ** 2))
    yIntercept = (1/len(x)) * (partC - slope * partB)
    #returning results
    return slope,yIntercept


def check(x,y):
    # checking input variables (exceptions)
    if type(x) != list:
        raise TypeError(f"First Argument has the wrong type: {type(x)}. Please provide a list.")
    if type(y) != list:
        raise TypeError(f"Second Argument has the wrong type: {type(y)}. Please provide a list.")
    if len(x) < 2 or len(y) < 2:
        raise ValueError(f"You provided not enough data. Please provide more data in order to use the function.")
    if len(x) != len(y):
        raise TypeError(f"The lists don't have the same length. In order to use this function the lists have to be the same length.")