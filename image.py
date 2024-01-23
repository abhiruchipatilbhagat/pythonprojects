from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Learn')


my_img1 = ImageTk.PhotoImage(Image.open(r"D:\Fp1ihIuXsAARiDM.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open(r"D:\MV5BMmM4NjU0MjgtMTc4MC00NzRiLWI0YjctZDUyN2I1NjQxMWQ4XkEyXkFqcGdeQXVyNjgyMTI1MDE@._V1_.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open(r"D:\Fp1ihIuXsAARiDM.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open(r"D:\palindromenumberari.png"))
my_img5 = ImageTk.PhotoImage(Image.open(r"D:\music\296793009_3314029345485634_3973962927133617743_n.jpg"))
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label1 = Label(root, image=my_img1)
my_label1.grid(row=1, column=0, columnspan=3)

counter = 0

def forward():
    global counter
    counter += 1
    if counter >= len(image_list):
        counter = 0
    my_label1.configure(image=image_list[counter])

def backward():
    global counter
    counter -= 1
    if counter < 0:
        counter = len(image_list) - 1
    my_label1.configure(image=image_list[counter])

button_back = Button(root, text="<<", command=backward)
button_exit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text=">>", command=forward)

button_back.grid(row=0, column=0)
button_exit.grid(row=0, column=1)
button_forward.grid(row=0, column=2)

root.mainloop()
