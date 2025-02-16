import numpy as np
import pandas as pd
import os

train_data = pd.read_csv("djiatrain.csv")
n = len(train_data)
x_data = train_data.iloc[:, np.r_[1,11,12,13]]
#p(y)
prob_y1 = train_data['1b-Future'].sum() / n
#print(prob_y1)
prob_y5 = train_data['5b-Future'].sum() / n
#print(prob_y5)
prob_y30 = train_data['30b-Future'].sum() / n
#print(prob_y30)

#p(x)
prob_x1 = train_data['1b-Trend'].sum() / n
prob_x5 = train_data['5b-Trend'].sum() / n
prob_x30 = train_data['30b-Trend'].sum() / n

print("\n\n\n1-day trend")
#p(x1|y)
print("given 1-day growth")
x1y1 = train_data.loc[train_data['1b-Future']==1, '1b-Trend'].sum() / (train_data['1b-Future']==1).sum()
x1ny1 = train_data.loc[train_data['1b-Future']==0, '1b-Trend'].sum() / (train_data['1b-Future']==0).sum()
print(x1y1)
print(x1ny1)

print("given 5-day growth")
x1y5 = train_data.loc[train_data['5b-Future']==1, '1b-Trend'].sum() / (train_data['5b-Future']==1).sum()
x1ny5 = train_data.loc[train_data['5b-Future']==0, '1b-Trend'].sum() / (train_data['5b-Future']==0).sum()
print(x1y5)
print(x1ny5)

print("given 30-day growth")
x1y30 = train_data.loc[train_data['30b-Future']==1, '1b-Trend'].sum() / (train_data['30b-Future']==1).sum()
x1ny30 = train_data.loc[train_data['30b-Future']==0, '1b-Trend'].sum() / (train_data['30b-Future']==0).sum()
print(x1y30)
print(x1ny30)

print("\n\n\n5-day trend")
#p(x5|y)
print("given 1-day growth")
x5y1 = train_data.loc[train_data['1b-Future']==1, '5b-Trend'].sum() / (train_data['1b-Future']==1).sum()
x5ny1 = train_data.loc[train_data['1b-Future']==0, '5b-Trend'].sum() / (train_data['1b-Future']==0).sum()
print(x5y1)
print(x5ny1)

print("given 5-day growth")
x5y5 = train_data.loc[train_data['5b-Future']==1, '5b-Trend'].sum() / (train_data['5b-Future']==1).sum()
x5ny5 = train_data.loc[train_data['5b-Future']==0, '5b-Trend'].sum() / (train_data['5b-Future']==0).sum()
print(x5y5)
print(x5ny5)

print("given 30-day growth")
x5y30 = train_data.loc[train_data['30b-Future']==1, '5b-Trend'].sum() / (train_data['30b-Future']==1).sum()
x5ny30 = train_data.loc[train_data['30b-Future']==0, '5b-Trend'].sum() / (train_data['30b-Future']==0).sum()
print(x5y30)
print(x5ny30)


print("\n\n\n30-day trend")
#p(x5|y)
print("given 1-day growth")
x30y1 = train_data.loc[train_data['1b-Future']==1, '30b-Trend'].sum() / (train_data['1b-Future']==1).sum()
x30ny1 = train_data.loc[train_data['1b-Future']==0, '30b-Trend'].sum() / (train_data['1b-Future']==0).sum()
print(x30y1)
print(x30ny1)

print("given 5-day growth")
x30y5 = train_data.loc[train_data['5b-Future']==1, '30b-Trend'].sum() / (train_data['5b-Future']==1).sum()
x30ny5 = train_data.loc[train_data['5b-Future']==0, '30b-Trend'].sum() / (train_data['5b-Future']==0).sum()
print(x30y5)
print(x30ny5)

print("given 30-day growth")
x30y30 = train_data.loc[train_data['30b-Future']==1, '30b-Trend'].sum() / (train_data['30b-Future']==1).sum()
x30ny30 = train_data.loc[train_data['30b-Future']==0, '30b-Trend'].sum() / (train_data['30b-Future']==0).sum()
print(x30y30)
print(x30ny30)

d1 = 0.0
d5 = 0.0
d30 = 0.0
os.system('clear')
incdec = input("Are you looking for increases or decreses?[i/d]\n")
is_1 = input("Is the stock higher now than it was one day ago?[y/n]\n")
#is_5 = input("Is the stock higher now than it was five days ago?[y/n]\n")
#is_30 = input("Is the stock higher now than it was thirty days ago?[y/n]\n")

num1 = 1.0
num5 = 1.0
num30 = 1.0

if is_1 == 'y':
    d1 = prob_x1
    if incdec == 'i':
      num1 = num1 * x1y1
      num5 = num5 * x1y5
      num30 = num30 * x1y30
    else:
      num1 = num1 * x1ny1
      num5 = num5 * x1ny5
      num30 = num30 * x1ny30
else:
    d1 = 1 - prob_x1
    if incdec == 'i':
      num1 = num1 * (1 - x1y1)
      num5 = num5 * (1 - x1y5)
      num30 = num30 * (1 - x1y30)
    else:
      num1 = num1 * (1 - x1ny1)
      num5 = num5 * (1 - x1ny5)
      num30 = num30 * (1 - x1ny30)
#print(num1)
#print(num5)
#print(num30)
is_5 = input("Is the stock higher now than it was five days ago?[y/n]\n")
#is_30 = input("Is the stock higher now than it was thirty days ago?[y/n]\n")
if is_5 == 'y':
    d5 = prob_x5
    if incdec == 'i':
      num1 = num1 * x5y1
      num5 = num5 * x5y5
      num30 = num30 * x5y30
    else:
      num1 = num1 * x5ny1
      num5 = num5 * x5ny5
      num30 = num30 * x5ny30
else:
    d5 = 1 - prob_x5
    if incdec == 'i':
      num1 = num1 * (1 - x5y1)
      num5 = num5 * (1 - x5y5)
      num30 = num30 * (1 - x5y30)
    else:
      num1 = num1 * (1 - x5ny1)
      num5 = num5 * (1 - x5ny5)
      num30 = num30 * (1 - x5ny30)
#print(num1)
#print(num5)
#print(num30)
is_30 = input("Is the stock higher now than it was thirty days ago?[y/n]\n")
if is_30 == 'y':
    d30 = prob_x30
    if incdec == 'i':
      num1 = num1 * x30y1
      num5 = num5 * x30y5
      num30 = num30 * x30y30
    else:
      num1 = num1 * x30ny1
      num5 = num5 * x30ny5
      num30 = num30 * x30ny30
else:
    d30 = 1 - prob_x30
    if incdec == 'i':
      num1 = num1 * (1 - x30y1)
      num5 = num5 * (1 - x30y5)
      num30 = num30 * (1 - x30y30)
    else:
      num1 = num1 * (1 - x30ny1)
      num5 = num5 * (1 - x30ny5)
      num30 = num30 * (1 - x30ny30)
#print(num1)
#print(num5)
#print(num30)
denom = d1 * d5 * d30

if incdec == 'i':
  num1 = num1 * prob_y1
  num5 = num5 * prob_y5
  num30 = num30 * prob_y30
  word = "be higher"
else:
  num1 = num1 * (1 - prob_y1)
  num5 = num30 * (1 - prob_y5)
  num30 = num30 * (1 - prob_y30)
  word = "be lower"

ratio1 = num1 / denom
ratio5 = num5 / denom
ratio30 = num30 / denom
print("\n\n\n\nYour predictions are:\n")

print("I am " + str(ratio1 * 100) + "% confident the stock will " + word + " in 1 day.")
print("I am " + str(ratio5 * 100) + "% confident the stock will " + word + " in 5 days.")
print("I am " + str(ratio30 * 100) + "% confident the stock will " + word + " in 30 days.")
