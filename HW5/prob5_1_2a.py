#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def A(n):
    return 2*((2 - np.pi**2*n**2)*(-1)**n - 2)/(np.pi**3*n**3)


fig,ax = plt.subplots(nrows=1,ncols=1,figsize=(7,5))

x  = np.linspace(0,1)
f1 = x**2 
ax.plot(x,f1,'k--',label=r'$x^{2}$')

f = np.zeros(len(x))
for m in range(1,5):
    f += A(m)*np.sin(m*np.pi*x)
    ax.plot(x,f,label=r'$S_{%d}$'%m)

ax.set_xlabel(r'$x$',size=20)
ax.set_ylabel(r'$y$',size=20)
ax.legend(fontsize=15)
fig.savefig('prob5_1_2a.pdf',bbox_inches='tight')
#plt.show()


