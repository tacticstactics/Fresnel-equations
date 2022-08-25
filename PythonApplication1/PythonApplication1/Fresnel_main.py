

#Fresnel_main.py


import numpy as np
import matplotlib.pyplot as plt

import Fresnel_def

param = 0.001
m = 512

aoicol, PTscol, PRscol, PTpcol, PRpcol = Fresnel_def.proc1(param,m)

print('')
print('Etalon_Phase_main.py')
print('')

fig = plt.figure(figsize = (10,6), facecolor='lightblue')


ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2, sharey=ax1)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4, sharey=ax3)

ax1.plot(aoicol,PTscol)
ax2.plot(aoicol,PRscol)
ax3.plot(aoicol,PTpcol)
ax4.plot(aoicol,PRpcol)

#ax3.plot(wlcol,np.real(Signalcol))


plt.show()