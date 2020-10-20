
import os

#Define Variables
filename="haneef.txt"
person="Mr. Haneef"


# Do not edit below this line
out1="#######   Hello ""+person+  #########"
file1 = open(filename,"r+")
out2=file1.read()
file1.close() 
##### output is below this line
print("")
print(out1)
print("")
print("Output of Read function is ")
print("")
print(out2)
print("")
print("")
##Note that all output is available at out1 and out2
