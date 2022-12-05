import string
valuesL = dict()
valuesU = dict()

for index, letter in enumerate(string.ascii_lowercase):
    valuesL[letter] = index + 1
for index, letter in enumerate(string.ascii_uppercase):
    valuesU[letter] = index + 1

letterIndex = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
str1 = ""
str2 = ""
str3 = ""
score = 0
letter = ""
currentLine = 0
with open("E:\Téléchargement\inputDayThree.txt", "r") as file: 
    for line in file.readlines():     
        if currentLine == 3: 
            for i in letterIndex:
                if(i in str1) and (i in str2) and (i in str3):
                    print(i)
                    if i.islower() == True:
                        score += valuesL[i]
                        print(valuesL[i])
                    else:
                        score += valuesU[i] + 26
                        print(valuesU[i] + 26)
                    
                    str1 = ""
                    str2 = ""
                    str3 = ""
                currentLine = 0 
            
        length = len(line)
        line = line.replace("\n", "")
        if currentLine == 0:        
            for i in range(length-1):
                str1 += line[i]
            print(str1)
        if currentLine == 1:
            for i in range(length-1):
                str2 += line[i]
            print(str2)
        if currentLine == 2:
            for i in range(length-1):
                str3 += line[i]
            print(str3)
        if currentLine < 3: 
            currentLine += 1  
            
print(score) #2607