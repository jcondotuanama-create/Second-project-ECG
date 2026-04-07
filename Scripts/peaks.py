from plot import PlotECG

class DetecPeaks(PlotECG):
    def __init__(self, signal, fs):
        super().__init__(signal, fs)
    