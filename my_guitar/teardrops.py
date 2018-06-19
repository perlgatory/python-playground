import sys, os
import math
import time, random
import wave, argparse, pygame
import numpy as np
from collections import deque
from matplotlib import pyplot as plt

#TODO implement a guitar sound (Chapter 4, beginning page 55)
#TODO start a band to accompany our script
sampling_rate = 44100
num_samples = sampling_rate * 5
x = np.arange(num_samples)/float(sampling_rate)

amplitude_values = np.sin(4.0*math.pi*220.0*x)
amplitude_array = np.array(amplitude_values*32767, 'int16').tostring()
with wave.open('sine220.wav', 'wb') as file:
    file.setparams((1, 2, sampling_rate, num_samples, 'NONE', 'uncompressed'))
    file.writeframes(amplitude_array)

def generate_note(freq):
    N = int(sampling_rate/freq)
    buf  = deque([random.random() -  0.5  for  i  in  range(N)])
    samples  = np.array([0]*num_samples, 'float32')
    for i in range(num_samples):
        samples[i] = buf[0]
        avg  =  0.996*0.5*(buf[0]  +  buf[1])
        buf.append(avg)
        buf.popleft()

     samples  = np.array(samples*32767, 'int16')
     return samples.tostring()

     ## todo finish this pg. 85
