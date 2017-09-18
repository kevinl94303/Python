"""
Name: Kevin Li
UNI: krl2134
Date: 3 Nov 2016

This program takes a list and returns a histogram of the list
"""

def make_histogram(a):
    '''returns histogram for list a as a string'''
    
    histolist = ["","","","","","","","","","",""]
    histogram = "\n"
    
    for i in a:
        histolist[int(round(i))//10]+= "*" #rounds to handle floats
    
    for i in range(0,len(histolist)):
        if i < 10: #leaves equal white space after colons to left-align stars
            histogram += "{}0-{}9:{:1s}{}".format(i,i,"",histolist[i])
        else:
            histogram += "{}0:{:3s}{}".format(i,"",histolist[i])
        
        histogram = histogram.rstrip() #removes whitespace from empty bins
        histogram += "\n"
    
    return histogram

if __name__ == '__main__':

    input_list = [73, 65, 92, 74, 100, 70]
    expected_result=\
"""
00-09:
10-19:
20-29:
30-39:
40-49:
50-59:
60-69: *
70-79: ***
80-89:
90-99: *
100:   *
"""
    print("Input:", input_list)
    print("Your result:\n", make_histogram(input_list))
    print("Expected result:\n", expected_result)
