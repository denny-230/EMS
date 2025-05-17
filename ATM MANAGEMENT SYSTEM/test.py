from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox








class Employee :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Management System")




        lbl_title=Label(self,root,text='Employee Management System',font=('times new roman', 37,'bold'),fg='darkblue',bg='white')
        lbl_title.pack(x=0,y=0,width=1530,height=60)

    
    
    
if __name__=="__main__":
        root=Tk()
        obj=Employee(tk)
        root.mainloop()


def add_data():
    if var_dep.get()=="" or  var_email.get()=="":
        messagebox.showerror('Error','All fields are required')

        # variable declarations
var_dep=StringVar(),
var_name=StringVar(),
var_designition=StringVar(),
var_email=StringVar(),
var_address=StringVar(),
var_married=StringVar(),
var_dob=StringVar(),
var_doj=StringVar(),
var_idproofcomb=StringVar(),
var_idproof=StringVar(),
var_gender=StringVar(),
var_phone=StringVar(),
var_country=StringVar(),
var_salary=StringVar()

def add_data(self):
     if self.var_dep.get()=="" or self.var_email.get()=="":
       messagebox.showerror('Error','All fields are mandatory')
     else:
        try:
             conn=mysql.connector.connect(host='localhost',username='root',password='Test@123',database='new_data')
             my_cursor=conn.cursor()
             my_cursor.execute('insert into people values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
               
                                                                              self.var_dep.get(),
                                                                              self.var_name.get(),
                                                                              self.var_designition.get(),
                                                                              self.var_email.get(),
                                                                              self.var_address.get(),
                                                                              self.var_married.get(),
                                                                              self.var_dob.get(),
                                                                              self.var_doj.get(),
                                                                              self.var_idproofcomb.get(),
                                                                              self.var_idproof.get(),
                                                                              self.var_gender.get(),
                                                                              self.var_phone.get(),
                                                                              self.var_country.get(),
                                                                              self.var_salaary.get()

                                                                                                       ))                                                                                               
               
               
             conn.commit()
             conn.close()
             messagebox.showinfo('Success','Employ has been added successfully',parent=self.root)                                                                                   
        except Exception as es:
             messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
employee_table.heading('dep',text='Department')
    employee_table.heading('name',text='Name')
    employee_table.heading('designition',text='Designition')
    employee_table.heading('email',text='Email')
    employee_table.heading('address',text='Address')
    employee_table.heading('married',text='Married')
    employee_table.heading('dob',text='DoB')
    employee_table.heading('doj',text='DoJ')
    employee_table.heading('idproof',text='IDproof')
    employee_table.heading('idtype',text='IDtype')
    employee_table.heading('phone',text='Phone')
    employee_table.heading('country',text='Country')
    employee_table.heading('salary',text='Salary')
    employee_table.heading('gender',text='Gender')
