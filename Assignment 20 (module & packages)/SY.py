"""1. create a package “SY” which has class SYMARKS (Computer Total,
MathsTotal, ElectronicsTotal)."""
class SYMARKS:
    def __init__(self, comp, maths, elec):
        self.comp = comp
        self.maths = maths
        self.elec = elec

    def Computer_Total(self):
        return self.comp

    def Maths_Total(self):
        return self.maths

    def Electronic_Total(self):
        return self.elec
