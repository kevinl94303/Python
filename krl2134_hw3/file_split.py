'''
Name: Kevin Li
UNI: krl2134
Date: 4 November 2016

file_split takes a file name as an argument and splits the file into even
and odd lines
'''
def file_split(f):
    '''procedure that generates two files that contain the even and odd lines
    of file f'''
    
    file = open(f + ".txt","r")
    even_file = open(f + "_even.txt","w")
    odd_file = open(f + "_odd.txt","w")
    
    n = 0
    line = file.readline()
    while line != "": #empty string means end of file
        if n%2 == 0:
            print(line, end = "", file = even_file)
        else:
            print(line, end = "", file = odd_file)
        line = file.readline()
        n += 1
    
    file.close()
    even_file.close()
    odd_file.close()
    
    return None
    

file_split("file")