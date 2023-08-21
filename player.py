from tkinter import *
from tkinter import filedialog

# Importing OS module
import os

# FInd initial directory
RUNDIR = os.getcwd()

root = Tk()
root.title("MP3 Player")
root.geometry("500x400")
root.iconbitmap("01 Nenebiker.ico")

# Add singlw song to end of playlist
def add_song():
    song = filedialog.askopenfilename(initialdir=RUNDIR+'/music/', 
                                      title="Choose A Song", 
                                      filetypes=(("mp3 Files", "*.mp3"), ))
    #my_label.config(text=song)

    # Strip out the directory info and .mp3 extension from the song name
    song = song.replace("C:/Users/zenby/OneDrive/Projects/2023/ZAI-008.23.03 Tkinter GUI Masterclass/05 MP3 Music Player/music/", "")
    song = song.replace(".mp3", "")
    playlist_box.insert(END, song)

# Add Many Songs to end of Playlist
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir=RUNDIR+'/music/', 
                                      title="Choose A Song", 
                                      filetypes=(("mp3 Files", "*.mp3"), ))

    # Loop through song list and replace directory info and mp3 extension
    for song in songs:
        song = song.replace("C:/Users/zenby/OneDrive/Projects/2023/ZAI-008.23.03 Tkinter GUI Masterclass/05 MP3 Music Player/music/", "")
        song = song.replace(".mp3", "")
        playlist_box.insert(END, song)

# Create Playlist Box
playlist_box = Listbox(root, bg="black", fg="white", width=80, 
                       selectbackground="green", selectforeground="white",
                       activestyle='none')
playlist_box.pack(pady=20)

# Crete Player Control Frame
controls_frame = Frame(root)
controls_frame.pack(pady=20)

# Deefine Button Images for Controls
back_btn_img = PhotoImage(file="images/back50.png")
forward_btn_img = PhotoImage(file="images/forward50.png")
play_btn_img = PhotoImage(file="images/play50.png")
pause_btn_img = PhotoImage(file="images/pause50.png")
stop_btn_img = PhotoImage(file="images/stop50.png")

# Create Player Control Buttons
# Buttons with images
back_button = Button(controls_frame, image=back_btn_img, borderwidth=0)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0)
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0)

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



# Temporary Label
my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()