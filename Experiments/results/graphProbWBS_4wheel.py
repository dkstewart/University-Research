import matplotlib.pyplot as plt
import csv
import os.path
#print os.getcwd()

x1 = []
y1 = []
x2 = []
y2 = []

userhome = os.path.expanduser('~')
csvfileNominal= os.path.join(userhome, 'git/dkstewart/University-Research/Experiments', 'probWBS_4wheelMonoData.csv')
csvfileFault= os.path.join(userhome, 'git/dkstewart/University-Research/Experiments', 'probWBS_4wheelCompData.csv')

with open(csvfileNominal,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x1.append(float(row[0]))
        y1.append(float(row[1]))

with open(csvfileFault,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x2.append(float(row[0]))
        y2.append(float(row[1]))
        
plt.scatter(x1, y1, label= "Monolithic Analysis", color= "blue", marker= "x", s=30)
plt.scatter(x2, y2, label= "Compositional Analysis", color= "red", marker= "x", s=30) 
  
# naming the x axis 
plt.xlabel('Probability Threshold') 
# naming the y axis 
plt.ylabel('Time in Seconds')
plt.xscale("log")
#plt.ticklabel_format(axis="x", style="sci", scilimits=(-12,-1))
plt.xlim([-0.01, 0.0000000001])
# show a legend on the plot 
plt.legend(loc="upper left") 
plt.show() 
