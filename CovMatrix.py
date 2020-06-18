import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (12, 8)

x = np.random.normal(0, 1, 500)
y = np.random.normal(0, 1, 500)
X = np.vstack((x, y)).T
print(x)

plt.scatter(X[:, 0], X[:, 1])
plt.title('Generated Data')
plt.axis('equal')
plt.show()


# calculating the covariance matrix
def cov(x, y):
    xbar, ybar = x.mean(), y.mean()
    return np.sum((x-xbar)*(y-ybar))/(len(x)-1)


def cov_mat(X):
    return np.array([[cov(X[0], X[0]), cov(X[0], X[1])],
                     [cov(X[1], X[0]), cov(X[1], X[1])]])


cov_mat(X.T)
