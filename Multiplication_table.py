# HC Multiplication Table 1st
import time


for i in range(1, 61):  
    for x in range(1, 61):  
        print(f"{i * x:4}", end=" ")
        time.sleep(.001)
    print()