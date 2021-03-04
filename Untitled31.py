
# coding: utf-8

# In[149]:


from tkinter import *
from  PIL import ImageTk
from tkinter import messagebox
class Login:
    def __init__(self,root):
    # pass initializer
        self.root=root
        self.root.title("Python Login System")
        self.root.geometry("1200x600")
        self.root.resizable(False,False)
    # image loader
        self.bg=ImageTk.PhotoImage(file="C:/Users/COMPUTER/Desktop/LoginSystemPython/background_image.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        self.logo=ImageTk.PhotoImage(file="C:/Users/COMPUTER/Desktop/LoginSystemPython/pylogo.jpg")
        
    # Login Frame
    
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=320,y=100,height=400,width=500)
        title=Label(Frame_login,text=" Authentication", font=("Impact",30,"bold"),fg="brown",bg="white").place(x=125,y=30)
        pyimage=Label(Frame_login,image=self.logo).place(x=200,y=90,width=100,height=100)
        
    ## Username field
        
        lbl_user=Label(Frame_login,text="Username", font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=90,y=190)
        self.txt_user=Entry(Frame_login,font=("times new roman",15), bg="lightgrey")
        self.txt_user.place(x=90,y=220,width=350,height=35)
    
    ## Password field
    
        lbl_pass=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=90,y=260)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),show="*", bg="lightgrey")
        self.txt_pass.place(x=90,y=290,width=350,height=35)
        
    ## Login button
        Login_button=Button(self.root,command=self.login_function,text="Login ",fg="white",bg="brown",font=("garamond",20,"bold")).place(x=490,y=480,width=160,height=40)
    
    def login_function(self):
        if (self.txt_pass.get()=="" or self.txt_user.get()==""):
            messagebox.showerror("Error","All fields are required for authentication",parent=self.root)
        elif (self.txt_pass.get()!="1234" or self.txt_user.get()!="Abhishek"):
            messagebox.showinfo("Error","Invalid Username/Password",parent=self.root)
        else:
            messagebox.showinfo("Welcome",f"Welcome, {self.txt_user.get()}\nAuthentication successfull !",parent=self.root)
            
root=Tk()
obj=Login(root)
root.mainloop()

