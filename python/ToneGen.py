import sys
import numpy as np
import math
import scipy
import scipy.io.wavfile

DEFAULT_OUT = "out.wav"
DEFAULT_SAMPLES = 44100

def sinWave(time):
    return math.sin(2*math.pi*time)
sinWaveV = np.vectorize(sinWave)

def main():
    outFile = DEFAULT_OUT
    samples = DEFAULT_SAMPLES
    freq = 1
    dur = 1
    if len(sys.argv) < 3:
        print("Usage: python3 ToneGen.py freq duration [out.wav] [samplesPerSec]")
        exit()
    if len(sys.argv) >= 4:
        outFile = sys.argv[3]
    if len(sys.argv) >= 5:
        samples = int(sys.argv[4])
    freq = int(sys.argv[1])
    dur = int(sys.argv[2])

    time = np.arange(0,dur,1/samples)
    data = sinWaveV(freq*time)
    data2chan = np.array([data,data]).T

    scipy.io.wavfile.write(outFile,samples,data2chan)

if __name__ == "__main__":main()


