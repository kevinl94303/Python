'''
Name; Kevin Li
UNI: krl2134
knn returns the predicted label for each point in test_data based on
the majority_vote

'''
from majority_vote import majority_vote
from find_k_nearest_neighbors import find_k_nearest_neighbors

def knn(train_data, test_data, k):
    #returns vertical matrix listing predicted labels for all points in 
    #test_data based on its k nearest neighbors
    predicted_labels = []
    for row in test_data:
        predicted = majority_vote(find_k_nearest_neighbors(row,train_data,k))
        predicted_labels.append([predicted])

    return predicted_labels

