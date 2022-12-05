part1 = []
part2 = []
part3 = []
part4 = []
counter = 0
with open("E:\Téléchargement\Advent code\DayFour\input.txt", "r") as file:
    for line in file.readlines():
        line = line.replace("\n", "")
        line = line.split(",")
        
        for sect1 in line[0]:
            if sect1 == "-":
                part2 = part1
                part1 = []
            else:
                part1.append(sect1)
        
        for sect2 in line[1]:
            if sect2 == "-":
                part4 = part3
                part3 = []
            else:
                part3.append(sect2)
        n1 = 0
        str1 = ""           
        for l in part2:
            str1 += l
            n1 = int(str1) 
        n2 = 0
        str2 = ""
        for l in part1:
            str2 += l
            n2 = int(str2)
        n3 = 0
        str3 = ""
        for l in part4:
            str3 += l
            n3 = int(str3)
        n4 = 0
        str4 = "" 
        for l in part3:
            str4 += l
            n4 = int(str4)       
        
        if n2 >= n3 and n1 <= n4 :
            counter +=1
        
        part1 = []
        part2 = []
        part3 = []
        part4 = []
 
print(counter) #905