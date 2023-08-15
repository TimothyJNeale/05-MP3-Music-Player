from tkinter import *

root = Tk()
root.title("MP3 Player")
root.geometry("500x400")
root.iconbitmap("01 Nenebiker.ico")

# Create Playlist Box
playlist_box = Listbox(root, bg="black", fg="green", width=60, selectbackground="green", selectforeground="black")
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
# back_button = Button(controls_frame, text="<< Back", bg="black", fg="white")
# forward_button = Button(controls_frame, text="Forward >>", bg="black", fg="white")
# play_button = Button(controls_frame, text="Play", bg="black", fg="white")
# pause_button = Button(controls_frame, text="Pause", bg="black", fg="white")
# stop_button = Button(controls_frame, text="Stop", bg="black", fg="white")

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




root.mainloop()