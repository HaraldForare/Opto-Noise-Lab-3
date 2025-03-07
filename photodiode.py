

import numpy as np




def print_suggested_points():
    good_led_currents = np.geomspace(0.07E-3, 55E-3, 10, endpoint=True)
    print("Suggested LED currents:")
    for i in good_led_currents:
        print(f"  {round(i * 1000, 3)} mA")

if __name__ == "__main__":
    print_suggested_points()




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






# The resistor over which we measure photodiode current
RL = 100E3




Iled_mA_Vphoto_mV_unbiased = np.array((
    (0.0697, 3.8),
    (0.141, 8.1),
    (0.308, 23.28),
    (0.674, 70.12),
    (1.356, 182.63),
    (2.869, 380.99),
    (5.702, 431),
    (12.07, 460.90),
    (27.017, 486),
    (55.3, 505)
))





Iled_mA_Vphoto_mV_biased = np.array((
    (0.0687, 3.56),
    (0.1460, 7.584),
    (0.3083, 19.95),
    (0.6408, 55.44),
    (1.3509, 154.18),
    (2.844, 398.25),
    (5.956, 950.95),
    (12.57, 2171.1),
    (27.5, 4967),
    (55.3, 9750)
))


reverse_bias_model = ExponentialModel(Iled_mA_Vphoto_mV_biased[:, 0], Iled_mA_Vphoto_mV_biased[:, 1])



# Noise is micro-volt / (sqrt(Hz))
Iled_mA_noise_N_biased = np.array((
    (0.0687, 0.047),
    (0.147, 0.051),
    (0.3083, 0.070),
    (0.646, 0.071),
    (1.355, 0.095),
    (2.8469, 0.142),
    (5.967, 0.222),
    (12.20, 0.340),
    (26.97, 0.540),
    (52.038, 0.024)
))




if __name__ == "__main__":

    import matplotlib.pyplot as plt



    plt.figure("Unbiased")
    plt.loglog(Iled_mA_Vphoto_mV_unbiased[:, 0], Iled_mA_Vphoto_mV_unbiased[:, 1], marker="x")
    plt.xlabel("LED Current [mA]")
    plt.ylabel("Resistor Voltage [mV]")
    plt.grid(True)



    plt.figure("9V Reverse Biased")
    plt.loglog(Iled_mA_Vphoto_mV_biased[:, 0], Iled_mA_Vphoto_mV_biased[:, 1], marker="x", label="Data")
    plt.loglog(
        Iled_mA_Vphoto_mV_biased[:, 0],
        reverse_bias_model.y(Iled_mA_Vphoto_mV_biased[:, 0]),
        linestyle=":",
        label="Model"
    )
    plt.xlabel("LED Current [mA]")
    plt.ylabel("Resistor Voltage [mV]")
    plt.grid(True)
    plt.legend()


    plt.figure("9V Reverse Biased Noise")
    plt.loglog(Iled_mA_noise_N_biased[:, 0], Iled_mA_noise_N_biased[:, 1], marker="x")
    plt.xlabel("LED Current [mA]")
    plt.ylabel("Noise Spectral Density [uV/sqrt(Hz)]")
    plt.grid(True)

    plt.show()


