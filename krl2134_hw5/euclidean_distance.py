'''
Name; Kevin Li
UNI: krl2134
euclidean_distance returns the euclidean distance between two vectors

'''
from math import pow
def euclidean_distance(x1,x2):
    #returns euclidean distance between x1 and x2
    abs_dist = 0
    for i in range (0, len(x1) - 1):
        abs_dist += pow(float(x1[i]) - float(x2[i]) , 2)
    
    distance = math.sqrt(abs_dist)

    return distance
