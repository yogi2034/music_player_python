from tkinter import *
from tkinter import filedialog
import pygame
import os

root =Tk()
root.title("music player")
root.geometry("500x300")

pygame.mixer.init()

menubar=Menu(root)
root.config(menu=menubar)

songs=[]
current_song=""
paused=False


def load_music():
    global current_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name,ext=os.path.splitext(song)
        if ext==".mp3":
            songs.append(song)

    for song in songs:
        songlist.insert("end",song)

    songlist.selection_set(0)

    current_song=songs[songlist.curselection()[0]]

organise_menu=Menu(menubar,tearoff=False)
organise_menu.add_command(label='choose Folder',command=load_music)
menubar.add_cascade(label='Organise ',menu=organise_menu)

songlist=Listbox(root,bg="#080808",fg="white",width=100,height=13)
songlist.pack()

def play_music():
    global current_song,paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory,current_song))
        pygame.mixer.music.play()


def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused=True
def prev_music():
    global current_song,paused
    try:
        songlist.selection_clear(0,END)
        index = songs.index(current_song) - 1
        songlist.selection_set(index)
        current_song=songs[index]
        play_music()
    except :
        pass

def next_music():
    global current_song,paused
    try:
        songlist.selection_clear(0,END)
        index = songs.index(current_song) + 1
        songlist.selection_set(index)
        current_song=songs[index]
        play_music()
    except :
        pass




play_button_image=PhotoImage(file="play.png")
pause_button_image=PhotoImage(file="pause.png")
prev_button_image=PhotoImage(file="previous.png")
next_button_image=PhotoImage(file="next.png")

control_frame=Frame(root)
control_frame.pack()
#
play_button=Button(control_frame,image=play_button_image,borderwidth=0,command=play_music)
pause_button=Button(control_frame,image=pause_button_image,borderwidth=0,command=pause_music)
prev_button=Button(control_frame,image=prev_button_image,borderwidth=0,command=prev_music)
next_button=Button(control_frame,image=next_button_image,borderwidth=0,command=next_music)


play_button.grid(row=0,column=1,padx=7,pady=10)
pause_button.grid(row=0,column=2,padx=7,pady=10)
prev_button.grid(row=0,column=0,padx=7,pady=10)
next_button.grid(row=0,column=3,padx=7,pady=10)





root.mainloop()

