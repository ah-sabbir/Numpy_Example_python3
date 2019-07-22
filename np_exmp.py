#This is Numpy example for practice how to create N'th list into the M'th list
# Create Multiple Array in Multiple Array
import pandas as pd
from random import randint as rand
import numpy as np
import time
clock = time.time()
list_ = [
          [
            [
              [rand(0,100) for s_l in range(5)
              ] for i in range(2)
            ] for j in range(10)
          ] 
    
       ]

df = np.array(list_)

print(df)
print("###################################################################")
print(df.max())
print("mili second : ",round(time.time() - clock,2))
