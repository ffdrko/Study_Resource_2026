# Experiment - 1 using glob
# glob is a module in Python that 
# finds all the pathnames matching 
# a specified pattern according to 
# the rules used by the Unix shell, 
# although results are returned in arbitrary order.


import glob

myfiles =glob.glob("File/*.txt")

for file in myfiles:
    print(file.strip("File\\"))