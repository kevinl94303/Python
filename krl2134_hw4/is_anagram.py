"""
Name: Kevin Li
UNI: krl2134
is_anagram takes two strings and returns whether they are anagrams

"""
import string

def is_anagram(a, b):
    #compares a and b and returns True if they are anagrams, False otherwise

    alist = list(a.lower().replace(" ",""))
    blist = list(b.lower().replace(" ",""))
    
    adict = {}
    bdict = {}
    
    for letter in string.ascii_lowercase:
        #makes a dictionary that corresponds count of each letter
        #with the letter for each string
        adict[letter] = 0
        bdict[letter] = 0
        for char in alist:
            if letter == char:
                adict[letter] += 1
        for char in blist:
            if letter == char:
                bdict[letter] += 1
                
    is_an_anagram = adict == bdict #compares dictionaries of a and b


    return is_an_anagram

if __name__ == '__main__':

    str1 = "Tom Marvolo Riddle"
    str2 = "I am Lord Voldemort"
    str3 = "I am Ansaf your Professor"

    print("Checking for anagrams:", str1, str2)
    print("Your output:", is_anagram(str1,str2))
    print("Expected output:", True)

    print("Checking for anagrams:", str1, str3)
    print("Your output:", is_anagram(str1,str3))
    print("Expected output:", False)
