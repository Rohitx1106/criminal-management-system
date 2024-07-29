from customtkinter import *
from PIL import ImageA
import tkinter as tk
from tkinter import messagebox
import subprocess

def validate(username, password):
    # Perform validation here
    if username.upper() == "TUSHAR" and password == "password":
        return True
    else:
        return False

def login():
    username = usrname_entry.get()
    password = passwd_entry.get()

    if validate(username, password):
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        # Dispatch to other Python file
        subprocess.call(["python", "criminal.py"])
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create main window

main = CTk()
main.title("Login Page")
main.config(bg="white")
main.resizable(False, False)




bg_img = CTkImage(dark_image=Image.open("logo_in.png"), size=(500, 500))

bg_lab = CTkLabel(main, image=bg_img, text="")
bg_lab.grid(row=0, column=0)

frame1 = CTkFrame(main,fg_color="#D9D9D9", bg_color="white", height=350, width=300,corner_radius=20)
frame1.grid(row=0, column=1,padx=40)

title = CTkLabel(frame1,text="\nLogin to Account",text_color="black",font=("",30,"bold"))
title.grid(row=0,column=0,sticky="nw",pady=30,padx=10)

usrname_entry = CTkEntry(frame1,text_color="white", placeholder_text="Username", fg_color="black", placeholder_text_color="white",
                         font=("",16,"bold"), width=200, corner_radius=15, height=45)
usrname_entry.grid(row=1,column=0,sticky="nwe",padx=30)

passwd_entry = CTkEntry(frame1,text_color="white",placeholder_text="Password",fg_color="black",placeholder_text_color="white",
                         font=("",16,"bold"), width=200,corner_radius=15, height=45, show="*")
passwd_entry.grid(row=2,column=0,sticky="nwe",padx=30,pady=20)


l_btn = CTkButton(frame1,text="Login",command=login,font=("",15,"bold"),height=40,width=60,fg_color="#0085FF",cursor="hand2",
                  corner_radius=15)
l_btn.grid(row=3,column=0,sticky="ne",pady=20, padx=35)


main.mainloop()