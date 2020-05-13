from math import sin, pi
import matplotlib.pyplot as plt 
import random
import numpy

def x(t, A, phi ):
    return sum(A[i]*sin(partial_frequency[i] * t + phi[i]) for i in range(n))

N = 256
n = 8
frequency = 1100

Ax   = [random.random() for _ in range(n)]
phix = [random.uniform(0, 2*pi) for _ in range(n)]

Ay   = [random.random() for _ in range(n)]
phiy = [random.uniform(0, 2*pi) for _ in range(n)]

partial_frequency = [frequency/n * (i+1) for i in range(n)]

x_result = [x(i,Ax,phix) for i in range(N)]
y_result = [x(i, Ay, phiy) for i in range(N)]

Mx = sum(x_result)/N
Dx = sum((x_result[i] - Mx)**2 for i in range(N))/(N-1)

My = sum(y_result)/N
Dy = sum((y_result[i] - My)**2 for i in range(N))/(N-1)

half = int(N/2)
Rxx = [sum((x(t, Ax, phix)-Mx)*(x(t+tau, Ax, phix)-Mx) for t in range(N))/((N-1)*Dx) for tau in range(half)]
Ryy = [sum((x(t, Ay, phiy)-My)*(x(t+tau, Ay, phiy)-My) for t in range(N))/((N-1)*Dy) for tau in range(half)]
Rxy = [sum((x(t, Ax, phix)-Mx)*(x(t+tau, Ay, phiy)-My) for t in range(N))/(N-1) for tau in range(half)]

fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(7, 1, sharex=True)

ax1.plot(list(range(N)), x_result)
ax1.set_xlim([0, half])
ax1.set_title('Mx = {}, Dx = {}'.format(Mx, Dx))
ax1.set_ylabel('x(t)')

ax2.bar(list(range(half)), Rxx, color=(0, 0, 0, 1))
ax2.set_ylabel('Rxx')


ax3.plot(list(range(N)), y_result, "green")
ax3.set_ylabel('y(t)')

ax4.bar(list(range(half)), Ryy, color=(0,0.7,1, 1))
ax4.set_ylabel('Ryy')

ax5.plot(list(range(half)), Rxy, "red")
ax5.set_ylabel('Rxy')

ax6.acorr(x_result, usevlines=True, normed=True, maxlags= 128, lw=2)
ax7.acorr(y_result, usevlines=True, normed=True, maxlags= 128, lw=2)
ax7.set_xlabel('My = {}, Dy = {}'.format(My, Dy))
plt.show()

