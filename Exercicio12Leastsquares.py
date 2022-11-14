# Least squares solving
# y = m x + c
# y0 = m x0 + c
# y1 = m x1 + c
# y2 = m x2 + c
# y3 = m x3 + c
# equivalent to A p = y
# with
# A = [x0 1
#      x1 1
#      x2 1
#      x3 1]
#  p = [m
#       c]
import numpy as np
from scipy.linalg import lstsq as scipy_lstsq
import matplotlib.pyplot as plt
from numpy.random import default_rng

rng = default_rng(1)

x = np.array(range(5))
m = 0.5
c = 1
y = m * x + c
noise_std = 0.1
noise = rng.standard_normal(len(y)) * noise_std
y_with_noise = y + noise


A = np.vstack([x, np.ones(len(x))]).T
solution, residuals, rank, s = np.linalg.lstsq(A, y_with_noise)
m_est, c_est = solution
solution_scipy, residuals_scipy, rank_scipy, s_scipy = scipy_lstsq(A, y_with_noise, lapack_driver='gelsy')  # lapack_driver choices: 'gelsd', 'gelsy', 'gelss'
m_est_scipy, c_est_scipy = solution_scipy

plt.plot(x, y, 'ko', label='Original data', markersize=10)
plt.plot(x, y, 'k')
plt.plot(x, y_with_noise, 'rx', label='Noisy data', markersize=10)
plt.plot(x, y_with_noise, 'r')
plt.plot(x, m_est*x + c_est, 'b*', label='Fitted line', markersize=5)
plt.plot(x, m_est*x + c_est, 'b')
plt.plot(x, m_est_scipy*x + c_est_scipy, 'c*', label='Fitted line (Scipy)', markersize=5)
plt.plot(x, m_est_scipy*x + c_est_scipy, 'c')
plt.legend()
plt.show()

