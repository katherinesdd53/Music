import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import pandas as pd

def wavelengthMono(song):
    y,sr = librosa.load("C:\Users\Katherine\Music\\"+song+".mp3",duration=60)
    plt.figure()
    librosa.display.waveplot(y,sr=sr,alpha=0.30, label=song)
    plt.legend()
    plt.title('Monophonic')
    
def harmpercWave(song):
    y,sr = librosa.load("C:\Users\Katherine\Music\\"+song+".mp3", duration=60)
    y_harm, y_perc = librosa.effects.hpss(y)
    plt.figure()
    librosa.display.waveplot(y_harm, sr=sr, alpha=0.25,label=song+' Harmony')
    librosa.display.waveplot(y_perc, sr=sr, color = 'r', alpha=0.25,label=song+' Percussion')
    plt.legend()
    plt.title('Harmonic + Percussive')
    plt.tight_layout()
    
def spectralCent(song):
    y,sr = librosa.load("C:\Users\Katherine\Music\\"+song+".mp3", duration=60)
    cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    S, phase = librosa.magphase(librosa.stft(y=y))
    librosa.feature.spectral_centroid(S=S)
    if_gram, D = librosa.ifgram(y)
    librosa.feature.spectral_centroid(S=np.abs(D), freq=if_gram)
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.semilogy(cent.T, label=song)
    plt.ylabel('Hz')
    plt.xticks([])
    plt.xlim([0, cent.shape[-1]])
    plt.legend()
    
def tonalCent(song):
    y,sr = librosa.load("C:\Users\Katherine\Music\\"+song+".mp3", duration=60)
    y = librosa.effects.harmonic(y)
    tonnetz = librosa.feature.tonnetz(y=y, sr=sr)
    plt.figure()
    plt.subplot(2, 1, 1)
    librosa.display.specshow(tonnetz, y_axis='tonnetz')
    plt.colorbar()
    plt.title('Tonal Centroids '+song)
    
def onsetDetect(song):
    y,sr = librosa.load("C:\Users\Katherine\Music\\"+song+".mp3", duration=30)
    o_env = librosa.onset.onset_strength(y, sr=sr)
    times = librosa.frames_to_time(np.arange(len(o_env)), sr=sr)
    onset_frames = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr)
    plt.figure(figsize=(8, 4))
    #plt.subplot(8,4)
    plt.plot(times, o_env, label='Onset strength')
    plt.vlines(times[onset_frames], 0, o_env.max(), color='r', alpha=0.9,linestyle='--', label='Onsets')
    plt.axis('tight')
    plt.legend(frameon=True, framealpha=0.75)
    plt.title(song)
    
def beatDetect(song):
    y,sr = librosa.load("C:\Users\Katherine\Music\\"+song+".mp3", duration=30)
    onset_env = librosa.onset.onset_strength(y, sr=sr,aggregate=np.median)
    tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env,sr=sr)
    hop_length = 512
    plt.figure(figsize=(8, 4))
    times = librosa.frames_to_time(np.arange(len(onset_env)),sr=sr, hop_length=hop_length)
    plt.plot(times, librosa.util.normalize(onset_env),label='Onset strength')
    plt.vlines(times[beats], 0, 1, alpha=0.5, color='r',linestyle='--', label='Beats')
    plt.legend(frameon=True, framealpha=0.75)
    plt.title(song)
    
    
def main():
    data = pd.read_csv('Top 3 List.csv', usecols=['Song'])
    names = data.Song.tolist()
    for i in names:
        wavelengthMono(i)
        harmpercWave(i)
        spectralCent(i)
        tonalCent(i)
        onsetDetect(i)
        beatDetect(i)
        
        
main()