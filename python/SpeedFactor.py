import sys
import numpy as np
import scipy
import scipy.io.wavfile

DEFAULT_OUT = "out.wav"

def music(name, factor, outFile):
    sampleRate, data = scipy.io.wavfile.read(name)
    print("Old:")
    print("SampleRate: " + str(sampleRate))
    print("DataLen: " + str(len(data)))
    
    sampleRate*=factor

    print("New:")
    print("SampleRate: " + str(sampleRate))
    print("DataLen: " + str(len(data)))
    scipy.io.wavfile.write(outFile, sampleRate, data)
    
def main():
    outFile = DEFAULT_OUT
    if len(sys.argv) < 3:
        print("Usage: python3 DownSample.py input.wav downSampleRate [output.wav]")
        exit()
    elif len(sys.argv) >= 4:
        outFile = sys.argv[3]
    factor = 1
    try:
        factor = float(sys.argv[2])
    except:
        print("factor must be an flaot")
        exit()
    music(sys.argv[1], int(factor), outFile)    

    
if __name__=="__main__":main()




