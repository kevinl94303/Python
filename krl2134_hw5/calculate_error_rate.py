'''
Name; Kevin Li
UNI: krl2134
calculate_error_rate returns error rate of tested data

'''
def calculate_error_rate(predicted_labels, test_data):
    #returns rate of errors from predicted_labels
    errors = 0
    for i in range(len(predicted_labels)):
        if predicted_labels[i][0] != test_data[i][len(test_data[0]) - 1]:
            errors += 1
    
    error_rate = errors / len(predicted_labels)
    
    return error_rate
