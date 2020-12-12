# This is to extract the timing from both ivc benchmarks and granularity benchmarks
__author__ = "Danielle Stewart"
__date__ = "June 2020"

import xml.etree.cElementTree as ET
import os, glob, sys, shelve, shutil, csv
from operator import itemgetter

IVC_RESULTS_DIR = 'all_ivcs_results_eg_small'  
GRAN_RESULTS_DIR = 'gran_ivcs_results'

MINED_DIR = 'mined'

if not os.path.exists(IVC_RESULTS_DIR):
    print(IVC_RESULTS_DIR + " does not exist!")
    sys.exit(-1)
if not os.path.exists(GRAN_RESULTS_DIR):
    print(GRAN_RESULTS_DIR + " does not exist!")
    sys.exit(1)

if not os.path.exists(MINED_DIR):
    os.mkdir(MINED_DIR)

#
# Open csv file for write
#
csv_out = open('time_comparison.csv', 'w')
csvwriter = csv.writer(csv_out)

#
# Iterate through xml files in IVC_RESULTS_DIR and GRAN_RESULTS_DIR
#
ivctime = []
grantime = []
for ivcname in os.listdir(IVC_RESULTS_DIR):
    for granname in  os.listdir(GRAN_RESULTS_DIR):
        if ivcname == granname:
	    #print(os.path.join(IVC_RESULTS_DIR, ivcname))
	    #print(os.path.join(GRAN_RESULTS_DIR, granname))
	    ivctree = ET.parse(os.path.join(IVC_RESULTS_DIR, ivcname))
	    grantree = ET.parse(os.path.join(GRAN_RESULTS_DIR, granname))	    
	    for elem in ivctree.iter(tag = 'Runtime'):
		ivctime.append(float(elem.text))
	    for elem in grantree.iter(tag = 'Runtime'):
                grantime.append(float(elem.text))
		if float(elem.text) == 26.776:
		    print(os.path.join(GRAN_RESULTS_DIR, granname))

#
# Save timing to csv file
#
for i in range(len(ivctime)):
    row = []
    row.append(ivctime[i])
    row.append(grantime[i])
    csvwriter.writerow(row)

csv_out.close()



