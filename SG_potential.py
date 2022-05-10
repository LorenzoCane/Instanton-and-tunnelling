#from cmath import sqrt, tanh
import numpy as np
import matplotlib.pyplot as plt
import os

#Variabili globali
g = 1
tau0 = 1

#Sine Gordon potential 

q= np.linspace(-17, 17, 100000)
V = g*g*(1+np.cos(q))

fig, ax = plt.subplots()

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_ylabel('V(q)', loc='top')
ax.set_xlabel('q', loc='right')

ticks = np.arange(-5*np.pi , 5*np.pi+1 , step= np.pi)
plt.xticks(ticks, ['-5π', '-4π', '-3π' , '-2π', '-π', '0', 'π', '2π', '3π', '4π', '5π'])

plt.ylim(-0.4 , 3)
ax.plot(q,V, 'orangered')

plt.savefig(os.path.join('Sine Gordon potential.png'))

#----------------------------------------------------------------------------------------
#Single instanton

t = np.linspace(-5.5, 6.5, 10000)
q_inst = 2*np.arcsin(np.tanh((t-tau0)*g))

fig2 , ax2 = plt.subplots()

ax2.spines['left'].set_position('center')
ax2.spines['bottom'].set_position('zero')
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('left')
ax2.set_ylabel(r'q($\tau)$', loc='top')
ax2.set_xlabel(r'$\tau$', loc='right')

#plt.axhline(y=np.pi, color='gray' , linestyle='--')

ax2.plot(t, q_inst, 'orangered')

plt.savefig(os.path.join('SG_Instanton'))

#----------------------------------------------------------------------------------------
#Second derivative of the potential

V_sec = g*g*(-1+2*(np.tanh(g*(t-tau0)))**2)

figg,ax3= plt.subplots()

ax3.spines['left'].set_position('center')
ax3.spines['bottom'].set_position('zero')
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')
ax3.xaxis.set_ticks_position('bottom')
ax3.yaxis.set_ticks_position('left')
ax3.set_ylabel(r'V"($\tau)$', loc='top')
ax3.set_xlabel(r'$\tau$', loc='right')

ax3.plot(t, V_sec , 'orangered')

plt.savefig(os.path.join('SG_pot_secondder.png'))