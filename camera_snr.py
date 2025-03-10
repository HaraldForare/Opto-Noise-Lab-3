


from scipy.io import loadmat
import numpy as np


resolution = 1000

exposure_time = loadmat("data/camera_snr/exposure_time.mat")["StatsTime"].flatten()
signal = loadmat("data/camera_snr/mean_count.mat")["StatsMean"].flatten()
noise = loadmat("data/camera_snr/std_dev.mat")["StatsStd"].flatten()


snr = signal / noise


assert exposure_time.shape == signal.shape == noise.shape



signal_pred = np.geomspace(np.min(signal), np.max(signal), resolution)
snr_shot_noise_pred = np.sqrt(signal_pred)


read_noise = 5
snr_read_noise_pred = signal_pred / read_noise



eq_shot_and_read_index = np.argmin(np.abs(snr_read_noise_pred - snr_shot_noise_pred))
eq_shot_and_read_signal = signal_pred[eq_shot_and_read_index]




exposure_time_pred = np.geomspace(np.min(exposure_time), np.max(exposure_time), resolution)



if __name__ == "__main__":

    print(f"Shot and read noise is equal when the signal is {eq_shot_and_read_signal} counts")



    import matplotlib.pyplot as plt


    plt.figure("SNR_vs_signal")
    plt.loglog(signal, snr, marker="x", label="Camera performance")
    plt.loglog(signal_pred, snr_shot_noise_pred, linestyle=":", label="Shot noise limit")
    plt.loglog(signal_pred, snr_read_noise_pred, linestyle=":", label="Read noise limit")

    plt.axvline(eq_shot_and_read_signal, linestyle=":", label="Equal read and shot noise")

    plt.xlabel("Signal [counts]")
    plt.ylabel("SNR [1]")
    plt.grid(True)
    plt.legend()


    plt.figure("SNR_vs_exposure_time")
    plt.loglog(exposure_time, snr, marker="x")
    plt.xlabel("Exposure time [s]")
    plt.ylabel("SNR [1]")
    plt.grid(True)
    #plt.legend()



    plt.figure("signal_vs_exposure_time")
    plt.loglog(exposure_time, signal, marker="x")
    plt.grid()

    plt.show()











