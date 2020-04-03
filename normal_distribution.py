import numpy as np
import scipy

class normal_distribution():
    def __init__(self, x, mean, variance):
        '''
        Initialise parameters
        mean
        variance
        scale
        PDF (Probability Density Function)
        CDF (Probabiity Distribution Function)

        Returns
        -------
        None.

        '''
        self.mean=mean
        self.variance=variance
        self.scale=np.sqrt(self.variance)
        self.x=x
        self.pdf=(1/self.scale*np.sqrt(2*np.pi))*np.exp(-0.5*((self.x-self.mean)/self.scale)**2)
        self.cdf=0.5*(1+scipy.special.erf((self.x-self.mean)/(self.scale*np.sqrt(2))))
        
        return
    
    def p(self, xp):
        '''
        Computes the probability of xp to happen
        '''
        return np.interp(xp, self.x, self.cdf)

