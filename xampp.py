import tkinter
import pymysql
root=tkinter.Tk()
root.title("DB Connectivity")
root.geometry("400x300")

def reset():
    u.set("")
    p.set("")
    e.set("")
 
u=tkinter.StringVar()
p=tkinter.StringVar()
e=tkinter.StringVar()

#-----------------------------------database connectivity------------------
def submit():
    user=u.get()
    pswd=p.get()
    email=e.get()
    mycon=pymysql.connect(host="localhost",user="root",password="",db="std1")
    mycur = mycon.cursor()
    mycur.execute("insert into reg (user,pswd,email) values('"+user+"','"+pswd+"','"+email+"')")
    mycon.commit()
    mycon.close()
    
    if(mycon):
        print("connection succefull")
    else:
        print("connection unsuccefull")


l1=tkinter.Label(root,text="Login page").pack()

user=tkinter.Label(root,text="User",font="Arial 14")
user.place(x=10,y=50)
e1=tkinter.Entry(root,textvariable=u)
e1.place(x=100,y=50)

pswd=tkinter.Label(root,text="passwd",font="Arial 14")
pswd.place(x=10,y=100)
e2=tkinter.Entry(root,textvariable=p)
e2.place(x=100,y=100)

email=tkinter.Label(root,text="email",font="Arial 14")
email.place(x=10,y=150)
e3=tkinter.Entry(root,textvariable=e)
e3.place(x=100,y=150)

b1=tkinter.Button(root,text="Reset",font="Arial 14",command=reset)
b1.place(x=100,y=200)


b2=tkinter.Button(root,text="submit",font="Arial 14",command=submit)
b2.place(x=200,y=200)



root.mainloop()
