from bs4 import BeautifulSoup
import urllib #changed urllib.request
import pandas as pd

def gettingText(info):
    info_list = []
    for i in info:
        information = i.get_text()
        info_list.append(information)
    return info_list[:3]

def flattenList(list_info):
    flattened = [val for sublist in list_info for val in sublist]
    return flattened

prefix = "http://tsort.info/music/ds"
suffix = ".htm"
artist_list = []
song_list = []
year_list = []
for decade in range(1900,2010):
    if decade%10 == 0:
        url = prefix + str(decade) + suffix
        song_info = urllib.urlopen(url) #changed urllib.request.urlopen(url)
        soup = BeautifulSoup(song_info,"lxml")
        
        art,tit,yer = soup.find_all(attrs = {"class" : "art"}),soup.find_all(attrs = {"class" : "tit"}),soup.find_all(attrs = {"class" : "yer"})
        
        artist_names,song_names,song_years = gettingText(art),gettingText(tit),gettingText(yer)
        artist_list.append(artist_names), song_list.append(song_names),year_list.append(song_years)
        
def main():
    artist,song,year = flattenList(artist_list),flattenList(song_list),flattenList(year_list)
    
    df = pd.DataFrame({"Artist":artist,"Song":song,"Year":year})
    df.to_csv("Top 3 List.csv", index=False)
    
main()
        
