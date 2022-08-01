from tkinter import *
import server


root = Tk()
root.geometry("300x200")

label_teacher = Label(root, text="Teacher")
label_teacher.grid(row=0, column=0)
name = Entry(root)
name.grid(row=2, column=1)
teacher_ip = Entry(root)
teacher_ip.grid(row=4, column=1)
teacher_ip.insert(0, server.host_ip)

label_name = Label(root, text="Name =")
label_name.grid(row=2, column=0)
label_teacher_ip = Label(root, text="Your Ip Address =")
label_teacher_ip.grid(row=4, column=0)

mybutton = Button(root, text="Start Server", command=lambda: main_button())
mybutton.grid(row=6, column=1)

myinstruction = Label(root, text="After starting server, press q to exit")
myinstruction.grid(row=6, column=0)

emptylabel1 = Label(root, text="   ")
emptylabel1.grid(row=3, column=0)
emptylabel2 = Label(root, text="   ")
emptylabel2.grid(row=5, column=1)
emptylabel3 = Label(root, text="   ")
emptylabel3.grid(row=1, column=0)


def main_button():
    root.destroy()
    server.run_show_client()




root.mainloop()
