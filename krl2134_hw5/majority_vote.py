'''
Name; Kevin Li
UNI: krl2134
majority_vote returns the most common label of the k nearest neighbors of
a test point

'''
def majority_vote(neighbors):
    #returns the label that has the most frequency in neighbors
    votes = {}
    for data in neighbors:
        if data[len(data)-1] not in votes.keys():
            votes[data[len(data)-1]] = 1
        else:
            votes[data[len(data)-1]] += 1
    majority_label = sorted(votes.items(),key=lambda t:t[1])[len(votes)-1][0]
    #tie will arbitrarily return the lower valued label
    
    return majority_label
