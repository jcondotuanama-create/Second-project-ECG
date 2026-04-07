import matplotlib.pyplot as plt
import wfdb as wf
import pandas as pd
###Path to the ECG DATA. 
Data_path = "C:\\Users\\jm635\\OneDrive\\Desktop\\Projects\\Second-project-ECG\\Data\\104"
#####Read the ECG data using wfdb
record = wf.rdrecord(Data_path)

###Extract the signal and the sampling frequency
signals = record.p_signal
sampling_frequency = record.fs
print("Sampling frequency:", sampling_frequency)
print("Signal shape:", signals.shape)
print("Duration of ECG (seconds):", signals.shape[0] / sampling_frequency)