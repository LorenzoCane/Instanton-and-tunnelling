
from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
import os

#Variabili globali
path = '/home/Desktop/Università/Tesi/Pics'
lam = 40
a =1
omega= a*sqrt(2*lam)
tau0 = 1


#----------------------------------------------------------------------------------------
#Double well potential (real and imaginary time) : V (q) = \lambda / 4 (q^2 - a^2)^2



q = np.linspace(-1.5,1.5,10000)
V = lam/4 * (q**2-a**2)**2

fig, (ax, ax2) = plt.subplots(1, 2 )
fig.tight_layout()

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_ylabel('V(q)', loc='top')
ax.set_xlabel('q', loc='right')

ax2.spines['left'].set_position('center')
ax2.spines['bottom'].set_position('zero')
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('left')
ax2.set_ylabel('V(q)', loc='top')
ax2.set_xlabel('q', loc='right')

plt.ylim(-2 , 10)
ax.plot(q,V, 'orangered') #real time
plt.ylim(-12 , 2)
ax2.plot(q, -V , 'b') #imaginary time


plt.savefig(os.path.join('Double well potential.png'))

#----------------------------------------------------------------------------------------
# Single Instanton 



t = np.linspace (-4.5, 4.5 , 10000)
q_inst= a*np.tanh(a* (lam/2)**(0.5)*(t - tau0))

fig1 , ax3 = plt.subplots()

ax3.spines['left'].set_position('center')
ax3.spines['bottom'].set_position('zero')
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')
ax3.xaxis.set_ticks_position('bottom')
ax3.yaxis.set_ticks_position('left')
ax3.set_ylabel(r'q($\tau)$', loc='top')
ax3.set_xlabel(r'$\tau$', loc='right')

ax3.plot(t , q_inst, 'orangered')
#ax3.axvspan(tau0 - 1/2/omega , tau0 + 1/2/omega , alpha = 0.5 , color = 'mediumorchid')
#plt.axhline(y=1 , color='gray' , linestyle='--')

plt.savefig(os.path.join('Instanton.png'))

#----------------------------------------------------------------------------------------
# Single anti-instanton
fig2 , ax4 = plt.subplots()

ax4.spines['left'].set_position('center')
ax4.spines['bottom'].set_position('zero')
ax4.spines['right'].set_color('none')
ax4.spines['top'].set_color('none')
ax4.xaxis.set_ticks_position('bottom')
ax4.yaxis.set_ticks_position('left')
ax4.set_ylabel(r'q($\tau)$', loc='top')
ax4.set_xlabel(r'$\tau$', loc='right')

ax4.plot(t , -q_inst, 'orangered')
#plt.axhline(y=1 , color='gray' , linestyle='--')
#ax4.axvspan(tau0 - 1/2/omega , tau0 + 1/2/omega , alpha = 0.5 , color = 'mediumorchid')
plt.savefig(os.path.join('Anti-instanton.png'))

#----------------------------------------------------------------------------------------
#Second derivative of the potential
V_sec1 = 2*lam*a**2*(1-3/2*(np.cosh(a*(lam/2)**0.5*(t-tau0)))**(-2))

fig3 , ax5 = plt.subplots()

ax5.spines['left'].set_position('zero')
ax5.spines['bottom'].set_position('zero')
ax5.spines['right'].set_color('none')
ax5.spines['top'].set_color('none')
ax5.xaxis.set_ticks_position('bottom')
ax5.yaxis.set_ticks_position('left')
ax5.set_ylabel(r'V"($\tau)$', loc='top')
ax5.set_xlabel(r'$\tau$', loc='right')

plt.ylim(-55 , 100)

#ax5.axvspan(tau0 - 1/2/omega , tau0 + 1/2/omega , alpha = 0.5 , color = 'mediumorchid')
ax5.plot(t , V_sec1, 'orangered')
#plt.axhline(y=1 , color='gray' , linestyle='--')

plt.savefig(os.path.join('DW_pot_secondder.png'))