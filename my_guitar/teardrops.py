import sys, os
import math
import time, random
import wave, argparse, pygame
import numpy as np
from collections import deque
from matplotlib import pyplot as plt

#TODO start a band to accompany our script

def generate_note(freq, g_show_plot):
    num_samples = 44100
    N = int(44100/freq)
    buf  = deque([random.random() -  0.5  for  i  in  range(N)])
    if g_show_plot:
    	axline, =plt.plot(buf)
    samples  = np.array([0]*num_samples, 'float32')
    for i in range(num_samples):
        samples[i] = buf[0]
        avg  =  0.996*0.5*(buf[0]  +  buf[1])
        buf.append(avg)
        buf.popleft()
        # plot of flag set
        if g_show_plot:
        	if i % 1000 == 0:
        		axline.set_ydata(buf)
        		plt.draw()
        		plt.pause(0.0001)
    samples  = np.array(samples*32767, 'int16')
    return samples.tostring()

def write_wave(file_name, data):
    with wave.open(file_name, 'wb') as fh:
        num_channels = 1
        sample_width = 2
        sampling_rate = 44100
        num_samples = 44100
        fh.setparams((num_channels, sample_width, sampling_rate, num_samples, 'NONE', 'noncompressed'))
        fh.writeframes(data)

class NotePlayer:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 1, 2048)
        pygame.init()
        self.notes = {}

    def add(self, file_name):
        self.notes[file_name] = pygame.mixer.Sound(file_name)

    def play(self, file_name):
        try:
            self.notes[file_name].play()
        except:
            print("{} not found!".format(file_name))

    def play_random(self):
        index = random.randint(0, len(self.notes)-1)
        note = list(self.notes.values())[index]
        note.play()

def main():
    parser = argparse.ArgumentParser(description="Generating sounds with Karplus String Algorithm")
    parser.add_argument('--display', action='store_true', required=False)
    parser.add_argument('--play', action='store_true', required=False)
    parser.add_argument('--piano', action='store_true', required=False)
    args = parser.parse_args()

    if args.display:
        g_show_plot = True
        plt.ion()
        plt.show()
        
    else:
    	g_show_plot = False

    note_player = NotePlayer()

    #notes of a Pentatonic Minor scale
    #piano C4-E(b)-F-G-B(b)-C5
    notes = {'C4': 262, 'Eb': 311, 'F': 349, 'G': 391, 'Bb': 466}

    for name, frequency in list(notes.items()):
        file_name = "{}.wav".format(name)
        if not os.path.exists(file_name) or args.display:
            data = generate_note(frequency, g_show_plot)
            print("creating {} ..".format(file_name))
            write_wave(file_name, data)
        else:
            print("{} already created. Skipping.".format(file_name))

        note_player.add(file_name)

        if args.display:
            note_player.play(file_name)
            time.sleep(0.5)

    if args.play:
        while True:
            try:
                note_player.play_random()
                rest = np.random.choice([1, 2, 4, 8], 1, p=[0.15, 0.7, 0.1, 0.05])
                time.sleep(0.25*rest[0])
            except KeyboardInterrupt:
                exit()

if __name__ == '__main__':
    main()

#TODO implement function for --piano to create the piano guitar!
