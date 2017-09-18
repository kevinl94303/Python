'''
Name; Kevin Li
UNI: krl2134
integerized_labels returns a numpy array with the last column in data
converted to an integer and a dictionary showing how labels are converted
to integers

'''
import numpy as np

def integerize_labels(data):
    #returns integerized array and dictionary showing label mappings
    label_dict = {}
    integerized_data = np.copy(data)
    n = 0
    for line in integerized_data:
        if line[len(line) - 1] not in label_dict.keys():
            label_dict[line[len(line) - 1]] = n
            n += 1
    for line in integerized_data:
        line[len(line) - 1] = label_dict[line[len(line) - 1]]

    return (integerized_data, label_dict)
    
