# Name: Luke Voyer
import numpy as np

################################################################################
# Return a NEW numpy array where the distance column is converted to centimeters
def question1(A):
    inputArray = np.array(A)
    reshapedArray = inputArray.reshape(-1,3)
    splitArray = np.hsplit(reshapedArray, 3)
    colCm = splitArray[1]
    colIn = np.multiply(colCm, 100)
    
    return np.concatenate((splitArray[0], colIn, splitArray[2]), 1)


################################################################################
# Return a NEW numpy array that only contains the data for car 2
def question2(A):
    inputArray = np.array(A)
    
    return inputArray[inputArray[:,2] == 2] 


################################################################################
# Return a NEW numpy that corresponds to the row that has the maximum distance
# of all the trials involving car 1
def question3(A):
    inputArray = np.array(A)
    
    return np.amax(inputArray[inputArray[:,2] == 1], 0)


################################################################################
# Return  the number of trials with distance greater than the mean distance
# of all the trials
def question4(A):
    inputArray = np.array(A)
    mean = np.mean(inputArray[:,1])
    
    return np.size(inputArray[mean < inputArray[:,1]], 0)


################################################################################
# Return the maximum angle in radians
def question5(A):
    inputArray = np.array(A)
    
    return np.radians(np.max(inputArray[:,0]))


################################################################################
# Return a NEW numpy array where that transforms the data to a form where the
# columns correspond to cars and each row is the distance traveled for all
# the cars at the same angle in the order that the angles appear in the data
# set
def question6(A):
    inputArray = np.array(A)
    splitArray = np.hsplit(inputArray, 3)
    colDist = splitArray[1]
    colDistReshaped = colDist.reshape(-1,3)
    
    return colDistReshaped


################################################################################
# This function depends on the return value of question6. Return a NEW numpy
# array where the columns correspond to the mean, standard deviation, min, and
# max for each row of the result from question6
def question7(A):
    colMean = np.mean(A, axis = 1).reshape(-1,1)
    colStDev = np.std(A, axis = 1).reshape(-1,1)
    colMin = np.min(A, axis = 1).reshape(-1,1)
    colMax = np.max(A, axis = 1).reshape(-1,1)
    
    return np.concatenate((colMean, colStDev, colMin, colMax), axis=1)


if __name__ == '__main__':
    data = np.genfromtxt('toycars.csv', skip_header=1, delimiter=',')

    print('Question 1:')
    q1 = question1(data)
    print(q1, end='\n\n')

    print('Question 2:')
    q2 = question2(data)
    print(q2, end='\n\n')

    print('Question 3:')
    q3 = question3(data)
    print(q3, end='\n\n')

    print('Question 4:')
    q4 = question4(data)
    print(q4, end='\n\n')

    print('Question 5:')
    q5 = question5(data)
    print(q5, end='\n\n')

    print('Question 6:')
    q6 = question6(data)
    print(q6, end='\n\n')

    print('Question 7:')
    q7 = question7(q6)
    print(q7, end='\n\n')

