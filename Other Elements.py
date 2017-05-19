import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import pandas as pd

def meanEachElement(songList):
    smean = [sum(tup) for tup in songList]
    return smean

def makingList(infoList):
    return zip(*[iter(infoList)]*3)
    
def plottingList(elementList):
    year = []
    for i in range(1900,2010):
        if i%10 == 0:
            year.append(i)
    plt.plot(year,elementList,'ro')
    plt.show()


def main():
    data = pd.read_csv('Top 3 List.csv', usecols=['Song','Year'])
    names = data.Song.tolist()
    
    t = []
    o = []
    temp = []
    b = []
    
    for i in names:
       y,sr = librosa.load("C:\Users\Katherine\Music\\"+i+".mp3",duration=60)
       tone = librosa.feature.tonnetz(y=y, sr=sr)
       t.append(tone.max())
       onset = librosa.onset.onset_strength(y, sr=sr)
       o.append(onset.max())
       tempo, beat = librosa.beat.beat_track(onset_envelope=onset,sr=sr)
       temp.append(tempo)
       b.append(beat.max())

    tmax = meanEachElement(makingList(t))
    omax = meanEachElement(makingList(o))
    tpmax = meanEachElement(makingList(temp))
    bmax = meanEachElement(makingList(b))
    plottingList(tmax)
    plottingList(omax)
    plottingList(tpmax)
    plottingList(bmax)
  
main()
















