from math import sin
import matplotlib.pyplot as plt 
import random

def x(t):
    return sum(A[i]*sin(partial_frequency[i] * t + phi[i]) for i in range(n))

N = 256
n = 10
frequency = 2700
A = [random.randint(10, 15) for i in range(n)]
phi = [random.randint(10, 15) for i in range(n)]

partial_frequency = [frequency/n * (i+1) for i in range(n)]
x_result = [x(i) for i in range(N)]

Mx = sum(x_result)/N
Dx = sum((x_result[i] - Mx)**2 for i in range(N))/(N-1)

fig, graphic = plt.subplots()
graphic.plot(list(range(N)), x_result)
graphic.set_title('Mx = {}\n Dx = {}'.format(Mx, Dx))
graphic.set_xlabel('N = {}'.format(N))
graphic.set_ylabel('x(t)')
plt.show()

