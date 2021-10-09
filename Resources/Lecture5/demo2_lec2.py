import numpy as np
import scipy.optimize as op

########## The function "mcmc" wraps Scipy's Baishopping. Probably it
########## does not need to change for the exercises. 

def mcmc(func,  niter=50, start_point=0, method='powell'):
    tol=1e-16
    def callback_global(x,f,accepted):
        conclusion= 'good!' if f<tol else "not good enough"
        print("MCMC Sampling:: At x=%.10f,  f=%g,  ==> %s" % (x,f,  conclusion))
        
    op.basinhopping(func,start_point,callback=callback_global,minimizer_kwargs={'method':'powell'},niter=niter)

####################### This part should change following different functions.

def FOO(x):
    if x < 1.0:
        y= x + 1
        if y>=2: raise Exception ("UNEXPECTED! Input %.17f" %x)


            
def FOO_I(x):
    r = 1
    r *= (x-1.0)**2
    if x < 1.0:
        y= x + 1
        r *= (y-2)**2
        if y>=2: raise Exception ("UNEXPECTED! Input %.17f" %x)
    return r

def R(x):
    r=FOO_I(x)
    return r


if __name__=="__main__":
    
    mcmc(R,5000)
