import wfdb as wf

path = "C:/Users/jm635/Documents/Projects/Second-project-ECG/data/Data/104"

class ECGdata:
    def __init__(self, path):
        self.path = path
        self.record = wf.record(path)
        self.signal = self.record.p_signal
        self.samples = self.record.sig_len
    def get_signal(self):
        return self.signal
    def get_samples(self):
        return self.samples

class ECGdataConfiguration(ECGdata):
    def __init__(self, path):
        super().__init__(path)
        self.fs = self.record.fs
        self.n_sig = self.record.n_sig
        self.units = self.record.units
        self.sig_name = self.record.sig_name

    def get_fs(self):
        return self.fs
    def get_n_sig(self):
        return self.n_sig
    def get_units(self):
        return self.units
    def get_sig_name(self):
        return self.sig_name

class ECGdataCalibration(ECGdata):
    def __init__(self, path):
        super().__init__(path)
        self.adc_gain = self.record.adc_gain
        self.baseline = self.record.baseline
        self.adc_res = self.record.adc_res
    def get_adc_gain(self):
        return self.adc_gain
    def get_baseline(self):
        return self.baseline
    def get_adc_res(self):
        return self.adc_res

class ECGdataInformation(ECGdata):
    def __init__(self, path):
        super().__init__(path)
        self.name = self.record.name
        self.base_time = self.record.base_time
        self.base_date = self.record.base_date
        self.comments = self.record.comments
    def get_comments(self):
        return self.comments
    def get_name(self):
        return self.name
    def get_base_time(self):
        return self.base_time
    def get_base_date(self):
        return self.base_date