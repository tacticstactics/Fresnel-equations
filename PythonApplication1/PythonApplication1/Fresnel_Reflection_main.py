

#Fresnel_Reflection_main.py


import numpy as np
import matplotlib.pyplot as plt

import Fresnel_Reflection_def

param = 0.001
m = 256

theta1col, theta2col, rscol, tscol, PTscol, PRscol, PTpcol, PRpcol = Fresnel_Reflection_def.proc1(param,m)

#print('tscol')
#print(tscol)

print('')
print('Fresnel_Reflection_main.py')
print('')

fig = plt.figure(figsize = (10,6), facecolor='lightblue')


ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2, sharey=ax1)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4, sharey=ax3)



ax1.plot(theta1col,PTscol,label = "Line 1")
ax2.plot(theta1col,PRscol,label = "Line 2")
ax3.plot(theta1col,PTpcol,label = "Line 3")
ax4.plot(theta1col,PRpcol)

#ax3.plot(wlcol,np.real(Signalcol))



plt.show()

