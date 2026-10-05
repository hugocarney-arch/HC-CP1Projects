# HC Multiplication Table 1st
import time

for i in range(1, 31):  
    for x in range(1, 31):  
        print(f"{i * x:4}", end="")
        time.sleep(0.001)
    print()