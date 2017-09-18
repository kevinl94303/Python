'''
Name; Kevin Li
UNI: krl2134
a variation of majority_vote that returns the species based on a weighted
voting system

'''
from euclidean_distance import euclidean_distance
def weighted_majority_vote(test_point, neighbors):
    #returns the label that has the most weighted votes in neighbors
    votes = {}
    relative = euclidean_distance(test_point,neighbors[0])
    #all weights are relative to the distance of the closest neighbor
    
    for data in neighbors:
        label = data[len(data)-1]
        weight = relative / (euclidean_distance(test_point,data) + 1)
            #each vote is weighted according to the inverse 
            #of its euclidean_distance from the test point + 1
            #avoids dividing by zero by making weight relative to closest
            #distance
        
        if label not in votes.keys():
            votes[label] = weight
        else:
            votes[label] += weight
            
    weighted_majority_label = \
    sorted(votes.items(),key=lambda t:t[1])[len(votes)-1][0]

    return weighted_majority_label
