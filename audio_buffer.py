import numpy as np
import soundfile as sf

class AudioBuffer:
    def __init__(self) -> None:
        self.samples = None
        self.sample_rate = 0
        self.file_name = "None"
        self.bit_depth = 0
    
    def load_from(self, file_path):
        self.samples, self.sample_rate = sf.read(file_path)
        self.file_name = file_path
        self.bit_depth = np.dtype(self.samples[0][0]).itemsize * 8
        #left = [i[0] for i in data]
        #right = [i[1] for i in data]
        print("Loaded file!\nSample Rate:%d\nBit Depth:%d" % (self.sample_rate, self.bit_depth))
    
    def save_to(self, file_path):
        sf.write(file_path, self.samples, self.sample_rate)

    #def apply_effect(self, effect):
        #pass