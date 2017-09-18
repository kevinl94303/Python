'''
Name: Kevin Li
UNI: krl2134
Date: 4 Nov 2016

compress_string takes a string and converts it to a compressed form with
repeating letters compacted. decompress_string reverses this, expanding
a compressed string. to_compressed and to_decompressed are helper methods.
'''
def to_compressed(s,i):
    '''returns the compressed form of a single sequence of the same letter
    starting at index i'''
    
    k = i
    while(k != len(s) and s[k] == s[i]):
        k += 1
    return str(k-i) + s[i]
    

def to_decompressed(s,nindex,cindex):
    '''returns the decompressed form of a combination of a number at index
    nindex and letter at index cindex'''
    
    decompressed = ""
    
    for k in range(0,int(s[nindex:cindex])): #handles multi-digit numbers
       decompressed += s[cindex]
    
    return decompressed
    
    
def compress_string(s):
    '''returns compressed string for string s'''
    
    compressed_string = ""
    
    cindices = [] #indices for all instances of a new letter
    target = None
    for i in range (0, len(s)):
        if s[i] != target: 
            cindices.append(i) #adds index to cindices if different from prev
            target = s[i]
    
    for index in cindices:
        compressed_string += to_compressed(s,index)
    
    return compressed_string
    

def decompress_string(s):
    '''returns decompressed string for string s'''
    
    decompressed_string = ""
    cindices = [] #indices of letters in s
    nindices = [0] #indices of numbers in s, hard coded first index
    for i in range(0,len(s)):
        if s[i].islower():
            cindices.append(i)
            if i < len(s):
                nindices.append(i+1) #1st index of number always after letter
            
    for i in range(0,len(cindices)):
        decompressed_string += to_decompressed(s,nindices[i],cindices[i])
    
    return decompressed_string


if __name__ == '__main__':

    input_s = "aaabccaaadaccbbb"
    compressed_s = "3a1b2c3a1d1a2c3b"
    print("Input:", input_s)
    print("Your compressed string result:", compress_string(input_s))
    print("Expected compressed string:", compressed_s)

    print("Input:",compressed_s)
    print("Your decompressed string result:",
    	   decompress_string(compressed_s))
    print("Expected decompressed string:", input_s)
