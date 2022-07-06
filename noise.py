import math

k = 1.38e-23 # Boltzmann's Constant (J/K)

def thermal_noise(R, fH, fL, T=298):
    """Calculates the Johnson Thermal Noise in mV (RMS)

    Args:
        R (float): Resistance in Ohms
        fH (UINT): Upper Frequency Limit in Hz
        fL (UINT): Lower Frequency Limit in Hz
        T (float): Temperature in Kelvin (K) default set to 25°C

    Returns:
        float: Thermal noise in V (RMS)
    """
    return math.sqrt(4*k*T*R*(fH-fL))


def cal_F(snr_i, snr_o):
    """Calculate the noise figure

    Args:
        snr_i (float): Signal to Noise (SNR) ratio of input
        snr_o (float): Signal to Noise (SNR) ratio of output

    Returns:
        float: Noise Figure F
    """
    return snr_i/snr_o
