from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
from tkinter import messagebox

root = Tk()
root.minsize(600, 600)
root.maxsize(600, 600)

open_img = ImageTk.PhotoImage(Image.open("open_file.png"))
save_img = ImageTk.PhotoImage(Image.open("save_file.png"))
run_img = ImageTk.PhotoImage(Image.open("run.png"))


    

label_file_name = Label(root, text = "File Name :", bg = "white")
label_file_name.place(relx = 0.40, rely = 0.05, anchor = CENTER)

input_file_name = Entry(root)
input_file_name.place(relx = 0.57, rely = 0.05, anchor = CENTER)



my_text = Text(root, height = 33, width = 74, bg = "gray", fg = "white")
my_text.place(relx = 0.5, rely = 0.55, anchor = CENTER)


name=""
def openFile():
    global name
    my_text.delete(1.0, END)
    input_file_name.delete(0, END)
    text_file = filedialog.askopenfilename(title=" Open Text File", filetypes=(("Text Files", "*.txt"),))
    print(text_file)
    name=os.path.basename(text_file)
    formated_name=name.split(".")[0]
    input_file_name.insert(END,formated_name)
    root.title(formated_name)
    text_file = open(name,'r')
    paragraph =text_file.read()
    my_text.insert(END,paragraph)
    text_file.close()

open_button = Button(root, image = open_img, text = "Open File")
open_button.place(relx = 0.05, rely = 0.05, anchor = CENTER)

save_button = Button(root, image = save_img, text = "Save File")
save_button.place(relx = 0.15, rely = 0.05, anchor = CENTER)

run_button = Button(root, image = run_img, text = "Run File")
run_button.place(relx = 0.23, rely = 0.05, anchor = CENTER)

root.mainloop()