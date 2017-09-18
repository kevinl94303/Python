'''
Name: Kevin Li
UNI: krl2134
Date: 4 November 2016
summation returns sum of k^3 with k from 1 to n
'''

def summation(n):
    #recursive function adding n^3 for each n from n to 1
    if n == 0:
        return 0
    else:
        return n**3 + summation(n-1)
