import matplotlib.pyplot as plt
import numpy as np

class PlotECG:
    def __init__(self, signal, fs):
        self.signal = signal
        self.fs = fs
    def plot_ecg_signal_with_samples(self):
        plt.figure(figsize = (12,8))
        for i in range(self.signal.shape[1]):
            plt.subplot(self.signal.shape[1], 1, i+1)
            plt.plot(self.signal[:, i])
            plt.title(f"Lead {i+1}")
        plt.tight_layout()
        plt.xlabel("Time (samples)")
        plt.ylabel("Amplitude (mV)")
        plt.show()

    def plot_ecg_signal_with_time(self):
        time = np.arange(len(self.signal)) / self.fs
        plt.figure(figsize = (12,8))
        for i in range(self.signal.shape[1]):
            plt.subplot(self.signal.shape[1], 1, i+1)
            plt.plot(time, self.signal[:, i])
            plt.title(f"Lead {i+1}")
        plt.tight_layout()
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude (mV)")
        plt.show()
    def plot_ecg_between_samples(self, start_time, end_time):
        start_sample = int(start_time * self.fs)
        end_sample = int(end_time * self.fs)
        plt.figure(figsize = (12,8))
        for i in range(self.signal.shape[1]):
            plt.subplot(self.signal.shape[1], 1, i+1)
            plt.plot(self.signal[start_sample:end_sample])
            plt.title(f"Lead {i+1}")
        plt.tight_layout()
        plt.xlabel("Time (samples)")    
        plt.ylabel("Amplitude (mV)")
        plt.show()
    def plot_ecg_between_time(self, start_time, end_time):
        start_sample = int(start_time * self.fs)
        end_sample = int(end_time * self.fs)
        bound_signal = self.signal[start_sample:end_sample]
        time = np.arange(len(bound_signal)) / self.fs
        plt.figure(figsize = (12,8))
        for i in range(bound_signal.shape[1]):
            plt.subplot(bound_signal.shape[1], 1, i+1)
            plt.plot(time, bound_signal[:, i])
            plt.title(f"Lead {i+1}")
        plt.tight_layout()
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude (mV)")
        plt.show()







