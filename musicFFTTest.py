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
    return (np.fft.ifft(Y_raw)).real

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
    #freqDataL = my_fft(dataL)
    
    size = len(freqDataR)
    
    newFreqDataR = shiftFreqData(freqDataR, 10000)
    
    #dataR = my_ifft(freqDataR[int(size/4):int(3*size/4)])
    newDataR = my_ifft(newFreqDataR)
    
    #data = np.array([dataR, dataL]).T

    print("New:")
    print("SampleRate: " + str(sampleRate))
    print("DataLen: " + str(len(newDataR)))
    scipy.io.wavfile.write("out.wav", sampleRate, newDataR)

    plotAll(sampleRate, dataR, freqDataR, newFreqDataR, newDataR)

def plotAll(sampleRate, dataR, freqDataR, newFreqDataR, newDataR):
    plt.subplot(411)
    timeAxis = np.arange(0,len(dataR)/sampleRate,1/sampleRate)
    plt.plot(timeAxis[0:1000], dataR[0:1000])
    
    plt.subplot(412)
    freqAxis = sampleRate*np.arange(-1/2,1/2,1/len(freqDataR))
    plt.plot(freqAxis, freqDataR)
    
    plt.subplot(413)
    plt.plot(freqAxis, newFreqDataR)
    
    plt.subplot(414)
    plt.plot(timeAxis[0:1000], newDataR[0:1000])
    
    
    
    plt.show()

#positive shifts up in freq
def shiftFreqData(data, samnt):
    positive = data[len(data)//2:]
    negitive = data[:len(data)//2]
    np.roll(positive, samnt)
    np.roll(negitive, -samnt)
    if(samnt > 0):
        mids = np.zeros(samnt)
        neg = np.append(negitive[:-samnt], mids)
        pos = np.append(mids, negitive[samnt:])
        all = np.append(neg, pos)
        return all
    elif(samnt < 0):
        ends = np.zeros(-samnt)
        neg = np.append(ends, negitive[-samnt:])
        pos = np.append(negitive[:samnt], ends)
        all = np.append(neg, pos)
        return all
    return data   

    
def main():
    if len(sys.argv) < 2:
        print("pass name of .wav file")
        exit()
    music(sys.argv[1])    

    
if __name__=="__main__":main()




