from random import randint
# Default list:
bootcamp = ["Aaron", "Bhavneesh", "Carlos", "Dovydas", "Emilia", "Filippo", "Habon", "Jeffrey", "Joe", "Kalliszta", "Liam", "Louisa", "Martyn", "Lateef", "Omkar", "Paige", "Paula", "Simon"]

start = input("please input all the names you will use, followed by the amount of people per group (only add number for default bootcamp list): ")

# Determining if default should be used, then extracting the needed info
if  len(start.split()) == 1:
    list = bootcamp 
    people = int(start) 
else:
    list = start.split() 
    people = list.pop(len(list) - 1) 

#error code to prevent groups with more members than people in list
if int(people) > len(list): 
    print("Too many people") and quit()

#setting variables for later use
y = len(list) 
z = 0
groups = {} 
#Iteration for making each group
while y//int(people)>z: 
    x = int(people) 
    group = [] 
    
    #Iteration for adding members to group
    while x > 0: 
        choice = randint(0,len(list)-1)
        result = list.pop(choice)
        group.append(result)
        x -= 1
    groups[f"group{z + 1}"] = group
    z += 1

#Adding lefftover people to bonus sad group
if y**int(people)> 1:
    group = []
    for members in list:
        group.append(members)
        groups[f"group{z + 1}"] = group
#it is done
print(groups)