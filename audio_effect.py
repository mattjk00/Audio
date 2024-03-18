import numpy as np
import math
from scipy.fftpack import fft

def clamp(n, smallest, largest): 
        return max(smallest, min(n, largest))

def fft_mono(data, channel, bitDepth=24, maxSamples=None):
    '''
    Performs FFT on single channel. Assumes input data is stereo.
    '''
    F = data.T[channel]         # Get out single channel
    if maxSamples != None:
        F = F[:maxSamples]
    G = [(x/2**bitDepth) for x in F]  # Normalize into -1,1 range
    G_fft = fft(G)              # Do fft
    return G_fft

def get_real(data):
    N = len(data)//2               
    out = abs(data[:(N-1)])   # Get first half (symmetry) real part.
    return out

class AudioEffect:
    def __init__(self) -> None:
        pass

    def process(self, buffer):
        """
        out = np.copy(buffer)

        for i,pair in enumerate(buffer):
        
            for channel,sample in enumerate(buffer[i]):
            
                # do something #

                pass
                
        return out
        """
        raise NotImplementedError()
        

    def process_in_chunks(self, buffer, nchunks):
        raise NotImplementedError()

class ClipEffect(AudioEffect):

    

    def process(self, buffer):
        out = np.copy(buffer)
        for i,pair in enumerate(buffer):
            for channel,sample in enumerate(buffer[i]):
                out[i][channel] = clamp(math.atan(sample * 8), -0.75, 0.75)
                #print(channel, sample)
        return out
            