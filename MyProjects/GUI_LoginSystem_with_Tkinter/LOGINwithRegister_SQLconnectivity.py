
# coding: utf-8

# In[45]:


from tkinter import *
from  PIL import ImageTk
from tkinter import messagebox
import mysql.connector
import re
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
    
    ## New user registration
    
        new_user=Button(Frame_login,text=" New user? Register here! ",command=self.register,fg="brown",bg="white",bd=0,font=("garamond",14,"bold")).place(x=110,y=330,width=300,height=30)
        
    ## Login button
    
        Login_button=Button(self.root,command=self.login_function,text="Login ",fg="white",bg="brown",font=("garamond",20,"bold")).place(x=490,y=480,width=160,height=40)
    
    ## registration window
    
    def register(self):
        
        ## initialization of window
        
        global registerWindow
        registerWindow=Toplevel()
        registerWindow.title("New user registration")
        registerWindow.geometry("600x400")
        registerWindow.configure(bg="white")
        registerWindow.resizable(False,False)
        
        ## adding image and labels
        
        pyimage2=Label(registerWindow,image=self.logo).place(x=250,y=20,width=100,height=100)
        
        name=Label(registerWindow,text="Name",font=("times new roman",14),fg="black",bg="white").place(x=100,y=150)
        self.username=Entry(registerWindow,font=("times new roman",14), bg="lightgrey")
        self.username.place(x=280,y=150,width=250)
        
        email=Label(registerWindow,text="Email ID",font=("times new roman",14),fg="black",bg="white").place(x=100,y=200)
        self.useremail=Entry(registerWindow,font=("times new roman",14), bg="lightgrey")
        self.useremail.place(x=280,y=200,width=250)
        
        password=Label(registerWindow,text="Your Password",font=("times new roman",14),fg="black",bg="white").place(x=100,y=250)
        self.user_pass=Entry(registerWindow,font=("times new roman",14), bg="lightgrey")
        self.user_pass.place(x=280,y=250,width=250)
        
        confirm_password=Label(registerWindow,text="Confirm Password",font=("times new roman",14),fg="black",bg="white").place(x=100,y=300)
        self.userpass_confirm=Entry(registerWindow,font=("times new roman",14),show='*', bg="lightgrey")
        self.userpass_confirm.place(x=280,y=300,width=250)
        
        ## registration button
        
        reg=Button(registerWindow,text=" Register ",command=self.register_function,fg="brown",bg="white",font=("garamond",18,"bold")).place(x=160,y=350,width=300,height=40)
        
    def login_function(self):
        if (self.txt_pass.get()=="" or self.txt_user.get()==""):
            messagebox.showerror("Error","All fields are required for authentication",parent=self.root)
        elif (self.txt_pass.get()!="1234" or self.txt_user.get()!="Abhishek"):
            messagebox.showinfo("Error","Invalid Username/Password",parent=self.root)
        else:
            messagebox.showinfo("Welcome",f"Welcome, {self.txt_user.get()}\nAuthentication successfull !",parent=self.root)
            
        
            
    def register_function(self):
        
        ## connecting to SQL database
        
        con=mysql.connector.connect(host="localhost",user="root",password="",database="mysql")
        cur=con.cursor(buffered=True)
        insert=("insert into register (name,useremail,password,confirm_password) values(%s,%s,%s,%s)")
        values=[self.username.get(),self.useremail.get(),self.user_pass.get(),self.userpass_confirm.get()]
        cur.execute(insert,values)
        
        # boolean variables to check validity of user entry,set to False
        
        c1=False
        c2=False
        
        if((bool(re.match('^[a-zA-Z0-9]*$',self.username.get()))==False) or ('@' not in self.useremail.get())):
            c2=True
            messagebox.showerror("Error",f"Invalid Username/Email ID, check again!",parent=self.root)
        if(self.username.get()=="" or self.user_pass.get()=="" or self.useremail.get()=="" or self.userpass_confirm==""):
            messagebox.showerror("Error","All fields are required for registration",parent=self.root)
        if(self.user_pass.get()!=self.userpass_confirm.get()):
            c=True
            messagebox.showerror("Error","Passwords do not match, please retry!",parent=self.root)
        if(c1==False and c2==False and self.username.get()!="" and self.user_pass.get()!="" and self.useremail.get()!="" and (self.userpass_confirm.get()==self.user_pass.get())):
            
            ## executing SQL query to find an entry
            
            cur.execute('SELECT useremail FROM register WHERE useremail= %s',(self.useremail.get(),))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","User already exists,login via your credentials!",parent=self.root)
            else:
                con.commit()
                con.close()
                messagebox.showinfo("Registration",f"Welcome to Python World, you are successfully registered! Login with your credentials..",parent=self.root)
                registerWindow.destroy()
                
                
          
root=Tk()
obj=Login(root)
root.mainloop()

# GO THROUGH README FILE TO CHECK HOW THE APPLICATION LOOKS

