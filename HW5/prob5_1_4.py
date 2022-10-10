#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def A(n):
    return 1/(4*n**2 - 1) 


fig,ax = plt.subplots(nrows=1,ncols=1,figsize=(7,5))

x  = np.linspace(0,np.pi,100)
f1 = np.abs(np.sin(x))
ax.plot(x,f1,'k--',label=r'$x^{2}$')

f = 2/np.pi + np.zeros(len(x))
for m in range(1,5):
    f += 4/np.pi*A(m)*np.cos(m*x)
    ax.plot(x,f,label=r'$S_{%d}$'%m)

ax.set_xlabel(r'$x$',size=20)
ax.set_ylabel(r'$y$',size=20)
ax.legend(fontsize=15)
#fig.savefig('prob5_1_4.pdf',bbox_inches='tight')
plt.show()


