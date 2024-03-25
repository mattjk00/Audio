from audio_buffer import AudioBuffer
from audio_effect import ClipEffect, fft_mono, get_real, ifft_mono
from matplotlib import pyplot as plt
import numpy as np

def print_opening():
    print("VINO Digital Audio Tool -- Matthew Kleitz 2024")

if __name__ == "__main__":
    print_opening()

    afile = AudioBuffer()
    afile.load_from("./input/clean_git.wav")

    clip_effect = ClipEffect()
    afile.samples = clip_effect.process(afile.samples)

    x = fft_mono(afile.samples, 0, bitDepth=afile.bit_depth, maxSamples=44100)
    x2= fft_mono(afile.samples, 1, bitDepth=afile.bit_depth, maxSamples=44100)
    afile.samples = np.array([ifft_mono(x), ifft_mono(x2)]).T

    plt.plot(get_real(x))
    plt.show()


    afile.save_to("out.wav")