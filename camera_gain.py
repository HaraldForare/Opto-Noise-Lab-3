



import matplotlib.pyplot as plt


from scipy.io import loadmat
import numpy as np

from exponential_model import *



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
        self.assert_equal_shape()
        return self.signal / self.noise


    def index(self):
        self.assert_equal_shape()
        return np.arange(len(self.signal))


    def keep(self, indices):
        self.signal = self.signal[indices]
        self.noise = self.noise[indices]
        self.exposure_time = self.exposure_time[indices]
        self.assert_equal_shape()





series = [Series(path) for path in (
    "data/camera_gain_0/data.mat",
    "data/camera_gain_25/matlab.mat",
    "data/camera_gain_80/data.mat"
)]


# Remove saturated outlier
series[0].keep(series[0].index()[:-1])



S_all = np.concatenate([s.signal for s in series])
T_all = np.concatenate([s.exposure_time for s in series])


t_pred = np.array((np.min(T_all), np.max(T_all)))
s_pred = np.array((np.min(S_all), np.max(S_all)))
n_pred = np.sqrt(s_pred)


if __name__ == "__main__":




    plt.figure("snr_vs_time_different_gain")

    plt.loglog(series[0].exposure_time, series[0].snr(), label="Gain 0", marker="x")
    plt.loglog(series[1].exposure_time, series[1].snr(), label="Gain 25", marker="o")
    plt.loglog(series[2].exposure_time, series[2].snr(), label="Gain 80", marker="*")

    plt.loglog(t_pred, n_pred, linestyle=":", label="Shot noise limit (gain 0)")

    plt.xlabel("Exposure Time (s)")
    plt.ylabel("Signal to Noise Ratio (1)")

    plt.grid(True, which="both")
    plt.legend()
    plt.show()

