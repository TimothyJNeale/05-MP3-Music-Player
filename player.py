from tkinter import *
from tkinter import filedialog
from pygame import mixer
from mutagen.mp3 import MP3
from tkinter import ttk

import time
import os

MUSIC_PATH = 'C:/Users/zenby/OneDrive/Projects/2023/ZAI-008.23.03 Tkinter GUI Masterclass/05 MP3 Music Player/music/'
STATUS_BAR_INTI_TEXT = 'Time Elapsed: 00:00 of 00:00  '

# FInd initial directory
RUNDIR = os.getcwd()

global song_length
song_length = 0

global current_position
current_time = 0

global paused
paused = False

global current_song
current_song = ''

root = Tk()
root.title("MP3 Player")
root.geometry("500x400")
root.iconbitmap("01 Nenebiker.ico")

# Initialize Pygame Mixer
mixer.init()

# Function to deal with time
def play_time():
    global current_time
    global paused

    # Increament timer if not paused
    if not paused and song_length != 0 and current_time <= song_length:
        current_time += 1

        converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

        song_slider.config(to=song_length, value=current_time)

        # Update status bar if song is playing
        if current_time > 0:
            status_bar.config(text=f'Time Elapsed: {converted_current_time} of {time.strftime("%M:%S", time.gmtime(song_length))}  ') 

    status_bar.after(1000, play_time) # Call play_time after 1 second

# Add singlw song to end of playlist
def add_song():
    song = filedialog.askopenfilename(initialdir=RUNDIR+'/music/', 
                                      title="Choose A Song", 
                                      filetypes=(("mp3 Files", "*.mp3"), ))
    #my_label.config(text=song)

    # Strip out the directory info and .mp3 extension from the song name
    song = song.replace(MUSIC_PATH, "")
    song = song.replace(".mp3", "")
    playlist_box.insert(END, song)

# Add Many Songs to end of Playlist
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir=RUNDIR+'/music/', 
                                      title="Choose A Song", 
                                      filetypes=(("mp3 Files", "*.mp3"), ))

    # Loop through song list and replace directory info and mp3 extension
    for song in songs:
        song = song.replace(MUSIC_PATH, "")
        song = song.replace(".mp3", "")
        playlist_box.insert(END, song)

# Delete a song from playlist
def delete_song():
    playlist_box.delete(ANCHOR)

# Delete all songs from playlist
def delete_all_songs():
    playlist_box.delete(0, END)

# Play selected song
def play():
    song = playlist_box.get(ACTIVE)
    song = MUSIC_PATH+f'{song}.mp3'

     # Get current song length
    song_mut = MP3(song)
    global song_length
    song_length = song_mut.info.length

    #my_label.config(text=song)
    mixer.music.load(song)
    mixer.music.play(loops=0)

    # Initialise current time and paused
    global current_song
    current_song = song
    global current_time
    current_time = 0
    global paused
    paused = False

# Stop playing current song
def stop():
    mixer.music.stop()
    playlist_box.selection_clear(ACTIVE)

    global song_length
    song_length = 0

    # Initialise current time and paused
    global current_time
    current_time = 0
    global paused
    paused = False
    global current_song
    current_song = ''

    # Reset slider and status bar
    status_bar.config(text=STATUS_BAR_INTI_TEXT)
    song_slider.config(value=0)

# Pause and Unpause The Current Song
def pause():
    global paused
 
    if paused:
        # Unpause
        mixer.music.unpause()
    else:
        # Pause
        mixer.music.pause()

    # set paused to opposite of what it was
    paused = not paused

# Play the next song in the playlist
def next_song():
    # Reset slider and status bar
    status_bar.config(text=STATUS_BAR_INTI_TEXT)
    song_slider.config(value=0)

    # Get the current song tuple number
    next_one = playlist_box.curselection() # returns a tuple

    # Add one to the current song number
    next_one = next_one[0]+1

    # Grab the song title from the playlist
    song = playlist_box.get(next_one)

    # Add directory structure stuffs to the song title
    song = MUSIC_PATH+f'{song}.mp3'
    # Load and play the new song
    mixer.music.load(song)
    mixer.music.play(loops=0)

    # Initialise current time and paused
    global current_song
    current_song = song
    global current_time
    current_time = 0
    global paused
    paused = False

     # Get current song length
    song_mut = MP3(song)
    global song_length
    song_length = song_mut.info.length

    # Clear Active Bar in Playlist
    playlist_box.selection_clear(0, END)

    # Move active bar to next song
    playlist_box.activate(next_one)

    # Set Active Bar to next song
    playlist_box.selection_set(next_one, last=None)

# Play the previous song in the playlist
def previous_song():
    # Reset slider and status bar
    status_bar.config(text=STATUS_BAR_INTI_TEXT)
    song_slider.config(value=0)
    
    # Get the current song tuple number
    next_one = playlist_box.curselection() # returns a tuple

    # AMinus one to the current song number
    next_one = next_one[0]-1

    # Grab the song title from the playlist
    song = playlist_box.get(next_one)

    # Add directory structure stuffs to the song title
    song = MUSIC_PATH+f'{song}.mp3'

    # Get current song length
    song_mut = MP3(song)
    global song_length
    song_length = song_mut.info.length

    # Load and play the new song
    mixer.music.load(song)
    mixer.music.play(loops=0)

    # Initialise current time and paused
    global current_song
    current_song = song
    global current_time
    current_time = 0
    global paused
    paused = False

    # Clear Active Bar in Playlist
    playlist_box.selection_clear(0, END)

    # Move active bar to next song
    playlist_box.activate(next_one)

    # Set Active Bar to next song
    playlist_box.selection_set(next_one, last=None)

# Create Volume Function
def volume(x):
    mixer.music.set_volume(volume_slider.get())

# Creae slider function for song position
def slide(x):
    # Get currently selected song
    global current_song
    global current_time
    
    # Load song with pygame mixer
    mixer.music.load(current_song)
    current_time = song_slider.get()
    mixer.music.play(loops=0, start=current_time)

# Create main frame
main_frame = Frame(root)
main_frame.pack(pady=20)

# Create Playlist Box
playlist_box = Listbox(main_frame, bg="black", fg="white", width=60, 
                       selectbackground="green", selectforeground="white",
                       activestyle='none')
playlist_box.grid(row=0, column=0)

# Crete volume frame
volume_frame = LabelFrame(main_frame, text="Volume")
volume_frame.grid(row=0, column=1, padx=20)

# Create Volume Slider
volume_slider = ttk.Scale(volume_frame, from_=1, to=0, orient=VERTICAL, 
                          length=125, value=.5, command=volume)
volume_slider.pack(pady=10)

# Create Song Slider
song_slider = ttk.Scale(main_frame, from_=0, to=100, orient=HORIZONTAL,
                        length=360, value=0, command=slide)
song_slider.grid(row=2, column=0, pady=20)

# Crete Player Control Frame
controls_frame = Frame(main_frame)
controls_frame.grid(row=1, column=0, pady=20)

# Deefine Button Images for Controls
back_btn_img = PhotoImage(file="images/back50.png")
forward_btn_img = PhotoImage(file="images/forward50.png")
play_btn_img = PhotoImage(file="images/play50.png")
pause_btn_img = PhotoImage(file="images/pause50.png")
stop_btn_img = PhotoImage(file="images/stop50.png")

# Create Player Control Buttons
# Buttons with images
back_button = Button(controls_frame, image=back_btn_img, borderwidth=0,command=previous_song)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0, command=next_song)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=pause)
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Song Menu dropdown
add_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
# Add one song to playlist
add_song_menu.add_command(label="Add One Song to Playlist", command=add_song)
# Add many songs to playlist
add_song_menu.add_command(label="Add Many Songs to Playlist", command=add_many_songs)

# Remove Song Menu dropdown
remove_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
# Remove one song from playlist
remove_song_menu.add_command(label="Remove One Song from Playlist", command=delete_song)
# Remove all songs from playlist
remove_song_menu.add_command(label="Remove All Songs from Playlist", command=delete_all_songs)

# Creste Status Bar
status_bar = Label(root, text=STATUS_BAR_INTI_TEXT, bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)


# Call the play_time 
play_time()

root.mainloop()