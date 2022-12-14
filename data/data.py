# I finished one extra : Use more than one data source and have my analysis compare,contrast, or correlate them.

# First data source - wind turbines
# Basic 
import csv

reader = csv.reader(open("wind_turbines.csv"))
data=[]
for row in reader:
    data.append(row)
    print(row)
  
# Look for average
height = [float(row[7]) for row in data[1:]]
def get_Height(height):
  sum_height = sum(height)
  count_height = len(height)
  average = sum_height / count_height
  return average
print("The average of total height of the turbine:", get_Height(height))

# Second data source - hydropower
# Basic 
import csv

f = csv.reader(open("hydropower.csv"))
number=[]
for row in f:
    number.append(row)
    print(row)
  
# Look for average
Structural_Height = [float(row[2]) for row in number[1:]]
def get_Height(Structural_Height):
  sum_height = sum(Structural_Height)
  count_height = len(Structural_Height)
  average = sum_height / count_height
  return average
print("The average of Structural Height:", get_Height(Structural_Height))

# Compare average of the total height of the turbines and the structural height of the hydropower

if get_Height(height) < get_Height(Structural_Height):
  print("The average of Structural Height is greater than the average of total height of the turbine")
else:
  print("The average of Structural Height is less than the average of total height of the turbine")

