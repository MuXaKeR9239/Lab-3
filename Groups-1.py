import csv
import sys
import os
def readfile():
    print("Group 8")
    filename = "Groups/Group8.txt"
    text_file=open(filename,mode="r", encoding="utf-8")
    reader=csv.reader(text_file, delimiter="\t")
    for str in reader:
        print(str)
    text_file.close()

    print("Group 7")
    filename = "Groups/Group 7.txt"
    text_file=open(filename,mode="r", encoding="utf-8")
    reader=csv.reader(text_file, delimiter="\t")
    for str in reader:
        print(str)
    text_file.close()

    print("Group 10")
    filename = "Groups/Group 10.txt"
    text_file=open(filename,mode="r", encoding="utf-8")
    reader=csv.reader(text_file, delimiter="\t")
    for str in reader:
        print(str)
    text_file.close()

def writefile():
    Group=input("Введите номер группы")
    fd=open("Groups/Group"+ Group + ".txt", "w") 
    while True:
        name=input("Введите имя студента")
        score=input("Введите бал студента")
        fd.write(score + name + "\n")
        Choice=input("Продолжить?")
        if Choice=="n":
            break
    fd.close()

def readdir():
    files=os.listdir("Groups")
    for file in files:
        print(file)

def find():
    findName=input("Введите имя студента, балл которого хотите найти ")
    group=input("Введите группу ")
    try:
        fd=open("Groups/Group" + group + ".txt", mode="r", encoding="utf-8")
    except:
        print("Группа не найдена")
        return
    for line in fd.readlines():
        line=line.replace("\n", "")
        score=line.split(" ")[0]
        name=line.split(" ")[1] +" "+ line.split(" ")[2]
        if name == findName:
            print("Имя: " + name + "\nБалл: " + score)
            return score
    print("Студент не найден")

def sort():
    def getScore(line):
        if len(line) < 3:
            return 100
        line=line.replace("\n", "")
        line=line.split(" ")
        return int(line[0])
    group=input("Введите группу ")
    try:
        fd=open("Groups/Group" + group + ".txt", "r")
    except:
        print("Группа не найдена")
        return
    lines=fd.readlines()
    sortedLines=sorted(lines, key=getScore)
    fd.close()
    fd=open("Groups/Group" + group + ".txt", "w")
    for line in sortedLines:
        fd.write(line)
    fd.close()

def unit():
    filesList = os.listdir("Groups")
    fs = open('Groups/United.txt', mode='w', encoding='utf-8')
    for filename in filesList:
        rfs = open('Groups/' + filename, mode='r', encoding='cp1251')
        lines = rfs.readlines()
        for line in lines:
            fs.write(line)
        rfs.close()
    fs.close()
unit()        