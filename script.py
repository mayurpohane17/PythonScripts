#Author:Mayur17
#Date: Who cares
#Functionality: Generates table in CSV
import re
import os
import csv
with open('Config1.csv', 'w', newline='') as file:
    fieldnames = ['Accuracy', 'MPKI','IPC']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writerow({'Accuracy':"Accuracy",'MPKI':"MPKI",'IPC':"IPC"})
    for fil in os.listdir('Config111/'):
        with open ('Config111/' + fil) as f:
            fin=f.read()
            writer.writerow({'Accuracy':re.search('Accuracy: (.*?)%' , fin).group(1),'MPKI':re.search('MPKI: (.*?) ' , fin).group(1),'IPC':re.search('IPC: (.*?) i' , fin).group(1)})
