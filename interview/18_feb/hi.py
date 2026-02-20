
# * input is palindrome or not


def Q1():
    inputA = input("GIve me a sentence or any thing to check wether it is a palindrome or not :")
    rev = ""
    for a in inputA:
        rev = a + rev 
    
    if inputA == rev :
        print("it is a plindrome ")
    else :
        print("it is not a plindrome")
        
Q1()

"""
packing 
unpacking
identifier 
closure
function composition




"""