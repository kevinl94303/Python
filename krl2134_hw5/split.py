'''
Name; Kevin Li
UNI: krl2134
split returns two lists, one with 15 randomly selected members of each
flower species, and one with all nonselected points

'''
import numpy as np
import random
import copy

def split(integerized_data):
    #selects 15 random point from each species and returns combined list
    #train_data, and all nonselected points test_data

    train_data_raw = []
    test_data_raw = []    
    
    setosa_list = []
    versicolor_list = []
    virginica_list = []
    for line in integerized_data:
        if line[len(line)-1] == '0':
            setosa_list.append(line.tolist())
        elif line[len(line)-1] == '1':
            versicolor_list.append(line.tolist())
        elif line[len(line)-1] == '2':
            virginica_list.append(line.tolist())
    #splits data into three lists according to species
    
    testsetosa = copy.deepcopy(setosa_list)
    testversicolor = copy.deepcopy(versicolor_list)
    testvirginica = copy.deepcopy(virginica_list)
    
    random.shuffle(testsetosa)
    random.shuffle(testversicolor)
    random.shuffle(testvirginica)
    
    trainsetosa = []
    trainversicolor = []
    trainvirginica = []
    
    for i in range (0,15):
        #selects first 15 members of randomly shuffled lists
        trainsetosa.append(testsetosa.pop())
        trainversicolor.append(testversicolor.pop())
        trainvirginica.append(testvirginica.pop())
    
    test_data_raw = trainsetosa + trainversicolor + trainvirginica
    train_data_raw = testsetosa + testversicolor + testvirginica
    
    train_data = np.array(train_data_raw)
    test_data = np.array(test_data_raw)
    
    return (train_data, test_data)
