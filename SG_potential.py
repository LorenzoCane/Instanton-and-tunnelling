#import
import numpy as np
import matplotlib.pyplot as plt
import os

#**********************************************
#Control panel 
# This code will draws: - potential and second derivative : V(q) = g^2(1+np.cos(q))
#                                                           V_sec = g^2(-1+2*(np.tanh(g*(t-tau0)))^2)
#                       - instanton : q_inst = 2*np.arcsin(np.tanh((t-tau0)*g))



Letter_mode = True #True: the ticks on x and y axis are generic constant, no number will appear

g = 1
tau0 = 3
FunctionColor = 'orangered' #color of the plot

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



if Letter_mode:
    xTicksPot = np.arange(-5*np.pi , 5*np.pi+1 , step= np.pi)
    yTicksPot = [2*g*g]
    plt.xticks(xTicksPot, ['-5π', '-4π', '-3π' , '-2π', '-π', '0', 'π', '2π', '3π', '4π', '5π'])
    plt.yticks(yTicksPot , ['g'])
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.setp( ax.xaxis.get_majorticklabels(), ha="left" )
    plt.setp( ax.yaxis.get_majorticklabels(), va="bottom" )


plt.ylim(-0.4 , (2*g*g)+1)
ax.plot(q,V, FunctionColor)

plt.savefig(os.path.join('Sine Gordon potential.png'))

#----------------------------------------------------------------------------------------
#Single instanton

t = np.linspace(-5, 10.5, 10000)
q_inst = 2*np.arcsin(np.tanh((t-tau0)*g))

fig2 , ax2 = plt.subplots()

ax2.spines['left'].set_position('zero')
ax2.spines['bottom'].set_position('zero')
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('left')
ax2.set_ylabel(r'q($\tau)$', loc='top')
ax2.set_xlabel(r'$\tau$', loc='right')

#plt.axhline(y=np.pi, color='gray' , linestyle='--')

if Letter_mode:
    yTicksInst = [-np.pi,np.pi]
    xTicksInst = [ 0, tau0]
    plt.yticks (yTicksInst , ['-π', 'π'])
    plt.xticks(xTicksInst, ['0', r'$\tau_0$'])
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.setp( ax2.xaxis.get_majorticklabels(), ha="left" )
    plt.setp( ax2.yaxis.get_majorticklabels(), va="top" )
    

ax2.plot(t, q_inst, FunctionColor)

plt.savefig(os.path.join('SG_Instanton'))

#----------------------------------------------------------------------------------------
#Second derivative of the potential

V_sec = g*g*(-1+2*(np.tanh(g*(t-tau0)))**2)

figg,ax3= plt.subplots()

ax3.spines['left'].set_position('zero')
ax3.spines['bottom'].set_position('zero')
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')
ax3.xaxis.set_ticks_position('bottom')
ax3.yaxis.set_ticks_position('left')
ax3.set_ylabel(r'V"($\tau)$', loc='top')
ax3.set_xlabel(r'$\tau$', loc='right')

if Letter_mode:
    yTicksSec = [-g, g]
    xTicksSec = [ 0, tau0]
    plt.yticks (yTicksSec , [r'$-g^2$', r'$g^2$'])
    plt.xticks(xTicksSec, ['0', r'$\tau_0$'])
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.setp( ax3.xaxis.get_majorticklabels(), ha="left" )
    plt.setp( ax3.yaxis.get_majorticklabels(), va="bottom" )

plt.ylim((-g*g)-0.3 , g*g+0.3)
ax3.plot(t, V_sec , FunctionColor)

plt.savefig(os.path.join('SG_pot_secondder.png'))