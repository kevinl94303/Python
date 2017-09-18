'''
Name: Kevin Li
UNI: krl2134
Date: 4 November 2016

is_SNP compares two strings and returns true if s1 is a mutation, insertion, 
or deletion of s2. is_deletion, is_insertion, and is_mutation are helper
methods. 
'''

def is_deletion(i,s1,s2):
    '''returns true if s1 is a deletion of s2'''    
    
    s2new1 = s2[:i] + s2[(i+1):]
    s2new2 = s2[:i+1] + s2[(i+2):] #remove s2 char before and after difference
    return s2new1 == s1 or s2new2 == s1 #compares strings after deletion
    
    
def is_insertion(i,s1,s2):
    '''returns true if s1 is an insertion of s2'''     
    
    s1new1 = s1[:i] + s1[(i+1):] 
    s1new2 = s1[:i+1] + s1[(i+2):] #remove s1 char before and after difference
    return s1new1 == s2 or s1new2 == s2 #compares strings after deletion
    

def is_mutation(i,s1,s2):
    '''returns true if s1 is a mutation of s2''' 
    
    s1new = s1[:i] + s1[(i+1):]
    s2new = s2[:i] + s2[(i+1):] #remove conflicting char from both strings
    return s1new == s2new #compare after removal
    
    
def is_SNP(s1,s2):
    '''returns true if s1 is a deletion, insertion, or mutation of s2'''
    
    result = False
    
    if len(s1) == len(s2):
        for i in range (0, len(s1)):
            if s1[i] != s2[i]:
                return is_mutation(i,s1,s2)
                
    elif len(s1) < len(s2):
        for i in range (0, len(s2)):
            try:
                if s1[i] != s2[i]:
                    return is_deletion(i,s1,s2)
            except IndexError: #if conflict is in last char, test last char
                return is_deletion(i,s1,s2)
                
    elif len(s1) > len(s2):
        for i in range (0, len(s1)):
            try:
                if s1[i] != s2[i]:
                    return is_insertion(i,s1,s2)
            except IndexError: #if conflict is in last char, test last char
                return is_insertion(i,s1,s2)


    return result



if __name__ == '__main__':

    DNA1 = "AGATCTA"
    DNA2 = "AGATCGA"
    print("Input:", DNA1, "and", DNA2)
    print("Your result:", is_SNP(DNA1,DNA2))
    print("Expected result:", True)

    DNA1 = "AGATCTA"
    DNA2 = "CCCCCCC"
    print("Input:", DNA1, "and", DNA2)
    print("Your result:", is_SNP(DNA1,DNA2))
    print("Expected result:", False)

    DNA1 = "A"
    DNA2 = "AC"
    print("Input:", DNA1, "and", DNA2)
    print("Your result:", is_SNP(DNA1,DNA2))
    print("Expected result:", True)

    DNA1 = "ACA"
    DNA2 = "CA"
    print("Input:", DNA1, "and", DNA2)
    print("Your result:", is_SNP(DNA1,DNA2))
    print("Expected result:", True)


