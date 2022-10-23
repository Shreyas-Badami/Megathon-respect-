from webbrowser import get
import mysql.connector as mysql
from tkinter import *

connection = mysql.connect(host='localhost',
                           database='docnetmd',
                           user='root',
                           password='ben10:01')

cursor = connection.cursor()
def findDocWithTags(PId, tags):
    data = []
    cursor.execute('''select Language from patients where PId = "%s"''' %(PId))
    language = cursor.fetchall()[0][0]
    for tag in tags:
        cursor.execute('''select specialization from
                        specializations where Tag =
                        "%s"''' %(tag))
        specializations = cursor.fetchall()
        for specialization in specializations:
            cursor.execute('''select DId, Name, 
                            Specialization, Price,
                            Insurance, PhoneNumber,
                            Location from doctors where
                            Specialization = "%s" and 
                            Language = "%s"''' 
                            %(specialization[0], language))
            doc = cursor.fetchall()
            for i in doc:
                data.append(i)
    return data


def findDocWithId(DId):
    cursor.execute('''select DId, Name, 
                    Specialization, Price,
                    Insurance, PhoneNumber,
                    Location, Language from doctors where
                    DId = "%s"''' 
                    %(DId))
    data = cursor.fetchone()
    return data

def findDocWithSpecialization(specialization):
    cursor.execute('''select DId, Name, 
                    Specialization, Price,
                    Insurance, PhoneNumber,
                    Location, Language from doctors where
                    Specialization = "%s"''' 
                    %(specialization))
    data = cursor.fetchall()
    return data

def makeAppointment(PId, DId):
    cursor.execute('''select count(*) from appointments''')
    AId = cursor.fetchall()[0][0] + 1
    cursor.execute('''select Price from doctors where DId = %s''' %(DId))
    cost = cursor.fetchall()[0][0]
    cursor.execute('''insert into appointments 
                    values(%s, %s, %s, "o", %s)''' 
                    %(AId, PId, DId, cost))


s = ["diabetes", "sore throat", "cerebral palsy"]
#print(findDocWithTags(1,s))
#print(findDocWithSpecialization("ent"))
#makeAppointment(1,2)


patient_id=0
def commonsubmit(f,t):
    global root
    f.destroy()
    main=Frame(root)
    main.pack()
    makeAppointment(int(patient_id),int(t))
    l=Label(main,text="Booking confirmed")
    l.pack()
    root.mainloop()
def submitdoc(x,f):
    global root
    f.destroy()
    main=Frame(root)
    main.pack()
    lbl=Label(main,text="your doctor's id is:"+x)
    lbl.pack()
    root.mainloop()
def patient():
    global root
    main=Frame(root)
    main.pack()
    lbl=Label(main,text="Please enter your patient's id")
    lbl.pack()
    txt=Entry(main,width=10)
    txt.pack()
    button=Button(main,text="Submit",command=lambda: patient1(txt.get(),main))
    button.pack()
    root.mainloop()
def symptomsdata(f,t1,t2,t3):
    global root
    f.destroy()
    main=Frame(root)
    main.pack()
    arr=[t1,t2,t3]
    print(t1,t2,t3,int(patient_id))
    data=findDocWithTags(int(patient_id),arr)
    count1=0
    for i in data:
        count2=0
        for j in i:
            lbl=Label(main,text=j)
            lbl.grid(row=count1,column=count2)
            count2+=1
        count1+=1
    back=Button(main,text="Go back",command=lambda:search(main))
    back.grid(row=count1,column=count2)
    l=Label(main,text="please give id of doctor you want to book")
    l.grid(row=count1+1,column=count2)
    txt1 = Entry(main, width=10)
    txt1.grid(row=count1+2,column=count2)
    submit=Button(main,text="submit",command=lambda: commonsubmit(main,txt1.get()))
    submit.grid(row=count1+3,column=count2)
    root.mainloop()

def symptoms(f):
    global root
    f.destroy()
    main=Frame(root)
    main.pack()
    lbl=Label(main,text="please enter your symptoms")
    lbl.pack()
    txt1 = Entry(main, width=10)
    txt1.pack()
    txt2 = Entry(main, width=10)
    txt2.pack()
    txt3 = Entry(main, width=10)
    txt3.pack()
    button1=Button(main,text="Submit",command=lambda: symptomsdata(main,txt1.get(),txt2.get(),txt3.get()))
    button1.pack()
    back=Button(main,text="Go back",command=lambda:search(main))
    back.pack()
    root.mainloop()
def IDdata(f,t):
    global root
    f.destroy()
    main=Frame(root)
    main.pack()
    data=findDocWithId(t)
    count =0
    for j in data:
        lbl=Label(main,text=j)
        lbl.grid(row=0,column=count)
        count+=1
    back=Button(main,text="Go back",command=lambda:search(main))
    back.grid(row=1,column=count)
    l=Label(main,text="please give id of doctor you want to book")
    l.grid(row=2,column=count)
    txt1 = Entry(main, width=10)
    txt1.grid(row=3,column=count)
    submit=Button(main,text="submit",command=lambda: commonsubmit(main,txt1.get()))
    submit.grid(row=4,column=count)
    root.mainloop()
def ID(f):
    global root
    f.destroy()
    main=Frame(root)
    main.pack()
    lbl=Label(main,text="please enter your doctor's id")
    lbl.pack()
    txt1 = Entry(main, width=10)
    txt1.pack()
    button1=Button(main,text="Submit",command=lambda: IDdata(main,txt1.get()))
    button1.pack()
    back=Button(main,text="Go back",command=lambda:search(main))
    back.pack()
    root.mainloop()
def specializationdata(f,t):
    global root
    f.destroy()
    main=Frame(root)
    main.pack()
    data=findDocWithSpecialization(t)
    count1=0
    for i in data:
        count2=0
        for j in i:
            lbl=Label(main,text=j)
            lbl.grid(row=count1,column=count2)
            count2+=1
        count1+=1
    back=Button(main,text="Go back",command=lambda:search(main))
    back.grid(row=count1,column=count2)
    l=Label(main,text="please give id of doctor you want to book")
    l.grid(row=count1+1,column=count2)
    txt1 = Entry(main, width=10)
    txt1.grid(row=count1+2,column=count2)
    submit=Button(main,text="submit",command=lambda: commonsubmit(main,txt1.get()))
    submit.grid(row=count1+3,column=count2)
    root.mainloop()
    
def specialization(f):
    global root
    f.destroy()
    main=Frame(root)
    main.pack()
    lbl=Label(main,text="please enter specialization you are looking for")
    lbl.pack()
    txt1 = Entry(main, width=10)
    txt1.pack()
    button1=Button(main,text="Submit",command=lambda: specializationdata(main,txt1.get()))
    button1.pack()
    back=Button(main,text="Go back",command=lambda:search(main))
    back.pack()
    root.mainloop()

def search(f):
    global root
    f.destroy()
    main=Frame(root)
    main.pack()
    button1=Button(main,text="Symptoms",command=lambda: symptoms(main))
    button1.pack()
    button2=Button(main,text="ID",command=lambda: ID(main))
    button2.pack()
    button3=Button(main,text="Specialization",command=lambda: specialization(main))
    button3.pack()
    back=Button(main,text="Go back",command=lambda:patient1(patient_id,main))
    back.pack()
    root.mainloop()
def patient1(x,f):
    global root,patient_id
    f.destroy()
    patient_id=x
    main=Frame(root)
    main.pack()
    button1=Button(main,text="check bookings")
    button1.pack()
    button2=Button(main,text="Search",command=lambda: search(main))
    button2.pack()
    root.mainloop()
def doctor():
    global root
    main=Frame(root)
    main.pack()
    lbl=Label(main,text="Please enter your doctor's id")
    lbl.pack()
    txt = Entry(main, width=10)
    txt.pack()
    button=Button(main,text="Submit",command=lambda: submitdoc(txt.get(),main))
    button.pack()
    root.mainloop()
def clearwelcome(x,f):
    global root
    f.destroy()
    if x ==1:
        doctor()
    else: 
        patient()

root = Tk()
root.geometry("1920x1080")
root.title("DocnetMD")
main = Frame(root)
main.pack()
lbl=Label(main,text="Welcome to DocnetMD")
lbl.pack()
button1 = Button(main,text="Click here if you are a doctor", fg="black", command=lambda: clearwelcome(1,main))
button1.pack()
button2 = Button(main,text="Click here if you are a patient", fg="black", command=lambda: clearwelcome(2,main))
button2.pack()
root.mainloop()

connection.commit()

