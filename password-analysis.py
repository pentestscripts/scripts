from __future__ import division
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
bigList = []

def checkDictionary(myPassword):
    myNewPassword = ''
    for character in myPassword:
        if character.lower() in lowercase:
            myNewPassword=myNewPassword+character.lower() 
    if len(myNewPassword) == 0:
        return False
    for dictWord in open('brit-a-z.txt'):
        if myNewPassword == dictWord.strip().lower():
            return True
    return False
        


for password in open("passwords.txt"):
    password = password.strip()
    numLower = 0
    numUpper = 0
    numDigit = 0
    numSymbo = 0
    for character in password:
        if character in lowercase:
            numLower = numLower + 1
        elif character in uppercase:
            numUpper = numUpper + 1
        elif character in digits:
            numDigit = numDigit + 1
        else:
            numSymbo = numSymbo+1
    # number of character sets:
    numSets = 4
    if numLower == 0:
        numSets = numSets-1
    if numUpper == 0:
        numSets = numSets-1
    if numDigit == 0:
        numSets = numSets-1
    if numSymbo == 0:
        numSets = numSets-1
    
    bigList.append([password,len(password),numLower,numUpper,numDigit,numSymbo,numSets,checkDictionary(password)])
    

print "Password\tLength\tnumLower\tnumUpper\tnumDigit\tnumSymbols\tnumCharSets\tDictionaryWord"
for smallList in bigList:
    for item in smallList:
        print str(item)+"\t",
    print

