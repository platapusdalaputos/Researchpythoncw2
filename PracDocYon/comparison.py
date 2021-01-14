"""

This program will compute a variety of functions given the input.

"""

import numpy as np
import math


def algorithm_x(data1, data2, weights):
    # TODO case when data1 and data2 aren't the same
    # TODO deal with case if they give the weights in dimension n*1 instead of 1*n
    # THIS IS WHAT WE USED TO HAVE
    # AT THE BEGINNING IN CASE WE WANT TO GO BACK
    num_samples, num_features = data1.shape
    sample_difference = np.zeros(num_samples)
    """
    
    Computes the variables associated with the function algorithm_x
    
    :type data1: float
    :type data2: float
    :type weights: integer
    
    
    """

    for sample in range(0, num_samples):
        d = 0
        for feature in range(0, num_features):
            feature1 = data1[sample][feature]
            feature2 = data2[sample][feature]
            if math.isnan(feature1) or math.isnan(feature2):
                continue
            d += weights[0][feature] * (abs(feature1 - feature2))
        sample_difference[sample] = d

    return sample_difference


def algorithm_y(data1, data2, weights):
    
    
    """
    
    Computes the variables associated with the function algorithm_y
    
    :type data1: float
    :type data2: float
    :type weights: integer
    
    
    """
    

    num_samples, num_features = data1.shape

    discrepancy = np.zeros(num_samples)

    for sample in range(0, num_samples):
        s = 0
        for feature in range(0, num_features):
            feature1 = data1[sample][feature]
            feature2 = data2[sample][feature]
            if math.isnan(feature1) or math.isnan(feature2):
                continue
            s += weights[0][feature] * pow(feature1 - feature2, 2)
        d = pow(s, 0.5)
        discrepancy[sample] = d

    return discrepancy


def sum_criticality(d_index, threshold):
    
        
    """
    
    Computes the variables associated with the function sum_criticality
    
    :type d_index: float
    :type threshold: integer
    
    
    """
    num = 0
    for i in range(0, d_index.shape[0]):
        if d_index[i] > threshold:
            num += 1
    print(f'criticality: {num} result above {threshold}')


def sum_d(d_index):
    
    
    """
    
    Computes and prints the d_index.mean 
    
    :type d_index: float
    :type threshold: integer
    
    
    """
    
    print('d-index: ', d_index.mean())


def check_weight_negative(weights):
    
    """
    
    Computes the variables associated with the function sum_criticality
    

    :type weights: integer
    
    
    """
    
    for weight in range(weights.shape[1]):
        if(weights[0][weight]<0):
            raise ValueError('weight invalid, a weight is negative')


def check_weight_match_feature(weights, data1):
    num_feature = data1.shape[1]
    num_weights = weights.shape[1]

    if(num_feature!=num_weights):
        raise ValueError('the number of weights don’t match the number of features')


def open_file(filename):
    #with open(filename) as f:
    #    data = np.loadtxt(f, delimiter=",", ndmin=2)

    with open(filename) as f:
        lines = f.readlines()
        data = []
        for line in lines:
            row = []
            for n in line.split(','):
                row.append(float(n.strip()))
            data.append(row)
    data = np.array(data)
    if data.size==0:
        raise ValueError('the data file you have selected is empty')
    return data


def analyse(input_data, weights_file='', analysis='x', summary='d', threshold=0):
    # read data lists from data files

    data1 = input_data[0]
    data2 = input_data[1]

    # check weight's special cases
    if weights_file != '':
        weights = weights_file
        check_weight_negative(weights)
        check_weight_match_feature(weights, data1)
    else:
        weights = np.ones([1, data1.shape[1]])

    # calculate d-index
    if analysis == 'x':
        print("using algorithm x")
        algorithm_output = algorithm_x(data1, data2, weights)
    elif analysis == 'y':
        print("using algorithm y")
        algorithm_output = algorithm_y(data1, data2, weights)
    else:
        raise ValueError('the analysis you input is invalid. Please choose either x or y')
    print(algorithm_output)

    # get summary
    if summary == 'criticality':
        sum_criticality(algorithm_output, threshold)
    elif summary == 'd':
        sum_d(algorithm_output)
    else:
        raise ValueError('the summary you input is invalid. Please choose either criticality or d')

