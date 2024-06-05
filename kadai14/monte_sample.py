import multiprocessing
import random
import sys
import time

def sampling(num):
    cnt = 0
    for i in range(num):
        x = random.random()
        y = random.random()
        calc =x**2+y**2 
        
        if calc < 1:
            cnt+=1
            
    
    return cnt

if __name__ == "__main__":
    bgn = time.time()
    
    total = 100000000

    pl = multiprocessing.Pool(int(sys.argv[1]))   
    
    num = int(total/1000)
    nums = [num for _ in range(1000)]
    result = pl.map(sampling,nums)
    end=time.time()
    calc1 =sum(result)
    print(f"{calc1*4}/{total}={calc1/total*4}")
    print(f"所要時間:{end-bgn:.2f}")
    
