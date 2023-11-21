from pytube import YouTube #imports YouTube class from the pytube module 
from sys import argv #this line imports the argv variable from the sys module.

""" 
argv is a list in Python that contains the command-line arguments passed to the script.

"""
#we must pass two command line argument first is ytDownloader.py and second is the video link or URL.
#ytDownloader.py stores in index 0 i.e argv[0] and <youtube_link> stores in index 1 or argv[1].

if len(argv) < 2:  #if we pass less than 2 command line arguments this code runs
    print("Usage: python ytDownloader.py <youtube_link>") #explains how to pass command line argument
    exit(1) #exits

link = argv[1]    #assigns the second command line argument we pass (link or URL of the video) that is stored in the index 1 in argv variable to the variable 'link'.
yt = YouTube(link) #creats the object(instance) of the YouTube class named yt where argument link is passed

print("Title: ", yt.title) #prints the title of the particular  video using the instance
print("Views: ", yt.views) #prints the view in the video

yd = yt.streams.get_highest_resolution()  #This line gets the stream with the highest resolution for the video and assign it to the variable yd

yd.download(r'C:\Users\ASUS\Downloads') #downloads the video in the specified directory


