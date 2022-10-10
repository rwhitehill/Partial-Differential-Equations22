#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def A(n):
    return 4*(-1)**n/(np.pi**2*n**2)


fig,ax = plt.subplots(nrows=1,ncols=1,figsize=(7,5))

x  = np.linspace(0,1)
f1 = x**2 
ax.plot(x,f1,'k--',label=r'$x^{2}$')

f = 1/3 + np.zeros(len(x))
for m in range(1,5):
    f += A(m)*np.cos(m*np.pi*x)
    ax.plot(x,f,label=r'$S_{%d}$'%m)

ax.set_xlabel(r'$x$',size=20)
ax.set_ylabel(r'$y$',size=20)
ax.legend(fontsize=15)
fig.savefig('prob5_1_2b.pdf',bbox_inches='tight')
#plt.show()


