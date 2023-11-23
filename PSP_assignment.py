# *********************************************************
# Program: G9.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL1V , TL4V
# Trimester: 2115
# Year: 2021/22 Trimester 1
# Member_1: 1211104786 | NICHOLAS TAN ZHI XUAN TL1V | 0177183063
# Member_2: 1211104977 | TOH KAI RU TL1V | 01111980502
# Member_3: 1211103412 | LAI CHI NYET TL4V | 01126693839
# Member_4: 1211102952 | CHIN WEI KANG TL4V | 01128730664
# *********************************************************
# Task Distribution
# Member_1: Connect Gui with Database
# Member_2: Flowchart planner , Bug Fixer
# Member_3: Gui design
# Member_4: Database planner
# *********************************************************

# IMPORT MODULES #######################################################################################################################################################

from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
connection = mysql.connector.connect(
  host="localhost",
  user="root",
  port='3306',
  password="Tanzhixuan_1217",
  database="psp_assignment_db"
)
c = connection.cursor()

# USER LOGIN PAGE ######################################################################################################################################################

def login_panel_loop():

    global username
    global useremail
    global userpassword
    
    # page design ------------------------------------------------------------------------------------------------------------------------------------------------------
    login_panel=Tk()
    login_panel.title("Covid-19 Vaccination Program")
    login_panel.attributes('-topmost',1)
    login_panel.iconbitmap('vaccination_icon.ico')
    login_panel.resizable(0,0)
    login_panel.config(bg = '#0063b2')
    login_panel.geometry('+200+50')
    
    welcome=Label(login_panel, text="Welcome!",fg ='white' , bg="#0063b2",font="15").grid(row=0,column=1)

    # data entry -------------------------------------------------------------------------------------------------------------------------------------------------------
    username=StringVar()
    username_label=Label(login_panel, text="Username *" ,fg ='white', bg="#0063b2").grid(row=1,column=0)
    username_entry=ttk.Entry(login_panel, textvariable=username,width="30").grid(row=1,column=1)

    useremail=StringVar()
    email_label=Label(login_panel, text="Email *",fg ='white', bg="#0063b2").grid(row=2,column=0)
    email_entry=ttk.Entry(login_panel, textvariable=useremail,width="30").grid(row=2,column=1)

    userpassword=StringVar()
    password_label=Label(login_panel, text="Password *",fg ='white', bg="#0063b2").grid(row=3,column=0)
    password_entry=ttk.Entry(login_panel, textvariable=userpassword,width="30",show="*").grid(row=3,column=1)

    # login button -----------------------------------------------------------------------------------------------------------------------------------------------------
    def from_loginpage_to_menu():
        global get_username
        global get_useremail
        global get_userpassword
        get_username = username.get()
        get_useremail = useremail.get()
        get_userpassword = userpassword.get()
        if get_username == ""  or get_useremail == "" or get_userpassword == "":
            messagebox.showwarning('WARNING','PLEASE COMPLETE ALL FILLING')
        else: 
            c.execute ('SELECT * FROM `registration` where `name` = "%s" and `email` = "%s" and `password` = "%s"'% (get_username , get_useremail , get_userpassword))
            if c.fetchone():
                global user_login
                user_login = get_username
                login_panel.destroy()
                menu_loop()
            else: 
                messagebox.showwarning('WARNING','PLEASE TRY AGAIN')
    login_button=ttk.Button(login_panel, text="Login" , command = from_loginpage_to_menu).grid(row=4,column=1,pady=10)

    Label(login_panel, text=" ", bg="#0063b2").grid(row=5,column=0)

    # register button --------------------------------------------------------------------------------------------------------------------------------------------------
    def from_loginpage_to_registration():
        login_panel.destroy()
        registration_loop()
    register_label=Label(login_panel, text="New user?Here",fg ='white', bg="#0063b2").grid(row=6,column=0)
    register_button=ttk.Button(login_panel, text="Register" , command = from_loginpage_to_registration).grid(row=7,column=0)

    # admin button -----------------------------------------------------------------------------------------------------------------------------------------------------
    def from_loginpage_to_adminlogin():
        login_panel.destroy()
        adminlogin_loop()
    admin_label=Label(login_panel, text="Admin?Here",fg ='white', bg="#0063b2").grid(row=6,column=2)
    admin_button=ttk.Button(login_panel, text="Admin Login" , command = from_loginpage_to_adminlogin).grid(row=7,column=2)

    login_panel.mainloop()

# REGISTRATION  PAGE ###################################################################################################################################################

def registration_loop():

    global name
    global age
    global ic
    global phone
    global postcode
    global address
    global email
    global password

    # page design ------------------------------------------------------------------------------------------------------------------------------------------------------
    registration=Tk()
    registration.title("Registration")
    registration.attributes('-topmost',1)
    registration.iconbitmap('vaccination_icon.ico')
    registration.resizable(0,0)
    registration.config(bg = '#0063b2')
    registration.geometry('+200+50')

    instruction=Label(registration, text="Please fill in the details!", fg = 'white', bg="#0063b2",font="15").grid(row=0,column=1)

    # data entry -------------------------------------------------------------------------------------------------------------------------------------------------------
    name=StringVar()
    name_label=Label(registration, text="Name", fg = 'white', bg="#0063b2").grid(row=1,column=0)
    name_entry=ttk.Entry(registration, textvariable=name,width="60").grid(row=1,column=1)

    age=StringVar()
    age_label=Label(registration, text="Age", fg = 'white', bg="#0063b2").grid(row=2,column=0)
    age_entry=ttk.Entry(registration, textvariable=age,width="60").grid(row=2,column=1)

    ic=StringVar()
    ic_label=Label(registration, text="IC", fg = 'white', bg="#0063b2").grid(row=3,column=0)
    ic_entry=ttk.Entry(registration, textvariable=ic,width="60").grid(row=3,column=1)

    phone=StringVar()
    phone_label=Label(registration, text="Phone", fg = 'white', bg="#0063b2").grid(row=4,column=0)
    phone_entry=ttk.Entry(registration, textvariable=phone,width="60").grid(row=4,column=1)

    postcode=StringVar()
    postcode_label=Label(registration, text="Postcode", fg = 'white', bg="#0063b2").grid(row=5,column=0)
    postcode_entry=ttk.Entry(registration, textvariable=postcode,width="60").grid(row=5,column=1)

    address=StringVar()
    address_label=Label(registration, text="Address", fg = 'white', bg="#0063b2").grid(row=6,column=0)
    address_entry=ttk.Entry(registration, textvariable=address,width="60").grid(row=6,column=1)

    email=StringVar()
    email_label=Label(registration, text="Email", fg = 'white', bg="#0063b2").grid(row=7,column=0)
    email_entry=ttk.Entry(registration, textvariable=email,width="60").grid(row=7,column=1)

    password=StringVar()
    password_label=Label(registration, text="Password", fg = 'white', bg="#0063b2").grid(row=8,column=0)
    password_entry=ttk.Entry(registration, textvariable=password,width="60").grid(row=8,column=1)

    # register button --------------------------------------------------------------------------------------------------------------------------------------------------
    def registersuccess():
        get_name = name.get()
        get_age = age.get()
        get_IC = ic.get()
        get_phone = phone.get()
        get_postcode = postcode.get()
        get_address = address.get()
        get_email = email.get()
        get_password = password.get()         
        if get_name == "" or get_age == "" or get_IC == "" or get_phone == "" or get_postcode == "" or get_address == ""  or get_email == "" or get_password == "":
            messagebox.showwarning('WARNING','PLEASE ENSURE THAT THE INFORMATION ENTERED IS COMPLETE')
        else:
            sql = "INSERT INTO `psp_assignment_db`.`registration` (`IC`, `name`, `age`, `phone`, `postcode`, `address`, `email`, `password`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (get_IC,get_name,get_age,get_phone,get_postcode,get_address,get_email,get_password)
            c.execute(sql,val)
            connection.commit()
            print(c.rowcount, "record inserted.")
            registration.destroy()
            registersuccess_loop()
    register_button=ttk.Button(registration, text="Register" , command = registersuccess).grid(row=9,column=1,pady=10)

    Label(registration, text="          ", bg="#0063b2").grid(row=10,column=2)

    # login page button ------------------------------------------------------------------------------------------------------------------------------------------------
    def from_registration_to_loginpage():
        registration.destroy()
        login_panel_loop()
    Login_page=ttk.Button(registration, text="Login Page" , command = from_registration_to_loginpage).grid(row=11,column=1)

    registration.mainloop()

# REGISTRATION SUCCESS PAGE ############################################################################################################################################

def registersuccess_loop():

    # page design ------------------------------------------------------------------------------------------------------------------------------------------------------
    success= Tk()
    success.title("Registration")
    success.attributes('-topmost',1)
    success.iconbitmap('vaccination_icon.ico')
    success.resizable(0,0)
    success.config(bg = '#0063b2')
    success.geometry('+200+50')

    Label(success, text=" ", fg = 'white', bg="#0063b2").grid(row=0,column=0)
    status=Label(success, text="SUCCESS!", fg = 'white' , bg="#0063b2",font="15").grid(row=1,column=0)
    Label(success, text=" ", fg = 'white', bg="#0063b2").grid(row=2,column=0)
    Label(success, text="Congratulations, your account has been succesfully registered.", fg = 'white', bg="#0063b2").grid(row=3,column=0)
    Label(success, text=" ", fg = 'white', bg="#0063b2").grid(row=4,column=0)

    # login page button ------------------------------------------------------------------------------------------------------------------------------------------------
    def from_success_to_loginpage():
        success.destroy()
        login_panel_loop()
    loginpage_button=Button(success, text="Login Page" , command = from_success_to_loginpage).grid(row=5,column=0)

    success.mainloop()

# ADMIN LOGIN PAGE #####################################################################################################################################################

def adminlogin_loop():

    global adminusername
    global adminemail
    global adminpassword

    # page design ------------------------------------------------------------------------------------------------------------------------------------------------------
    adminlogin=Tk()
    adminlogin.title("Admin Login")
    adminlogin.attributes('-topmost',1)
    adminlogin.iconbitmap('vaccination_icon.ico')
    adminlogin.resizable(0,0)
    adminlogin.config(bg="#0063b2")
    adminlogin.geometry('+200+50')

    welcome=Label(adminlogin, text="Welcome!", fg = 'white', bg="#0063b2",font="15").grid(row=0,column=1)

    # data entry -------------------------------------------------------------------------------------------------------------------------------------------------------
    adminusername=StringVar()
    adminusername_label=Label(adminlogin, text="Username *" , fg = 'white', bg="#0063b2").grid(row=1,column=0)
    adminusername_entry=ttk.Entry(adminlogin, textvariable=adminusername,width="30").grid(row=1,column=1)

    adminemail=StringVar()
    adminemail_label=Label(adminlogin, text="Email *" , fg = 'white', bg="#0063b2").grid(row=2,column=0)
    adminemail_entry=ttk.Entry(adminlogin, textvariable=adminemail,width="30").grid(row=2,column=1)

    adminpassword=StringVar()
    adminpassword_label=Label(adminlogin, text="Password *" , fg = 'white', bg="#0063b2").grid(row=3,column=0)
    adminpassword_entry=ttk.Entry(adminlogin, textvariable=adminpassword,width="30",show="*").grid(row=3,column=1)

    Label(adminlogin, text="          " , fg = 'white', bg="#0063b2").grid(row=4,column=2)

    # login button -----------------------------------------------------------------------------------------------------------------------------------------------------
    def from_adminlogin_to_adminpanel():
        global get_adminusername
        global get_adminemail
        global get_adminpassword
        get_adminusername = adminusername.get()
        get_adminemail = adminemail.get()
        get_adminpassword = adminpassword.get()

        if get_adminusername == "" or get_adminemail == "" or get_adminpassword == "":
            messagebox.showwarning('WARNING','PLEASE COMPLETE ALL FILLING')
        else:
            c.execute ('SELECT * FROM `admin_login` where `admin_name` = "%s" and `admin_email` = "%s" and admin_pass ="%s"'% (get_adminusername , get_adminemail , get_adminpassword))
            if c.fetchone():
                adminlogin.destroy()
                admin_panel_loop()
            else: 
                messagebox.showwarning('WARNING','PLEASE TRY AGAIN')
    login_button=ttk.Button(adminlogin, text="Login" , command = from_adminlogin_to_adminpanel).grid(row=5,column=2)

    # back button ------------------------------------------------------------------------------------------------------------------------------------------------------
    def from_adminlogin_to_loginpage():
        adminlogin.destroy()
        login_panel_loop()
    go_back_btn = ttk.Button(adminlogin, text = 'Back' , command = from_adminlogin_to_loginpage).grid(row = 5 , column = 0)

    adminlogin.mainloop()

# USER MENU PAGE #######################################################################################################################################################

def menu_loop():

    # page design ------------------------------------------------------------------------------------------------------------------------------------------------------
    menu = Tk()
    menu.title("Main Menu")
    menu.attributes('-topmost',1)
    menu.iconbitmap('vaccination_icon.ico')
    menu.resizable(0,0)
    menu.config(bg="#0063b2")
    menu.geometry('+200+50')

    Label(menu, text="    ", fg = 'white', bg="#0063b2").grid(row=0,column=0)

    # update status button ---------------------------------------------------------------------------------------------------------------------------------------------
    def from_menu_to_updatestatus():
        menu.destroy()
        updatestatus_loop()
    update_status = ttk.Button(menu, text="Click me to update your status" , command = from_menu_to_updatestatus).grid(row=1,column=1)

    Label(menu, text="    ", fg = 'white', bg="#0063b2").grid(row=2,column=2)

    # view status button -----------------------------------------------------------------------------------------------------------------------------------------------
    def from_menu_to_viewstatus():
        menu.destroy()
        mystatus_loop()
    view_status = ttk.Button(menu, text="Click me to view your status" , command = from_menu_to_viewstatus).grid(row=3,column=1)

    Label(menu, text="    ", fg = 'white', bg="#0063b2").grid(row=4,column=2)

    # select appointment button -----------------------------------------------------------------------------------------------------------------------------------------
    def from_menu_to_selectappointment():
        menu.destroy()
        appointmentpanel_loop()
    select_appointmnet = ttk.Button(menu, text="Click me to select your appointment" , command = from_menu_to_selectappointment).grid(row=5,column=1)

    Label(menu, text="    ", fg = 'white', bg="#0063b2").grid(row=6,column=2)
    
    # logout button ----------------------------------------------------------------------------------------------------------------------------------------------------
    def from_menu_to_loginpage():
        menu.destroy()
        login_panel_loop()
    logout_button = ttk.Button(menu, text="Logout" , command = from_menu_to_loginpage).grid(row=7,column=1)

    menu.mainloop()

# UPDATE STATUS PAGE ###################################################################################################################################################

def updatestatus_loop():

    global var1
    global var2
    global var3
    global var4
    global var4
    global var6
    global var7
    global var8
    global var9

    # page design ------------------------------------------------------------------------------------------------------------------------------------------------------
    updatestatus=Tk()
    updatestatus.title("Update Status")
    updatestatus.attributes('-topmost',1)
    updatestatus.iconbitmap('vaccination_icon.ico')
    updatestatus.resizable(0,0)
    updatestatus.config(bg="#0063b2")
    updatestatus.geometry('+200+50')

    instruction=Label(updatestatus, text="Please Update Your Current Status!", fg = 'white', bg="#0063b2", font="15").grid(row=0,column=0)

    # data entry -------------------------------------------------------------------------------------------------------------------------------------------------------
    question1_label=Label(updatestatus, text="Question 1: Are you exhibiting 2 or more symptoms mentioned below?", fg = 'white', bg="#0063b2").grid(row=1,column=0)
    question1_label=Label(updatestatus, text="Fever/Chills/Shievering/Sore Throat/Body Ache/Diarrhea/Headache/Fatique/Runny Nose", fg = 'white', bg="#0063b2").grid(row=2,column=0)
    question1=["NO","YES"]
    var1=StringVar()
    question1_combo=ttk.Combobox(updatestatus,value=question1,textvariable=var1,width=30,state="readonly").grid(row=3,column=0)

    question2_label=Label(updatestatus, text="Question 2: Besides the above, are you exhibiting any of the symptoms mentioned below?", fg = 'white', bg="#0063b2").grid(row=4,column=0)
    question2_label=Label(updatestatus, text="Cough/Difficulty Breathing/Loss of Smell/Loss of Taste", fg = 'white', bg="#0063b2").grid(row=5,column=0)
    question2=["NO","YES"]
    var2=StringVar()
    question2_combo=ttk.Combobox(updatestatus,value=question2,textvariable=var2,width=30,state="readonly").grid(row=6,column=0)

    question3_label=Label(updatestatus, text="Question 3: Have you attended any event/areas associated with known COVID-19 cluster? ", fg = 'white', bg="#0063b2").grid(row=7,column=0)
    question3=["NO","YES"]
    var3=StringVar()
    question3_combo=ttk.Combobox(updatestatus,value=question3,textvariable=var3,width=30,state="readonly").grid(row=8,column=0)

    question4_label=Label(updatestatus, text="Question 4: Have you travelled abroud within the last 14 days?", fg = 'white', bg="#0063b2").grid(row=9,column=0)
    question4=["NO","YES"]
    var4=StringVar()
    question4_combo=ttk.Combobox(updatestatus,value=question4,textvariable=var4,width=30,state="readonly").grid(row=10,column=0)

    question5_label=Label(updatestatus, text="Question 5: Have you had close contact with any comfirmed or suspected COVID-19 cases within 14 days?", fg = 'white', bg="#0063b2").grid(row=11,column=0)
    question5=["NO","YES"]
    var5=StringVar()
    question5_combo=ttk.Combobox(updatestatus,value=question5,textvariable=var5,width=30,state="readonly").grid(row=12,column=0)

    question6_label=Label(updatestatus, text="Question 6: Are you a MOH COVID-19 volunteer in the last 14 days?", fg = 'white', bg="#0063b2").grid(row=13,column=0)
    question6=["NO","YES"]
    var6=StringVar()
    question6_combo=ttk.Combobox(updatestatus,value=question6,textvariable=var6,width=30,state="readonly").grid(row=14,column=0)

    question7_label=Label(updatestatus, text="Question 7: Are you under quarantine?", fg = 'white', bg="#0063b2").grid(row=15,column=0)
    question7=["NO","YES"]
    var7=StringVar()
    question7_combo=ttk.Combobox(updatestatus,value=question7,textvariable=var7,width=30,state="readonly").grid(row=16,column=0)

    question8_label=Label(updatestatus, text="Question 8: What is your occupation?", fg = 'white', bg="#0063b2").grid(row=17,column=0)
    question8=["health-care worker","community services" , "energy" , "food" , "transportation" , "workers" , "student" , 'others']
    var8=StringVar()
    question8_combo=ttk.Combobox(updatestatus,value=question8,textvariable=var8,width=30,state="readonly").grid(row=18,column=0)

    question9_label=Label(updatestatus, text="Question 9: What is your age?", fg = 'white', bg="#0063b2").grid(row=19,column=0)
    question9=['age >= 60' , 'age < 60']
    var9=StringVar()
    question9_combo=ttk.Combobox(updatestatus,value=question9,textvariable=var9,width=30,state="readonly").grid(row=20,column=0)

    Label(updatestatus, text=" ", fg = 'white', bg="#0063b2").grid(row=21,column=0)

    # submit button ----------------------------------------------------------------------------------------------------------------------------------------------------
    def update_status():
        global risk
        global occupation
        global quarantine
        global risklevel
        risk = [var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),var6.get(),var7.get()]
        occupation = var8.get()
        quarantine = var7.get()
        agelevel = var9.get()
        # risk level algorithm -----------------------------------------------------------------------------------------------------------------------------------------
        if risk == ['NO', 'NO', 'NO', 'NO', 'NO', 'NO' , 'NO']:
            risklevel = 'low_risk'
        else:
            risklevel = 'high_risk'
        c.execute("""UPDATE registration SET risk = '%s' WHERE name = '%s'"""% (risklevel, get_username))
        c.execute("""UPDATE registration SET occupation = '%s' WHERE name = '%s'"""% (occupation, get_username))
        c.execute("""UPDATE registration SET under_quarantine = '%s' WHERE name = '%s'""" % (quarantine, get_username))
        connection.commit()
        print(c.rowcount, "record(s) affected")
        # priority ranking algorithm -----------------------------------------------------------------------------------------------------------------------------------
        def priority_algorithm() :
            pr5 = '5'
            pr4 = '4'
            pr3 = '3'
            pr2 = '2'
            pr1 = '1'
            if occupation == "health-care worker" :
                c.execute("""UPDATE registration SET priority_ranking = '%s' WHERE name = '%s'"""% (pr5, get_username))
                connection.commit()
            else :
                if occupation == "community services":
                    c.execute("""UPDATE registration SET priority_ranking = '%s' WHERE name = '%s'"""% (pr4, get_username))
                    connection.commit()  
                if occupation == "energy":
                    c.execute("""UPDATE registration SET priority_ranking = '%s' WHERE name = '%s'"""% (pr4, get_username))
                    connection.commit()  
                if occupation == "food":
                    c.execute("""UPDATE registration SET priority_ranking = '%s' WHERE name = '%s'"""% (pr4, get_username))
                    connection.commit()  
                if occupation == "transportation":
                    c.execute("""UPDATE registration SET priority_ranking = '%s' WHERE name = '%s'"""% (pr4, get_username))
                    connection.commit()  
                if occupation == "workers":
                    c.execute("""UPDATE registration SET priority_ranking = '%s' WHERE name = '%s'"""% (pr4, get_username))
                    connection.commit()  
                else :     
                    if occupation == 'others' and agelevel == 'age >= 60' :
                        c.execute("""UPDATE registration SET priority_ranking = '%s' WHERE name = '%s'"""% (pr3, get_username))
                        connection.commit() 
                    if occupation == 'others' and agelevel == 'age < 60' and risklevel == 'high_risk' :
                        c.execute("""UPDATE registration SET priority_ranking = '%s' WHERE name = '%s'"""% (pr2, get_username))
                        connection.commit()
                    if occupation == 'others' and agelevel == 'age < 60' and risklevel == 'low_risk' :
                        c.execute("""UPDATE registration SET priority_ranking = '%s' WHERE name = '%s'"""% (pr1, get_username))
                        connection.commit()
                    else:    
                        if occupation == "student" and agelevel == 'age < 60' and risklevel == 'high_risk':  
                            c.execute("""UPDATE registration SET priority_ranking = '%s' WHERE name = '%s'"""% (pr2, get_username))
                            connection.commit() 
                        if occupation == "student" and agelevel == 'age < 60' and risklevel == 'low_risk':  
                            c.execute("""UPDATE registration SET priority_ranking = '%s' WHERE name = '%s'"""% (pr1, get_username))
                            connection.commit() 
        priority_algorithm()                                        
        updatestatus.destroy()
        updatesuccess_loop()
    submit_button=ttk.Button(updatestatus, text="Submit" , command = update_status).grid(row=22,column=0)

    Label(updatestatus, text=" ", fg = 'white', bg="#0063b2").grid(row=23,column=0)
    Label(updatestatus, text=" ", fg = 'white', bg="#0063b2").grid(row=21,column=0)

    # main menu button -------------------------------------------------------------------------------------------------------------------------------------------------
    def from_updatestatus_to_menu():
        updatestatus.destroy()
        menu_loop()
    mainmenu_button=ttk.Button(updatestatus, text="Main Menu" , command = from_updatestatus_to_menu).grid(row=24,column=0)

    updatestatus.mainloop()

# UPDATE STATUS SUCCESS PAGE ###########################################################################################################################################
def updatesuccess_loop():

    # page design ------------------------------------------------------------------------------------------------------------------------------------------------------
    updatesuccess= Tk()
    updatesuccess.title("Update Status")
    updatesuccess.attributes('-topmost',1)
    updatesuccess.iconbitmap('vaccination_icon.ico')
    updatesuccess.resizable(0,0)
    updatesuccess.config(bg="#0063b2")
    updatesuccess.geometry('+200+50')

    Label(updatesuccess, text=" ", fg = 'white', bg="#0063b2").grid(row=0,column=0)
    status=Label(updatesuccess, text="SUCCESS!", fg = 'white', bg="#0063b2",font="15").grid(row=1,column=0)
    Label(updatesuccess, text=" ", fg = 'white', bg="#0063b2").grid(row=2,column=0)
    Label(updatesuccess, text="Congratulations, your status has been succesfully updated.", fg = 'white', bg="#0063b2").grid(row=3,column=0)
    Label(updatesuccess, text=" ", fg = 'white', bg="#0063b2").grid(row=4,column=0)
    
    # main menu button -------------------------------------------------------------------------------------------------------------------------------------------------
    def from_updatesuccess_to_menu():
        updatesuccess.destroy()
        menu_loop()
    mainmenu_button=ttk.Button(updatesuccess, text="Main Menu" , command = from_updatesuccess_to_menu).grid(row=5,column=0)

    updatesuccess.mainloop()

# VIEW STATUS PAGE #####################################################################################################################################################

def mystatus_loop():

    # page design ------------------------------------------------------------------------------------------------------------------------------------------------------
    mystatus=Tk()
    mystatus.title("My Status")
    mystatus.attributes('-topmost',1)
    mystatus.iconbitmap('vaccination_icon.ico')
    mystatus.resizable(0,0)
    mystatus.config(bg="#0063b2")
    mystatus.geometry('+200+50')

    status=Label(mystatus, text="My Current Status", fg = 'white', bg="#0063b2",font="15").grid(row=0,column=1)
    Label(mystatus, text="           ", fg = 'white', bg="#0063b2").grid(row=1,column=0)
    
    # data output ------------------------------------------------------------------------------------------------------------------------------------------------------
    c.execute('SELECT risk from registration where name = "%s" and password = "%s"'% (get_username, get_userpassword))
    myrisk = c.fetchone()
    myrisk_show = myrisk[0]
    risk_label=Label(mystatus, text=f"Risk : {myrisk_show}",font="10", fg = 'white', bg="#0063b2").grid(row=2,column=1)
    Label(mystatus, text="        ", fg = 'white', bg="#0063b2").grid(row=3,column=3)

    c.execute('SELECT occupation from registration where name = "%s" and password = "%s"'% (get_username, get_userpassword))
    myoccupation = c.fetchone()
    myoccupation_show = myoccupation[0]
    occupation_label=Label(mystatus, text=f"Occupation : {myoccupation_show}",font="10", fg = 'white', bg="#0063b2").grid(row=4,column=1)
    Label(mystatus, text="    ", fg = 'white', bg="#0063b2").grid(row=5,column=3)

    c.execute('SELECT under_quarantine from registration where name = "%s" and password = "%s"'% (get_username, get_userpassword))
    myquarantine = c.fetchone()
    myquarantine_show = myquarantine[0]
    quarantine_label=Label(mystatus, text=f"Under Quarantine? : {myquarantine_show}",font="10", fg = 'white', bg="#0063b2").grid(row=6,column=1)
    Label(mystatus, text="    ", fg = 'white', bg="#0063b2").grid(row=7,column=2)

    # main menu button -------------------------------------------------------------------------------------------------------------------------------------------------
    def from_viewstatus_to_menu():
        mystatus.destroy()
        menu_loop()
    mainmenu_button=ttk.Button(mystatus, text="Main menu" , command = from_viewstatus_to_menu).grid(row=8,column=1)

    mystatus.mainloop()

# RVSP PAGE ############################################################################################################################################################

def appointmentpanel_loop():

    global vaccentre_tree
    global vaccentre_data_tree

    # page design ------------------------------------------------------------------------------------------------------------------------------------------------------
    appointment_panel=Tk()
    appointment_panel.title("Appointment")
    appointment_panel.attributes('-topmost',1)
    appointment_panel.iconbitmap('vaccination_icon.ico')
    appointment_panel.resizable(0,0)
    appointment_panel.config(bg="#0063b2")
    appointment_panel.geometry('+200+50')

    instruction=Label(appointment_panel, text="Please pay attention to Your Location, Date and Time for your vaccination!", fg = 'white', bg="#0063b2", font="15").grid(row=0,column=0)
    
    Label(appointment_panel, text=" ", fg = 'white', bg="#0063b2").grid(row=1,column=0)

    appointment_label=Label(appointment_panel, text="Can you come on this vaccination centre at this time?", font="10", fg = 'white', bg="#0063b2").grid(row=2,column=0)

    # data output ------------------------------------------------------------------------------------------------------------------------------------------------------
    c.execute('SELECT location from registration where name = "%s" and password = "%s"'% (get_username, get_userpassword))
    mylocation = c.fetchone()
    mylocation_show = mylocation[0]    
    location_label=Label(appointment_panel, text=f"vaccination centre id :   {mylocation_show}", fg = 'white', bg="#0063b2").grid(row=3,column=0)

    c.execute('SELECT date from registration where name = "%s" and password = "%s"'% (get_username, get_userpassword))
    mydate = c.fetchone()
    mydate_show = mydate[0]     
    date_label=Label(appointment_panel, text=f"vaccination date :   {mydate_show}", fg = 'white', bg="#0063b2").grid(row=4,column=0)

    c.execute('SELECT time from registration where name = "%s" and password = "%s"'% (get_username, get_userpassword))
    mytime = c.fetchone()
    mytime_show = mytime[0]  
    time_label=Label(appointment_panel, text=f"vaccination time :   {mytime_show}", fg = 'white', bg="#0063b2").grid(row=5,column=0)

    # vaccination centre treeview --------------------------------------------------------------------------------------------------------------------------------------
    vaccentre_tree = Frame (appointment_panel)
    vaccentre_tree.grid(row = 6, column = 0 , columnspan = 20)
    vaccentre_data_tree = ttk.Treeview (vaccentre_tree,height = 6)
    vaccentre_data_tree['columns'] = ('location_ID', 'location_name','location_address')

    vaccentre_data_tree.column ('#0', width = 0 , stretch = NO)
    vaccentre_data_tree.column ('location_ID', width = 100 , anchor = CENTER)
    vaccentre_data_tree.column ('location_name', width = 150)
    vaccentre_data_tree.column ('location_address', width =200)

    vaccentre_data_tree.heading ('#0')
    vaccentre_data_tree.heading ('location_ID', text = 'Location_ID')
    vaccentre_data_tree.heading ('location_name', text = 'Location_Name')
    vaccentre_data_tree.heading ('location_address', text = 'Address')

    vaccentre_data_tree.pack(pady = 20)

    # check vaccination centre  ----------------------------------------------------------------------------------------------------------------------------------------
    def check_centre():
        global vaccentre_tree
        global vaccentre_data_tree
        vaccentre_data_tree.delete(*vaccentre_data_tree.get_children())
        c.execute("SELECT * FROM vac_centre ORDER BY location_id ASC")
        fetch3 = c.fetchall()
        for data in fetch3:
            vaccentre_data_tree.insert('', 'end', values=(data[0], data[1],data[2]))
        connection.commit()
    
    Label(appointment_panel, text=" ", fg = 'white', bg="#0063b2").grid(row=8,column=0)

    # data entry -------------------------------------------------------------------------------------------------------------------------------------------------------
    appointment=["NO","YES"]
    appointment_var = StringVar()
    appointment_combo=ttk.Combobox(appointment_panel,value=appointment,textvariable=appointment_var,width=50,state="readonly").grid(row=9,column=0)
    Label(appointment_panel, text=" ", fg = 'white', bg="#0063b2").grid(row=10,column=0) 

    # submit button ----------------------------------------------------------------------------------------------------------------------------------------------------
    def RVSP_insert():
        global get_RVSP
        get_RVSP = appointment_var.get()
        if get_RVSP == "":
            messagebox.showwarning('WARNING','PLEASE ENSURE THAT THE INFORMATION ENTERED IS COMPLETE')
        else :
            c.execute("""UPDATE registration SET RVSP = '%s' WHERE name = '%s'""" % (get_RVSP, get_username))
            connection.commit()
            print(c.rowcount, "record(s) affected") 
            appointment_panel.destroy()
            RVSPsuccess_loop()         
    submit_button=ttk.Button(appointment_panel, text="Submit", command = RVSP_insert).grid(row=11,column=0)

    Label(appointment_panel, text=" ", fg = 'white', bg="#0063b2").grid(row=12,column=0)

    # main menu button -------------------------------------------------------------------------------------------------------------------------------------------------
    def from_selectappointment_to_menu():
        appointment_panel.destroy()
        menu_loop()
    mainmenu_button=ttk.Button(appointment_panel, text="Main Menu" , command = from_selectappointment_to_menu).grid(row=13,column=0)

    check_centre()

    appointment_panel.mainloop()

#RVSP SUCCESS PAGE #####################################################################################################################################################

def RVSPsuccess_loop():

    # page design ------------------------------------------------------------------------------------------------------------------------------------------------------
    RVSPsuccess= Tk()
    RVSPsuccess.title("Appointment")
    RVSPsuccess.attributes('-topmost',1)
    RVSPsuccess.iconbitmap('vaccination_icon.ico')
    RVSPsuccess.resizable(0,0)
    RVSPsuccess.config(bg="#0063b2")
    RVSPsuccess.geometry('+200+50')

    Label(RVSPsuccess, text=" ", fg = 'white', bg="#0063b2").grid(row=0,column=0)
    status=Label(RVSPsuccess, text="SUCCESS!", fg = 'white', bg="#0063b2",font="15").grid(row=1,column=0)
    Label(RVSPsuccess, text=" ", fg = 'white', bg="#0063b2").grid(row=2,column=0)
    Label(RVSPsuccess, text="Congratulations, your RVSP has been succesfully updated.", fg = 'white', bg="#0063b2").grid(row=3,column=0)
    Label(RVSPsuccess, text=" ", fg = 'white', bg="#0063b2").grid(row=4,column=0)

    # main menu button -------------------------------------------------------------------------------------------------------------------------------------------------
    def from_RVSPsuccess_to_menu():
        RVSPsuccess.destroy()
        menu_loop()
    mainmenu_button=ttk.Button(RVSPsuccess, text="Main Menu" , command = from_RVSPsuccess_to_menu).grid(row=5,column=0)

    RVSPsuccess.mainloop()

# ADMIN PANEL PAGE #####################################################################################################################################################

def admin_panel_loop():

    global searchID
    global location_insert
    global date
    global time_var
    global priority_var
    global locationtree
    global locationdata_tree
    global tree
    global userdata_tree

    # page design ------------------------------------------------------------------------------------------------------------------------------------------------------
    admin_panel = Tk()
    admin_panel.title("Admin Panel")
    admin_panel.attributes('-topmost',1)
    admin_panel.iconbitmap('vaccination_icon.ico')
    admin_panel.resizable(0,0)
    admin_panel.config(bg="#0063b2")
    admin_panel.geometry('+200+50')

    # data entry -------------------------------------------------------------------------------------------------------------------------------------------------------
    searchID=StringVar()
    searchID_label=Label(admin_panel, text="ID", fg = 'white', bg="#0063b2").grid(row=0,column=0)
    searchID_entry=Entry(admin_panel, textvariable=searchID,width="30").grid(row=0,column=1)

    location_insert = StringVar()
    location_label=Label(admin_panel, text="Vaccine Location ID", fg = 'white', bg="#0063b2").grid(row=1,column=0)
    location_entry=Entry(admin_panel, textvariable=location_insert,width="30").grid(row=1,column=1)

    date=StringVar()
    date_label=Label(admin_panel, text="Vaccine Date (YYYY-MM-DD)", fg = 'white', bg="#0063b2").grid(row=2,column=0)
    date_enrty=Entry(admin_panel,textvariable=date,width="30").grid(row=2,column=1)
    
    time_label=Label(admin_panel, text="Vaccine Time", fg = 'white', bg="#0063b2").grid(row=3,column=0)
    time=["8am","9am", "10am","11am","12pm","1pm","2pm","3pm","4pm","5pm","6pm","7pm","8pm"]
    time_var = StringVar()
    time_combo=ttk.Combobox(admin_panel , value=time , textvariable=time_var , width=30,state="readonly").grid(row=3,column=1)

    # priority rank information treeview -------------------------------------------------------------------------------------------------------------------------------
    Label(admin_panel, text="                                      ", fg = 'white', bg="#0063b2").grid(row=0,column=3)
    PR_RANK_label=Label(admin_panel, text="PRIORITY RANKING INFORMATION", fg = 'white', bg="#0063b2" ,font="8" ).grid(row=0,column=4)

    PRtree = Frame (admin_panel)
    PRtree.grid(row = 1, column = 3 , columnspan = 20 , rowspan = 6)
    PRdata_tree = ttk.Treeview (PRtree , height = 6)
    PRdata_tree['columns'] = ('PR', 'INFORMATION')

    PRdata_tree.column ('#0', width = 0 , stretch = NO)
    PRdata_tree.column ('PR', width = 75 , anchor = CENTER)
    PRdata_tree.column ('INFORMATION', width = 325)

    PRdata_tree.heading ('#0')
    PRdata_tree.heading ('PR', text = 'PR')
    PRdata_tree.heading ('INFORMATION', text = 'INFORMATION')

    PRdata = [
        [5 , 'health-care worker'],
        [4 , 'community services,energy,food,transportation,workers'],
        [3 , 'others , age>=60'],
        [2 , 'others,student , age<60 , high_risk'],
        [1 , 'others,student , age<60 , low_risk']
    ]

    count = 0
    for record in PRdata:
        PRdata_tree.insert(parent='' , index='end' , iid=count , text='' , values=(record[0] , record[1]))
        count += 1
             
    PRdata_tree.pack(pady = 20)  

    # refresh data button ----------------------------------------------------------------------------------------------------------------------------------------------
    def refresh_page():
        global locationdata_tree
        global userdata_tree
        locationdata_tree.delete(*locationdata_tree.get_children())
        userdata_tree.delete(*userdata_tree.get_children())
        c.execute("SELECT * FROM vac_centre ORDER BY location_id ASC")
        fetch2 = c.fetchall()
        for data in fetch2:
            locationdata_tree.insert('', 'end', values=(data[0], data[1], data[3], data[2], data[4]))
        connection.commit()
        c.execute("SELECT * FROM registration ORDER BY ID ASC")
        fetch = c.fetchall()
        for data in fetch:
            userdata_tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[9], data[10], data[11], data[12], data[13], data[14], data[15] , data[16]))
        connection.commit()
    searchID_refresh=ttk.Button(admin_panel, text="Refresh Data" , width = 15, command=refresh_page).grid(row=5,column=2)

    # assign location button -------------------------------------------------------------------------------------------------------------------------------------------
    def locationID_insert():
        global get_locationID
        global get_searchID
        get_locationID = location_insert.get()
        get_searchID = searchID.get()
        c.execute("""UPDATE registration SET location = '%s' WHERE ID = '%s'""" % (get_locationID, get_searchID))
        connection.commit()
        print(c.rowcount, "record(s) affected")
    location_button=ttk.Button(admin_panel, text="Assign Location" , width = 15 , command = locationID_insert).grid(row=1,column=2)

    # assign date button -----------------------------------------------------------------------------------------------------------------------------------------------
    def date_insert():
        global get_date
        global get_searchID
        get_date = date.get()
        get_searchID = searchID.get()
        c.execute("""UPDATE registration SET date = '%s' WHERE ID = '%s'""" % (get_date, get_searchID))
        connection.commit()
        print(c.rowcount, "record(s) affected")
    date_button=ttk.Button(admin_panel, text="Assign Date" , width = 15 , command = date_insert).grid(row=2,column=2)

    # assign time button -----------------------------------------------------------------------------------------------------------------------------------------------
    def time_insert():
        global get_time
        global get_searchID
        get_time = time_var.get()
        get_searchID = searchID.get()
        c.execute("""UPDATE registration SET time = '%s' WHERE ID = '%s'""" % (get_time, get_searchID))
        connection.commit()
        print(c.rowcount, "record(s) affected")
    time_button=ttk.Button(admin_panel, text="Assign Time" , width = 15 , command = time_insert).grid(row=3,column=2)

    # create new vaccination centre button -----------------------------------------------------------------------------------------------------------------------------
    def from_adminpanel_to_newcentre():
        admin_panel.destroy()
        newcentre_loop()
    newcentre_button=ttk.Button(admin_panel, text="Create new vaccination centres"  , command = from_adminpanel_to_newcentre).grid(row=7,column=1,pady=10)

    # logout button ----------------------------------------------------------------------------------------------------------------------------------------------------
    def from_adminpanel_to_loginpage():
        admin_panel.destroy()
        login_panel_loop()
    logout_button=ttk.Button(admin_panel, text="Logout" , command = from_adminpanel_to_loginpage).grid(row=5,column=0)

    # location data treeview -------------------------------------------------------------------------------------------------------------------------------------------
    vac_location_label = Label(admin_panel, text="VAC CENTRE" , font="10", fg = 'white', bg="#0063b2").grid(row=7,column=0)
    locationtree = Frame (admin_panel)
    locationtree.grid(row = 8, column = 0 , columnspan = 20)
    locationdata_tree = ttk.Treeview (locationtree,height = 6) 
    locationdata_tree['columns'] = ('location_ID', 'location_name', 'location_postcode','location_address', 'capacity_per_hour')

    locationdata_tree.column ('#0', width = 0 , stretch = NO)
    locationdata_tree.column ('location_ID', width = 200 , anchor = CENTER)
    locationdata_tree.column ('location_name', width = 200)
    locationdata_tree.column ('location_postcode', width = 200 , anchor = CENTER)
    locationdata_tree.column ('location_address', width =200)
    locationdata_tree.column ('capacity_per_hour', width = 200 ,anchor = CENTER )

    locationdata_tree.heading ('#0')
    locationdata_tree.heading ('location_ID', text = 'Location_ID')
    locationdata_tree.heading ('location_name', text = 'Location_Name')
    locationdata_tree.heading ('location_postcode', text = 'Postcode')
    locationdata_tree.heading ('location_address', text = 'Address')
    locationdata_tree.heading ('capacity_per_hour', text = 'Capacity/Hour')

    locationdata_tree.pack(pady = 20)

    # check priority from high to low button ---------------------------------------------------------------------------------------------------------------------------
    def refresh_PR():
        global userdata_tree
        userdata_tree.delete(*userdata_tree.get_children())
        c.execute("SELECT * FROM registration ORDER BY priority_ranking DESC")
        fetch = c.fetchall()
        for data in fetch:
            userdata_tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[9], data[10], data[11], data[12], data[13], data[14], data[15] , data[16]))
        connection.commit()
    searchID_refresh=ttk.Button(admin_panel, text="PR" , width = 15, command=refresh_PR).grid(row=9,column=1,pady=10)

    # check RVSP from YES to NO button ---------------------------------------------------------------------------------------------------------------------------------
    def refresh_RVSP():
        global userdata_tree
        userdata_tree.delete(*userdata_tree.get_children())
        c.execute("SELECT * FROM registration ORDER BY RVSP DESC")
        fetch = c.fetchall()
        for data in fetch:
            userdata_tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[9], data[10], data[11], data[12], data[13], data[14], data[15] , data[16]))
        connection.commit()
    searchID_refresh=ttk.Button(admin_panel, text="RVSP" , width = 15, command=refresh_RVSP).grid(row=9,column=2,pady=10)

    # user data treeview -----------------------------------------------------------------------------------------------------------------------------------------------
    userdata_label=Label(admin_panel, text="USER DATA" , font="10", fg = 'white', bg="#0063b2").grid(row=9,column=0)
    tree = Frame (admin_panel)
    tree.grid(row = 10, column = 0 , columnspan = 20)
    userdata_tree = ttk.Treeview (tree)
    userdata_tree['columns'] = ('ID', 'IC', 'name','age', 'phone', 'postcode', 'address','risk', 'occupation', 'under_quarantine', 'priority_ranking', 'location', 'date' , 'time' , 'RVSP')

    userdata_tree.column ('#0', width = 0 , stretch = NO)
    userdata_tree.column ('ID', width = 25 , anchor = CENTER)
    userdata_tree.column ('IC', width = 75)
    userdata_tree.column ('name', width = 100)
    userdata_tree.column ('age', width = 30 , anchor = CENTER)
    userdata_tree.column ('phone', width = 75)
    userdata_tree.column ('postcode',width = 75 , anchor = CENTER)
    userdata_tree.column ('address')
    userdata_tree.column ('risk', width = 75 , anchor = CENTER)
    userdata_tree.column ('occupation', width = 100)
    userdata_tree.column ('under_quarantine', width = 75 , anchor = CENTER)
    userdata_tree.column ('priority_ranking', width = 30 , anchor = CENTER)
    userdata_tree.column ('location', width = 75 , anchor = CENTER)
    userdata_tree.column ('date', width = 75 , anchor = CENTER)
    userdata_tree.column ('time', width = 40 , anchor = CENTER)
    userdata_tree.column ('RVSP', width = 40 , anchor = CENTER)

    userdata_tree.heading ('#0')
    userdata_tree.heading ('ID', text = 'ID')
    userdata_tree.heading ('IC', text = 'IC')
    userdata_tree.heading ('name', text = 'Name')
    userdata_tree.heading ('age', text = 'Age')
    userdata_tree.heading ('phone', text = 'Phone')
    userdata_tree.heading ('postcode', text = 'Postcode')
    userdata_tree.heading ('address', text = 'Address')
    userdata_tree.heading ('risk', text = 'Risk')
    userdata_tree.heading ('occupation', text = 'Occupation')
    userdata_tree.heading ('under_quarantine', text = 'Quarantine')
    userdata_tree.heading ('priority_ranking', text = 'PR')
    userdata_tree.heading ('location', text = 'Location_ID')
    userdata_tree.heading ('date', text = 'Date')
    userdata_tree.heading ('time', text = 'Time')
    userdata_tree.heading ('RVSP', text = 'RVSP')

    userdata_tree.pack()

    refresh_page()

    admin_panel.mainloop()

# CREATE VACCINATION CENTRE PAGE #######################################################################################################################################

def newcentre_loop():

    global newlocation
    global addresscentre
    global postcodecentre
    global capacity

    # page design ------------------------------------------------------------------------------------------------------------------------------------------------------
    newcentre = Tk()
    newcentre.title("Create New Vaccination Centre")
    newcentre.attributes('-topmost',1)
    newcentre.iconbitmap('vaccination_icon.ico')
    newcentre.resizable(0,0)
    newcentre.config(bg="#0063b2")
    newcentre.geometry('+200+50')

    # data entry -------------------------------------------------------------------------------------------------------------------------------------------------------
    newlocation=StringVar()
    newlocation_label=Label(newcentre, text="Location Name", fg = 'white', bg="#0063b2").grid(row=0,column=0)
    newlocation_entry=Entry(newcentre, textvariable=newlocation,width="60").grid(row=0,column=1,padx=100)

    addresscentre=StringVar()
    addresscentre_label=Label(newcentre, text="Address", fg = 'white', bg="#0063b2").grid(row=1,column=0)
    addresscentre_entry=Entry(newcentre, textvariable=addresscentre,width="60").grid(row=1,column=1)

    postcodecentre=StringVar()
    postcodecentre_label=Label(newcentre, text="Postcode", fg = 'white', bg="#0063b2").grid(row=2,column=0)
    postcodecentre_entry=Entry(newcentre, textvariable=postcodecentre,width="60").grid(row=2,column=1)

    capacity=StringVar()
    capacity_label=Label(newcentre, text="Capacity Per Hour", fg = 'white', bg="#0063b2").grid(row=3,column=0)
    capacity_entry=Entry(newcentre, textvariable=capacity,width="60").grid(row=3,column=1)

    # submit new location and capacity button --------------------------------------------------------------------------------------------------------------------------
    def submit_new_location():
      global get_newlocation
      global get_addresscentre
      global get_postcodecentre
      global get_capacity
      get_newlocation = newlocation.get()
      get_addresscentre = addresscentre.get()
      get_postcodecentre = postcodecentre.get()
      get_capacity = capacity.get()
      if get_newlocation == "" or get_addresscentre == "" or get_postcodecentre == "" or get_capacity == "":
        messagebox.showwarning('WARNING','PLEASE ENSURE THAT THE INFORMATION ENTERED IS COMPLETE')
      else:
        sql = "INSERT INTO `psp_assignment_db`.`vac_centre` (`location_name`,`location_address`,`location_postcode`,`capacity_per_hour`) VALUES (%s, %s, %s, %s)"
        val = (get_newlocation,get_addresscentre,get_postcodecentre,get_capacity)
        c.execute(sql,val)
        connection.commit()
        print(c.rowcount, "record inserted.")
        newcentre.destroy()
        createsuccess_loop()
    submitnewlocation_button=ttk.Button(newcentre, text="Submit new location and capacity" , command = submit_new_location).grid(row=4,column=1,pady=10)

    # back button ------------------------------------------------------------------------------------------------------------------------------------------------------
    def from_newcentre_to_adminpanel():
        newcentre.destroy()
        admin_panel_loop()
    back_button=ttk.Button(newcentre, text="Back" , command = from_newcentre_to_adminpanel).grid(row=5,column=1,pady = 20)

    newcentre.mainloop()

# CREATE VACCINATION CENTRE SUCCESS ####################################################################################################################################

def createsuccess_loop():

    # page design ------------------------------------------------------------------------------------------------------------------------------------------------------
    create_success= Tk()
    create_success.title("Create New Vaccination Centre")
    create_success.attributes('-topmost',1)
    create_success.iconbitmap('vaccination_icon.ico')
    create_success.resizable(0,0)
    create_success.config(bg = '#0063b2')
    create_success.geometry('+200+50')

    Label(create_success, text=" ", fg = 'white', bg="#0063b2").grid(row=0,column=0)
    status=Label(create_success, text="SUCCESS!", fg = 'white' , bg="#0063b2",font="15").grid(row=1,column=0)
    Label(create_success, text=" ", fg = 'white', bg="#0063b2").grid(row=2,column=0)
    Label(create_success, text="----------------------------------------     CREATE SUCCESS     ----------------------------------------", fg = 'white', bg="#0063b2").grid(row=3,column=0)
    Label(create_success, text=" ", fg = 'white', bg="#0063b2").grid(row=4,column=0)

    # login page button ------------------------------------------------------------------------------------------------------------------------------------------------
    def from_createsuccess_to_adminpanel():
        create_success.destroy()
        admin_panel_loop()
    back_button=Button(create_success, text="Back" , command = from_createsuccess_to_adminpanel).grid(row=5,column=0)

    create_success.mainloop()

# LOGIN PANEL LOOP #####################################################################################################################################################

login_panel_loop()