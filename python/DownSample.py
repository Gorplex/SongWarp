import sys
import numpy as np
import scipy
import scipy.io.wavfile

DEFAULT_OUT = "out.wav"


def downSample(sampleRate, data, divisor):
    newSampleRate = int(sampleRate/divisor)
    newData = removeRatio(data, divisor-1, divisor)
    return (newSampleRate, newData)

#removes remove number of elements every sample
def removeRatio(list, remove, sample):
    out = []
    cur = 0
    for ele in list:
        if cur%sample >= remove:
            out.append(ele)
        cur+=1
    return np.array(out)

def music(name, downSampleRate, outFile):
    sampleRate, data = scipy.io.wavfile.read(name)
    print("Old:")
    print("SampleRate: " + str(sampleRate))
    print("DataLen: " + str(len(data)))
    
    sampleRate, data = downSample(sampleRate, data, downSampleRate)

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
    rate = 1
    try:
        rate = int(sys.argv[2])
    except:
        print("DownSampleRate must be an int")
        exit()
    music(sys.argv[1], rate, outFile)    

    
if __name__=="__main__":main()




