import matplotlib.pyplot as plt
import csv
import os.path
#print os.getcwd()

i1 = []
i2 = []
g1 = []
g2 = []

userhome = os.path.expanduser('~')
csvfile= os.path.join(userhome, 'git/dkstewart/University-Research/Experiments/scripts/sorted_time_comparison.csv')
with open(csvfile,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    i = 1
    for row in plots:
	i1.append(i)
        i2.append(float(row[0]))
	g1.append(i)
        g2.append(float(row[1]))
	i = i+1

plt.scatter(i1, i2, label= "IVCs", color= "blue", marker= "x", s=30)
plt.scatter(g1, g2, label= "IVCs with granularity", color= "red", marker= "o",s=30)

# naming the x axis
plt.xlabel('Models')
# naming the y axis
plt.ylabel('Time in Seconds')

# set xy range
plt.xlim(0, 56)
plt.ylim(0,40)
# show a legend on the plot
plt.legend(loc="upper left")
plt.show()
