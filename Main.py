#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


shooting = pd.read_csv("Shooting.csv")
defense = pd.read_csv("Defense.csv")
rebounding = pd.read_csv("Rebounding.csv")
ball = pd.read_csv("Ball_Handling.csv")
rows = ["MW", "KV", "MV", "IK", "LV", "AL", "MG", "LH", "DB", "AR", "RS", "MK", "LK", "TH"]

Scolumns = ["LR", "3PC", "SFD", "3PT", "2PT", "FGm", "FD", "FT", "FTm", "RUN", "BAD", "HC", "TOTAL"]
s_df = pd.DataFrame(shooting.values, index = rows, columns = Scolumns)

Dcolumns = ["GB", "BBM", "BBB", "DF", "STL", "CHARGE", "GR", "BR", "SLOW", "TOTAL"]
d_df = pd.DataFrame(defense.values, index = rows, columns = Dcolumns)

Rcolumns = ["BO", "MBO", "OR", "DR", "PB", "TOTAL"]
r_df = pd.DataFrame(rebounding.values, index = rows, columns = Rcolumns)

Bcolumns = ["A", "VA", "P/P", "TO", "TOTAL"]
b_df = pd.DataFrame(ball.values, index = rows, columns = Bcolumns)


# In[3]:


def main():
    choice = 0
    print("1.  Enter stat")
#enter wont affect actual csv until exit 
    print("2.  Print player stats")
#prints what we temporarily have
    print("3.  Print category")
#prints what we temporarily have
    print("4.  Exit")
#exit rewrites to the csv file to make the changes
    choice=int(input("Enter your choice:"))
    print("")
    while(choice != 4):
        if choice==1:
            enter()
        elif choice == 2:
            name = str(input("Enter player initials: "))
            cat = str(input("Enter category: "))
            displayPlayer(name, cat)
        elif choice == 3:
            cat = str(input("Enter category: "))
            displayCategory(cat)
        choice=int(input("Enter your choice:"))
        print("")
    
    if choice == 4:
        exit()


# In[4]:


def enter():
    name = input("Enter an initial: ")
    name = name.upper().strip()
#can be upper or lowercase, don't matter
    cat = input("Enter a category: ")
    cat = cat.lower().strip()
#(Shooting, Rebounding, Defense, Ball_Handling), case don't matter
    key = input("Enter a key: ")
    key = key.upper().strip()
#(LR, 3PC, SFD,......), case don't matter
    value = float(input("Enter value: "))
#negative or positive, negative can be used to remove any mistakes made
    invalid = True
    
    while(invalid):
        if(cat == "shooting"):
            s_add(name, key, value)
            invalid = False
        elif(cat == "defense"):
            d_add(name, key, value)
            invalid = False
        elif(cat == "rebounding"):
            r_add(name, key, value)
            invalid = False
        elif(cat == "ball handling"):
            b_add(name, key, value)
            invalid = False
        else:
            print("Invalid category")
            category = input("Enter a valid category: ")


# In[5]:


def s_add(name, key, value): 
    invalid = True
    
    while(invalid):
        if key == "LR": 
            s_df.loc[name, "LR"] += (value * 3.2)
            s_df.loc[name, "TOTAL"] += (value * 3.2)
            print(s_df.loc[name, "LR"])
            invalid = False
        elif key == "3PC":
            s_df.loc[name, "3PC"] += (value * 3.2)
            s_df.loc[name, "TOTAL"] += (value * 3.2)
            print(s_df.loc[name, "3PC"])
            invalid = False
        elif key == "SFD":
            s_df.loc[name, "SFD"] += (value * 3.5)
            s_df.loc[name, "TOTAL"] += (value * 3.5)
            print(s_df.loc[name, "SFD"])
            invalid = False
        elif key == "3PT":
            s_df.loc[name, "3PT"] += (value * 3)
            s_df.loc[name, "TOTAL"] += (value * 3)
            print(s_df.loc[name, "3PT"])
            invalid = False
        elif key == "2PT":
            s_df.loc[name, "2PT"] += (value * 2)
            s_df.loc[name, "TOTAL"] += (value * 2)
            print(s_df.loc[name, "2PT"])
            invalid = False
        elif key == "FGm":
            s_df.loc[name, "FGm"] += (value * -2)
            s_df.loc[name, "TOTAL"] += (value * -2)
            print(s_df.loc[name, "FGm"])
            invalid = False
        elif key == "FD":
            s_df.loc[name, "FD"] += (value * 1)
            s_df.loc[name, "TOTAL"] += (value * 1)
            print(s_df.loc[name, "FD"])
            invalid = False
        elif key == "FT":
            s_df.loc[name, "FT"] += (value * 1)
            s_df.loc[name, "TOTAL"] += (value * 1)
            print(s_df.loc[name, "FT"])
            invalid = False
        elif key == "FTm":
            s_df.loc[name, "FTm"] += (value * -2)
            s_df.loc[name, "TOTAL"] += (value * -2)
            print(s_df.loc[name, "FTm"])
            invalid = False
        elif key == "RUN":
            s_df.loc[name, "RUN"] += (value * -1)
            s_df.loc[name, "TOTAL"] += (value * -1)
            print(s_df.loc[name, "RUN"])
            invalid = False
        elif key == "BAD":
            s_df.loc[name, "BAD"] += (value * -1)
            s_df.loc[name, "TOTAL"] += (value * -1)
            print(s_df.loc[name, "BAD"])
            invalid = False
        elif key == "HC":
            s_df.loc[name, "HC"] += (value * 1)
            s_df.loc[name, "TOTAL"] += (value * 1)
            print(s_df.loc[name, "HC"])
            invalid = False
        else:
            print("Invalid key")
            key = input("Enter a valid key: ")
        
#     date = input("Enter date(mm/dd): ") not yet


# In[6]:


def d_add(name, key, value):
    invalid = True
    
    while(invalid):
        if key == "GB": 
            d_df.loc[name, "GB"] += (value * -3)
            d_df.loc[name, "TOTAL"] += (value * -3)
            print(d_df.loc[name, "GB"])
            invalid = False
        elif key == "BBM":
            d_df.loc[name, "BBM"] += (value * -3)
            d_df.loc[name, "TOTAL"] += (value * -3)
            print(d_df.loc[name, "BBM"])
            invalid = False
        elif key == "BBB":
            d_df.loc[name, "BBB"] += (value * -2)
            d_df.loc[name, "TOTAL"] += (value * -2)
            print(d_df.loc[name, "BBB"])
            invalid = False
        elif key == "DF":
            d_df.loc[name, "DF"] += (value * 2)
            d_df.loc[name, "TOTAL"] += (value * 2)
            print(d_df.loc[name, "DF"])
            invalid = False
        elif key == "STL":
            d_df.loc[name, "STL"] += (value * 3)
            d_df.loc[name, "TOTAL"] += (value * 3)
            print(d_df.loc[name, "STL"])
            invalid = False
        elif key == "CHARGE":
            d_df.loc[name, "CHARGE"] += (value * 6)
            d_df.loc[name, "TOTAL"] += (value * 6)
            print(d_df.loc[name, "CHARGE"])
            invalid = False
        elif key == "GR":
            d_df.loc[name, "GR"] += (value * 1)
            d_df.loc[name, "TOTAL"] += (value * 1)
            print(d_df.loc[name, "GR"])
            invalid = False
        elif key == "BR":
            d_df.loc[name, "BR"] += (value * -1)
            d_df.loc[name, "TOTAL"] += (value * -1)
            print(d_df.loc[name, "BR"])
            invalid = False
        elif key == "SLOW":
            d_df.loc[name, "SLOW"] += (value * -2)
            d_df.loc[name, "TOTAL"] += (value * -2)
            print(d_df.loc[name, "SLOW"])
            invalid = False
        else:
            print("Invalid key")
            key = input("Enter a valid key: ")


# In[7]:


def r_add(name, key, value):
    invalid = True
    
    while(invalid):
        if key == "BO": 
            r_df.loc[name, "BO"] += (value * 1)
            r_df.loc[name, "TOTAL"] += (value * 1)
            print(r_df.loc[name, "BO"])
            invalid = False
        elif key == "MBO":
            r_df.loc[name, "MBO"] += (value * -2)
            r_df.loc[name, "TOTAL"] += (value * -2)
            print(r_df.loc[name, "MBO"])
            invalid = False
        elif key == "OR":
            r_df.loc[name, "OR"] += (value * 4)
            r_df.loc[name, "TOTAL"] += (value * 4)
            print(r_df.loc[name, "OR"])
            invalid = False
        elif key == "DR":
            r_df.loc[name, "DR"] += (value * 2.5)
            r_df.loc[name, "TOTAL"] += (value * 2.5)
            print(r_df.loc[name, "DR"])
            invalid = False
        elif key == "PB":
            r_df.loc[name, "PB"] += (value * 1)
            r_df.loc[name, "TOTAL"] += (value * 1)
            print(r_df.loc[name, "PB"])
            invalid = False
        else:
            print("Invalid key")
            key = input("Enter a valid key: ")


# In[8]:


def b_add(name, key, value):
    invalid = True
    
    while(invalid):
        if key == "A": 
            b_df.loc[name, "A"] += (value * 4)
            b_df.loc[name, "TOTAL"] += (value * 4)
            print(b_df.loc[name, "A"])
            invalid = False
        elif key == "VA":
            b_df.loc[name, "VA"] += (value * 2)
            b_df.loc[name, "TOTAL"] += (value * 2)
            print(b_df.loc[name, "VA"])
            invalid = False
        elif key == "P/P":
            b_df.loc[name, "P/P"] += (value * 1)
            b_df.loc[name, "TOTAL"] += (value * 1)
            print(b_df.loc[name, "P/P"])
            invalid = False
        elif key == "TO":
            b_df.loc[name, "TO"] += (value * -3)
            b_df.loc[name, "TOTAL"] += (value * -3)
            print(b_df.loc[name, "TO"])
            invalid = False
        else:
            print("Invalid key")
            key = input("Enter a valid key: ")


# In[9]:


def displayPlayer(name, cat):
    name = name.upper().strip()
    cat = cat.lower().strip()
    
    if(cat == "shooting"):
        print(s_df.loc[name])
    elif(cat == "defense"):
        print(d_df.loc[name])
    elif(cat == "rebounding"):
        print(r_df.loc[name])
    elif(cat == "ball handling"):
        print(b_df.loc[name])
    


# In[10]:


def displayCategory(cat):
    cat = cat.lower().strip()
    
    if(cat == "shooting"):
        print(s_df)
    elif(cat == "defense"):
        print(d_df)
    elif(cat == "rebounding"):
        print(r_df)
    elif(cat == "ball handling"):
        print(b_df)


# In[11]:


def exit():
    s_df.set_index('LR', inplace = True)
    d_df.set_index('GB', inplace = True)
    r_df.set_index('BO', inplace = True)
    b_df.set_index('A', inplace = True)
    
    s_df.to_csv("Shooting.csv")
    d_df.to_csv("Defense.csv")
    r_df.to_csv("Rebounding.csv")
    b_df.to_csv("Ball_Handling.csv")


# In[12]:


main()

