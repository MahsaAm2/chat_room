import tkinter
import socket
from tkinter import *
from threading import Thread


def send():
    msg = my_msg.get()
    my_msg.set("")
    sock.send(bytes(msg, "utf8"))
    if msg == "#quit":
        sock.close()
        win.close()


def receive():
    while True:
        try:
            msg = sock.recv(1024).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except:
            print("there is an error receiving the message")


def on_closing():
    my_msg.set("#quit")
    send()


win = Tk()
win.title("chat room")
win.configure(bg="pink")
message_frame = Frame(win, height=100, width=100, bg='skyblue')
message_frame.pack()

my_msg = StringVar()
my_msg.set("")

sb = Scrollbar(message_frame)
msg_list = Listbox(message_frame, height=15, width=100, bg='skyblue', yscrollcommand=sb.set)
sb.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()

l1 = Label(win, text='Enter the message', fg='blue', font="Arial", bg="skyblue")
l1.pack()

e1 = Entry(win, textvariable=my_msg, fg='blue', width=50)
e1.pack()

send_b = Button(win, text="send", font="Arial", fg="blue", background="skyblue", command=send)
send_b.pack()

quit_b = Button(win, text="quit", font="Arial", fg="blue", background="skyblue", command=on_closing)
quit_b.pack()

HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

rec_Thread = Thread(target=receive)
rec_Thread.start()


mainloop()