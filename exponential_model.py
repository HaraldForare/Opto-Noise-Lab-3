

import numpy as np


class ExponentialModel:
    def __init__(self, X, Y):
        X_log = np.log2(X)
        Y_log = np.log2(Y)
        self.p = np.polyfit(X_log, Y_log, 1)


    def y(self, x):
        x_log = np.log2(x)
        y_log = np.polyval(self.p, x_log)
        y = np.exp2(y_log)
        return y

