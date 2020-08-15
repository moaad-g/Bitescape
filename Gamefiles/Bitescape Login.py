from tkinter import *
from tkinter import messagebox as ms
import time
import sqlite3
import os
from passlib.hash import sha256_crypt
#------------------------------------------------------------------------------------------------------------------------------------------------#
#Creates database if it doesnt already exist in the same folder as the game
if not os.path.isfile("GameData2.db"):
            Database= sqlite3.connect("GameData2.db")
            c= Database.cursor()
            
            c.execute('''CREATE TABLE IF NOT EXISTS "User" (
            "Username"	TEXT NOT NULL UNIQUE,
            "Password"	TEXT NOT NULL,
            "Firstname"	TEXT NOT NULL,
            "Surname"	TEXT NOT NULL,
            "DateOfBirth" TEXT,
            PRIMARY KEY("Username")
            );''')
            
            c.execute('''CREATE TABLE IF NOT EXISTS "Points" (
            "Username" TEXT,
            "Level1points" INTEGER,
            "Level2points" INTEGER,
            "Level3points" INTEGER,
            "Level4points" INTEGER,
            "Level5points" INTEGER,
            "Level6points" INTEGER,
            FOREIGN KEY ("Username") REFERENCES "User"("Username")
            PRIMARY KEY ("Username")
            );''')

            c.execute('''CREATE TABLE IF NOT EXISTS Progress
            (Username TEXT,
            "Level" INTEGER,
            "Level2" INTEGER,
            "Level3" INTEGER,
            "Level4" INTEGER,
            "Level5" INTEGER,
            "Level6" INTEGER,
            FOREIGN KEY ("Username") REFERENCES "User"("Username")
            PRIMARY KEY ("Username")
            );''')
      
            Database.commit()
            Database.close()

#Creates text if it doesnt already exist in the same folder as the game            
if not os.path.isfile("Player_Details"):
        file = open("Player_Profile.txt","w+") 
#------------------------------------------------------------------------------------------------------------------------------------------------#
screen= Tk()            
class LoginRegister:
    def __init__(self, screen):
        self.username = StringVar()
        self.password = StringVar()
        self.username_reg = StringVar()
        self.password_reg = StringVar()
        self.password_reg_confirm = StringVar()
        self.firstname_reg = StringVar()
        self.surname_reg = StringVar()
        self.D_in = StringVar()
        self.M_in = StringVar()
        self.Y_in = StringVar()
        

    def main_menu(self):
        #functions which close the main menu window before directing the user to the desired tab
        def to_reg():
            mainscreen.destroy()
            self.register()
        def to_log():
            mainscreen.destroy()
            self.login()


        screen.withdraw()    
        mainscreen=Toplevel(screen)
        #size of screen
        mainscreen.geometry("280x200")
        #label of window
        mainscreen.title("Menu")
        
        Label(mainscreen, text="BITESCAPE" , font = ("Arial", 20)).pack()
        Label(mainscreen,text="",width="640").pack()
        
        Button(mainscreen,text="Login",height="2",width="15",bg= "white",command= to_log).pack()
        Label(mainscreen,text="",width="640").pack()
        
        Button(mainscreen,text="Register",height="2", width="15",bg= "white",command= to_reg).pack()
 #------------------------------------------------------------------------------------------------------------------------------------------------#       
    def login(self):
        def dbcheck():
            screen.withdraw() 
            username= (self.username.get())
            password= (self.password.get())
            
            print(password)
            if username == "" or password== "":
                ms.showerror("ERROR","Please ensure all fields have been completed")
            else:
                Database= sqlite3.connect("GameData2.db")
                c= Database.cursor()
                c.execute('''SELECT * FROM User WHERE Username= ?''',(username,))
                result = c.fetchall()
                print (result)
                if  str(result) == "[]":
                     ms.showerror("ERROR","Username invalid.")
                verify = sha256_crypt.verify(password,result[0][1])
                if  verify == False:
                     ms.showerror("ERROR","Password invalid.")
                else:
                    ms.showinfo("","Loading Game...")
                    file = open("Player_Profile.txt","w")
                    file.write(username)
                    file.close()
                    logscreen.destroy()
                    import Bitescape
            
        logscreen = Toplevel(screen)
        logscreen.geometry("280x200")
        logscreen.title("Login")
        #Username_Input
        Label(logscreen, text="Username:").pack()
        Entry(logscreen, textvariable = self.username).pack()
        #Password_Input
        Label(logscreen, text="Password:").pack()
        Entry(logscreen, textvariable = self.password).pack()
        Label(logscreen, text="").pack()
        Button(logscreen, text="->", height="1", width="7",bg="white",command=dbcheck).pack()

 #------------------------------------------------------------------------------------------------------------------------------------------------#
    def register(self):
            #------------------------Binary Search-----------------------#
            def Search_For_Prohibited_Text(prohibited_list, list_length, list_rear, word_input):
                    if list_rear >= list_length: 
                        mid = int(list_length + (list_rear - list_length)/2)
        
                        if prohibited_list[mid] == word_input: 
                            return True 
                        elif prohibited_list[mid] > word_input: 
                            return Search_For_Prohibited_Text(prohibited_list, list_length, mid-1, word_input) 
                        else: 
                            return Search_For_Prohibited_Text(prohibited_list, mid+1, list_rear, word_input) 
                    else: 
                        return False

            def prohibited_text(word_input):
                word_input = word_input.lower()
                with open("Prohibited_Words.txt","r") as Prohibited_File:
                        prohibited_list_1 = Prohibited_File.readlines()

                        prohibited_list = []
                        for x in range (0,(len(prohibited_list_1))):
                            word = (prohibited_list_1[x][0:(len(prohibited_list_1[x])-1)])
                            prohibited_list.append(word)
                            username_prohibited = Search_For_Prohibited_Text(prohibited_list, 0, len(prohibited_list)-1, word_input)
                        return username_prohibited
            #------------------------------------------------------------------#
            def usernameandpasswordcheck():
                #retrieves the username password etc.
                username_input= (self.username_reg.get())
                password_input= (self.password_reg.get())
                password_confirm= (self.password_reg_confirm.get())
                fname=(self.firstname_reg.get())
                sname=(self.surname_reg.get())
                fname = fname.upper()
                sname = sname.upper()
                DOB= ((self.D_in.get())+"/"+(self.M_in.get())+"/"+(self.Y_in.get()))
                username_prohibited = prohibited_text(username_input)
                #open database
                Database= sqlite3.connect("GameData2.db")
                c= Database.cursor()
                #checks for blank inputs
                if username_prohibited == True:
                    ms.showerror("ERROR","username prohibited")
                else:
                    if username_input=="" or password_input=="" or password_confirm=="":
                        ms.showerror("ERROR","Please ensure all fields have been completed")
                    elif password_input != password_confirm:
                        ms.showerror("ERROR","Password you entered is different")
                    else:
                        #Checks database for username input
                        c.execute('''SELECT * FROM User WHERE Username= ?''',(username_input,))
                        result=c.fetchall()

                        if str(result) == "[]":
                            password_input = sha256_crypt.hash(password_input)
                            c.execute('''INSERT INTO User
                            VALUES (?,?,?,?,?)''',(username_input,password_input,fname,sname,DOB))
                            c.execute('''INSERT INTO Points
                            VALUES (?,?,?,?,?,?,?)''',(username_input,0,0,0,0,0,0))
                            c.execute('''INSERT INTO Progress
                            VALUES (?,?,?,?,?,?,?)''',(username_input,0,0,0,0,0,0))
                            ms.showinfo("","Registration Successful, Close Screen")
                            Database.commit()
                            Database.close()
                            self.main_menu()
                        else:
                            ms.showerror("ERROR","Username Taken")
                              
            def personalinfocheck():
                #retrieves the inputs and stores in local variables
                fname=(self.firstname_reg.get())
                sname=(self.surname_reg.get())
                DOB= ((self.D_in.get())+"/"+(self.M_in.get())+"/"+(self.Y_in.get()))  
                #sets names to uppercase
                fname = fname.upper()
                sname = sname.upper()
                #checks for blank inputs (if any are blank then the program returns an error)
                if (fname == "" or sname == "") or (DOB=="//"):
                    ms.showerror("ERROR","Please ensure all fields have been completed")
                    
                
                else:
                    #opens database and checks for a matching firstname and surname already in the database(BOTH have to match)
                    Database= sqlite3.connect("GameData2.db")
                    c= Database.cursor()
                    c.execute('''SELECT * FROM User WHERE Firstname= ? AND Surname= ?''',(fname,sname,))
                    result=c.fetchall()
                    Database.close()
                    
                    if str(result) == "[]":
                        #closes previous registration screen
                        regscreen.destroy()
                        #if there are no matching rows then the user can input a username and password
                        rcompscreen = Toplevel(screen)
                        rcompscreen.geometry("280x200")
                        rcompscreen.title("Complete registration")
                        Label(rcompscreen, text="Username:                            (case sensitive)").pack()
                        Entry(rcompscreen, textvariable = self.username_reg).pack()
                        Label(rcompscreen, text="Password:                            (case sensitive)").pack()
                        Entry(rcompscreen, textvariable = self.password_reg).pack()
                        Label(rcompscreen, text="Confirm Password:                            (case sensitive)").pack()
                        Entry(rcompscreen, textvariable = self.password_reg_confirm).pack()
                        Label(rcompscreen, text="").pack()
                        Button(rcompscreen, text="Complete registration",height="3", width="30",bg= "white", command= usernameandpasswordcheck).pack()

                    else:
                        ms.showerror("ERROR","User Already Exists")

            #registration_screen_setup
            regscreen = Toplevel(screen)
            regscreen.geometry("280x200")
            regscreen.title("Register")
            #Firstname_entry
            Label(regscreen, text="Firstname:").grid(row=0,column=1)
            Entry(regscreen, textvariable = self.firstname_reg).grid(row=1,column=1)
            #Surname_entry
            Label(regscreen, text="Surname:").grid(row=2,column=1)
            Entry(regscreen, textvariable = self.surname_reg).grid(row=3,column=1)
            #Date_Of_Birth_entry
            Label(regscreen, text="Date Of Birth (DD/MM/YY):").grid(row=6,column=1)
            dayentry= OptionMenu(regscreen, self.D_in, "01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","24","25","26","27","28","29","30","31")
            monthentry= OptionMenu(regscreen, self.M_in, "Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
            yearentry= OptionMenu(regscreen, self.Y_in, "2000","2001","2002","2003","2004","2005","2006","2007")
            dayentry.grid(row=7, column= 0)
            monthentry.grid(row=7, column= 1)
            yearentry.grid(row=7, column= 2)
            #usernameandpasswordentry
            Button(regscreen, text="Check For User", height="2", width="15",bg="white",command= personalinfocheck).grid(row=9,column=1)


#------------------------------------------------------------------------------------------------------------------------------------------------#
 #instantiates object 'Display' in LoginRegister Class
#calls method main_menu()
file = open("Player_Profile.txt","w")
file.writelines("")
file.close()
Display= LoginRegister(screen)
Display.main_menu()
