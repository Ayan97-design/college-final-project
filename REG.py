from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
class Register:

    def __init__(self,root):
        self.root=root
        #background image
        self.bg=ImageTk.PhotoImage(file = "C:\\Users\\Ayan\\Desktop\\projectt\\Images\\image2.jpg") 
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        #left label image
        self.bg1=ImageTk.PhotoImage(file = "C:\\Users\\Ayan\\Desktop\\projectt\\Images\\image3.jpg") 
        left_lbl=Label(self.root,image=self.bg1) 
        left_lbl.place(x=50,y=100,width=470,height=550)

        #main fram@ Register
        frame_Register=Frame(self.root,bg="beige")
        frame_Register.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame_Register,text="Register Here",font=("times new roman",20,"bold"),fg="green",bg="white")
        register_lbl.place(x=20,y=20)
        #entry feilds
        fname=Label(frame_Register,text="Full Name",font=("times now roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=Entry(root)
        fname_entry.place(x=674,y=207)
        #gender
        fname=Label(frame_Register,text="gender",font=("times now roman",15,"bold"),bg="white")
        fname.place(x=50,y=145)

        #fname_entry=Entry(root)
        #fname_entry.place(x=674,y=250)
        
        fname_entry = Label(self.root, text="Gender",width=20,font=("bold", 10))
        var = IntVar()
        Radiobutton(self.root, text="Male",padx = 5, variable=var, value=1).place(x=675,y=250)
        Radiobutton(self.root, text="Female",padx = 20, variable=var, value=2).place(x=730,y=250)
        #age
        fname=Label(frame_Register,text="Age",font=("times now roman",15,"bold"),bg="white")
        fname.place(x=50,y=190)

        fname_entry=Entry(self.root)
        fname_entry.place(x=674,y=295)
        #email
        fname=Label(frame_Register,text="Email",font=("times now roman",15,"bold"),bg="white")
        fname.place(x=50,y=230)

        fname_entry=Entry(self.root)
        fname_entry.place(x=674,y=335)
        #password
        fname=Label(frame_Register,text="Password",font=("times now roman",15,"bold"),bg="white")
        fname.place(x=50,y=270)

        fname_entry=Entry(self.root)
        fname_entry.place(x=674,y=375)

        #checkbutton
        Checkbtn=Checkbutton(frame_Register,text="I agree  all Terms & Conditions",font=("times new roman",15,"bold"))
        Checkbtn.place(x=50,y=340)

        #submit button
        Register_btn=Button(frame_Register,text="Register",fg="white",bg="grey",font=("times new roman",22,)).place(x=50,y=400,anchor="nw",)
                
        #login button
        Login_btn=Button(frame_Register,text="Login",bg="black",fg="white",bd=0,font=("times new roman",32)).place(x=570,y=170)



                #function declaration
        def Register_function(self):
            
            if first_name.get()=="" or last_name.get()=="" or age.get()=="" or city.get()=="" or add.get()=="" or user_name.get()=="" or password.get()=="" or very_pass.get()=="":
    		        messagebox.showerror("Error" , "All Fields Are Required" ,parent=self.root)
		        
            elif password.get() != very_pass.get():
			             messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" ,parent=self.root)

        
            else:messagebox.showinfo("Success" , "Registration Successfull" ,parent=self.root)
					
            print(self.txt_fname.get(),
                    self.txt_gender.get(),
                    self.txt_age.get(),
                    self.txt_Email.get(),
                    self.txt_password.get())
root=Tk()


root.title('Automobilios App')
obj=Register(root)
root.geometry("1200x600")
root.mainloop()