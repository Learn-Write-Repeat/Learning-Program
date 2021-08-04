# PYTHON MUSIC PLAYER 

## Introduction
In this project, we have created a Music Player Application in Python using the Tkinter and Pygame module.
In our daily life, we see every person has a hobby and that is listening to music. So in order to listen to music, they all need a Music player(hardware or software) where they can play their favorite songs. And we have to install this music player on our computer, based the Operating system i.e Windows, Macintosh, Android, Linux, etc. Then we can listen to our favorite songs.
Now we have created a Music Player using Python code from scratch.

## Libraries used for Music Player Application
The Libraries we used in our code :
### 1. Tkinter
We had already told you in the title of this page that we are going to use the Tkinter library, which is a standard library for GUI creation. The Tkinter library is most popular and very easy to use and it comes with many widgets (these widgets helps in the creation of nice-looking GUI Applications).
Also, Tkinter is a very light-weight module and it is helpful in creating cross-platform applications(so the same code can easily work on Windows, macOS, and Linux)
To use all the functions of Tkinter you need to import it in your code and the command for the same is:

```python
from tkinter import *
```

### 2. Pygame module
Pygame is a Python module that works with computer graphics and sound libraries and designed with the power of playing with different multimedia formats like audio, video, etc. While creating our Music Player application, we will be using Pygame's mixer.music module for providing different functionality to our music player application that is usually related to the manipulation of the song tracks.
Command used to install pygame is:

```python
from pygame import mixer
```

### 3. OS module
There is no need to install this module explicitly, as it comes with the standard library of Python. This module provides different functions for interaction with the Operating System. In this tutorial, we are going to use the OS module for fetching the playlist of songs from the specified directory and make it available to the music player application.
To use this module in your code you need to import its and command for the same is as follows:

```python
import os
```

### 4. Pywhatkit
Python offers numerous inbuilt libraries to ease our work. Among them pywhatkit is a Python library for sending WhatsApp messages at a certain time, it has several other features too.

Following are some features of pywhatkit module:

1. Send WhatsApp messages.
2. Play a YouTube video.
3. Perform a Google Search.
4. Get information on particular topic.

In Python3 pywhatkit module will not come pre-installed, so you can install it by using the command:

```python3
pip install pywhatkit
```

You can import it using:

```python3
import pywhatkit
```


After importing Libraries and modules, now it's time to create a basic window where we will add our UI elements.

### MusicPlayer Class

The functions defined in the MusicPlayer class are:

1.The addsongs() Function

```python
def addsongs():
    #a list of songs is returned 
    temp_song=filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3",""),))
    #loop through everyitem in the list
    for s in temp_song:
        s=s.replace("C:/Users/KIIT/Desktop/Hackon-2.0/music-files/","")
        songs_list.insert(END,s)
```

2.The deletesong() Function

```python
def deletesong():
    curr_song=songs_list.curselection()
    songs_list.delete(curr_song[0])
```

3.The playonline() Function

```python
def playonline():
    command = input("Enter your song in command line to play online: ")
    pywhatkit.playonyt(command)
```

4.The Play() Function

```python
def Play():
    song=songs_list.get(ACTIVE)
    song=f'C:/Users/KIIT/Desktop/Hackon-2.0/music-files/{song}'
    mixer.music.load(song)
    mixer.music.play()
```

5.The Pause()  Function

```python
def Pause():
    mixer.music.pause()
```

6.The Stop() Function

```python
def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)
```

7. The Resume() Function

```python
def Resume():
    mixer.music.unpause()
```

8. The Previous() Function

```python
def Previous():
    #to get the selected song index
    previous_one=songs_list.curselection()
    #to get the previous song index
    previous_one=previous_one[0]-1
    #to get the previous song
    temp2=songs_list.get(previous_one)
    temp2=f'C:/Users/KIIT/Desktop/Hackon-2.0/music-files/{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    #activate new song
    songs_list.activate(previous_one)
    #set the next song
    songs_list.selection_set(previous_one)
```

9. The Next() Function

```python
def Next():
    #to get the selected song index
    next_one=songs_list.curselection()
    #to get the next song index
    next_one=next_one[0]+1
    #to get the next song 
    temp=songs_list.get(next_one)
    temp=f'C:/Users/KIIT/Desktop/Hackon-2.0/music-files/{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    #activate newsong
    songs_list.activate(next_one)
     #set the next song
    songs_list.selection_set(next_one)
```

10. The Root Window 

```python
root=Tk()
root.title('Music player App ')
#initialize mixer 
mixer.init()
```
 
## Buttons in the Music Player

1. Play Button
2. Pause Button
3. Stop Button
4. Resume Button
5. Previous Button
6. Next Button

On clicking on a particular button , the command will take place accordingly.

<hr>

## Additional Information

### Team Name: 
- dlp-21-july-py-8

### Mentor: 
- <b>Mr. Samnit Mehandiratta</b> <a href="https://www.linkedin.com/in/lankabhedi/"> <img width=15x src=https://user-images.githubusercontent.com/50140975/128177441-45e52062-fbe8-426d-9bbe-8d5554a30f78.png></a>

### Team Members:
- <b>Mr. Devansh Shaw</b> <a href="https://www.linkedin.com/in/devansh-shaw"> <img width=15px src=https://user-images.githubusercontent.com/50140975/128177441-45e52062-fbe8-426d-9bbe-8d5554a30f78.png></a>: Project Brainstorming/Requirement Analysis, Project Programming and Development, and Feature Implementation and UI Design


- <b>Ms. Khushi Roy</b> <a href="https://www.linkedin.com/in/khushi-roy"> <img width=15px src=https://user-images.githubusercontent.com/50140975/128177441-45e52062-fbe8-426d-9bbe-8d5554a30f78.png></a>: Project Brainstorming/Requirement Analysis, Project Programming and Development, and Feature Implementation and UI Design


- <b>Mr. Dharnish R S</b> <a href="https://www.linkedin.com/in/dharnish-r-04676b1b0/"> <img width=15px src=https://user-images.githubusercontent.com/50140975/128177441-45e52062-fbe8-426d-9bbe-8d5554a30f78.png></a>: Project Brainstorming/Requirement Analysis, Feature Suggestion


- <b>Ms. Riya Singh</b> <a href="https://www.linkedin.com/in/riya-singh-b00b26158"> <img width=15px src=https://user-images.githubusercontent.com/50140975/128177441-45e52062-fbe8-426d-9bbe-8d5554a30f78.png></a>: Project Documentation


- <b>Ms. Krithi Rai</b> <a href="http://linkedin.com/in/krithi-rai-777610187"> <img width=15px src=https://user-images.githubusercontent.com/50140975/128177441-45e52062-fbe8-426d-9bbe-8d5554a30f78.png></a>: Written the Statement of Work

<hr>

## Some Glimpses
![image](https://user-images.githubusercontent.com/50140975/128181030-fbb661b6-5f2f-4b01-9d9b-8e7651a0ffcf.png)

![image](https://user-images.githubusercontent.com/50140975/128181061-cb681013-d3df-462e-9e57-a618f46f9090.png)

![image](https://user-images.githubusercontent.com/50140975/128181092-bbfac74e-fd47-47d4-98a8-fc0ee25cc07d.png)

![image](https://user-images.githubusercontent.com/50140975/128181129-69f13285-00e3-4d19-9aef-f528a9deb948.png)

![image](https://user-images.githubusercontent.com/50140975/128181174-bbf4965a-7a3b-4a9d-ab75-06202ad18777.png)

![image](https://user-images.githubusercontent.com/50140975/128181322-96127013-b15a-4816-b2ca-42b621c6d4e1.png)

