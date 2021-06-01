#!/usr/bin/python
# -*- coding: utf8 -*-


import random
import codecs
import telebot
import schedule
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import pandas as pd
from openpyxl import Workbook
import csv
from array import array





date = []
time = []
Player1 = []
Player2 = []
totalscore = []
r1 = []
r2 = []
r3 = []
r4 = []
r5 = []
r6 = []
r7 = []
r8 = []
r9 = []
winP1 = []
winP2 = []
F = []
B = []
NoFB = []
line_sum = []
line1_sum = []
suml = []
sumr = []
summa = []
FBR_list = []
playerslist = []



chrome_path = r'C:\Python_mini\chromedriver.exe'
driver = webdriver.Chrome(chrome_path)
url = "C:/Python_mini/messages.html"
#page = open(url)
#soup = BeautifulSoup(open("C:\Python_mini\messages.html"), encoding='utf-8')
#div1 = soup.find_all('div', class_='message default clearfix joined')
#print(div1)
driver.get(url)
driver.maximize_window()
container = driver.find_element_by_css_selector("div[class=history]").get_attribute("innerHTML")
#html1 = requests.get(url)
soup = BeautifulSoup(container, 'html.parser')


div1 = soup.find_all('div', class_='message default clearfix')
for div in div1:
    div = div.find('div', class_='text')
    for i in div.select("br"):
        i.replace_with("\n")

    try:

        names = div.findAll('a')
        for name in names:
            playerslist.append(name.text)
        print(playerslist[1][0:2])
        if playerslist[1][0:2] == '#L':
            for name in names[3:4]:
                print(name.text[1:])
                Player1.append(name.text[1:])
            for name in names[4:5]:
                print(name.text[1:])
                Player2.append(name.text[1:])
        else:
            for name in names[2:3]:
                print(name.text[1:])
                Player1.append(name.text[1:])
            for name in names[3:4]:
                print(name.text[1:])
                Player2.append(name.text[1:])

        #for name in names[3:4]:
            #print(name.text[1:])
            #Player1.append(name.text[1:])
        #for name in names[4:5]:
            #print(name.text[1:])
            #Player2.append(name.text[1:])

        print(div.text)
        lines1 = []
        lines1 = div.text.split('\n')
        print(len(lines1))
        for line in lines1:
            line1_sum.append(int(line.count('. P')))
        print(sum(line1_sum))

        if 0 <= int(sum(line1_sum)) < 1:
            totalscore.append('0:0')
            r1.append(' ')
            r2.append(' ')
            r3.append(' ')
            r4.append(' ')
            r5.append(' ')
            r6.append(' ')
            r7.append(' ')
            r8.append(' ')
            r9.append(' ')



        if 1 <= int(sum(line1_sum)) < 2:
            for line in lines1[len(lines1) - 3:len(lines1) - 2]:
                totalscore.append(line)
            for line in lines1[len(lines1) - 2:len(lines1) - 1]:
                summa.append(line[line.find('P') + 1:line.find('P') + 2])
                FBR_list.append(line[line.find('P') + 4:line.find('P') + 5])
            print(summa)
            for su in summa:
                if int(str(su)) == 1:
                    suml.append(1)
                    sumr.append(0)
                else:
                    suml.append(0)
                    sumr.append(1)
                r1.append(str(sum(suml[0:1])) + ':' + str(sum(sumr[0:1])) + ' ' + FBR_list[0])
                r2.append(' ')
                r3.append(' ')
                r4.append(' ')
                r5.append(' ')
                r6.append(' ')
                r7.append(' ')
                r8.append(' ')
                r9.append(' ')

        if 2 <= int(sum(line1_sum)) < 3:
            for line in lines1[len(lines1) - 4:len(lines1) - 3]:
                totalscore.append(line)
            for line in lines1[len(lines1) - 3:len(lines1) - 1]:
                summa.append(line[line.find('P') + 1:line.find('P') + 2])
                FBR_list.append(line[line.find('P')+4:line.find('P')+5])
            print(summa)
            for su in summa:
                if int(str(su)) == 1:
                    suml.append(1)
                    sumr.append(0)
                else:
                    suml.append(0)
                    sumr.append(1)
            r1.append(str(sum(suml[0:1])) + ':' +str(sum(sumr[0:1])) + ' ' + FBR_list[0])
            r2.append(str(sum(suml[0:2])) + ':' +str(sum(sumr[0:2])) + ' ' + FBR_list[1])
            r3.append(' ')
            r4.append(' ')
            r5.append(' ')
            r6.append(' ')
            r7.append(' ')
            r8.append(' ')
            r9.append(' ')

        if 3 <= int(sum(line1_sum)) < 4:
            for line in lines1[len(lines1) - 5:len(lines1) - 4]:
                totalscore.append(line)
            for line in lines1[len(lines1) - 4:len(lines1) - 1]:
                summa.append(line[line.find('P') + 1:line.find('P') + 2])
                FBR_list.append(line[line.find('P') + 4:line.find('P') + 5])
            print(summa)
            for su in summa:
                if int(str(su)) == 1:
                    suml.append(1)
                    sumr.append(0)
                else:
                    suml.append(0)
                    sumr.append(1)
            r1.append(str(sum(suml[0:1])) + ':' + str(sum(sumr[0:1])) + ' ' + FBR_list[0])
            r2.append(str(sum(suml[0:2])) + ':' + str(sum(sumr[0:2])) + ' ' + FBR_list[1])
            r3.append(str(sum(suml[0:3])) + ':' + str(sum(sumr[0:3])) + ' ' + FBR_list[2])
            r4.append(' ')
            r5.append(' ')
            r6.append(' ')
            r7.append(' ')
            r8.append(' ')
            r9.append(' ')

        if 4 <= int(sum(line1_sum)) < 5:
            for line in lines1[len(lines1) - 6:len(lines1) - 5]:
                totalscore.append(line)
            for line in lines1[len(lines1) - 5:len(lines1) - 1]:
                summa.append(line[line.find('P') + 1:line.find('P') + 2])
                FBR_list.append(line[line.find('P') + 4:line.find('P') + 5])
            print(summa)
            for su in summa:
                if int(str(su)) == 1:
                    suml.append(1)
                    sumr.append(0)
                else:
                    suml.append(0)
                    sumr.append(1)
            r1.append(str(sum(suml[0:1])) + ':' + str(sum(sumr[0:1])) + ' ' + FBR_list[0])
            r2.append(str(sum(suml[0:2])) + ':' + str(sum(sumr[0:2])) + ' ' + FBR_list[1])
            r3.append(str(sum(suml[0:3])) + ':' + str(sum(sumr[0:3])) + ' ' + FBR_list[2])
            r4.append(str(sum(suml[0:4])) + ':' + str(sum(sumr[0:4])) + ' ' + FBR_list[3])
            r5.append(' ')
            r6.append(' ')
            r7.append(' ')
            r8.append(' ')
            r9.append(' ')

        if 5 <= int(sum(line1_sum)) < 6:
            for line in lines1[len(lines1) - 7:len(lines1) - 6]:
                totalscore.append(line)
            for line in lines1[len(lines1) - 6:len(lines1) - 1]:
                summa.append(line[line.find('P') + 1:line.find('P') + 2])
                FBR_list.append(line[line.find('P') + 4:line.find('P') + 5])
            print(summa)
            for su in summa:
                if int(str(su)) == 1:
                    suml.append(1)
                    sumr.append(0)
                else:
                    suml.append(0)
                    sumr.append(1)
            r1.append(str(sum(suml[0:1])) + ':' + str(sum(sumr[0:1])) + ' ' + FBR_list[0])
            r2.append(str(sum(suml[0:2])) + ':' + str(sum(sumr[0:2])) + ' ' + FBR_list[1])
            r3.append(str(sum(suml[0:3])) + ':' + str(sum(sumr[0:3])) + ' ' + FBR_list[2])
            r4.append(str(sum(suml[0:4])) + ':' + str(sum(sumr[0:4])) + ' ' + FBR_list[3])
            r5.append(str(sum(suml[0:5])) + ':' + str(sum(sumr[0:5])) + ' ' + FBR_list[4])
            r6.append(' ')
            r7.append(' ')
            r8.append(' ')
            r9.append(' ')

        if 6 <= int(sum(line1_sum)) < 7:
            for line in lines1[len(lines1) - 8:len(lines1) - 7]:
                totalscore.append(line)
            for line in lines1[len(lines1) - 7:len(lines1) - 1]:
                summa.append(line[line.find('P') + 1:line.find('P') + 2])
                FBR_list.append(line[line.find('P') + 4:line.find('P') + 5])
            print(summa)
            for su in summa:
                if int(str(su)) == 1:
                    suml.append(1)
                    sumr.append(0)
                else:
                    suml.append(0)
                    sumr.append(1)
            r1.append(str(sum(suml[0:1])) + ':' + str(sum(sumr[0:1])) + ' ' + FBR_list[0])
            r2.append(str(sum(suml[0:2])) + ':' + str(sum(sumr[0:2])) + ' ' + FBR_list[1])
            r3.append(str(sum(suml[0:3])) + ':' + str(sum(sumr[0:3])) + ' ' + FBR_list[2])
            r4.append(str(sum(suml[0:4])) + ':' + str(sum(sumr[0:4])) + ' ' + FBR_list[3])
            r5.append(str(sum(suml[0:5])) + ':' + str(sum(sumr[0:5])) + ' ' + FBR_list[4])
            r6.append(str(sum(suml[0:6])) + ':' + str(sum(sumr[0:6])) + ' ' + FBR_list[5])
            r7.append(' ')
            r8.append(' ')
            r9.append(' ')

        if 7 <= int(sum(line1_sum)) < 8:
            for line in lines1[len(lines1) - 9:len(lines1) - 8]:
                totalscore.append(line)
            for line in lines1[len(lines1) - 8:len(lines1) - 1]:
                summa.append(line[line.find('P') + 1:line.find('P') + 2])
                FBR_list.append(line[line.find('P') + 4:line.find('P') + 5])
            print(summa)
            for su in summa:
                if int(str(su)) == 1:
                    suml.append(1)
                    sumr.append(0)
                else:
                    suml.append(0)
                    sumr.append(1)
            r1.append(str(sum(suml[0:1])) + ':' + str(sum(sumr[0:1])) + ' ' + FBR_list[0])
            r2.append(str(sum(suml[0:2])) + ':' + str(sum(sumr[0:2])) + ' ' + FBR_list[1])
            r3.append(str(sum(suml[0:3])) + ':' + str(sum(sumr[0:3])) + ' ' + FBR_list[2])
            r4.append(str(sum(suml[0:4])) + ':' + str(sum(sumr[0:4])) + ' ' + FBR_list[3])
            r5.append(str(sum(suml[0:5])) + ':' + str(sum(sumr[0:5])) + ' ' + FBR_list[4])
            r6.append(str(sum(suml[0:6])) + ':' + str(sum(sumr[0:6])) + ' ' + FBR_list[5])
            r7.append(str(sum(suml[0:7])) + ':' + str(sum(sumr[0:7])) + ' ' + FBR_list[6])
            r8.append(' ')
            r9.append(' ')

        if 8 <= int(sum(line1_sum)) < 9:
            for line in lines1[len(lines1) - 10:len(lines1) - 9]:
                totalscore.append(line)
            for line in lines1[len(lines1) - 9:len(lines1) - 1]:
                summa.append(line[line.find('P') + 1:line.find('P') + 2])
                FBR_list.append(line[line.find('P') + 4:line.find('P') + 5])
            print(summa)
            for su in summa:
                if int(str(su)) == 1:
                    suml.append(1)
                    sumr.append(0)
                else:
                    suml.append(0)
                    sumr.append(1)
            r1.append(str(sum(suml[0:1])) + ':' + str(sum(sumr[0:1])) + ' ' + FBR_list[0])
            r2.append(str(sum(suml[0:2])) + ':' + str(sum(sumr[0:2])) + ' ' + FBR_list[1])
            r3.append(str(sum(suml[0:3])) + ':' + str(sum(sumr[0:3])) + ' ' + FBR_list[2])
            r4.append(str(sum(suml[0:4])) + ':' + str(sum(sumr[0:4])) + ' ' + FBR_list[3])
            r5.append(str(sum(suml[0:5])) + ':' + str(sum(sumr[0:5])) + ' ' + FBR_list[4])
            r6.append(str(sum(suml[0:6])) + ':' + str(sum(sumr[0:6])) + ' ' + FBR_list[5])
            r7.append(str(sum(suml[0:7])) + ':' + str(sum(sumr[0:7])) + ' ' + FBR_list[6])
            r8.append(str(sum(suml[0:8])) + ':' + str(sum(sumr[0:8])) + ' ' + FBR_list[7])
            r9.append(' ')








        if int(sum(line1_sum)) >= 9:
            for line in lines1[len(lines1) - 11:len(lines1) - 10]:
                totalscore.append(line)
            for line in lines1[len(lines1) - 10:len(lines1) - 1]:
                #print(line[line.find('P') + 1:line.find('P') + 2])
                summa.append(line[line.find('P') + 1:line.find('P') + 2])
                FBR_list.append(line[line.find('P') + 4:line.find('P') + 5])
            print(summa)
            for su in summa:
                if int(str(su)) == 1:
                    suml.append(1)
                    sumr.append(0)
                else:
                    suml.append(0)
                    sumr.append(1)
            #print (suml[0], ':', sumr[0])
            print (sum(suml[0:1]), ':', sum(sumr[0:1]))
            print (sum(suml[0:2]), ':', sum(sumr[0:2]))
            print (sum(suml[0:3]), ':', sum(sumr[0:3]))
            print (sum(suml[0:4]), ':', sum(sumr[0:4]))
            print (sum(suml[0:5]), ':', sum(sumr[0:5]))
            print (sum(suml[0:6]), ':', sum(sumr[0:6]))
            print (sum(suml[0:7]), ':', sum(sumr[0:7]))
            print (sum(suml[0:8]), ':', sum(sumr[0:8]))
            print (sum(suml[0:9]), ':', sum(sumr[0:9]))
            r1.append(str(sum(suml[0:1])) + ':' + str(sum(sumr[0:1])) + ' ' + FBR_list[0])
            r2.append(str(sum(suml[0:2])) + ':' + str(sum(sumr[0:2])) + ' ' + FBR_list[1])
            r3.append(str(sum(suml[0:3])) + ':' + str(sum(sumr[0:3])) + ' ' + FBR_list[2])
            r4.append(str(sum(suml[0:4])) + ':' + str(sum(sumr[0:4])) + ' ' + FBR_list[3])
            r5.append(str(sum(suml[0:5])) + ':' + str(sum(sumr[0:5])) + ' ' + FBR_list[4])
            r6.append(str(sum(suml[0:6])) + ':' + str(sum(sumr[0:6])) + ' ' + FBR_list[5])
            r7.append(str(sum(suml[0:7])) + ':' + str(sum(sumr[0:7])) + ' ' + FBR_list[6])
            r8.append(str(sum(suml[0:8])) + ':' + str(sum(sumr[0:8])) + ' ' + FBR_list[7])
            r9.append(str(sum(suml[0:9]))+':'+str(sum(sumr[0:9])) + ' ' + FBR_list[8])

        for line in lines1[1:2]:
            print (line[0:5])  # time
            time.append(line[0:5])
            print (line[6:16])  # date
            date.append(line[6:16])

        for line in lines1[4:5]:
            print (line[8:])
            winP1.append(float(line[8:].split('/')[0]))  # P1/P2
            winP2.append(float(line[8:].split('/')[1]))

        for line in lines1[5:6]:
            print (line[6:])
            F.append(float(line[6:].split(' | ')[0]))  # FBR
            B.append(float(line[6:].split(' | ')[1]))
            NoFB.append(float(line[6:].split(' | ')[2]))
    except Exception:
        print(Exception)


    print("_______________________________________________________________")
    line1_sum.clear()
    suml.clear()
    sumr.clear()
    summa.clear()
    FBR_list.clear()
    playerslist.clear()

    matches = soup.find_all('div', class_='message default clearfix joined')
    for match in matches:
        match = match.find('div', class_='text')

        try:
            for i in match.select("br"):
                i.replace_with("\n")
        except Exception:
            print(Exception)

        try:

            names = match.findAll('a')
            for name in names:
                playerslist.append(name.text)
            print(playerslist[1][0:2])
            if playerslist[1][0:2] == '#L':
                for name in names[3:4]:
                    print (name.text[1:])
                    Player1.append(name.text[1:])
                for name in names[4:5]:
                    print (name.text[1:])
                    Player2.append(name.text[1:])
            else:
                for name in names[2:3]:
                    print (name.text[1:])
                    Player1.append(name.text[1:])
                for name in names[3:4]:
                    print (name.text[1:])
                    Player2.append(name.text[1:])


            print (match.text)
            lines = []
            lines = match.text.split('\n')
            print(len(lines))
            for line in lines:
                line_sum.append(int(line.count('. P')))
            print(sum(line_sum))

            if 0 <= int(sum(line_sum)) < 1:
                totalscore.append('0:0')
                r1.append(' ')
                r2.append(' ')
                r3.append(' ')
                r4.append(' ')
                r5.append(' ')
                r6.append(' ')
                r7.append(' ')
                r8.append(' ')
                r9.append(' ')

            if 1 <= int(sum(line_sum)) < 2:
                for line in lines[len(lines) - 3:len(lines) - 2]:
                    totalscore.append(line)
                for line in lines[len(lines) - 2:len(lines) - 1]:
                    summa.append(line[line.find('P') + 1:line.find('P') + 2])
                    FBR_list.append(line[line.find('P') + 4:line.find('P') + 5])
                    print(summa)
                    for su in summa:
                        if int(str(su)) == 1:
                            suml.append(1)
                            sumr.append(0)
                        else:
                            suml.append(0)
                            sumr.append(1)
                    r1.append(str(sum(suml[0:1])) + ':' + str(sum(sumr[0:1])) + ' ' + FBR_list[0])
                    r2.append(' ')
                    r3.append(' ')
                    r4.append(' ')
                    r5.append(' ')
                    r6.append(' ')
                    r7.append(' ')
                    r8.append(' ')
                    r9.append(' ')

            if 2 <= int(sum(line_sum)) < 3:
                for line in lines[len(lines) - 4:len(lines) - 3]:
                    totalscore.append(line)
                for line in lines[len(lines) - 3:len(lines) - 1]:
                    summa.append(line[line.find('P') + 1:line.find('P') + 2])
                    FBR_list.append(line[line.find('P') + 4:line.find('P') + 5])
                print(summa)
                for su in summa:
                    if int(str(su)) == 1:
                        suml.append(1)
                        sumr.append(0)
                    else:
                        suml.append(0)
                        sumr.append(1)
                r1.append(str(sum(suml[0:1])) + ':' + str(sum(sumr[0:1])) + ' ' + FBR_list[0])
                r2.append(str(sum(suml[0:2])) + ':' + str(sum(sumr[0:2])) + ' ' + FBR_list[1])
                r3.append(' ')
                r4.append(' ')
                r5.append(' ')
                r6.append(' ')
                r7.append(' ')
                r8.append(' ')
                r9.append(' ')

            if 3 <= int(sum(line_sum)) < 4:
                for line in lines[len(lines) - 5:len(lines) - 4]:
                    totalscore.append(line)
                for line in lines[len(lines) - 4:len(lines) - 1]:
                    summa.append(line[line.find('P') + 1:line.find('P') + 2])
                    FBR_list.append(line[line.find('P') + 4:line.find('P') + 5])
                print(summa)
                for su in summa:
                    if int(str(su)) == 1:
                        suml.append(1)
                        sumr.append(0)
                    else:
                        suml.append(0)
                        sumr.append(1)
                r1.append(str(sum(suml[0:1])) + ':' + str(sum(sumr[0:1])) + ' ' + FBR_list[0])
                r2.append(str(sum(suml[0:2])) + ':' + str(sum(sumr[0:2])) + ' ' + FBR_list[1])
                r3.append(str(sum(suml[0:3])) + ':' + str(sum(sumr[0:3])) + ' ' + FBR_list[2])
                r4.append(' ')
                r5.append(' ')
                r6.append(' ')
                r7.append(' ')
                r8.append(' ')
                r9.append(' ')

            if 4 <= int(sum(line_sum)) < 5:
                for line in lines[len(lines) - 6:len(lines) - 5]:
                    totalscore.append(line)
                for line in lines[len(lines) - 5:len(lines) - 1]:
                    summa.append(line[line.find('P') + 1:line.find('P') + 2])
                    FBR_list.append(line[line.find('P') + 4:line.find('P') + 5])
                print(summa)
                for su in summa:
                    if int(str(su)) == 1:
                        suml.append(1)
                        sumr.append(0)
                    else:
                        suml.append(0)
                        sumr.append(1)
                r1.append(str(sum(suml[0:1])) + ':' + str(sum(sumr[0:1])) + ' ' + FBR_list[0])
                r2.append(str(sum(suml[0:2])) + ':' + str(sum(sumr[0:2])) + ' ' + FBR_list[1])
                r3.append(str(sum(suml[0:3])) + ':' + str(sum(sumr[0:3])) + ' ' + FBR_list[2])
                r4.append(str(sum(suml[0:4])) + ':' + str(sum(sumr[0:4])) + ' ' + FBR_list[3])
                r5.append(' ')
                r6.append(' ')
                r7.append(' ')
                r8.append(' ')
                r9.append(' ')

            if 5 <= int(sum(line_sum)) < 6:
                for line in lines[len(lines) - 7:len(lines) - 6]:
                    totalscore.append(line)
                for line in lines[len(lines) - 6:len(lines) - 1]:
                    summa.append(line[line.find('P') + 1:line.find('P') + 2])
                    FBR_list.append(line[line.find('P') + 4:line.find('P') + 5])
                print(summa)
                for su in summa:
                    if int(str(su)) == 1:
                        suml.append(1)
                        sumr.append(0)
                    else:
                        suml.append(0)
                        sumr.append(1)
                r1.append(str(sum(suml[0:1])) + ':' + str(sum(sumr[0:1])) + ' ' + FBR_list[0])
                r2.append(str(sum(suml[0:2])) + ':' + str(sum(sumr[0:2])) + ' ' + FBR_list[1])
                r3.append(str(sum(suml[0:3])) + ':' + str(sum(sumr[0:3])) + ' ' + FBR_list[2])
                r4.append(str(sum(suml[0:4])) + ':' + str(sum(sumr[0:4])) + ' ' + FBR_list[3])
                r5.append(str(sum(suml[0:5])) + ':' + str(sum(sumr[0:5])) + ' ' + FBR_list[4])
                r6.append(' ')
                r7.append(' ')
                r8.append(' ')
                r9.append(' ')

            if 6 <= int(sum(line_sum)) < 7:
                for line in lines[len(lines) - 8:len(lines) - 7]:
                    totalscore.append(line)
                for line in lines[len(lines) - 7:len(lines) - 1]:
                    summa.append(line[line.find('P') + 1:line.find('P') + 2])
                    FBR_list.append(line[line.find('P') + 4:line.find('P') + 5])
                print(summa)
                for su in summa:
                    if int(str(su)) == 1:
                        suml.append(1)
                        sumr.append(0)
                    else:
                        suml.append(0)
                        sumr.append(1)
                r1.append(str(sum(suml[0:1])) + ':' + str(sum(sumr[0:1])) + ' ' + FBR_list[0])
                r2.append(str(sum(suml[0:2])) + ':' + str(sum(sumr[0:2])) + ' ' + FBR_list[1])
                r3.append(str(sum(suml[0:3])) + ':' + str(sum(sumr[0:3])) + ' ' + FBR_list[2])
                r4.append(str(sum(suml[0:4])) + ':' + str(sum(sumr[0:4])) + ' ' + FBR_list[3])
                r5.append(str(sum(suml[0:5])) + ':' + str(sum(sumr[0:5])) + ' ' + FBR_list[4])
                r6.append(str(sum(suml[0:6])) + ':' + str(sum(sumr[0:6])) + ' ' + FBR_list[5])
                r7.append(' ')
                r8.append(' ')
                r9.append(' ')

            if 7 <= int(sum(line_sum)) < 8:
                for line in lines[len(lines) - 9:len(lines) - 8]:
                    totalscore.append(line)
                for line in lines[len(lines) - 8:len(lines) - 1]:
                    summa.append(line[line.find('P') + 1:line.find('P') + 2])
                    FBR_list.append(line[line.find('P') + 4:line.find('P') + 5])
                print(summa)
                for su in summa:
                    if int(str(su)) == 1:
                        suml.append(1)
                        sumr.append(0)
                    else:
                        suml.append(0)
                        sumr.append(1)
                r1.append(str(sum(suml[0:1])) + ':' + str(sum(sumr[0:1])) + ' ' + FBR_list[0])
                r2.append(str(sum(suml[0:2])) + ':' + str(sum(sumr[0:2])) + ' ' + FBR_list[1])
                r3.append(str(sum(suml[0:3])) + ':' + str(sum(sumr[0:3])) + ' ' + FBR_list[2])
                r4.append(str(sum(suml[0:4])) + ':' + str(sum(sumr[0:4])) + ' ' + FBR_list[3])
                r5.append(str(sum(suml[0:5])) + ':' + str(sum(sumr[0:5])) + ' ' + FBR_list[4])
                r6.append(str(sum(suml[0:6])) + ':' + str(sum(sumr[0:6])) + ' ' + FBR_list[5])
                r7.append(str(sum(suml[0:7])) + ':' + str(sum(sumr[0:7])) + ' ' + FBR_list[6])
                r8.append(' ')
                r9.append(' ')

            if 8 <= int(sum(line_sum)) < 9:
                for line in lines[len(lines) - 10:len(lines) - 9]:
                    totalscore.append(line)
                for line in lines[len(lines) - 9:len(lines) - 1]:
                    summa.append(line[line.find('P') + 1:line.find('P') + 2])
                    FBR_list.append(line[line.find('P') + 4:line.find('P') + 5])
                print(summa)
                for su in summa:
                    if int(str(su)) == 1:
                        suml.append(1)
                        sumr.append(0)
                    else:
                        suml.append(0)
                        sumr.append(1)
                r1.append(str(sum(suml[0:1])) + ':' + str(sum(sumr[0:1])) + ' ' + FBR_list[0])
                r2.append(str(sum(suml[0:2])) + ':' + str(sum(sumr[0:2])) + ' ' + FBR_list[1])
                r3.append(str(sum(suml[0:3])) + ':' + str(sum(sumr[0:3])) + ' ' + FBR_list[2])
                r4.append(str(sum(suml[0:4])) + ':' + str(sum(sumr[0:4])) + ' ' + FBR_list[3])
                r5.append(str(sum(suml[0:5])) + ':' + str(sum(sumr[0:5])) + ' ' + FBR_list[4])
                r6.append(str(sum(suml[0:6])) + ':' + str(sum(sumr[0:6])) + ' ' + FBR_list[5])
                r7.append(str(sum(suml[0:7])) + ':' + str(sum(sumr[0:7])) + ' ' + FBR_list[6])
                r8.append(str(sum(suml[0:8])) + ':' + str(sum(sumr[0:8])) + ' ' + FBR_list[7])
                r9.append(' ')

            if int(sum(line_sum)) >= 9:
                for line in lines[len(lines) - 11:len(lines) - 10]:
                    totalscore.append(line)
                for line in lines[len(lines) - 10:len(lines) - 1]:
                    # print(line[line.find('P') + 1:line.find('P') + 2])
                    summa.append(line[line.find('P') + 1:line.find('P') + 2])
                    FBR_list.append(line[line.find('P') + 4:line.find('P') + 5])
                print(summa)
                for su in summa:
                    if int(str(su)) == 1:
                        suml.append(1)
                        sumr.append(0)
                    else:
                        suml.append(0)
                        sumr.append(1)
                # print (suml[0], ':', sumr[0])
                print (sum(suml[0:1]), ':', sum(sumr[0:1]))
                print (sum(suml[0:2]), ':', sum(sumr[0:2]))
                print (sum(suml[0:3]), ':', sum(sumr[0:3]))
                print (sum(suml[0:4]), ':', sum(sumr[0:4]))
                print (sum(suml[0:5]), ':', sum(sumr[0:5]))
                print (sum(suml[0:6]), ':', sum(sumr[0:6]))
                print (sum(suml[0:7]), ':', sum(sumr[0:7]))
                print (sum(suml[0:8]), ':', sum(sumr[0:8]))
                print (sum(suml[0:9]), ':', sum(sumr[0:9]))
                r1.append(str(sum(suml[0:1])) + ':' + str(sum(sumr[0:1])) + ' ' + FBR_list[0])
                r2.append(str(sum(suml[0:2])) + ':' + str(sum(sumr[0:2])) + ' ' + FBR_list[1])
                r3.append(str(sum(suml[0:3])) + ':' + str(sum(sumr[0:3])) + ' ' + FBR_list[2])
                r4.append(str(sum(suml[0:4])) + ':' + str(sum(sumr[0:4])) + ' ' + FBR_list[3])
                r5.append(str(sum(suml[0:5])) + ':' + str(sum(sumr[0:5])) + ' ' + FBR_list[4])
                r6.append(str(sum(suml[0:6])) + ':' + str(sum(sumr[0:6])) + ' ' + FBR_list[5])
                r7.append(str(sum(suml[0:7])) + ':' + str(sum(sumr[0:7])) + ' ' + FBR_list[6])
                r8.append(str(sum(suml[0:8])) + ':' + str(sum(sumr[0:8])) + ' ' + FBR_list[7])
                r9.append(str(sum(suml[0:9])) + ':' + str(sum(sumr[0:9])) + ' ' + FBR_list[8])

            for line in lines[1:2]:
                print (line[0:5])  # time
                time.append(line[0:5])
                print (line[6:16])  # date
                date.append(line[6:16])

            for line in lines[4:5]:
                print (line[8:])
                winP1.append(float(line[8:].split('/')[0]))  # P1/P2
                winP2.append(float(line[8:].split('/')[1]))

            for line in lines[5:6]:
                print (line[6:])
                F.append(float(line[6:].split(' | ')[0]))  # FBR
                B.append(float(line[6:].split(' | ')[1]))
                NoFB.append(float(line[6:].split(' | ')[2]))

        except Exception:
            print(Exception)

        print("_______________________________________________________________")
        line1_sum.clear()
        line_sum.clear()
        suml.clear()
        sumr.clear()
        summa.clear()
        FBR_list.clear()
        playerslist.clear()


    df = pd.DataFrame.from_dict(
        {'Date': date, 'Time': time, 'Player1': Player1, 'Player2': Player2, 'TotalScore': totalscore, 'R1': r1,
         'R2': r2, 'R3': r3, 'R4': r4, 'R5': r5, 'R6': r6, 'R7': r7, 'R8': r8, 'R9': r9, 'WinP1': winP1, 'WinP2': winP2,
         'Fatality': F, 'Brutality': B, 'NoFB': NoFB})
    df.to_excel('result.xlsx', header=True, index=False)

