# usr/bin/env python
__author__ = "Sandeep kumar Nayak"
__email__ = "nayak.sandeep@rm.is.tohoku.ac.jp"
__copyright__ = "Copyright 2020, Tadokoro Lab"

import matplotlib.pyplot as plt
import seaborn as sns;
sns.set()
import numpy as np

def make_data(N, f=0.3, rseed=1):
    rand = np.random.RandomState(rseed)
    x = rand.randn(N)
    x[int(f * N):] += 5
    return x

x = make_data(100)
# bins = np.linspace(-5, 10, 10)
# x_d = np.linspace(-4, 8, 2000)
# density = sum((abs(xi - x_d) < 0.5) for xi in x)
#
# plt.fill_between(x_d, density, alpha=0.5)
# plt.plot(x, np.full_like(x, -0.1), '|k', markeredgewidth=1)
#
# plt.axis([-4, 8, -0.2, 8]);


from sklearn.neighbors import KernelDensity

x_d = np.linspace(-4, 8, 2000)
# instantiate and fit the KDE model
kde = KernelDensity(bandwidth=1.0, kernel='gaussian')
kde.fit(x[:, None])

# score_samples returns the log of the probability density
logprob = kde.score_samples(x_d[:, None])

plt.fill_between(x_d, np.exp(logprob), alpha=0.5) # to get back the distribution
# in we do expt(log) = sigma
plt.plot(x, np.full_like(x, -0.01), '|k', markeredgewidth=1)
plt.ylim(-0.02, 0.22)

plt.show()