#import
from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
import os

#**********************************************
#Control panel 
# This code will draws: - potential and second derivative : V (q) = \lambda / 4 (q^2 - a^2)^2 (real and imaginary time)
#                                                           V_sec = 2*lam*a^22*(1-3/2*(np.cosh(a*(lam/2)^(1/2)*(t-tau0)))^(-2))
#                       - instanton : q_inst = a*np.tanh(a* (lam/2)^(1/2)*(t - tau0))
#                       - anti - instanton : q_inst = -a*np.tanh(a* (lam/2)^(1/2)*(t - tau0))



Letter_mode = True #True: the ticks on x and y axis are generic constant, no number will appear

lam = 40
a =1
omega= a*sqrt(2*lam)
tau0 = 2

FunctionColor = 'orangered' #color of the plot
SecondFunctionColor ='b'
#----------------------------------------------------------------------------------------
#Double well potential (real and imaginary time) : V (q) = \lambda / 4 (q^2 - a^2)^2



q = np.linspace(-1.5,1.5,10000)
V = lam/4 * (q**2-a**2)**2

figa, ax = plt.subplots()

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_ylabel('V(q)', loc='top')
ax.set_xlabel('q', loc='right')

if Letter_mode:
    xTicksPot = [-a , a ]
    yTicksPot = [0, a*a*lam/4]
    plt.xticks(xTicksPot, ['-a', 'a'])
    plt.yticks(yTicksPot , ['0' , r'$a^{2}\frac{\lambda}{4}$'])
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.setp( ax.yaxis.get_majorticklabels(), va="bottom" )

plt.ylim(-2 , a*a*lam/4+3)
ax.plot(q,V, FunctionColor) #real time
plt.savefig(os.path.join('Double well potential_r.png'))

figb, ax2= plt.subplots()

ax2.spines['left'].set_position('zero')
ax2.spines['bottom'].set_position('zero')
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('left')
ax2.set_ylabel('V(q)', loc='top')
ax2.set_xlabel('q', loc='right')

if Letter_mode:
    xTicksPot = [-a , a ]
    yTicksPot = [-a*a*lam/4 , 0]
    plt.xticks(xTicksPot, ['-a', 'a'])
    plt.yticks(yTicksPot , [r'$-a^{2}\frac{\lambda}{4}$', '0'])
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.setp( ax2.yaxis.get_majorticklabels(), va="top" )

plt.ylim(-a*a*lam/4-3 , 2)
ax2.plot(q, -V , SecondFunctionColor) #imaginary time


plt.savefig(os.path.join('Double well potential_im.png'))

#----------------------------------------------------------------------------------------
# Single Instanton 



t = np.linspace (-3, 7, 10000)
q_inst= a*np.tanh(a* (lam/2)**(0.5)*(t - tau0))

fig1 , ax3 = plt.subplots()

ax3.spines['left'].set_position('zero')
ax3.spines['bottom'].set_position('zero')
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')
ax3.xaxis.set_ticks_position('bottom')
ax3.yaxis.set_ticks_position('left')
ax3.set_ylabel(r'q($\tau)$', loc='top')
ax3.set_xlabel(r'$\tau$', loc='right')

if Letter_mode:
    xTicksInst = [0 ,tau0 ]
    yTicksInst = [-a , a]
    plt.xticks(xTicksInst, ['0', r'$\tau_0$'])
    plt.yticks(yTicksInst , ['-a','a'])
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.setp( ax3.xaxis.get_majorticklabels(), ha="left" )
    plt.setp( ax3.yaxis.get_majorticklabels(), va="top" )


plt.ylim(-a-0.3,a+0.3)
ax3.plot(t , q_inst, FunctionColor)
#ax3.axvspan(tau0 - 1/2/omega , tau0 + 1/2/omega , alpha = 0.5 , color = 'mediumorchid')
#plt.axhline(y=1 , color='gray' , linestyle='--')

plt.savefig(os.path.join('Instanton.png'))

#----------------------------------------------------------------------------------------
# Single anti-instanton
fig2 , ax4 = plt.subplots()

ax4.spines['left'].set_position('zero')
ax4.spines['bottom'].set_position('zero')
ax4.spines['right'].set_color('none')
ax4.spines['top'].set_color('none')
#ax4.xaxis.set_ticks_position('bottom')
ax4.yaxis.set_ticks_position('left')
ax4.set_ylabel(r'q($\tau)$', loc='top')
ax4.set_xlabel(r'$\tau$', loc='right')

if Letter_mode:
    plt.xticks(xTicksInst, ['0', r'$\tau_0$'])
    plt.yticks(yTicksInst , ['-a','a'])
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.setp( ax4.xaxis.get_majorticklabels(), ha="left" )
    plt.setp( ax4.yaxis.get_majorticklabels(), va="top" )

plt.ylim(-a-0.3,a+0.3)
ax4.plot(t , -q_inst, FunctionColor)
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

if Letter_mode:
    xTicksSec = [0 ,tau0 ]
    yTicksSec = [-lam*a**2, 2*lam*a**2]
    plt.xticks(xTicksSec, ['0', r'$\tau_0$'])
    plt.yticks(yTicksSec , [r'$-a^{2}\lambda$',r'$2a^{2}\lambda$'])
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.setp( ax5.xaxis.get_majorticklabels(), ha="left" )
    plt.setp( ax5.yaxis.get_majorticklabels(), va="bottom" )


plt.ylim(-55 , 100)

#ax5.axvspan(tau0 - 1/2/omega , tau0 + 1/2/omega , alpha = 0.5 , color = 'mediumorchid')
ax5.plot(t , V_sec1, FunctionColor)
#plt.axhline(y=1 , color='gray' , linestyle='--')

plt.savefig(os.path.join('DW_pot_secondder.png'))