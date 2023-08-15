from tkinter import *

root = Tk()
root.title("MP3 Player")
root.geometry("500x400")
root.iconbitmap("01 Nenebiker.ico")


playlist_box = Listbox(root, bg="black", fg="green", width=60, selectbackground="green", selectforeground="black")
playlist_box.pack(pady=20)





root.mainloop()