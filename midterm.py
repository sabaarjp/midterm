import tkinter
import json
from tkinter import messagebox

islogin=False
login_user=""
def jread():
    try:
        with open("users.json") as f:
            users=json.load(f)
    except:
        print("users file is damaged!!trying to make a new file")
        users={"admin":"123456789"}
        jwrite(users)
    return users
def jwrite(users):
    with open("users.json",'w')as f:
        json.dump(users,f)
def login():
    try:
        global islogin,login_user
        if(islogin==True):
            lbl5.configure(text="You are already login",fg="red",font=('arial', 12,'bold'))
            return
        if txt_user.get()=="" and txt_passw.get()=="":
            lbl5.configure(text="Enter your username and password!!!",fg="red",font=('arial', 12,'bold'))
        else:
            user=txt_user.get()
            passw=txt_passw.get()
            users=jread()
            if user in users and users[user]==passw:
                islogin=True
                login_user=user
                lbl5.configure(text="Welcome",fg="green",font=('arial', 12,'bold'))
            else:
                lbl5.configure(text="Wrong username or password",fg="red",font=('arial', 12,'bold')) 
            with open("log.json")as f:
                logins=json.load(f)
            if user in logins:
                logins[user]+=1                                                          #for the log file which was not needed in this project
            else:
                logins[user]=1
            with open("log.json",'w')as f:
                json.dump(logins,f)
    except FileNotFoundError:
        print("users file is damaged!!trying to make a new file")
        logins={"admin":1}
        with open("log.json",'w')as f:
            json.dump(logins,f)
def submit():
    try:
        if txt_user.get()=="" and txt_passw.get()=="":
            lbl5.configure(text="Enter your username and password!!!",fg="red",font=('Bold italic', 12, 'bold'))
        else:
            user=txt_user.get()
            passw=txt_passw.get()
            if(len(passw)<8):
                lbl5.configure(text="Password length error",fg="red",font=('Bold italic', 12, 'bold'))
                return
            users=jread()
            if user in users:
                lbl5.configure(text="This user is already exist",fg="red",font=('Bold italic', 12, 'bold'))
                return
            else:
                users[user]=passw
                jwrite(users)
                lbl5.configure(text="Submit done",fg="green",font=('Bold italic', 12, 'bold'))
    except FileNotFoundError:
        print("something went wrong!")
def logout():
    global islogin,login_user
    islogin=False
    login_user=""
    lbl5.configure(text="You are logged out now",fg="green",font=('Bold italic', 12, 'bold'))
    if islogin==False:
        lbl6.configure(text="")           
def delete_account():
    global islogin,login_user
    if islogin==False:
        lbl5.configure(text="Please login first",fg="red",font=('Bold italic', 12, 'bold'))
        return
    if login_user=="admin":
        lbl5.configure(text="Admin account is not removable",fg="red",font=('Bold italic', 12, 'bold'))
        return
    users=jread()
    result=messagebox.askquestion("confirm","Are you sure??")
    if result=="no":
        lbl5.configure(text="Canceld by user",fg="brown",font=('Bold italic', 12, 'bold'))
        return
    elif result=="yes":
        users.pop(login_user)
        jwrite(users)
        islogin=False
        login_user=""
        lbl5.configure(text="Your account successfully deleted",fg="green",font=('Bold italic', 12, 'bold'))        
def user_list():
    if login_user!="admin":
        lbl5.configure(text="Access error \n Just admin can !!\n",fg="red",font=('Bold italic', 12, 'bold'))                
        return
    users=jread()
    x=[]
    for key in users.keys():
        x.append(key)
        lbl6.configure(text= x,fg="black",font=('Bold italic', 13, 'bold'))
############################################frame of project        
win=tkinter.Tk()
win.title('midterm project')
win.geometry('740x530')
#################################################### the labels/entry part
lbl2=tkinter.Label(win,text = "Message Box" ,fg="blue",font=('Bold italic', 10, 'bold'))
lbl2.pack()
lbl2.place(x=400,y=11)
lbl5=tkinter.Label(win,text="",relief="groove")
lbl5.place(height=100,width=330,x=400,y=30,)
lbl2=tkinter.Label(win,text = "Users List" ,fg="blue",font=('Bold italic', 10, 'bold'))
lbl2.pack()
lbl2.place(x = 30,y = 180)
lbl6=tkinter.Label(win,text="",relief="groove")
lbl6.place(height=300,width=700,x=30,y=200,)
lbl2=tkinter.Label(win,text = "Username")
lbl2.pack()
lbl2.place(x=40,y=60)
txt_user =tkinter.Entry(win,width = 30)
txt_user.place(x = 110,y = 60)
lbl3 =tkinter.Label(win,text = "Password") 
lbl3.pack()
lbl3.place(x=40,y=100)
txt_passw =tkinter.Entry(win,width = 30)
txt_passw.pack()
txt_passw.place(x = 110,y =100)
#################################################### buttons part
submit_button = tkinter.Button(win,text = "Submit",font=('arial', 10,'bold'),command=submit).place(x = 40,y = 150)
login_button = tkinter.Button(win,text = "login",font=('arial', 10, 'bold'),command=login).place(x = 100,y = 150)
logout_button = tkinter.Button(win,text = "logout",font=('arial', 10, 'bold'),command=logout).place(x = 150,y = 150)
deletaccount_button = tkinter.Button(win,text = "delete account",font=('arial', 10, 'bold'),command=delete_account).place(x = 207,y = 150)
userlist_button = tkinter.Button(win,text = "user lsit",font=('arial', 10, 'bold'),command=user_list).place(x = 320,y = 150)

win.mainloop()


 
