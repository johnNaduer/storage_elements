
# Python program to demonstrate
# sys.argv
  
  
import sys
  
add = 0
  
# Getting the length of command
# line arguments
n = len(sys.argv)
  
for i in range(1, n):
    add += int(sys.argv[i])
  
print ("the sum is :", add)
