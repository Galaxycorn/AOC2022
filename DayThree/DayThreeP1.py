import string
valuesL = dict()
valuesU = dict()

for index, letter in enumerate(string.ascii_lowercase):
    valuesL[letter] = index + 1
for index, letter in enumerate(string.ascii_uppercase):
    valuesU[letter] = index + 1

str1 = ""
str2 = ""
score = 0
letter = ""
with open("E:\Téléchargement\inputDayThree.txt", "r") as file: 
    for line in file.readlines():
        length = len(line)
        line = line.replace("\n", "")         
        for i in range(length//2):
            str1 += line[i]
        for j in range(length//2, length - 1):
            str2 += line[j]
            
            for i in str1:
                if i in str2:
                    if i.islower() == True:
                        score += valuesL[i]
                    else:
                        score += valuesU[i] + 26
                    str1 = ""
                    str2 = ""    
print(score) #7898


        