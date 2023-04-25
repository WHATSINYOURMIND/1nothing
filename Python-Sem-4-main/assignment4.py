import numpy as np

def moving_average(a, n=3) :
    np.cumsum(a, dtype=float)
a[n:] = a[n:] - a[:-n] return a[n - 1:] / n
a=[3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150] 
a1=np.array(a)
 np.array(moving_average(a1,n=3)).round(2) array([ 5. , 4.67, 5.67, 6.67, 9.67, 28.67, 49.33, 72.67, 84. , 93.33, 116.33])
