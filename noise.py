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


def cal_F(snr_i=0, snr_o=0, Te=0):
    """Calculate the noise figure based on either signal to noise ratios or
        noise temperatures. Provide either/or, but not both, default is SNR.
        For temperature based calculation, assumption is input terminal is
        at standard T0=290K

    Args:
        snr_i (float): Signal to Noise (SNR) ratio of input
        snr_o (float): Signal to Noise (SNR) ratio of output
        Te (float): Noise temperature (K)

    Returns:
        float: Noise Figure F
    """
    if snr_i is not 0:
        return snr_i/snr_o
    else:
        return 1+Te/290


def cal_NF(snr_i_db, snr_o_db):
    return snr_i_db - snr_o_db