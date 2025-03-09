


from scipy.io import loadmat


exposure_time = loadmat("data/camera_snr/exposure_time.mat")["StatsTime"].flatten()
signal = loadmat("data/camera_snr/mean_count.mat")["StatsMean"].flatten()
error_std_dev = loadmat("data/camera_snr/std_dev.mat")["StatsStd"].flatten()


snr = signal / error_std_dev


assert exposure_time.shape == signal.shape == error_std_dev.shape






if __name__ == "__main__":

    import matplotlib.pyplot as plt


    plt.figure("SNR_vs_signal")
    plt.loglog(snr, signal, marker="x")
    plt.xlabel("Signal [counts]")
    plt.ylabel("SNR [1]")
    plt.grid(True)

    plt.show()











