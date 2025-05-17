from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox



class Employee:
 def __init__(self,root):
    self.root=root
    self.root.geometry("1530x790+0+0")
    self.root.title("Employee Management System")

    # variable declarations
    self.var_dep=StringVar()
    self.var_name=StringVar()
    self.var_designition=StringVar()
    self.var_email=StringVar()
    self.var_address=StringVar()
    self.var_married=StringVar()
    self.var_dob=StringVar()
    self.var_doj=StringVar()
    self.var_idproof=StringVar()
    self.var_idtype=StringVar()
    self.var_gender=StringVar()
    self.var_phone=StringVar()
    self.var_country=StringVar()
    self.var_salary=StringVar()


    lbl_title=Label(root,text='Employee Management System',font=('times new roman', 37,'bold'),fg='darkblue',bg='white')
    lbl_title.place(x=0,y=0,width=1530,height=60)

    img_logo=Image.open('colleg_images\\logo1.png')
    img_logo = img_logo.resize((50, 50), Image.LANCZOS)
    self.photo_logo=ImageTk.PhotoImage(img_logo)
    logo=Label(self.root, image=self.photo_logo)
    logo.place(x=380,y=8,width=50,height=50)

    img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
    img_frame.place(x=0,y=60,width=1530,height=160)
 
    img1=Image.open('colleg_images\\education123.jpg')
    img_logo = img_logo.resize((540, 160), Image.LANCZOS)
    self.photo_1=ImageTk.PhotoImage(img1)
    pic=Label(self.root, image=self.photo_1)
    pic.place(x=8,y=65,width=540,height=150)

    img2=Image.open('colleg_images\\education.webp')
    img_logo = img_logo.resize((540, 160), Image.LANCZOS)

    self.photo_2=ImageTk.PhotoImage(img2)
    pic=Label(self.root, image=self.photo_2)
    pic.place(x=525,y=65,width=540,height=150)

    img3=Image.open('colleg_images\\images123.png')
    img_logo = img_logo.resize((535, 150), Image.LANCZOS)

    self.photo_3=ImageTk.PhotoImage(img3)
    pic=Label(self.root, image=self.photo_3)
    pic.place(x=1000,y=65,width=540,height=150)

    #Main Frame
    Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
    Main_frame.place(x=10,y=220,width=1510,height=560)

   # upper frame
    upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information ',font=('times new roman', 11,'bold'),fg='red',)
    upper_frame.place(x=10,y=10,width=1480,height=270)

    # Labels and Entry fields
    lbl_dep=Label(upper_frame,text='Department',font=('arial', 11,'bold'),bg='white')
    lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

    combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial', 11,'bold'),width=17,state='readonly')
    combo_dep['value']=('Select Department','HR','Software Engineer','Manager')
    combo_dep.current(0)
    combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

    # Name
    lbl_Name=Label(upper_frame,font=('arial', 12,'bold'),text='Name:',bg='white')
    lbl_Name.grid(row=0,column=2,padx=2,pady=7,sticky=W)

    txt_Name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial', 11 ,'bold'))
    txt_Name.grid(row=0,column=3,padx=2,pady=7)

    # Designation

    lbl_Designition=Label(upper_frame,font=('arial', 12,'bold'),text='Designition',bg='white')
    lbl_Designition.grid(row=1,column=0,padx=2,pady=7,sticky=W)

    txt_Designition=ttk.Entry(upper_frame,textvariable=self.var_designition,width=22,font=('arial',11,'bold'))
    txt_Designition.grid(row=1,column=1,padx=2,pady=7)

    # Email
    lbl_email=Label(upper_frame,font=('arial', 12,'bold'),text='Email',bg='white')
    lbl_email.grid(row=1,column=2,padx=2,pady=7,sticky=W)
 
    txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=('arial',11,'bold'))
    txt_email.grid(row=1,column=3,padx=2,pady=7)

    # Address
    lbl_address=Label(upper_frame,font=('arial', 12,'bold'),text='Address',bg='white')
    lbl_address.grid(row=2,column=0,padx=2,pady=7,sticky=W)

    txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('arial',11,'bold'))
    txt_address.grid(row=2,column=1,padx=2,pady=7)

     # Married
    lbl_maritial_status=Label(upper_frame,text='Maritial Status',font=('arial', 12,'bold'),bg='white')
    lbl_maritial_status.grid(row=2,column=2,padx=2,sticky=W)

    combo_txt_maritial=ttk.Combobox(upper_frame,textvariable=self.var_married,font=('arial', 12,'bold'),width=18,state='readonly')
    combo_txt_maritial['value']=(' Maritial Status','Married','Unmarried')
    combo_txt_maritial.current(0)
    combo_txt_maritial.grid(row=2,column=3,padx=2,pady=10,sticky=W)

     # DOB
    lbl_dob=Label(upper_frame,font=('arial', 12,'bold'),text='DOB:',bg='white')
    lbl_dob.grid(row=3,column=0,padx=2,pady=7,sticky=W)

    txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=('arial',11,'bold'))
    txt_dob.grid(row=3,column=1,padx=2,pady=7)

    # DOJ
    lbl_doj=Label(upper_frame,font=('arial', 12,'bold'),text='DOJ:',bg='white')
    lbl_doj.grid(row=3,column=2,padx=2,pady=7,sticky=W)

    txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=('arial',11,'bold'))
    txt_doj.grid(row=3,column=3,padx=2,pady=7)

    # id proof

    combo_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_idtype,font=('arial', 12,'bold'),width=17,state='readonly')
    combo_txt_proof['value']=('Select ID Proof','Pan Crad','Aadhar Card','Driving license')
    combo_txt_proof.current(0)
    combo_txt_proof.grid(row=4,column=0,padx=2,pady=7,sticky=W)

    txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=22,font=('arial',11,'bold'))
    txt_proof.grid(row=4,column=1,padx=2,pady=7)

    # Gender
    lbl_gender=Label(upper_frame,text='Gender',textvariable=self.var_gender,font=('arial', 12,'bold'),bg='white')
    lbl_gender.grid(row=4,column=2,padx=2,sticky=W)

    combo_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,font=('arial', 12,'bold'),width=18,state='readonly')
    combo_txt_gender['value']=(' Select Gender','Male','female','Others')
    combo_txt_gender.current(0)
    combo_txt_gender.grid(row=4,column=3,padx=2,pady=10,sticky=W)

    # Phone
    lbl_phone=Label(upper_frame,font=('arial', 12,'bold'),text='Phone:',bg='white')
    lbl_phone.grid(row=0,column=4,padx=2,pady=7,sticky=W)

    txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=('arial',11,'bold'))
    txt_phone.grid(row=0,column=5,padx=2,pady=7)

    # Country
    lbl_country=Label(upper_frame,font=('arial', 12,'bold'),text='Country:',bg='white')
    lbl_country.grid(row=1,column=4,padx=2,pady=7,sticky=W)

    txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=('arial',11,'bold'))
    txt_country.grid(row=1,column=5,padx=2,pady=7)

    # CTC
    lbl_ctc=Label(upper_frame,font=('arial', 12,'bold'),text='CTC:',bg='white')
    lbl_ctc.grid(row=2,column=4,padx=2,pady=7,sticky=W)

    txt_ctc=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=('arial',11,'bold'))
    txt_ctc.grid(row=2,column=5,padx=2,pady=7)

    # Inserted Image
    img6=Image.open('colleg_images\\einstein.jpeg')
    img_logo = img_logo.resize((220, 220), Image.LANCZOS)
    self.photo_6=ImageTk.PhotoImage(img6)
    pic6=Label(self.root, image=self.photo_6)
    pic6.place(x=1000,y=260,width=220,height=220)

   # Buttons Frames
    button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
    button_frame.place(x=1290,y=10,width=170,height=210)

    # Add Buttons
    btn_add=Button(button_frame,text='Save',command=self.add_data,font=('arial', 15,'bold'),width=13,fg='white',bg='blue')
    btn_add.grid(row=0,column=0,padx=1,pady=5)

    btn_update=Button(button_frame,text='Update',font=('arial', 15,'bold'),width=13,fg='white',bg='blue')
    btn_update.grid(row=1,column=0,padx=1,pady=5)

    btn_delete=Button(button_frame,text='Delete',font=('arial', 15,'bold'),width=13,fg='white',bg='blue')
    btn_delete.grid(row=2,column=0,padx=1,pady=5)

    btn_clear=Button(button_frame,text='Clear',font=('arial', 15,'bold'),width=13,fg='white',bg='blue')
    btn_clear.grid(row=3,column=0,padx=1,pady=5) 
   








   #down frame
    down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information Table',font=('times new roman', 11,'bold'),fg='red',)
    down_frame.place(x=10,y=280,width=1480,height=270)

   #   search frame
    search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text=' Search Employee Information ',font=('times new roman', 11,'bold'),fg='red',)
    search_frame.place(x=0,y=0,width=1470,height=60)

    search_by=Label(search_frame,font=('arial', 12,'bold'),text='Search by',fg='white',bg='red')
    search_by.grid(row=0,column=0,padx=2,pady=7,sticky=W)

    combo_txt_search=ttk.Combobox(search_frame,font=('arial', 12,'bold'),width=17,state='readonly')
    combo_txt_search['value']=('Phone','Aadhar Card')
    combo_txt_search.current(0)
    combo_txt_search.grid(row=0,column=1,padx=7,sticky=W)

    txt_search=ttk.Entry(search_frame,width=22,font=('arial',11,'bold'))
    txt_search.grid(row=0,column=2,padx=7)

    btn_search=Button(search_frame,width=14,font=('arial',11,'bold'),text='Search',bg='blue',fg='white')
    btn_search.grid(row=0,column=3,padx=5)

    btn_showall=Button(search_frame,width=14,font=('arial',11,'bold'),text='Show All',bg='blue',fg='white')
    btn_showall.grid(row=0,column=4,padx=5)

  # Employee Tables

    table_frame=Frame(down_frame,bd=2,relief=RIDGE)
    table_frame.place(x=0,y=60,width=1470,height=560)

  # scroll bar

    scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
  # Creation of table

    self.employee_table=ttk.Treeview(table_frame,column=('dep','name','designition','email','address','married','dob','doj','idproof','idtype','phone','country','salary','gender'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=self.employee_table.xview)
    scroll_y.config(command=self.employee_table.yview)

    self.employee_table.heading('dep',text='Department')
    self.employee_table.heading('name',text='Name')
    self.employee_table.heading('designition',text='Designition')
    self.employee_table.heading('email',text='Email')
    self.employee_table.heading('address',text='Address')
    self.employee_table.heading('married',text='Married')
    self.employee_table.heading('dob',text='DoB')
    self.employee_table.heading('doj',text='DoJ')
    self.employee_table.heading('idproof',text='IDproof')
    self.employee_table.heading('idtype',text='IDtype')
    self.employee_table.heading('phone',text='Phone')
    self.employee_table.heading('country',text='Country')
    self.employee_table.heading('salary',text='Salary')
    self.employee_table.heading('gender',text='Gender')

    self.employee_table['show']='headings'

    self.employee_table.column('dep',width=100)
    self.employee_table.column('name',width=100)
    self.employee_table.column('designition',width=100)
    self.employee_table.column('email',width=100)
    self.employee_table.column('address',width=100)
    self.employee_table.column('married',width=100)
    self.employee_table.column('dob',width=100)
    self.employee_table.column('doj',width=100)
    self.employee_table.column('idproof',width=100)
    self.employee_table.column('idtype',width=100)
    self.employee_table.column('phone',width=100)
    self.employee_table.column('country',width=100)
    self.employee_table.column('salary',width=100)
    self.employee_table.column('gender',width=100)
    self.employee_table.pack(fill=BOTH,expand=1)

 def add_data(self):
     if self.root.var_dep.get()=="" or self.root.var_email.get()=="":
       messagebox.showerror('Error','All fields are mandatory')
     else:
        try:
             conn=mysql.connector.connect(host='localhost',username='root',password='Test@123',database='new_data')
             my_cursor=conn.cursor()
             my_cursor.execute('insert into person values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
               
                                                                              self.var_dep.get(),
                                                                              self.var_name.get(),
                                                                              self.var_designition.get(),
                                                                              self.var_email.get(),
                                                                              self.var_address.get(),
                                                                              self.var_married.get(),
                                                                              self.var_dob.get(),
                                                                              self.var_doj.get(),
                                                                              self.var_idproof.get(),
                                                                              self.var_idtype.get(),
                                                                              self.var_gender.get(),
                                                                              self.var_phone.get(),
                                                                              self.var_country.get(),
                                                                              self.var_salary.get()

                                                                                                       ))                                                                                               
               
               
             conn.commit()
             conn.close()
             messagebox.showinfo('Success','Employ has been added successfully',parent=root)                                                                                   
        except Exception as es:
             messagebox.showerror('Error',f'Due To:{str(es)}',parent=root)


               

     

    





if __name__=="__main__":
    root=Tk()
    object=Employee(root)
    root.mainloop()
