- requires a python install: https://docs.python.org/3/using/windows.html
- adding Python to PATH makes it much easier to use
- run in Powershell in Windows /  Terminal on Mac


steps to run the command:

1. Open Powershell  (or Terminal on Mac). Press Windows+R to open the Run dialog box, and then type “powershell” in the text box. You can either click “OK” (or press the Enter) to open 

2. Change directory in Powershell/Terminal, using the 'cd' command, to the folder where you downloaded the script. 
e.g. if you downloaded it to your downloads folder,  paste this commmand into Powershell/Terminal (change yourUsername to your username in your OS):

Windows: cd Downloads\ForumDownloader (try C:\Users\*yourUsername*\Downloads\ForumDownloader if that doesn't work)
Mac: cd Downloads/ForumDownloader

3. run the command ' pip install -r requirements.txt ' to install the modules required to run this script.

4. Run the command, using the first page of the thread you want to download, and the directory you want to DL the songs to, as arguments.

For example, to download songs from this thread https://ktt2.com/favourite-video-game-soundtrack-32517991, to your downloads folder, 
use the command: python forum_downloader https://ktt2.com/post-rap-songs-that-not-many-people-have-heard-32530962 C:\Users\yourUsername\Downloads

