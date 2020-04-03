import numpy as np
import matplotlib.pyplot as plt
from normal_distribution import *

mean=10
variance=100
x=np.arange(-50, 50, 0.01)
xp=0

nd=normal_distribution(x, mean, variance)

plt.figure()
plt.plot(nd.x, nd.pdf)
plt.xlabel('x')
plt.ylabel('PDF')
plt.show

plt.figure()
plt.plot(nd.x, nd.cdf)
plt.xlabel('x')
plt.ylabel('CDF')
plt.show

p=nd.p(xp)
print('probability of ' + str(xp) + ': ' + str(p))