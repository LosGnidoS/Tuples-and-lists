#!/usr/bin/python3
#Tuples and lists
#DIFFERENCE BETWEEN TUPLES AND LISTS by Kirill Shvedov.


#list
names = ["Tien","Omega","Marion",
"Dionna","Elise","Amparo","Janetta",
"Leslee","Wendi","Chantell","Deanne",
"Maire","Genaro","Merlyn","Lakeisha",
"Bobbie","Carolin","Raelene","Krystal","Felicia" ]

print(id(names))
#implement sorting in the alphabetical order
names.sort()
print(names)
#print the second one element in the list
print(names[1])


#tuple(can't be changed)
me = ("Kirill", "Shvedov", 22) 
tien = ("Tien","Tien", 32) #tuple
omega = ("Omega","Omega", 41) #tuple
marion = ("Marion","Marion", 41) #tuple
dionna = ("Dionna","Dionna", 23) #tuple
elise = ("Elise","Elise", 42) #tuple
amparo = ("Amparo","Amparo", 22) #tuple
janetta = ("Janetta","Janetta", 41) #tuple
leslee = ("Leslee","Leslee", 54) #tuple
wendi = ("Wendi","Wendi", 32) #tuple
chantell = ("Chantell","Chantell", 27) #tuple

people = []
# add extra elements to the lists 
people.append(me) #(lists can be changed)
people.append(tien)
people.append(omega)
people.append(marion)
people.append(dionna)
people.append(elise)
people.append(amparo)
people.append(janetta)
people.append(leslee)
people.append(wendi)
people.append(chantell)
names.sort()

print(people)

people.sort()