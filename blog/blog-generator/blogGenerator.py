# write the index files directly
#
# Rajesh Singh
# 20140817
#

import os,  sys
import numpy as np

A0 = sys.argv[1] # index.html file
A1 = sys.argv[2] # first few lines of the template
A2 = sys.argv[3] # html of ipython notebook file

f1 = open( '%s'%(A1), 'r')   # read from the first file
f2 = open( '%s'%(A2), 'r')   # read from the second file

template    = f1.readlines()
lines_write = f2.readlines()
#side_bar    = f3.readlines()


f0 = open( '%s'%(A0), 'w')   # open the index.html to be written
f0.writelines(template)
f0.writelines(lines_write)
#f0.writelines(side_bar)
f0.close()
