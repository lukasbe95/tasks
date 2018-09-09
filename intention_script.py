# -*- coding: utf-8 -*-
import docx2txt
import os
import re
import argparse

def br(instr):
    return "<b>{}</b>".format(instr)
def wholeP(instr):
    return "<p>{}</p>".format(instr)
def startP(instr):
    return "<p>{}".format(instr)
def endP(instr):
    return "{}</p>".format(instr)
def contains(instr):
    days = ['PONIEDZIAŁEK','WTOREK','ŚRODA','CZWARTEK','PIĄTEK','SOBOTA','NIEDZIELA']
    for word in instr.split(' '):
        if word in days:
            return True
    return False
def preprocess(mylist,last):
    tempList = []
    tempStr = ""
    for line in mylist:
        if contains(line):
            tempList.append(tempStr) if tempStr != "" else 0
            tempStr = ""
            tempList.append(line)
        elif line == last:
            tempStr += " {}".format(line)
            tempList.append(tempStr)
        else:
            tempStr += "{}".format(line)
    return tempList
def returnNotEmptyLines(path):
    ans = []
    with open(path,'r') as f:
        file = [re.sub(r"[^\S]+"," ",line) for line in f.readlines()]
        for line in file:
            if line != ' ':
                ans.append(line)
    return ans
def tagIt(path):
    whole = returnNotEmptyLines(path)
    first = whole.pop(0)
    second = whole.pop(0)
    first = "<p style=\"font-size:18px;\"><b>INTENCJE  MSZALNE</b></p>"
    last = whole[-1]
    toTag = preprocess(whole, last)
    ans = []
    ans.append(first)
    ans.append("<hr>")
    ans.append(br(wholeP(second)))
    for element in toTag:
        if contains(element):
            ans.append(br(wholeP(element)))
        else:
            ans.append(wholeP(element))
    return ans
def processHtml(name):
    ans = []
    flag = False
    with open(name, mode='r+') as file:
        for line in file.readlines():
            if "<div class=\"content\">" in line:
                flag = True
            elif "</div>" in line:
                flag = False
            if flag == False or "</div>" in line or "<div class=\"content\">" in line:
                ans.append(line)
    return ans
def merge(wholeHtml,intention):
    ans = []
    for line in wholeHtml:
        ans.append(line)
        if "<div class=\"content\">" in line:
            for iline in intention:
                ans.append(iline)
    return "".join(ans)
def main():
    parser = argparse.ArgumentParser(description='Podaj argumenty:')
    #add arg
    parser.add_argument("-i","--i",help="Podaj ścieżkę do pliku intencje.html",type=str)
    parser.add_argument("-f","--f",help="Plik tekstowy z zapisem intencji",type=str)
    args = parser.parse_args()
    inten = tagIt(args.f)
    whole = processHtml(args.i)
    os.remove(args.i)
    with open(args.i,"w") as f:
        f.write(merge(whole,inten))
if __name__ == '__main__':
    main()
