# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 19:21:25 2021

@author: One
"""

import pandas as pd
import datetime
import matplotlib.pyplot as plt

#from openpyxl import load_workbook
colony_dict = {"005":"Montipora capitata",
               "057":"Montipora capitata",
               "089": "Porites compressa",
                "012":"Porites lobata",
                "032":"Montipora capitata",
                "023":"Montipora capitata",
                
                #Not sure about this ID, its been overrided for now
                #"069":"Porites compressa",
                "069":"Montipora capitata",
                "011":"Porites compressa",
                "063":"Porites lobata",
                "030":"Porites lobata",
                "061":"Pocillopora meandrina",
                }

workbook = pd.read_excel("C:/Users/ligna/Documents/coralproject/Coral_Project.xls")

plates = workbook.iloc[:40,0].tolist()
frag_date = workbook.iloc[:40,1].tolist()
in_frag = workbook.iloc[:40,2].tolist()
pieces = workbook.iloc[:40,3].tolist()

location = workbook.iloc[:40,6].tolist()
origin =  workbook.iloc[:40,7].tolist()
colony=  workbook.iloc[:40,8].tolist()

first = workbook.iloc[:40,4].tolist()
first[0] = datetime.datetime(2021, 6, 15, 0, 0)
second = workbook.iloc[:40,13].tolist()
third= workbook.iloc[:40,14].tolist()
fourth= workbook.iloc[:40,15].tolist()
fifth= workbook.iloc[:40,16].tolist()
sixth= workbook.iloc[:40,17].tolist()

lists = zip(plates,frag_date,in_frag,pieces,location,origin,first,second,third,fourth,fifth,sixth, colony)
lists = list(lists)

title = lists[0]
data = lists[1:]

df = pd.DataFrame(data,columns = title)


df = df[df["Plate #"] != "???"]

days_lapse = {}
for i,x in enumerate(plates):
    if i == 0:
        continue
    days_lapse[x] = ((first[0]-frag_date[i]).days,(second[0]-frag_date[i]).days,(third[0]-frag_date[i]).days,(fourth[0]-frag_date[i]).days, (fifth[0]-frag_date[i]).days, (sixth[0]-frag_date[i]).days)

#all plates
for i,plate in enumerate(plates):
    if i ==0 or plate == "???" :
        continue
    x = list(days_lapse[plate])
    y = [first[i],second[i],third[i],fourth[i],fifth[i],sixth[i]]
    plt.plot(x, y, label = plate)
plt.show()

#outdoor plates
plt.title("Outdoor plates")
for i,plate in enumerate(plates):
    if i ==0 or plate == "???" or location[i] == "Indoor":
        continue
    x = list(days_lapse[plate])
    y = [first[i],second[i],third[i],fourth[i],fifth[i],sixth[i]]
    plt.plot(x, y, label = plate)
plt.show()

#indoor plates
plt.title("Indoor plates")
for i,plate in enumerate(plates):
    if i ==0 or plate == "???" or location[i] == "Outdoor":
        continue
    x = list(days_lapse[plate])
    y = [first[i],second[i],third[i],fourth[i],fifth[i],sixth[i]]
    plt.plot(x, y, label = plate)
plt.show()

#outdoor plates % growth
plt.title("Outdoor plates % growth")
for i,plate in enumerate(plates):
    if i ==0 or plate == "???" or location[i] == "Indoor":
        continue
    x = list(days_lapse[plate])
    y = [(first[i]-first[i])/first[i],(second[i]-first[i])/first[i],(third[i]-first[i])/first[i],(fourth[i]-first[i])/first[i],(fifth[i]-first[i])/first[i],(sixth[i]-first[i])/first[i]]
    plt.plot(x, y, label = plate)
plt.show()

#indoor plates % growth
plt.title("Indoor plates % growth")
for i,plate in enumerate(plates):
    if i ==0 or plate == "???" or location[i] == "Outdoor":
        continue
    x = list(days_lapse[plate])
    y = [(first[i]-first[i])/first[i],(second[i]-first[i])/first[i],(third[i]-first[i])/first[i],(fourth[i]-first[i])/first[i],(fifth[i]-first[i])/first[i],(sixth[i]-first[i])/first[i]]
    plt.plot(x, y, label = plate)
plt.show()

#average outdoor plates % growth
plt.title("Avg Outdoor plates % growth")
plate_count = 0

y = [0]*6
for i,plate in enumerate(plates):
    if i ==0 or plate == "???" or location[i] == "Indoor":
        continue
    y_i = [(first[i]-first[i])/first[i],(second[i]-first[i])/first[i],(third[i]-first[i])/first[i],(fourth[i]-first[i])/first[i],(fifth[i]-first[i])/first[i],(sixth[i]-first[i])/first[i]]
    plate_count += 1
    y = [x + y for x, y in zip(y, y_i)]
y = [x/plate_count for x in y]
x = [7, 14, 21, 28, 42, 49]
plt.plot(x, y, label = plate)
plt.show()

#average indoor plates % growth
plt.title("Avg Indoor plates % growth")
y = [0]*6
plate_count = 0
for i,plate in enumerate(plates):
    if i ==0 or plate == "???" or location[i] == "Outdoor":
        continue
    y_i = [(first[i]-first[i])/first[i],(second[i]-first[i])/first[i],(third[i]-first[i])/first[i],(fourth[i]-first[i])/first[i],(fifth[i]-first[i])/first[i],(sixth[i]-first[i])/first[i]]
    plate_count += 1
    y = [x + y for x, y in zip(y, y_i)]
y = [x/plate_count for x in y]
x = [7, 14, 21, 28, 42, 49]
plt.plot(x, y, label = plate)
plt.show()



genus = {"Porites":[0,[0]*6], "Pocillopora":[0,[0]*6], "Montipora":[0,[0]*6]}
#outdoor plates
plt.title("Outdoor plates")
for i,plate in enumerate(plates):
    if i ==0 or plate == "???" or location[i] == "Indoor":
        continue
    x = list(days_lapse[plate])
    genus[colony_dict[df[df["Plate #"] == plate]["Colony"].values[0]].split()[0]][0] += 1
    genus[colony_dict[df[df["Plate #"] == plate]["Colony"].values[0]].split()[0]][1] = [(first[i]-first[i])/first[i],(second[i]-first[i])/first[i],(third[i]-first[i])/first[i],(fourth[i]-first[i])/first[i],(fifth[i]-first[i])/first[i],(sixth[i]-first[i])/first[i]]
for g in genus:
    y = [x/genus[g][0] for x in genus[g][1]]
    x = [7, 14, 21, 28, 42, 49]
    plt.plot(x, y, label = g)
plt.legend()
plt.show()


genus = {"Porites":[0,[0]*6], "Pocillopora":[0,[0]*6], "Montipora":[0,[0]*6]}
#outdoor plates
plt.title("Indoor plates")
for i,plate in enumerate(plates):
    if i ==0 or plate == "???" or location[i] == "Outdoor":
        continue
    x = list(days_lapse[plate])
    genus[colony_dict[df[df["Plate #"] == plate]["Colony"].values[0]].split()[0]][0] += 1
    genus[colony_dict[df[df["Plate #"] == plate]["Colony"].values[0]].split()[0]][1] = [(first[i]-first[i])/first[i],(second[i]-first[i])/first[i],(third[i]-first[i])/first[i],(fourth[i]-first[i])/first[i],(fifth[i]-first[i])/first[i],(sixth[i]-first[i])/first[i]]
for g in genus:
    y = [x/genus[g][0] for x in genus[g][1]]
    x = [7, 14, 21, 28, 42, 49]
    plt.plot(x, y, label = g)
plt.legend()
plt.show()

genus = {"Porites":[0,[0]*6], "Pocillopora":[0,[0]*6], "Montipora":[0,[0]*6]}
#outdoor plates
plt.title("All plates")
for i,plate in enumerate(plates):
    if i ==0 or plate == "???":
        continue
    x = list(days_lapse[plate])
    genus[colony_dict[df[df["Plate #"] == plate]["Colony"].values[0]].split()[0]][0] += 1
    genus[colony_dict[df[df["Plate #"] == plate]["Colony"].values[0]].split()[0]][1] = [(first[i]-first[i])/first[i],(second[i]-first[i])/first[i],(third[i]-first[i])/first[i],(fourth[i]-first[i])/first[i],(fifth[i]-first[i])/first[i],(sixth[i]-first[i])/first[i]]
for g in genus:
    y = [x/genus[g][0] for x in genus[g][1]]
    x = [7, 14, 21, 28, 42, 49]
    plt.plot(x, y, label = g)
plt.legend()
plt.show()

###########
# #Overlay growth
# colors = {"Porites": "orange", "Pocillopora": "green", "Montipora":"blue"}
# genus = {"Porites":[0,[0]*6], "Pocillopora":[0,[0]*6], "Montipora":[0,[0]*6]}
# #outdoor plates
# plt.title("Average Coral Growth by Genus and Light")
# drop = False
# for i,plate in enumerate(plates):
#     if i ==0 or plate == "???" or location[i] == "Indoor":
#         continue
#     x = list(days_lapse[plate])
#     genus[colony_dict[df[df["Plate #"] == plate]["Colony"].values[0]].split()[0]][0] += 1
#     genus[colony_dict[df[df["Plate #"] == plate]["Colony"].values[0]].split()[0]][1] = [(first[i]-first[i])/first[i],(second[i]-first[i])/first[i],(third[i]-first[i])/first[i],(fourth[i]-first[i])/first[i],(fifth[i]-first[i])/first[i],(sixth[i]-first[i])/first[i]]
# if drop == True:
#     for g in genus:
#         if g == "Pocillopora":
#             y = [x/genus[g][0] for x in genus[g][1]]
#             del y[3]
#             x = [7, 14, 21, 42, 49]
#         else:
#             y = [x/genus[g][0] for x in genus[g][1]]
#             x = [7, 14, 21, 28, 42, 49]
#         plt.plot(x, y, color = colors[g],linestyle='dashed',label = g + " Outdoor")
# else:
#     for g in genus:
#         y = [(x/genus[g][0])*100 for x in genus[g][1]]
#         x = [7, 14, 21, 28, 42, 49]
#         plt.plot(x, y, color = colors[g],linestyle='dashed',label = g + " Outdoor")

# genus = {"Porites":[0,[0]*6], "Pocillopora":[0,[0]*6], "Montipora":[0,[0]*6]}
# #outdoor plates
# for i,plate in enumerate(plates):
#     if i ==0 or plate == "???" or location[i] == "Outdoor":
#         continue
#     x = list(days_lapse[plate])
#     genus[colony_dict[df[df["Plate #"] == plate]["Colony"].values[0]].split()[0]][0] += 1
#     genus[colony_dict[df[df["Plate #"] == plate]["Colony"].values[0]].split()[0]][1] = [(first[i]-first[i])/first[i],(second[i]-first[i])/first[i],(third[i]-first[i])/first[i],(fourth[i]-first[i])/first[i],(fifth[i]-first[i])/first[i],(sixth[i]-first[i])/first[i]]
# for g in genus:
#     y = [(x/genus[g][0])*100 for x in genus[g][1]]
#     x = [7, 14, 21, 28, 42, 49]
#     plt.plot(x, y,color = colors[g], label = g + " Indoor")
# plt.legend()
# plt.show()



##################

#average outdoor plates % growth
plt.title("Average Frag Plate Growth by Light")
plate_count = 0

y = [0]*6
for i,plate in enumerate(plates):
    if i ==0 or plate == "???" or location[i] == "Indoor":
        continue
    y_i = [(first[i]-first[i])/first[i],(second[i]-first[i])/first[i],(third[i]-first[i])/first[i],(fourth[i]-first[i])/first[i],(fifth[i]-first[i])/first[i],(sixth[i]-first[i])/first[i]]
    plate_count += 1
    y = [x + y for x, y in zip(y, y_i)]
y = [(x/plate_count)*100 for x in y]
x = [7, 14, 21, 28, 42, 49]
plt.plot(x, y,color = "green", linestyle = "dashed", label = "Outdoor")

#average indoor plates % growth
y = [0]*6
plate_count = 0
for i,plate in enumerate(plates):
    if i ==0 or plate == "???" or location[i] == "Outdoor":
        continue
    y_i = [(first[i]-first[i])/first[i],(second[i]-first[i])/first[i],(third[i]-first[i])/first[i],(fourth[i]-first[i])/first[i],(fifth[i]-first[i])/first[i],(sixth[i]-first[i])/first[i]]
    plate_count += 1
    y = [x + y for x, y in zip(y, y_i)]
y = [(x/plate_count)*100 for x in y]
x = [7, 14, 21, 28, 42, 49]
plt.plot(x, y, color = "orange", label = "Indoor")
plt.legend()
plt.xlabel("Days")
plt.ylabel("Percentage Growth")
plt.show()
##############



import numpy as np

colors = {"Porites": "orange", "Pocillopora": "green", "Montipora":"blue"}
genus = {"Porites":[0,np.array([0]*6)], "Pocillopora":[0,np.array([0]*6)], "Montipora":[0,np.array([0]*6)]}
#outdoor plates
plt.title("Average Coral Growth by Genus")
#The Porites values currently make no sense compared to average coral growth by genus and light
#outdoor plates
for i,plate in enumerate(plates):
    if i ==0 or plate == "???":
        continue
    genus[colony_dict[df[df["Plate #"] == plate]["Colony"].values[0]].split()[0]][0] += 1
    genus[colony_dict[df[df["Plate #"] == plate]["Colony"].values[0]].split()[0]][1] =  np.add(genus[colony_dict[df[df["Plate #"] == plate]["Colony"].values[0]].split()[0]][1],[(first[i]-first[i])/first[i],(second[i]-first[i])/first[i],(third[i]-first[i])/first[i],(fourth[i]-first[i])/first[i],(fifth[i]-first[i])/first[i],(sixth[i]-first[i])/first[i]])
    print(colony_dict[df[df["Plate #"] == plate]["Colony"].values[0]].split()[0],genus[colony_dict[df[df["Plate #"] == plate]["Colony"].values[0]].split()[0]][1])
for g in genus:
    y = [(x/genus[g][0])*100 for x in genus[g][1]]
    x = [7, 14, 21, 28, 42, 49]
    plt.plot(x, y,color = colors[g], label = g )
plt.legend()
plt.xlabel("Days")
plt.ylabel("Percentage Growth")
plt.show()
#####################

#Overlay growth
colors = {"Porites": "orange", "Pocillopora": "green", "Montipora":"blue"}
genus = {"Porites":[0,np.array([0]*6)], "Pocillopora":[0,np.array([0]*6)], "Montipora":[0,np.array([0]*6)]}
#outdoor plates
plt.title("Average Coral Growth by Genus and Light")
drop = False
for i,plate in enumerate(plates):
    if i ==0 or plate == "???" or location[i] == "Indoor":
        continue
    x = list(days_lapse[plate])
    genus[colony_dict[df[df["Plate #"] == plate]["Colony"].values[0]].split()[0]][0] += 1
    genus[colony_dict[df[df["Plate #"] == plate]["Colony"].values[0]].split()[0]][1] = np.add(genus[colony_dict[df[df["Plate #"] == plate]["Colony"].values[0]].split()[0]][1],[(first[i]-first[i])/first[i],(second[i]-first[i])/first[i],(third[i]-first[i])/first[i],(fourth[i]-first[i])/first[i],(fifth[i]-first[i])/first[i],(sixth[i]-first[i])/first[i]])
if drop == True:
    for g in genus:
        if g == "Pocillopora":
            y = [x/genus[g][0] for x in genus[g][1]]
            del y[3]
            x = [7, 14, 21, 42, 49]
        else:
            y = [x/genus[g][0] for x in genus[g][1]]
            x = [7, 14, 21, 28, 42, 49]
        plt.plot(x, y, color = colors[g],linestyle='dashed',label = g + " Outdoor")
else:
    for g in genus:
        y = [(x/genus[g][0])*100 for x in genus[g][1]]
        x = [7, 14, 21, 28, 42, 49]
        plt.plot(x, y, color = colors[g],linestyle='dashed',label = g + " Outdoor")

genus = {"Porites":[0,np.array([0]*6)], "Pocillopora":[0,np.array([0]*6)], "Montipora":[0,np.array([0]*6)]}
#outdoor plates
for i,plate in enumerate(plates):
    if i ==0 or plate == "???" or location[i] == "Outdoor":
        continue
    x = list(days_lapse[plate])
    genus[colony_dict[df[df["Plate #"] == plate]["Colony"].values[0]].split()[0]][0] += 1
    genus[colony_dict[df[df["Plate #"] == plate]["Colony"].values[0]].split()[0]][1] = np.add(genus[colony_dict[df[df["Plate #"] == plate]["Colony"].values[0]].split()[0]][1],[(first[i]-first[i])/first[i],(second[i]-first[i])/first[i],(third[i]-first[i])/first[i],(fourth[i]-first[i])/first[i],(fifth[i]-first[i])/first[i],(sixth[i]-first[i])/first[i]])
for g in genus:
    y = [(x/genus[g][0])*100 for x in genus[g][1]]
    x = [7, 14, 21, 28, 42, 49]
    plt.plot(x, y,color = colors[g], label = g + " Indoor")
plt.legend()
plt.xlabel("Days")
plt.ylabel("Percentage Growth")
plt.show()


lists = zip(plates,first,second,third,fourth,fifth,sixth)
lists = list(lists)
title = lists[0]
data = lists[1:]