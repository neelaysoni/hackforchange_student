import datetime
from lib2to3.pygram import pattern_symbols
from time import strftime
import csv
from typing import ParamSpecArgs
import pandas as pd
f=pd.read_csv('email-password-recovery-code.csv')
#taking username and password

flag = 0
while(flag == 0):
  with open('email-password-recovery-code.csv', 'r') as file:
    reader = csv.reader(file)
    print("-----------------------------------------------")
    print("Welcome to Student ID Portal")
    x=datetime.datetime.now()
    print("Date\t: ",x.strftime("%x"))
    print("-----------------------------------------------")
    id1=input("Enter Your Identifier\t: ")
    pswd=input("Enter Your Password\t: ")
    for row in reader:
      a = row[1]
      b = row[2]
      if id1 == a and pswd == b:
        print(row)
        flag = 1
    if flag==0:
      print("!-----Wrong Input-----!")
