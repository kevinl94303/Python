'''
Name; Kevin Li
UNI: krl2134
create_data returns a numpy array consisting of the data in input_data_file
'''

import numpy

def create_data(input_data_file):
    #returns numpy array of input_data_file
    data_raw = []
    data = []
    
    with open(input_data_file + ".data","r") as datafile:
    
        for line in datafile:
            if line != "\n":
                line = line.rstrip("\n")
                spt_data = line.split(",")
                data_raw.append(spt_data)
    
    data = numpy.array(data_raw)
    return data
