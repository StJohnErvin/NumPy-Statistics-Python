import numpy as np
import array as arr
from scipy import stats

f_usage = [5,4,3,5,8,2,5,2,5,8,10,8,7,9,10,5,7,5,7,5,4,3,5,8,4]

def display_stat():
    print("Mean : ",mean)
    print("Mode : ",mode)
    print("Median : ",median)
    print("Range : ",srange)
    print("Population Variance : ",pvariance)
    print("Population Standard Deviation : ",pstdev)
    print("Variance : ",variance)
    print("Standard Deviation : ",stdev)
    
mean = np.mean(f_usage)
median = np.median(f_usage)
pvariance = round(np.var(f_usage),2)
stdev = round(np.std(f_usage),2)

srange = np.ptp(f_usage)
mode = stats.mode(f_usage)

sample_data = arr.array('i',f_usage)
dataset = sample_data[0:5]
f_usage_s = dataset.tolist()

variance = round(np.var(f_usage_s,ddof=1),2)
stdev = round(np.std(f_usage_s,ddof=1))
