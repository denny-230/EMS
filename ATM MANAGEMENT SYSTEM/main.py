import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
current_balance=1000


class SampleApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.shared_data={'Balance':tk.IntVar()}
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage,WithdrawPage,DepositPage,BalancePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        self.controller.title('Securitex')
        self.controller.state('zoomed')
        self.controller.iconphoto(False,
                              tk.PhotoImage(file='C:/Users/Mohd Danish/Documents/Employee_Management_Project/ATM MANAGEMENT SYSTEM/atm-machine.png') )

        headingLabel1=tk.Label(self,
                             text='Infinity ATM',
                              font=('orbitron',45,'bold'),
                               foreground='white',
                               background='#3d3d5c')

        headingLabel1.pack(pady=25)
        space_label=tk.Label(self,height=4,bg='#3d3d5c')
        space_label.pack()

        password_label=tk.Label(self,
                                 text='Enter your password',
                                 font=('orbitron',13),
                                 bg='#3d3d5c',
                                 fg='#ffffff')
        password_label.pack()
        my_password=tk.StringVar()
        password_entry_box=tk.Entry(self,
                                    textvariable=my_password,
                                    font=('orbitron',12),
                                    width=22)
        password_entry_box.focus_set                           
        password_entry_box.pack(ipady=7) 
        def handle_focus_in(_):
            password_entry_box.configure(fg='black',show='*') 

        password_entry_box.bind('<FocusIn>',handle_focus_in)

        def check_password():
         if my_password.get()=='123':
            my_password.set('')
            incorrect_password_label['text']=''
            controller.show_frame('MenuPage')
         else:
                 incorrect_password_label['text']='Incorrect Password'

        enter_button=tk.Button(self,
                               text='ENTER',
                               command=check_password,
                                relief='raised',
                                borderwidth=3,
                                width=40,
                                height=3) 
        enter_button.pack(pady=10) 
        incorrect_password_label=tk.Label(self,
                                          text='',
                                          font=('orbitron',13),
                                          fg='white',
                                          bg='#33334d',
                                        anchor='n')  
        incorrect_password_label.pack(fill='both',expand=True)

        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3) 
        bottom_frame.pack(fill='x',side='bottom')

        visa_photo=tk.PhotoImage(file='C:/Users/Mohd Danish/Documents/Employee_Management_Project/ATM MANAGEMENT SYSTEM/visa.png')   
        visa_label=tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image=visa_photo 
    
        mastercard_photo=tk.PhotoImage(file='C:/Users/Mohd Danish/Documents/Employee_Management_Project/ATM MANAGEMENT SYSTEM/credit-card.png')   
        mastercard_label=tk.Label(bottom_frame,image=mastercard_photo)
        
        mastercard_label.pack(side='left')
        mastercard_label.image=mastercard_photo

        money_photo=tk.PhotoImage(file='C:/Users/Mohd Danish/Documents/Employee_Management_Project/ATM MANAGEMENT SYSTEM/money.png')   
        money_label=tk.Label(bottom_frame,image=money_photo)
        money_label.pack(side='left')
        money_label.image=money_photo



class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        headingLabel2=tk.Label(self,
                             text='Infinity ATM',
                              font=('orbitron',45,'bold'),
                               foreground='white',
                               background='#3d3d5c')

        headingLabel2.pack(pady=25)

        mainmenu_label=tk.Label(self,
                                 text='Main Menu',
                                 font=('orbitron',13),
                                 bg='#3d3d5c',
                                 fg='white')
        mainmenu_label.pack() 

        selection_label=tk.Label(self,
                                 text='Please make a selection',
                                 font=('orbitron',13),
                                 bg='#3d3d5c',
                                 fg='white',
                                 anchor='w') 
        selection_label.pack(fill='x')

        button_frame=tk.Frame(self,bg='#33334d') 
        button_frame.pack(fill='both',expand='True') 

        def withdraw():
         
                  controller.show_frame('WithdrawPage')
         

        withdraw_button=tk.Button(button_frame,
                               text='Withdraw',
                               command=withdraw,
                                relief='raised',
                                borderwidth=3,
                                width=40,
                                height=3) 
        withdraw_button.grid(row=0,column=0,pady=5) 

        def deposit():
         
                  controller.show_frame('DepositPage')
         

        deposit_button=tk.Button(button_frame,
                               text='Deposit',
                               command=deposit,
                                relief='raised',
                                borderwidth=3,
                                width=40,
                                height=3) 
        deposit_button.grid(row=1,column=0,pady=5) 

        def balance():
         
                  controller.show_frame('BalancePage')
         

        balance_button=tk.Button(button_frame,
                               text='Balance',
                               command=balance,
                                relief='raised',
                                borderwidth=3,
                                width=40,
                                height=3) 
        balance_button.grid(row=2,column=0,pady=5) 

        def exit():
         
                  controller.show_frame('StartPage')
         

        exit_button=tk.Button(button_frame,
                               text='exit',
                               command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=40,
                                height=3) 
        exit_button.grid(row=3,column=0,pady=5)  




        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3) 
        bottom_frame.pack(fill='x',side='bottom')

        visa_photo=tk.PhotoImage(file='C:/Users/Mohd Danish/Documents/Employee_Management_Project/ATM MANAGEMENT SYSTEM/visa.png')   
        visa_label=tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image=visa_photo 
    
        mastercard_photo=tk.PhotoImage(file='C:/Users/Mohd Danish/Documents/Employee_Management_Project/ATM MANAGEMENT SYSTEM/credit-card.png')   
        mastercard_label=tk.Label(bottom_frame,image=mastercard_photo)
        
        mastercard_label.pack(side='left')
        mastercard_label.image=mastercard_photo

        money_photo=tk.PhotoImage(file='C:/Users/Mohd Danish/Documents/Employee_Management_Project/ATM MANAGEMENT SYSTEM/money.png')   
        money_label=tk.Label(bottom_frame,image=money_photo)
        money_label.pack(side='left')
        money_label.image=money_photo

        

        




        
        


class WithdrawPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        headingLabel3=tk.Label(self,
                             text='Infinity ATM',
                              font=('orbitron',45,'bold'),
                               foreground='white',
                               background='#3d3d5c')

        headingLabel3.pack(pady=25)

        amount_label=tk.Label(self,
                                 text='Choose the amount you want to withdraw',
                                 font=('orbitron',13),
                                 bg='#3d3d5c',
                                 fg='white')
        amount_label.pack()
        button_frame=tk.Frame(self,bg='#33334d') 
        button_frame.pack(fill='both',expand='True') 

        def withdraw(amount):

           global current_balance
           current_balance-=amount
           controller.shared_data['Balance'].set(current_balance)
           controller.show_frame('MenuPage')

        hundred_button=tk.Button(button_frame,
                               text='100',
                               command=lambda:withdraw(100),
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5) 
        hundred_button.grid(row=0,column=0,pady=5)

        twohundred_button=tk.Button(button_frame,
                               text='200',
                               command=lambda:withdraw(200),
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5) 
        twohundred_button.grid(row=1,column=0,pady=5)

        fivehundred_button=tk.Button(button_frame,
                               text='500',
                               command=lambda:withdraw(500),
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5) 
        fivehundred_button.grid(row=0,column=1,pady=5,padx=850)

        twothousand_button=tk.Button(button_frame,
                               text='2000',
                               command=lambda:withdraw(2000),
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5) 
        twothousand_button.grid(row=1,column=1,pady=5)

        cash=tk.StringVar()
        other_amount_entry=tk.Entry(button_frame,
                                    textvariable=cash,
                                     width=59,
                                     justify='left')
        other_amount_entry.grid(row=3,column=1,pady=5,ipady=30)

        def other_amount(_):
                  global current_balance
                  current_balance-=int(cash.get())
                  controller.shared_data['Balance'].set(current_balance)
                  cash.set('')
         
                  controller.show_frame('MenuPage')
         
        other_amount_entry.bind('<Return>',other_amount)

        def exit():
                  
                  controller.show_frame('MenuPage')
        exit_button=tk.Button(button_frame,
                               text='Exit',
                               command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5) 
        exit_button.grid(row=2,column=0,pady=5)
        

        



        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3) 
        bottom_frame.pack(fill='x',side='bottom')

        visa_photo=tk.PhotoImage(file='C:/Users/Mohd Danish/Documents/Employee_Management_Project/ATM MANAGEMENT SYSTEM/visa.png')   
        visa_label=tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image=visa_photo 
    
        mastercard_photo=tk.PhotoImage(file='C:/Users/Mohd Danish/Documents/Employee_Management_Project/ATM MANAGEMENT SYSTEM/credit-card.png')   
        mastercard_label=tk.Label(bottom_frame,image=mastercard_photo)
        
        mastercard_label.pack(side='left')
        mastercard_label.image=mastercard_photo

        money_photo=tk.PhotoImage(file='C:/Users/Mohd Danish/Documents/Employee_Management_Project/ATM MANAGEMENT SYSTEM/money.png')   
        money_label=tk.Label(bottom_frame,image=money_photo)
        money_label.pack(side='left')
        money_label.image=money_photo



class DepositPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller 
        headingLabel3=tk.Label(self,
                             text='Infinity ATM',
                              font=('orbitron',45,'bold'),
                               foreground='white',
                               background='#3d3d5c')

        headingLabel3.pack(pady=25)
        space_label=tk.Label(self,height=4,bg='#3d3d5c')
        space_label.pack()

        enteramount_label=tk.Label(self,
                                 text='Enter amount',
                                 font=('orbitron',13),
                                 bg='#3d3d5c',
                                 fg='#ffffff')
        enteramount_label.pack(pady=10)
        cash=tk.StringVar()
        deposit_entry=tk.Entry(self,
                                textvariable=cash,
                                 font=('orbitron',12),
                                width=22,
                                       )
        deposit_entry.pack(ipady=7) 

        def deposit_cash():
                  global current_balance
                  current_balance+=int(cash.get())
                  controller.shared_data['Balance'].set(current_balance)
                  cash.set('')
                  controller.show_frame('MenuPage')
        enter_button=tk.Button(self,
                               text='Enter',
                               command=deposit_cash,
                                relief='raised',
                                borderwidth=3,
                                width=40,
                                height=3) 
        enter_button.pack(pady=10) 

        two_tone_label=tk.Frame(self,bg='#33334d') 
        two_tone_label.pack(fill='both',expand='True')                    

        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3) 
        bottom_frame.pack(fill='x',side='bottom')

        visa_photo=tk.PhotoImage(file='C:/Users/Mohd Danish/Documents/Employee_Management_Project/ATM MANAGEMENT SYSTEM/visa.png')   
        visa_label=tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image=visa_photo 
    
        mastercard_photo=tk.PhotoImage(file='C:/Users/Mohd Danish/Documents/Employee_Management_Project/ATM MANAGEMENT SYSTEM/credit-card.png')   
        mastercard_label=tk.Label(bottom_frame,image=mastercard_photo)
        
        mastercard_label.pack(side='left')
        mastercard_label.image=mastercard_photo

        money_photo=tk.PhotoImage(file='C:/Users/Mohd Danish/Documents/Employee_Management_Project/ATM MANAGEMENT SYSTEM/money.png')   
        money_label=tk.Label(bottom_frame,image=money_photo)
        money_label.pack(side='left')
        money_label.image=money_photo

class BalancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller 

        headingLabel4=tk.Label(self,
                             text='Infinity ATM',
                              font=('orbitron',45,'bold'),
                               foreground='white',
                               background='#3d3d5c')

        headingLabel4.pack(pady=25) 
        global current_balance
        controller.shared_data['Balance'].set(current_balance)
        balance_label=tk.Label(self,
                            textvariable=controller.shared_data['Balance'],
                              font=('orbitron',13),
                               foreground='white',
                               background='#3d3d5c',
                               anchor='w')

        balance_label.pack(fill='x')  
        button_frame=tk.Frame(self,bg='#33334d') 
        button_frame.pack(fill='both',expand='True')

        def menu():
                  
                  controller.show_frame('MenuPage')
        menu_button=tk.Button(button_frame,
                               text='Menu',
                               command=menu,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5) 
        menu_button.grid(row=0,column=0,pady=5) 
        def exit():
                  
                  controller.show_frame('MenuPage')
        exit_button=tk.Button(button_frame,
                               text='Exit',
                               command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5) 
        exit_button.grid(row=1,column=0,pady=5) 


        

        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3) 
        bottom_frame.pack(fill='x',side='bottom')

        visa_photo=tk.PhotoImage(file='C:/Users/Mohd Danish/Documents/Employee_Management_Project/ATM MANAGEMENT SYSTEM/visa.png')   
        visa_label=tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image=visa_photo 
    
        mastercard_photo=tk.PhotoImage(file='C:/Users/Mohd Danish/Documents/Employee_Management_Project/ATM MANAGEMENT SYSTEM/credit-card.png')   
        mastercard_label=tk.Label(bottom_frame,image=mastercard_photo)
        
        mastercard_label.pack(side='left')
        mastercard_label.image=mastercard_photo

        money_photo=tk.PhotoImage(file='C:/Users/Mohd Danish/Documents/Employee_Management_Project/ATM MANAGEMENT SYSTEM/money.png')   
        money_label=tk.Label(bottom_frame,image=money_photo)
        money_label.pack(side='left')
        money_label.image=money_photo 


        

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()