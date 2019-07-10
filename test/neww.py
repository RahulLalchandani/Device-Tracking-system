from tkinter import *
from tkinter import ttk
import sys
import sqlite3
from ardRfid import run
from datetime import datetime

con=sqlite3.connect("data.db")
cursor=con.cursor()
print("connected")


def raise_frame(frame):
    frame.tkraise()



def dashboardForm(master):
    Label(master,text='VESIT',font = ('Verdana',25,"bold"),padx=170,pady=10).place(x=250,y=10 )
    Button(master, text='Register Staff',height=2,width=25, padx=8,pady=10,command=lambda:raise_frame(registerDetails)).place(x=260,y=105)
    Button(master, text='Add Device',height=2,width=25, padx=8,pady=10,command=lambda:raise_frame(addDeviceDetails)).place(x=480,y=105)
    Button(master, text='Enter Device',height=2,width=25, padx=8,pady=10, command=lambda:raise_frame(enterDeviceDetails)).place(x=260,y=175)
    Button(master, text='Exit Device',height=2,width=25, padx=8,pady=10, command=lambda:raise_frame(exitDeviceDetails)).place(x=480,y=175)
    Button(master, text='View Device',height=2,width=25, padx=8,pady=10, command=lambda:raise_frame(viewDeviceDetails)).place(x=260,y=245)
    Button(master, text='Logout',height=2,width=25, padx=8,pady=10, command=lambda:raise_frame(loginDetails)).place(x=480,y=245)

def loginDetailsForm(master):
    def check():
        username=username_en.get()
        password=password_en.get()
        q=str("SELECT * FROM login WHERE username=? and password=?")
        res=con.execute(q,(username,password,))
        for i in res:
            if(username==i[3] and password==i[4]):
                print("LOGGED IN!!")
                username_en.delete(0,END)
                password_en.delete(0,END)
                raise_frame(dashboardDetails)
            else:
                print("INVALID DETAILS")
    Label(master,text='VESIT',font = ('Verdana',25,"bold"),padx=170,pady=10).place(x=300,y=105 )

    username_lb=Label(master,text="Username:",padx=10,pady=10)
    password_lb=Label(master,text="Password:",padx=10,pady=10)

    username_en=Entry(master,width=40)
    password_en=Entry(master,width=40,show="*")

    username_lb.place(x=300,y=175)
    password_lb.place(x=300,y=215)

    username_en.place(x=420,y=185)
    password_en.place(x=420,y=225)
    
    Button(master, text='Login',width=25, command=check).place(x=300,y=300)
    Button(master, text='exit',width=25,command=exit).place(x=500,y=300)
    master.config(width=500,height=500)
 
def registerDetailsForm(master):
    def insertStaffDetails():
        name=staff_name_en.get()
        email=staff_email_en.get()
        username=staff_username_en.get()
        password=staff_password_en.get()
        re_password=staff_re_password_en.get()
        query=str("INSERT INTO login(staff_name, staff_email, username, password) VALUES(?,?,?,?)")
        if(password==re_password):
            con.execute(query,(name,email,username,password))
            con.commit()
            print("staff registered!")
            raise_frame(dashboardDetails)
        else:
            print("Re-Entered password do not match")
    staff_name_lb=Label(master,text="Name:",padx=10,pady=10)
    staff_email_lb=Label(master,text="Email:",padx=10,pady=10)
    staff_username_lb=Label(master,text="Username:",padx=10,pady=10)
    staff_password_lb=Label(master,text="Password:",padx=10,pady=10)
    staff_re_password_lb=Label(master,text="Re-confirm Password:",padx=10,pady=10)
    
    staff_name_en=Entry(master,width=40)
    staff_email_en=Entry(master,width=40)
    staff_username_en=Entry(master,width=40)
    staff_password_en=Entry(master,width=40)
    staff_re_password_en=Entry(master,width=40)

    Label(master,text='VESIT',font = ('Verdana',25,"bold"),padx=170,pady=10).place(x=250,y=5 )

    staff_name_lb.place(x=300,y=100)
    staff_email_lb.place(x=300,y=150)
    staff_username_lb.place(x=300,y=200)
    staff_password_lb.place(x=300,y=250)
    staff_re_password_lb.place(x=300,y=300)
   

    staff_name_en.place(x=450,y=100)
    staff_email_en.place(x=450,y=150)
    staff_username_en.place(x=450,y=200)
    staff_password_en.place(x=450,y=250)
    staff_re_password_en.place(x=450,y=300)
    
    
    Button(master, text='Submit',pady=8,width=25, command=insertStaffDetails).place(x=300,y=350)
    Button(master, text='Leave',pady=8,width=25, command=lambda:raise_frame(dashboardDetails)).place(x=500,y=350)


def adddeviceForm(master):
    dev_id = None
    def registerdevice():
        adddeviceForm.dev_id = run()
        print(adddeviceForm.dev_id)
    
    def submit():
        query = "INSERT INTO devices VALUES(?, ?)"
        cursor.execute(query,(adddeviceForm.dev_id, device_name_en.get()))
        query = "INSERT INTO belongs VALUES (?, ?, ?, ?)"
        cursor.execute(query,(lab_no_en.get(), adddeviceForm.dev_id, "in", lab_no_en.get()))
        query = "INSERT INTO log VALUES (?, ?, ?, ?)"
        cursor.execute(query, (adddeviceForm.dev_id, lab_no_en.get(), "in", datetime.now()))
        con.commit()
#--------------------------------------#
    # def view(master):2
    #     def onSelect(event):
    #         for i in tree.selection():
    #             c_id=(tree.item(i,"text"))
    #             print(c_id)
    #             res=con.execute("SELECT * FROM login WHERE username=?",(c_id,))
    #     tree = ttk.Treeview(master)
    #     tree.grid(row=11,columnspan=2)
    #     records=tree.get_children()
    #     for elements in records:
    #         tree.delete(element)
    #     tree.config(columns=('id','staff_name','staff_email','username'))
    #     tree.heading('id',text='ID')
    #     tree.heading('staff_name',text='First Name')
    #     tree.heading('staff_email',text='Email')
    #     tree.heading('username',text='Username')
    #     res=con.execute("SELECT * FROM login ORDER BY username",())
    #     for i in res:
    #         tree.insert("",0,text="",values=(i[0],i[1],i[2],i[3]))
        #tree.bind('<ButtonRelease-1>',onSelect)
    #------------------------------------------#
    #view(master)
    Label(master,text='VESIT',font = ('Verdana',25,"bold"),padx=170,pady=10).place(x=250,y=10 )

    lab_no_lb=Label(master,text="Enter Lab_No.:",padx=10,pady=10).place(x=200,y=140)
    
    device_name_lb=Label(master,text="Enter Device Description:",padx=10,pady=10).place(x=150,y=190)
    Button(master, text='Get Device ID',pady=8,width=25, command=registerdevice).place(x=600,y=140)
    #cost_lb=Label(master,text="Enter Device Cost:",padx=10,pady=10)
    

    lab_no_en=Entry(master,width=40).place(x=320,y=150)
    #no_device_en=Entry(master,width=40)
    device_name_en=Entry(master,width=40).place(x=320,y=200)
    #cost_en=Entry(master,width=40)
    
    #lab_no_lb.grid(row=0,sticky=W)
    #no_device_lb.grid(row=1,sticky=W)
    #device_name_lb.grid(row=2,sticky=W)
    #cost_lb.grid(row=3,sticky=W)
   

    #lab_no_en.grid(row=0,column=1)
    #no_device_en.grid(row=1,column=1)
    #device_name_en.grid(row=2,column=1)
    #cost_en.grid(row=3,column=1)
   
    Button(master, text='Submit',pady=8,width=25, command=submit).place(x=250,y=250)
    Button(master, text='Leave',pady=8,width=25,command=lambda:raise_frame(dashboardDetails)).place(x=450,y=250)  
    master.config(width=500,height=500)

def enterdeviceForm(master):
    dev_id = None
     
    def enterdevice():
        enterdeviceForm.dev_id = run()
        print(enterdeviceForm.dev_id)
        flag = None
        res = lab_no_en.get()
        query1 = "update belongs set status = ?, current_lab = ? where device_id = ?"
        query_lab_id = "select lab_id from belongs where device_id = ?"
        lab_id = cursor.execute(query_lab_id, (enterdeviceForm.dev_id, ))
        res = lab_no_en.get()
        if res == lab_id:
            flag = "in"
        else:
            flag = "out"
        print(flag)
        cursor.execute(query1, (flag, res, enterdeviceForm.dev_id))
        query = "INSERT INTO log VALUES (?, ?, ?, ?)"
        cursor.execute(query, (enterdeviceForm.dev_id, res, "in", datetime.now()))
        con.commit()
        view(master)
#--------------------------------------#
    def view(master):
        tree = ttk.Treeview(master)
        tree.place(x=0,y=200)
        records=tree.get_children()
        for elements in records:
            tree.delete(element)
        tree.config(columns=('device_id', 'current_lab_id', 'status', 'time'))
        tree.heading('device_id',text='Device ID')
        tree.heading('current_lab_id',text='Current Lab ID')
        tree.heading('status',text='status')
        tree.heading('time',text='Time')
        res=con.execute("SELECT * FROM log")
        for i in res:
            tree.insert("",0,text="",values=(i[0],i[1],i[2],i[3]))
        #tree.bind('<ButtonRelease-1>',onSelect)
    #------------------------------------------#
    Label(master,text='VESIT',font = ('Verdana',25,"bold"),padx=170,pady=10).place(x=250,y=10 )

    lab_no_lb=Label(master,text="Enter Lab_No.:",padx=10,pady=10).place(x=300,y=65)
    lab_no_en=Entry(master,width=40).place(x=400,y=70)
    #lab_no_lb.grid(row=0,sticky=W)
    #lab_no_en.grid(row=0,column=1)
    Button(master, text='Get Device ID',pady=8,width=25, command=enterdevice).place(x=270,y=120)
    view(master)
    Button(master, text='Leave',pady=8,width=25,command=lambda:raise_frame(dashboardDetails)).place(x=470,y=120)   
    master.config(width=500,height=500)

def exitdeviceForm(master):
    dev_id = None
    def get_device_id():
        exitdeviceForm.dev_id = run()
        query1 = "update belongs set status = ?, current_lab = ? where device_id = ?"
        cursor.execute(query1, ("out", None, exitdeviceForm.dev_id))
        query = "INSERT INTO log VALUES (?, ?, ?, ?)"
        cursor.execute(query, (exitdeviceForm.dev_id, None, "out", datetime.now()))
        con.commit()
        view(master)

    # def exitdevice():
    #     query1 = "update belongs set status = ?, current_lab = ? where device_id = ?"
    #     cursor.execute(query1, ("out", None, exitdeviceForm.dev_id))
    #     query = "INSERT INTO log VALUES (?, ?, ?, ?)"
    #     cursor.execute(query, (exitdeviceForm.dev_id, None, "out", datetime.now()))
    #     con.commit()
#--------------------------------------#
    def view(master):
        tree = ttk.Treeview(master)
        tree.place(x=0,y=200)
        records=tree.get_children()
        for elements in records:
            tree.delete(element)
        tree.config(columns=('device_id', 'current_lab_id', 'status', 'time'))
        tree.heading('device_id',text='Device ID')
        tree.heading('current_lab_id',text='Current Lab ID')
        tree.heading('status',text='status')
        tree.heading('time',text='Time')
        res=con.execute("SELECT * FROM log")
        for i in res:
            tree.insert("",0,text="",values=(i[0],i[1],i[2],i[3]))
        #tree.bind('<ButtonRelease-1>',onSelect)
    #------------------------------------------#
    view(master)
    Label(master,text='VESIT',font = ('Verdana',25,"bold"),padx=170,pady=10).place(x=250,y=10 )

    Button(master, text='Get Device ID',pady=8,width=25, command=get_device_id).place(x=270,y=120)
    #lab_no_lb=Label(master,text="Enter Lab_No.:",padx=10,pady=10)
    # no_device_lb=Label(master,text="Enter Number of devices:",padx=10,pady=10)
    # device_name_lb=Label(master,text="Enter Device Name:",padx=10,pady=10)

    #lab_no_en=Entry(master,width=40)
    # no_device_en=Entry(master,width=40)
    # device_name_en=Entry(master,width=40)
    
    #lab_no_lb.grid(row=0,sticky=W)
    # no_device_lb.grid(row=1,sticky=W)
    # device_name_lb.grid(row=2,sticky=W)
   
    #lab_no_en.grid(row=0,column=1)
    # no_device_en.grid(row=1,column=1)
    # device_name_en.grid(row=2,column=1)
  
   
    # Button(master, text='Exit',pady=8,width=25, command=exitdevice).grid(row=9,column=0)
    Button(master, text='Leave',pady=8,width=25,command=lambda:raise_frame(dashboardDetails)).place(x=470,y=120)   
    master.config(width=500,height=500)


def viewdeviceForm(master):
    
    # def viewdevice():
    #     lab_no = lab_no_en.get()
    #     if lab_no:
    #         query = "select * from devices where device_id in (select device_id from belongs where lab_id = "+ lab_no +")"
        
    def view(master):
        tree = ttk.Treeview(master)
        tree.grid(row=1,columnspan=2)
        records=tree.get_children()
        for elements in records:
            tree.delete(element)
        tree.config(columns=('lab_id', 'device_id', 'status', 'current_lab'))
        tree.heading('lab_id',text='Lab ID')
        tree.heading('device_id',text='Device ID')
        tree.heading('status',text='status')
        tree.heading('current_lab',text='Current Lab')
        res=con.execute("SELECT * FROM belongs")
        for i in res:
            tree.insert("",0,text="",values=(i[0],i[1],i[2],i[3]))
        
        #tree = ttk.Treeview(master)
        #tree.grid(row=1,columnspan=2)
        #records=tree.get_children()
        ##for elements in records:
            #tree.delete(element)
        #tree.config(columns=('lab_id', 'device_id','description'))
        #tree.heading('lab_id',text="Lab ID")
        #tree.heading('device_id',text='ID')
        #tree.heading('description',text='Description')
        #query = "SELECT * FROM devices"
        #res=con.execute(query)
        #query = "select lab_id from belongs where device_id = ?"
        #for i in res:
            #query = "select lab_id from belongs where device_id = ?"
            #ress = cursor.execute(query, (i[0],))
            #tree.insert("",0,text="",values=(ress.fetchone()[0],i[0],i[1]))
        #tree.bind('<ButtonRelease-1>',onSelect)
    #------------------------------------------#
    #view(master)
   
    # lab_no_lb=Label(master,text="Enter Lab_No.:",padx=10,pady=10)
  
    # lab_no_en=Entry(master,width=40)

    # lab_no_lb.grid(row=0,sticky=W)
 
    # lab_no_en.grid(row=0,column=1)
   
    # Button(master, text='View',pady=8,width=25, command=view(master)).grid(row=9,column=0)   
    view(master)
    #Label(master,text='VESIT',font = ('Verdana',25,"bold"),padx=170,pady=10).place(x=250,y=10 )

    Button(master, text='Leave',pady=8,width=25,command=lambda:raise_frame(dashboardDetails)).grid(row=9,column=1)
    master.config(width=500,height=500)

    


root=Tk()
root.minsize(width=500,height=400)
root.resizable(width=False, height=False)
registerDetails = Frame(root)
registerDetailsForm(registerDetails)
addDeviceDetails=Frame(root)
adddeviceForm(addDeviceDetails)
enterDeviceDetails=Frame(root)
enterdeviceForm(enterDeviceDetails)
exitDeviceDetails=Frame(root)
exitdeviceForm(exitDeviceDetails)
viewDeviceDetails=Frame(root)
viewdeviceForm(viewDeviceDetails)
loginDetails = Frame(root)
loginDetailsForm(loginDetails)
dashboardDetails = Frame(root)
dashboardForm(dashboardDetails)

for frame in (registerDetails,loginDetails,dashboardDetails,addDeviceDetails,enterDeviceDetails,exitDeviceDetails,viewDeviceDetails):
    frame.grid(row=0, column=0, sticky='news')
raise_frame(loginDetails)
root.mainloop()
