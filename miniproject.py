import tkinter
from tkinter import *
from tkinter import ttk

#connecting to mysql
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="2002",database="studentdb")
print("connected")
mycursor=mydb.cursor()
#mycursor.execute("create database studentdb")
#mycursor.execute("USE studentdb")
#mycursor.execute("create table stu_details(Firstname varchar(20),Lastname varchar(20),Title varchar(10),Age int,State varchar(20),numcourses int, coursesname varchar(20),numcoursesyet int,coursesnameyet varchar(20),teststatus int )")




def enter_data():
        # User info
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    title = title_combobox.get()
    age = age_spinbox.get()
    State = state_combobox.get()
            
            # Course info
    numcourses= numcourses_spinbox.get()
    numcoursesyet = numcoursesyet_spinbox.get()
    coursesname = coursesname_Entry.get()
    coursesnameyet = coursesnameyet_Entry.get()
    teststatus=vars.get()
    #sql connection to insert value
    sql = "INSERT INTO stu_details (Firstname, Lastname, Title, Age, State, numcourses, coursesname, numcoursesyet, coursesnameyet, teststatus) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (firstname, lastname, title, age, State, numcourses, coursesname, numcoursesyet, coursesnameyet, teststatus)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    #printing to get value
    print("Test Status:", vars.get())
    print("First name: ", firstname, "Last name: ", lastname)
    print("Title: ", title, "Age: ", age, "State: ", State)
    print("Completed courses: ", numcourses, "Course Name: ",coursesname)
    print("Incompleted courses: ", numcoursesyet, "Incompleted Course Name: ",coursesnameyet)
    print("------------------------------------------")

#creat window
window= tkinter.Tk()
window.title("Data Entry Form")
#creat frame
frame = tkinter.Frame(window)
frame.pack()


user_info_frame = tkinter.LabelFrame(frame,text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=20)


first_name_label = tkinter.Label(user_info_frame, text= "First Name")
first_name_label.grid(row=0 ,column=0 )
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0,column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1,column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["MR.","Ms.","Mrs.","Dr."])
title_label.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox =tkinter.Spinbox(user_info_frame, from_= 18, to=110)
age_label.grid(row=2,column=0)
age_spinbox.grid(row=3, column=0)

state_label = tkinter.Label(user_info_frame, text="State")
state_combobox = ttk.Combobox(user_info_frame, values=["Tamil Nadu", "Kerala", "Karnataka", "Andhra"])
state_label.grid(row=2, column=1)
state_combobox.grid(row=3, column=1)


for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20 )


numcourses_lable = tkinter.Label(courses_frame, text="Completed Courses")
numcourses_spinbox =tkinter.Spinbox(courses_frame, from_=0, to= 'infinity')
numcourses_lable.grid(row=0,column=0)
numcourses_spinbox.grid(row=1,column=0)

coursesname_lable = tkinter.Label(courses_frame, text="Course Name")
coursesname_Entry =tkinter.Entry(courses_frame)
coursesname_lable.grid(row=0,column=1)
coursesname_Entry.grid(row=1,column=1)

numcoursesyet_lable = tkinter.Label(courses_frame, text="Incompleted Courses")
numcoursesyet_spinbox =tkinter.Spinbox(courses_frame, from_=0, to= 'infinity')
numcoursesyet_lable.grid(row=2,column=0)
numcoursesyet_spinbox.grid(row=3,column=0)

coursesnameyet_lable = tkinter.Label(courses_frame, text="Incompleted Course Name")
coursesnameyet_Entry =tkinter.Entry(courses_frame)
coursesnameyet_lable.grid(row=2,column=1)
coursesnameyet_Entry.grid(row=3,column=1)



for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


Test_details_frame = tkinter.LabelFrame(frame, text="Test Details")
Test_details_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20 )

vars =IntVar()
test_completed = tkinter.Radiobutton(Test_details_frame, text="Yes completed", variable=vars, value=1, command=enter_data)
test_completed.grid(row=0, column=0)

test_completed = tkinter.Radiobutton(Test_details_frame, text="Not completed", variable=vars, value=2, command=enter_data)
test_completed.grid(row=0, column=1)

button = tkinter.Button(frame, text="Submit")
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

      


window.mainloop()