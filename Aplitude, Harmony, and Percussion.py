import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import pandas as pd

def harmAndPercData(song):
    y,sr = librosa.load("C:\Users\Katherine\Music\\"+song+".mp3",duration=60)
    y_harm, y_perc = librosa.effects.hpss(y)
    return [y.max(),y_harm.max(),y_perc.max()]

def meanEachElement(songList):
    smean = [sum(tup) for tup in songList]
    return smean

def makingList(info,n):
    sList = []
    for i in info:
        hpList = harmAndPercData(i)
        sList.append(hpList[n])
    return zip(*[iter(sList)]*3)
    
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
    amax = meanEachElement(makingList(names,0))
    hmax = meanEachElement(makingList(names,1))
    pmax = meanEachElement(makingList(names,2))
    plottingList(amax)
    plottingList(hmax)
    plottingList(pmax)    
  
main()





































