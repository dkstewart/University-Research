import matplotlib.pyplot as plt
import csv
import os.path
#print os.getcwd()

x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []



userhome = os.path.expanduser('~')
csvfileNominal= os.path.join(userhome, 'git/dkstewart/University-Research/Experiments/results', 'nominalDataComp.csv')
csvfileFault= os.path.join(userhome, 'git/dkstewart/University-Research/Experiments/results', 'faultDataComp.csv')
csvfileExtended= os.path.join(userhome, 'git/dkstewart/University-Research/Experiments/results', 'extendedDataComp.csv')

with open(csvfileNominal,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x1.append(int(row[0]))
        y1.append(float(row[1]))

with open(csvfileFault,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x3.append(int(row[0]))
        y3.append(float(row[1]))

with open(csvfileExtended,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x2.append(int(row[0]))
        y2.append(float(row[1]))
        
plt.scatter(x1, y1, label= "Nominal Model Analysis", color= "green", marker= "x", s=30)
plt.scatter(x2, y2, label= "Extended Model Analysis", color= "blue", marker= "x", s=30) 
plt.scatter(x3, y3, label= "Fault Model Analysis", color= "red", marker= "x", s=30)

  
# naming the x axis 
plt.xlabel('Models') 
# naming the y axis 
plt.ylabel('Time in Seconds') 
  
# show a legend on the plot 
plt.legend(loc="upper left") 
plt.show() 
