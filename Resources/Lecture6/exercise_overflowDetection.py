import sys
import scipy.optimize as op
import numpy as np
MAX=sys.float_info.max

def average(X):
     x=X[0]
     y=X[1]
     averageResult = (x+y)/2.0
     return averageResult

def average_I(X):
     x=X[0]
     y=X[1]
     averageResult = (x+y)/2.0
     #r =  0 if averageResult>MAX else np.abs(averageResult - MAX)
     r = 0  if averageResult > MAX else np.abs(np.log(averageResult)-np.log(MAX))     
     return averageResult, r

def R(X):
     averageResult,r = average_I(X)
     return r

     
# #################
if __name__=="__main__":

     print (op.basinhopping(R,[1,1], niter=100,stepsize=1e2, minimizer_kwargs={'method':'nelder-mead'}))

#x: array([9.04808581e+307, 9.04808581e+307])



















































































# To make above work, one can change r = ... as follows

# r = 0 if averageResult > MAX else np.abs(np.log(averageResult)-np.log(MAX))
