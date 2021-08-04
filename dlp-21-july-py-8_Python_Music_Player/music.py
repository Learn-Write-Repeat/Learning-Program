from pygame import mixer
from tkinter import *
import os
import tkinter.font as font
from tkinter import filedialog
import pywhatkit

#add many songs to the playlist
def addsongs():
    #a list of songs is returned 
    temp_song=filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3",""),))
    #loop through everyitem in the list
    for s in temp_song:
        s=s.replace("C:/Users/KIIT/Desktop/Hackon-2.0/music-files/","")
        songs_list.insert(END,s)
        
            
def deletesong():
    curr_song=songs_list.curselection()
    songs_list.delete(curr_song[0])

def playonline():
    command = input("Enter your song in command line to play online: ")
    pywhatkit.playonyt(command)
    
    
def Play():
    song=songs_list.get(ACTIVE)
    song=f'C:/Users/KIIT/Desktop/Hackon-2.0/music-files/{song}'
    mixer.music.load(song)
    mixer.music.play()
 
def Pause():
    mixer.music.pause()

#to stop the  song 
def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

#to resume the song

def Resume():
    mixer.music.unpause()

#Function to navigate from the current song
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


#creating the root window 
root=Tk()
root.title('Music player App ')
#initialize mixer 
mixer.init()


#create the listbox to contain songs
songs_list=Listbox(root,selectmode=SINGLE,bg="#003638",fg="#5E8B7E",font=('arial',15,font.ITALIC),height=12,width=47,selectbackground="#444444",selectforeground="#F3F2C9")
songs_list.grid(columnspan=9)

#font is defined which is to be used for the button font 
defined_font = font.Font(family='Helvetica')

#play button
play_button=Button(root,text="Play",bg="#B2AB8C",width =11,height = 2,command=Play)
play_button['font']=defined_font
play_button.grid(row=1,column=0)

#pause button 
pause_button=Button(root,text="Pause",bg="#47597E",width =11,height = 2,command=Pause)
pause_button['font']=defined_font
pause_button.grid(row=1,column=1)

#stop button
stop_button=Button(root,text="Stop",bg="#DBE6FD",width =11,height = 2,command=Stop)
stop_button['font']=defined_font
stop_button.grid(row=1,column=2)

#resume button
Resume_button=Button(root,text="Resume",width =11,height = 2,bg="#F38BA0",command=Resume)
Resume_button['font']=defined_font
Resume_button.grid(row=1,column=3)

#previous button
previous_button=Button(root,text="Prev",bg="#39A6A3",width =11,height = 2,command=Previous)
previous_button['font']=defined_font
previous_button.grid(row=1,column=4)

#nextbutton
next_button=Button(root,text="Next",bg="#D79771",width =12,height = 2,command=Next)
next_button['font']=defined_font
next_button.grid(row=1,column=5)

#menu 
my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add songs",command=addsongs)
add_song_menu.add_command(label="Delete song",command=deletesong)
add_song_menu.add_command(label="Play online",command=playonline)
mainloop()