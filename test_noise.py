import noise
import pytest 

def test_thermal_noise():
    assert noise.thermal_noise(100,1e5,10) - 0.405677e-6 < 1e-9

def test_noise_figre():
    assert noise.cal_F(30,10) == 3.0
    assert noise.cal_F(Te=890) == pytest.approx(4.0689,rel=1e-4)
