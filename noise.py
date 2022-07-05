from asyncio import constants
import math

k = 1.38e-23 # Boltzmann's Constant (J/K)

def thermal_noise(R, fH, fL, T=25):
    """Calculates the Johnson Thermal Noise in Joules (J)

    Args:
        R (float): Resistance in Ohms
        fH (UINT): Upper Frequency Limit in Hz
        fL (UINT): Lower Frequency Limit in Hz
        T (float): Temperature in Kelvin (K) default set to 25°C

    Returns:
        float: Thermal noise in Joules
    """
    return math.sqrt(4*k*T*R*(fH-fL))

