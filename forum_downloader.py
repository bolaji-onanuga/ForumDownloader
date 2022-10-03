## TODO
# create playlist using list of links, or get names of tracks and add each to
# new spotify playlist titled after thread.

import os
import subprocess
import sys
import urllib.request
import re

# os.chdir("G:\Music\Singles") # directory to save dl'ed songs to
#start_url = "https://ktt2.com/favourite-video-game-soundtrack-32517991" + "/"

print("Hello! ^_^ \n")

start_url = sys.argv[1] + "/"

if sys.argv[2]:
    os.chdir(sys.argv[2]) # directory to save dl'ed songs to

url = start_url
i=1
r = urllib.request.urlopen(url).read()
r = r.decode("utf-8")

while r:
    
    # get contents of webpage
    title = str(r).split('<title>')[1].split('</title>')[0]
    print("Downloading songs from the thread {}".format(title))

    os.mkdir(title)
    os.chdir(title)

    # extract links from webpage using regex
    r = re.findall(r'https:\/\/youtu\.be\/.{11}', r)

    r = list(set(r))   # remove duplicate yt links

    if  r:  # if page is not null
        # if r is null, use the alternate yt link formation.

        print("Found {} links on page {} \n".format(len(r), i))

        # download each song in m4a format from the given link
        for link in r:
            print("Downloading {} \n".format(link))
            subprocess.run(["youtube-dl", link, "-f", "m4a"])

    # get url to next page -> repeat until there are no more pages.
    i += 1

    url = start_url + str(i)
    r = urllib.request.urlopen(url).read()
    r = r.decode("utf-8")

print("Finish! ^_^ \n")





    