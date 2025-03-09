


from scipy.io import loadmat
import numpy as np



exposure_time = loadmat("data/camera_snr/exposure_time.mat")["StatsTime"].flatten()
signal = loadmat("data/camera_snr/mean_count.mat")["StatsMean"].flatten()
noise = loadmat("data/camera_snr/std_dev.mat")["StatsStd"].flatten()


snr = signal / noise


assert exposure_time.shape == signal.shape == noise.shape



signal_pred = np.geomspace(np.min(signal), np.max(signal), 1000)
snr_shot_noise_pred = np.sqrt(signal_pred)


read_noise = 5
snr_read_noise_pred = signal_pred / read_noise



if __name__ == "__main__":

    import matplotlib.pyplot as plt


    plt.figure("SNR_vs_signal")
    plt.loglog(signal, snr, marker="x", label="Camera performance")
    plt.loglog(signal_pred, snr_shot_noise_pred, linestyle=":", label="Shot noise limit")
    plt.loglog(signal_pred, snr_read_noise_pred, linestyle=":", label="Read noise limit")

    plt.xlabel("Signal [counts]")
    plt.ylabel("SNR [1]")
    plt.grid(True)
    plt.legend()

    plt.show()











