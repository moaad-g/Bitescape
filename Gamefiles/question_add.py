from tkinter import *
from tkinter import messagebox as ms
import time
import sqlite3
import os
from passlib.hash import sha256_crypt

screen= Tk()
class QuestionWrite():
    def __init__(self, screen):
        self.question = StringVar()
        self.opt_1 = StringVar()
        self.opt_2 = StringVar()
        self.opt_3 = StringVar()
        self.correct_opt = StringVar()
        self.screen = screen
        fileread = open("Quiz.txt","r")
        self.filebefore = fileread.readlines()
        fileread.close()
        
    def write(self):
        question = (self.question.get())
        opt_1 = (self.opt_1.get())
        opt_2 = (self.opt_2.get())
        opt_3 = (self.opt_3.get())
        correct_opt = (self.correct_opt.get())
        print (opt_1)
        if correct_opt == "1":
            opt_1 = ("!"+opt_1)
        elif correct_opt == "2":
            opt_2 = ("!"+opt_2)
        elif correct_opt == "3":
            opt_3 = ("!"+opt_3)
        file = open("Quiz.txt","w")
        self.filebefore.append(question+"\n")
        self.filebefore.append(opt_1+"\n")
        self.filebefore.append(opt_2+"\n")
        self.filebefore.append(opt_3+"\n")
        file.writelines(self.filebefore)
        file.close()
        import Bitescape

    def retrieve(self):
        def checks():
            question = (self.question.get())
            opt_1 = (self.opt_1.get())
            opt_2 = (self.opt_2.get())
            opt_3 = (self.opt_3.get())
            correct_opt = (self.correct_opt.get())
            if question=="" or opt_1=="" or opt_2=="" or opt_3=="" or correct_opt =="":
                ms.showerror("ERROR","Please ensure all fields have been completed")
            else:
                self.screen.destroy()
                self.write()
        screen.withdraw()
        self.screen =Toplevel(screen)
        self.screen.geometry("300x300")
        self.screen.title("Write new question and options")
        Label(self.screen, text="Question:").grid(row=0,column=3)
        Entry(self.screen, textvariable = self.question).grid(row=1,column=3)
        Label(self.screen, text="Options:").grid(row=2,column=3)
        Entry(self.screen, textvariable = self.opt_1).grid(row=5,column=3)
        Entry(self.screen, textvariable = self.opt_2).grid(row=6,column=3)
        Entry(self.screen, textvariable = self.opt_3).grid(row=7,column=3)
        Label(self.screen, text="Correct Option:").grid(row=8,column=3)
        correct_opt = OptionMenu(self.screen,self.correct_opt,"1","2","3")
        correct_opt.grid(row=9,column=3)
        Label(self.screen, text="").grid(row=10,column=6)
        Button(self.screen, text="Submit", height="2", width="15",bg="white",command= checks).grid(row=11,column=3)

def run():
    Write = QuestionWrite(screen)
    Write.retrieve()

