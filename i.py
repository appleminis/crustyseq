import pyaudio
import numpy as np
#import matplotlib.pyplot as plt
fs = 11025
d=101
if 10:
    ns=d*fs   
    sr=np.zeros((ns,1),np.float64)
    sr[0]=0.5
    for i in range(1,ns):
        sr[i]=sr[i-1]/4-1/sr[i-1];

samples = np.clip((sr[fs/5:])/10000,-1,1).astype(np.float32)
#plt.plot(samples)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,channels=1,
                rate=fs,output=True)
stream.write(samples)
stream.stop_stream()
stream.close()
p.terminate()