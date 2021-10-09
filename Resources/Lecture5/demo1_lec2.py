import numpy as np
import scipy.optimize as op

########## The function "mcmc" wraps Scipy's Baishopping. Probably it
########## does not need to change for the exercises. 

def mcmc(func, start_point=0, niter=500,method='powell'):
    tol=1e-16
    def callback_global(x,f,accepted):
        conclusion= 'good!' if f<tol else "not good enough"
        print("MCMC Sampling:: At x=%.10f,  f=%g,  ==> %s" % (x,f,  conclusion))
        
    op.basinhopping(func,start_point,callback=callback_global,minimizer_kwargs={'method':'powell'},niter=niter,stepsize=10)

####################### This part should change following different functions.

def FOO(x):
    if x <= 1.0:
        x= x + 1

    y = x*x    
    if y <= 4.0:
        x = x - 1
    return x

def FOO_I(x):
    r = 1

    r *= (x-1.0)**2
    if x <= 1.0:
        x= x + 1
    y = x*x
    #this one does not work: r=0 if y == 4.0 else 1
    r *= (y - 4.0)*(y - 4.0)
    if y <= 4.0:
        x = x - 1
    return (r,x)

def R(x):
    r,a=FOO_I(x)
    return r

# R(x)=0 if and only if x is a bounday input
# R(x) >= 0

if __name__=="__main__":
    mcmc(R)
