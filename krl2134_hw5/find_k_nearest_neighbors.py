'''
Name; Kevin Li
UNI: krl2134
find_k_nearest_neighbors finds a list of k vectors that are closest in
terms of euclidean distance to the test point

'''

from euclidean_distance import euclidean_distance

def find_k_nearest_neighbors(test_point, train_data, k):
    #returns list of k points with lowest euclidean_distance to test_point
    distlist = {}
    k_nearest_neighbors = []
    for data in train_data:
        distlist[euclidean_distance(test_point,data)] = data
    
    for i in range (0, k):
        ith_point = sorted(distlist.items())[i][1]
        k_nearest_neighbors.append(ith_point)

    return k_nearest_neighbors
