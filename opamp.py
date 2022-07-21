from cmath import sqrt
import noise

class OpAmp:
    def __init__(self, Vdd, Vss, gain, specs):
        self.vdd = Vdd
        self.vss = Vss
        self.gain = gain
        self.vdd_max = specs["vdd_max"]
        self.vin_max = specs["vin_max"]
        self.vdd_max = specs["vdd_max"]
        self.i_max = specs["i_max"]
        self.slew = specs["slew"]
        self.gbp = specs['gbp']
        self.en = specs["en"] # spectral noise density

    def cal_output(self, vin):
        return self.gain*vin

    def cal_snr_input(self, pin, bw, Rin=50):
        return pin / (self.en*sqrt(bw))^2/Rin