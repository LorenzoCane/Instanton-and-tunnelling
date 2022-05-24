#import
from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
import os


#**********************************************
#Control panel 
# This code will draws: - DW Potential multiple-instantons : V (q) = \lambda / 4 (q^2 - a^2)^2 (real and imaginary time)
#                                                           V_sec = 2*lam*a^22*(1-3/2*(np.cosh(a*(lam/2)^(1/2)*(t-tau0)))^(-2))
#                       - SG multiple-instantons (adjacent minima)
#                       - anti - instanton (generic minima)
#See the other files for variable meaning



Letter_mode = True #True: the ticks on x and y axis are generic constant, no number will appear

lam = 40
a =1
omega= a*sqrt(2*lam)
tau0 = 2
N= 5 # # instantons + #anti-instantons for DW

g = 1
tau0_PP = 3
N_PP= 5 # # instantons + #anti-instantons

FunctionColor = 'orangered' #color of the plot
SecondFunctionColor ='b'

#----------------------------------------------------------------------------------------
#Double well potential multiple-instantons



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
    xTicksInst = np.arange(tau0, 10*N, step=10)
    yTicksInst = [-a ,0,  a]
    xTicksLabel = []
    for i in range(N):
        label = r'$\tau$'+ str(i+1)
        xTicksLabel.append(label)
    plt.xticks(xTicksInst, xTicksLabel)
    plt.yticks(yTicksInst , ['-a', '0', 'a'])
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.setp( ax3.xaxis.get_majorticklabels(), ha="left" )
    plt.setp( ax3.yaxis.get_majorticklabels(), va="top" )

plt.ylim(-a-0.3,a+0.3)
for i in range(N):
    t = np.linspace (-3+i*10, 7+i*10, 10000)
    q_inst= (-1)**i*a*np.tanh(a* (lam/2)**(0.5)*(t - (tau0+i*10)))
    ax3.plot(t , q_inst, FunctionColor)


plt.savefig(os.path.join('DW_Multiple-Instanton.png'))

#----------------------------------------------------------------------------------------
#Periodic Potential multiple-instantons (with  A-I order)


fig , ax = plt.subplots()

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_ylabel(r'q($\tau)$', loc='top')
ax.set_xlabel(r'$\tau$', loc='right')
if Letter_mode:
    xTicksInst = np.arange(tau0, 15*N_PP, step=15)
    yTicksInst = [-np.pi,0 , np.pi]
    xTicksLabel = []
    for i in range(N_PP):
        label = r'$\tau$'+ str(i+1)
        xTicksLabel.append(label)
    plt.xticks(xTicksInst, xTicksLabel)
    plt.yticks (yTicksInst , ['-π', '0','π'])
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.setp( ax.xaxis.get_majorticklabels(), ha="left" )
    plt.setp( ax.yaxis.get_majorticklabels(), va="top" )

#plt.ylim(-a-0.3,a+0.3)
for i in range(N_PP):
    t = np.linspace(-5+i*15, 10+i*15, 10000)
    q_inst = (-1)**i*2*np.arcsin(np.tanh((t-(tau0_PP+i*15))*g))   
    ax.plot(t , q_inst, FunctionColor)


plt.savefig(os.path.join('SG_Multiple-Instanton.png'))
