#hardcoded but I learnt a lot of things today specially with new functions that I didn't know like map and using dict variable. 
#I will maybe make a general program one day...
stacks = {
    1 : "G D V Z J S B".split(), #split because it's easier to use array than string
    2 : "Z S M G V P".split(),
    3 : "C L B S W T Q F".split(),
    4 : "H J G W M R V Q".split(),
    5 : "C L S N F M D".split(),
    6 : "R G C D".split(),
    7 : "H G T R J D S Q".split(),
    8 : "P F V".split(),
    9 : "D R S T J".split()
}
with open("DayFive\input.txt") as file:
    for line in file.readlines():
        line = line.replace("\n", "")
        if line.startswith("m"):
            #create 3 variables for instructions, map function is really usefull here to cast an int, adding a "," to split it for the three variables
            crate, instru_from, instru_to = map(int, line.replace("move", "").replace("from", ",").replace("to", ",").split(","))
            for i in range(crate):
                stacks[instru_to].append(stacks[instru_from].pop())
        
    print("Solution 1 : ", ''.join([stacks[i].pop() for i in stacks])) #WCZTHTMPS
    
    stacks = {
    1 : "G D V Z J S B".split(), #split because it's easier to use array than string
    2 : "Z S M G V P".split(),
    3 : "C L B S W T Q F".split(),
    4 : "H J G W M R V Q".split(),
    5 : "C L S N F M D".split(),
    6 : "R G C D".split(),
    7 : "H G T R J D S Q".split(),
    8 : "P F V".split(),
    9 : "D R S T J".split()
}  
with open("E:\Téléchargement\Advent code\DayFive\input.txt") as file:      
    for line in file.readlines():
        line = line.replace("\n", "")
        if line.startswith("m"):
            crate, instru_from, instru_to = map(int, line.replace("move", "").replace("from", ",").replace("to", ",").split(","))
            stacks[instru_to] = stacks[instru_to] + stacks[instru_from][(-1*crate):] #Start with last 
            stacks[instru_from] = stacks[instru_from][:(-1*crate)] #Start with first
            
    print("Solution 2 : ", ''.join([stacks[i].pop() for i in stacks])) #BLSGJSDTS