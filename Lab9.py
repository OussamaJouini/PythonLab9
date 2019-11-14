# Task1: This program reads each text file then converts it into a csv format: "name",count then saves the entry in a csv file. The output csv file must include the following header as its first line: "First Name","Count"
import csv
try:
    with open(r'C:\Users\jouin\OneDrive\Documents\Code\PYTHON\Week 9 Files\PythonLab9\2000_BoysNames.txt', 'r') as inFile, open(r'C:\Users\jouin\OneDrive\Documents\Code\PYTHON\Week 9 Files\PythonLab9\boysFile.csv', 'w') as outFile:
        writer = csv.writer(outFile)
        writer.writerow(('First Name', 'Count'))
        outFile.write(inFile.read().replace(" ", ","))
    with open(r'C:\Users\jouin\OneDrive\Documents\Code\PYTHON\Week 9 Files\PythonLab9\2000_GirlsNames.txt', 'r') as inFile, open(r'C:\Users\jouin\OneDrive\Documents\Code\PYTHON\Week 9 Files\PythonLab9\girlsFile.csv', 'w') as outFile:
        writer = csv.writer(outFile)
        writer.writerow(('First Name', 'Count'))
        outFile.write(inFile.read().replace(" ", ","))
except:
    print("Please make sure the file's name is correct!! ")


#Task2: This program prompts the user for the name of .csv file then reads and displays each line of the file as a Python list. Test your program on the 2 csv files that you generated in Task 1.
import csv
import pandas as pd
import os
def dispLineList (filename):
    os.getcwd()
    file = filename
    data = pd.read_csv(file)
    dataList = list(data)
    newList = [str(x) for x in dataList]
    return (newList)

fileinput = str(input("Which file you would like to use? "))
if not ".csv" in fileinput:
    fileinput += ".csv"
pythonList = dispLineList(fileinput)

pythonBList = dispLineList('boysFile.csv')
pythonGList = dispLineList('girlsFile.csv')

#Task3: *1. This is a function generateDictionary that reads the file font3.txt and generate a dictionary where the key is the character ane the vaue is the 8*8 bit list representation of the character.
import csv
import random
from gfxhat import lcd, backlight
def treatFile():
    with open('font3.txt', newline='', encoding='utf-8-sig') as csvFile:
        csvFileReader =csv.reader(csvFile, delimiter=",", quotechar=',', quoting=csv.QUOTE_MINIMAL) 
        dataList = list (csvFileReader)
        fileList = [[str(x) for x in dataList]]
        csvFile.close()
        for f in range(0, len(fileList), 2):
            fileList[f] = fileList[f][2:]
    return fileList

#  a function that creates a dictionary
def generateDictionary(fileList):
    gendict = {}
    j = 0
    k = 1
    i = 0
    lengthList = (len(fileList)) / 2
    while i < lengthList:
        gendict[fileList[k]] = fileList[j]
        j += 2
        k += 2
        i += 1
    return gendict


# Task3: 2*.This program that reads a character from the user and displays the associate character on the gfxHat at the coordinates of your choice.
def treatCharact(Charact, Dic):
    valueList = []
    value = Dic.get(Charact)
    for i in range(0, len(value), 2):
        valueList.append(value[i:i + 2])
    return valueList


# function that converts the value to binary list
def convBinaryList(hex):
    listBinary = []
    for l in range(0, len(hex)):
        tempList = hex[l]
        valueBin = bin(int(tempList, 16))[2:].zfill(8)
        listBinary.append(list(valueBin))
    for i in range(len(listBinary)):
        for j in range(len(listBinary[i])):
            listBinary[i][j] = int(listBinary[i][j])
    return listBinary

# this function to display object function
def displayObject(obj, x, y):
    i = 0
    for line in obj:
        j = 0
        for pixel in line:
            lcd.set_pixel(x + j, y + i, pixel)
            j = j+1
        i = i+1
    lcd.show()


Char = str(input("Could you please enter a character: "))
try:
    A = treatFile()
    B = generateDictionary(A)
    C = treatCharact(Char, B)
    D = convertBinaryList(C)
    print(D)
    displayObject(D, 50, 20)
except:
    print("The Character you have entered is not in the list, please try again later!!!")
