import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.io.wavfile

def fft_index(n):
    return np.append(np.arange(n//2,n), np.arange(0, n//2))
    
def fft_unpack(x):
    return [x[i] for i in fft_index(len(x))]

def my_fft(x):
    X = np.fft.fft(x)
    return fft_unpack(X)

def my_ifft(Y):
    Y_raw = fft_unpack(Y)
    return np.fft.ifft(Y_raw)

def music(name):
    sampleRate, data = scipy.io.wavfile.read(name)
    print("Old:")
    print("SampleRate: " + str(sampleRate))

    print("DataLen: " + str(len(data)))
    try:
        dataR, dataL = data.T
    except:
        dataR = data
        dataL = []

    freqDataR = my_fft(dataR) 
    #freqDataR = np.fft.fft(dataR) 
    #freqDataL = my_fft(dataL)
    print("freqLen: " + str(len(freqDataR))) 
    
    plt.subplot(211)
    timeAxis = np.arange(0,len(dataR)/sampleRate,1/sampleRate)
    plt.plot(timeAxis[0:1000], dataR[0:1000])
    
    plt.subplot(212)
    freqAxis = sampleRate*np.arange(-1/2,1/2,1/len(freqDataR))
    plt.plot(freqAxis, freqDataR)
    plt.show()

    print("New:")
    print("SampleRate: " + str(sampleRate))
    print("DataLen: " + str(len(data)))
    scipy.io.wavfile.write("out.wav", sampleRate, data)

    plotAll(sampleRate, dataR, freqDataR)

def plotAll(sampleRate, dataR, freqDataR):
    plt.subplot(211)
    timeAxis = np.arange(0,len(dataR)/sampleRate,1/sampleRate)
    plt.plot(timeAxis[0:1000], dataR[0:1000])
    
    plt.subplot(212)
    freqAxis = sampleRate*np.arange(-1/2,1/2,1/len(freqDataR))
    plt.plot(freqAxis, freqDataR)
    plt.show()

    
def main():
    if len(sys.argv) < 2:
        print("pass name of .wav file")
        exit()
    music(sys.argv[1])    

    
if __name__=="__main__":main()




