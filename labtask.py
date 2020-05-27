from math import sin, pi
from random import random
from time import time

import matplotlib.pyplot as plt

from Lab_01.lab1 import n, wmax, N


def generate_signal(n, wmax, t, A, phi):
    point = 0
    for i in range(n):
        w = wmax / n * (i + 1)
        point += A[i] * sin(w * t + phi[i])

    return point


def generate_random_values(n):
    A = [random() for _ in range(n)]
    phi = [2 * pi * random() for _ in range(n)]

    return A, phi


def expected_value(N, signal):
    return sum(signal) / N


def variance(N, signal, M):
    res = 0
    for i in range(N):
        res += (signal[i] - M) ** 2
    res /= (N - 1)

    return res


def auto_correlation(N, signal, M, D):
    correlation = []
    for tau in range(N):
        res = 0
        for t in range(N):
            res += (signal[t] - M) * (signal[t + tau] - M)
        correlation.append(res / (N - 1) * D)

    return correlation


def cross_correlation(N, signalx, signaly, Mx, My):
    correlation = []
    for tau in range(N):
        res = 0
        for t in range(N):
            res += (signalx[t] - Mx) * (signaly[t + tau] - My)
        correlation.append(res / (N - 1))

    return correlation


def show_res(N, half, x, Rxx, y, Ryy, Rxy, Rzz):
    # fig, (ax1, ax2, ax6, ax3, ax4, ax7, ax5) = plt.subplots(7, 1, sharex='all')
    # fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, 1, sharex='all')
    fig, (ax3, ax5) = plt.subplots(2, 1, sharex='all')

    #ax1.plot(list(range(N)), x)
    #ax1.set_xlim([0, half])
    #ax1.set_ylabel('x(t)')

    # ax2.bar(list(range(half)), Rxx, color=(0, 0, 0, 1))
    # ax2.set_ylabel('Rxx')
    # ax6.acorr(x, usevlines=True, normed=True, maxlags=128, lw=2)
    # ax6.set_ylabel('Rxx\'')

    # ax3.plot(list(range(2 * N)), y, "green")
    # ax3.set_ylabel('y(t)')
    ax3.bar(list(range(half)), Rzz, color=(0, 0.7, 1, 1))
    ax3.set_ylabel('Rzz')

    # ax4.bar(list(range(half)), Ryy, color=(0, 0.7, 1, 1))
    # ax4.set_ylabel('Ryy')
    # ax7.acorr(y, usevlines=True, normed=True, maxlags=128, lw=2)
    # ax7.set_ylabel('Ryy\'')

    ax5.plot(list(range(2 * half)), Rxy, "red")
    ax5.set_ylabel('Rxy')

    plt.show()


if __name__ == '__main__':
    Nlst = [2048, 3072, 4096]
    for N in Nlst:
        half = int(N / 2)

        Ax, phix = generate_random_values(n)
        Ay, phiy = generate_random_values(n)
        Az, phiz = generate_random_values(n)

        x = [generate_signal(n, wmax, t, Ax, phix) for t in range(N)]
        y = [generate_signal(n, wmax, t, Ay, phiy) for t in range(N)]
        z = [generate_signal(n, wmax, t, Az, phiz) for t in range(N)]
        for i in range(N):
            y.append(0)

        Mx = expected_value(N, x)
        My = expected_value(N, y)
        Mz = expected_value(N, z)

        Dx = variance(N, x, Mx)
        Dy = variance(N, y, My)
        Dz = variance(N, z, Mz)

        Rxx = auto_correlation(half, x, Mx, Dx)
        Ryy = auto_correlation(half, y, My, Dy)

        start_cross = time()
        Rxy = cross_correlation(N, x, y, Mx, My)
        end_cross = time()
        print('Cross-correlation: {}'.format(end_cross - start_cross))

        start_auto = time()
        Rzz = auto_correlation(half, z, Mz, Dz)
        end_auto = time()
        print('Auto-correlation: {}'.format(end_auto - start_auto))

        show_res(N, half, x, Rxx, y, Ryy, Rxy, Rzz)
        print()
