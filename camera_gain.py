



import matplotlib.pyplot as plt


from scipy.io import loadmat
import numpy as np

from exponential_model import *


resolution = 100


class Series:
    def __init__(self, path):
        data = loadmat(path)

        self.signal = data["StatsMean"].flatten()
        self.noise = data["StatsStd"].flatten()
        self.exposure_time = data["StatsTime"].flatten()

        self.assert_equal_shape()

    def assert_equal_shape(self):
        assert self.signal.shape == self.noise.shape == self.exposure_time.shape


    def snr(self):
        return self.signal / self.noise

    def index(self):
        return np.arange(len(self.signal))

    def keep(self, indices):
        self.signal = self.signal[indices]
        self.noise = self.noise[indices]
        self.exposure_time = self.exposure_time[indices]
        self.assert_equal_shape()



# X and Y have a linear relationship but they are logarithmically spaced
class LogLogModel:
    def __init__(self, X, Y):
        assert X.shape == Y.shape
        assert len(X.shape) == 1

        X_log = np.log2(X)
        Y_log = np.log2(Y)

        self._P_log = np.polyfit(X_log, Y_log, 1)

    def y(self, x):
        return np.exp2(np.polyval(self._P_log, x))





series = [Series(path) for path in (
    "data/camera_gain_0/data.mat",
    "data/camera_gain_25/matlab.mat",
    "data/camera_gain_80/data.mat"
)]


series[0].keep(series[0].index()[:-1])






if __name__ == "__main__":




    plt.figure("snr_vs_time_different_gain")

    plt.loglog(series[0].exposure_time, series[0].snr(), label="Gain 0", marker="x")
    plt.loglog(series[1].exposure_time, series[1].snr(), label="Gain 25", marker="o")
    plt.loglog(series[2].exposure_time, series[2].snr(), label="Gain 80", marker="*")



    plt.grid(True)
    plt.legend()
    plt.show()

