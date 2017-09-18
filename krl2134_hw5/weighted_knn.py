'''
Name; Kevin Li
UNI: krl2134
weighted_knn acts like knn, but uses the weighted_majority_vote instead
of majority_vote

'''

from weighted_majority_vote import weighted_majority_vote
from find_k_nearest_neighbors import find_k_nearest_neighbors

def weighted_knn(train_data, test_data, k):
    #returns vertical matrix listing predicted labels for all points in 
    #test_data based on k nearest neighbors using weighted voting
    weighted_predicted_labels = []
    for row in test_data:
        predicted = weighted_majority_vote(row,
            find_k_nearest_neighbors(row,train_data,k))
        
        weighted_predicted_labels.append([predicted])

    return weighted_predicted_labels

