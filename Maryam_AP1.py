from Tkinter import *
from Tkinter import Tk, Frame, BOTH
from PIL import ImageTk, Image
from PIL import Image, ImageTk

import getpass
import os
import tkFont
import MySQLdb
import tkMessageBox

#import unittest


db = MySQLdb.connect("localhost", "root", "", "maryam") #connecting to the database
cursor = db.cursor()

status = 0

#class for mcq type questions
def MCQ():
    tkinter = Tk()
    tkinter.maxsize(700, 500)
    tkinter.minsize(700, 500)
    tkinter.geometry("500x500")
    tkinter.title("MCQ questions")
    tkinter.configure(background='royal blue')
    global m0, m1, m2, m3, m4, m5, m6, m7, m8, m9
    Label(tkinter, text="MCQ type questions", font=(None, 15),bg="royal blue", pady=20, ).grid(row=0, columnspan=2)
    Label(tkinter, text="Question Number: ", font="arial" ,bg="royal blue").grid(row=1, column=0, sticky=E)
    m0 = Entry(tkinter, bg="white", fg="black", width=30)
    m0.grid(row=1, column=1, sticky=W)
    m1 = "MCQ"
    Label(tkinter, text="Quiz Id: ", font="arial",bg="royal blue" ).grid(row=2, column=0, sticky=E)
    m2 = Entry(tkinter, bg="white", fg="black", width=30)
    m2.grid(row=2, column=1, sticky=W)
    Label(tkinter, text="Course Name: ", font="arial" ,bg="royal blue").grid(row=3, column=0, sticky=E)
    m3 = Entry(tkinter, bg="white", fg="black", width=30)
    m3.grid(row=3, column=1, sticky=W)
    Label(tkinter, text="Question: ", font="arial" ,bg="royal blue").grid(row=4, column=0, sticky=E)
    m4 = Entry(tkinter, bg="white", fg="black", width=30)
    m4.grid(row=4, column=1, sticky=W)
    Label(tkinter, text="a. ", font="arial" ,bg="royal blue").grid(row=5, column=0, sticky=E)
    m5 = Entry(tkinter, bg="white", fg="black", width=30)
    m5.grid(row=5, column=1, sticky=W)
    Label(tkinter, text="b. ", font="arial",bg="royal blue").grid(row=6, column=0, sticky=E)
    m6 = Entry(tkinter, bg="white", fg="black", width=30)
    m6.grid(row=6, column=1, sticky=W)
    Label(tkinter, text="c. ", font="arial",bg="royal blue").grid(row=7, column=0, sticky=E)
    m7 = Entry(tkinter, bg="white", fg="black", width=30)
    m7.grid(row=7, column=1, sticky=W)
    Label(tkinter, text="d. ", font="arial",bg="royal blue").grid(row=8, column=0, sticky=E)
    m8 = Entry(tkinter, bg="white", fg="black", width=30)
    m8.grid(row=8, column=1, sticky=W)
    Label(tkinter, text="Correct Answer: ", font="arial",bg="royal blue").grid(row=9, column=0, sticky=E)
    m9 = Entry(tkinter, bg="white", fg="black", width=30)
    m9.grid(row=9, column=1, sticky=W)
    Button(tkinter, text="save", command=stor_data, font="arial", bg="orange").grid(row=11, column=0)
    Button(tkinter, text="Submit", command=sub_data, font="arial", bg="orange").grid(row=11, column=1)

    tkinter.grid_columnconfigure(0, weight=1)
    tkinter.grid_columnconfigure(1, weight=1)

#class for true false type questions
def TF():
        tkinter = Tk()
        global m0, m1, m2, m3, m4, m5, m6, m7, m8, m9
        tkinter.maxsize(700, 500)
        tkinter.minsize(700, 500)
        tkinter.geometry("500x500")
        tkinter.configure(background='royal blue')
        Label(tkinter, text="True/False",
              font=(None, 15),bg="royal blue", pady=20, ).grid(row=0, columnspan=2)
        Label(tkinter, text="Question Number: ", font="arial" ,bg="royal blue").grid(row=1, column=0, sticky=E)
        m0 = Entry(tkinter, bg="white", width=30)
        m0.grid(row=1, column=1, sticky=W)
        m1 = "T/F"
        Label(tkinter, text="Quiz Id: ", font="arial" ,bg="royal blue").grid(row=2, column=0, sticky=E)
        m2 = Entry(tkinter, bg="white", width=30)
        m2.grid(row=2, column=1, sticky=W)
        Label(tkinter, text="Course Name: ", font="arial" ,bg="royal blue").grid(row=3, column=0, sticky=E)
        m3 = Entry(tkinter, bg="white", width=30)
        m3.grid(row=3, column=1, sticky=W)
        Label(tkinter, text="Question: ", font="arial" ,bg="royal blue").grid(row=4, column=0, sticky=E)
        m4 = Entry(tkinter, bg="white", width=30)
        m4.grid(row=4, column=1, sticky=W)
        Label(tkinter, text="a. ", font="arial" ,bg="royal blue").grid(row=5, column=0, sticky=E)
        m5 = Entry(tkinter, bg="white", width=30)
        m5.grid(row=5, column=1, sticky=W)
        Label(tkinter, text="b. ", font="arial" ,bg="royal blue").grid(row=6, column=0, sticky=E)
        m6 = Entry(tkinter, bg="white", width=30)
        m6.grid(row=6, column=1, sticky=W)
        Label(tkinter, text="Correct Answer: ", font="arial" ,bg="royal blue").grid(row=7, column=0, sticky=E)
        m9 = Entry(tkinter, bg="white", width=30)
        m9.grid(row=7, column=1, sticky=W)
        Button(tkinter, text="save", command=stor_data, font="arial", bg="orange").grid(row=9, column=0)
        Button(tkinter, text="Submit", command=sub_data, font="arial", bg="orange").grid(row=9, column=1)

        tkinter.grid_columnconfigure(0, weight=1)
        tkinter.grid_columnconfigure(1, weight=1)


#class for numeric type questions
def NUMERIC():
    tkinter = Tk()
    global m0, m1, m2, m3, m4, m5, m6, m7, m8, m9  #global variables

    tkinter.maxsize(800, 600)
    tkinter.minsize(800, 600)
    tkinter.geometry("500x500") #setting the geometry of the screen
    tkinter.configure(background='royal blue')
    Label(tkinter, text="Numeric question",font=(None, 15), pady=20,bg="royal blue" ).grid(row=0, columnspan=2)
    Label(tkinter, text="Question Number: ", font="arial" ,bg="royal blue").grid(row=1, column=0,sticky=E)
    m0 = Entry(tkinter,width=30)
    m0.grid(row=1, column=1,sticky=W)
    m1 = "NUMERIC"
    Label(tkinter, text="Quiz Id: ", font="arial" ,bg="royal blue").grid(row=3, column=0,sticky=E)
    m2 = Entry(tkinter, bg="white", width=30)
    m2.grid(row=2, column=1,sticky=W)
    Label(tkinter, text="Course Name: ", font="arial" ,bg="royal blue").grid(row=4, column=0,sticky=E)
    m3 = Entry(tkinter,  bg="white",width=30)
    m3.grid(row=3, column=1,sticky=W)
    Label(tkinter, text="Question: ", font="arial",bg="royal blue").grid(row=2, column=0,sticky=E)
    m4 = Entry(tkinter, bg="white", width=30)
    m4.grid(row=4, column=1,sticky=W)
    Label(tkiner, text="Correct Answer: ", font="arial",bg="royal blue").grid(row=5, column=0,sticky=E)
    m9 = Entry(tkinter, bg="white", fg="black", width=30)
    m9.grid(row=5, column=1,sticky=W)
    Button(tkinter, text="SAVE", command=stor_data, font="arial", bg="orange").grid(row=6, column=0)
    Button(tkinter, text="Submit", command=sub_data, font="arial", bg="orange").grid(row=6, column=1)

    tkinter.grid_columnconfigure(0, weight=1)
    tkinter.grid_columnconfigure(1, weight=1)

def quiz_intro():
    tkinter = Tk()
    global m2, m3  # global variables

    tkinter.maxsize(800, 600)
    tkinter.minsize(800, 600)
    tkinter.geometry("500x500")  # setting the geometry of the screen
    tkinter.configure(background='royal blue')
    Label(tkinter, text="Quiz Id: ", font="arial").grid(row=2, column=0, sticky=E)
    m2 = Entry(tkinter, bg="white", width=30)
    m2.grid(row=2, column=1, sticky=W)
    Label(tkinter, text="Course Name: ", font="arial").grid(row=3, column=0, sticky=E)
    m3 = Entry(tkinter, bg="white", width=30)
    m3.grid(row=3, column=1, sticky=W)



def sub_data():
    if (status):
        tkMessageBox.showinfo("Title", "Quiz Submitted Successfully !!")
    else:
        tkMessageBox.showinfo("Title", "Quiz Submission Failed!!")


def stor_data():
    global status
    quNum = int(m0.get())
    quType = m1
    quId = int(m2.get())
    corName = m3.get()

    quStat = m4.get()

    if quType == "MCQ": #if the question is of MCQ type
        op1 = m5.get()
        op2 = m6.get()
        op3 = m7.get()
        op4 = m8.get()
        corA = m9.get()
        sql = "insert into question values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        status = cursor.execute(sql, (quNum, quType, quStat, op1, op2, op3, op4, corA, quId, corName))
    elif quType == "T/F": #if the question is of T/F type
        op1 = m5.get()
        op2 = m6.get()
        corA = m9.get()
        op3 = None
        op4 = None
        sql = "insert into question values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        status = cursor.execute(sql, (quNum, quType, quStat, op1, op2, op3, op4, corA, quId, corName))
    elif quType == "NUMERIC":  #if the question is of Numeric type
        op1 = None
        op2 = None
        op3 = None
        op4 = None
        corA = m9.get()
        sql = "insert into question values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        status = cursor.execute(sql, (quNum, quType, quStat, op1, op2, op3, op4, corA, quId, corName))


def make_quiz():
    tkinter = Tk()
    tkinter.maxsize(700, 500)
    tkinter.minsize(700, 500)
    tkinter.geometry("500x500")
    tkinter.title("Choice of Questions")
    tkinter.configure(background='royal blue')
    Label(tkinter, text="\n What kind of questions would you like to include in the quiz? ", font=("arial",16, 'bold'),bg="royal blue", pady=20).grid(row=1, columnspan=2)
    Button(tkinter, text=" MCQs ", command=MCQ, justify = "center", font="arial",bg="coral").grid(row=6, column=0 , padx = 15 , pady = 15)
    Button(tkinter, text=" T/F ", command=TF, font="arial", bg="coral").grid(row=8, column=0 , padx = 15 , pady = 15)
    Button(tkinter, text=" NUMERIC ", command=NUMERIC, font="arial",bg="coral").grid(row=10, column=0 , padx = 15 , pady = 15)
    tkinter.grid_columnconfigure(0, weight=1)

def atmt_quiz():
    root = Tk()
    root.minsize(700, 500)
    root.maxsize(700, 500)
    root.configure(background='royal blue')
    global ques0, ques1
    Label(root, text="Enter Course Name & ID \n", font=(None, 15, 'bold') ,bg = 'royal blue').grid(row=2, columnspan=2)

    Label(root, text="Quiz ID: ", font="arial", padx = 10,pady=10 ,bg = 'royal blue').grid(row=3, column=0, sticky=E)
    ques0 = Entry(root, bg="white", width=30)
    ques0.grid(row=3, column=1, sticky=W)
    Label(root, text="Course Name: ", font="arial", pady=6 ,bg = 'royal blue').grid(row=5, column=0, sticky=E)
    ques1 = Entry(root, bg="white", width=30)
    ques1.grid(row=5, column=1, sticky=W)

    Button(root, text="Create", command=lambda: fet_quiz(root, ques0.get(), ques1.get()), font="arial", bg="orange").grid(row=7, pady=20,columnspan=2)


    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

def add_marks(x1):
    s1 = "insert into student values ('Student',112200,1,%s)"
    cursor.execute(s1, x1)


def chk(x, y):
    print x, y

def fet_quiz(test1, ques0, ques1):
    marks = 0
    tkinter = Tk()
    tkinter.maxsize(700, 500)
    tkinter.minsize(700, 500)
    tkinter.geometry("500x500")
    tkinter.configure(background='sky blue')
    id = int(ques0)
    cn = str(ques1).upper()


    try:
        sql = "select * from question where qid=%s and _cour=%s"
        cursor.execute(sql, (id, cn))
        results = cursor.fetchall()
        x = [0, 0]
        answer = [0, 0]

        def nex():
            if x[0] > 0:
                print x[1]
                if answer[0].get() == answer[1]:
                    x[1] += 1
                    print x[1]
            if x[0] > (len(results) - 1):
                tkinter.destroy()
                tkMessageBox.showinfo("Title", ("Quiz finished. No more attempts are available. Marks Obtained: %s" % x[1]))
                typ = str(x[1])
                add_marks(typ)
                return
            y = Label(tkinter, text="Question: %s " % results[x[0]][2], justify=LEFT, anchor=W,font=("arial", 12) ,bg="sky blue")
            y.pack()
            z = Label(tkinter, text="1) %s" % results[x[0]][3] ,bg="sky blue")
            z.pack()
            a = Label(tkinter, text="2) %s" % results[x[0]][4] ,bg="sky blue")
            a.pack()
            b = Label(tkinter, text="3) %s" % results[x[0]][5] ,bg="sky blue")
            b.pack()
            c = Label(tkinter, text="4) %s" % results[x[0]][6] ,bg="sky blue")
            c.pack()
            var = StringVar()
            ans = Entry(tkinter, textvariable=var)
            ans.pack()
            answer[0] = ans
            answer[1] = results[x[0]][7]
            # print type(int(ans.get()))f
            # if (ans.get()==results[x[0]][7]):
            #   x[1]+=1
            # print var.get()
            # sub=Button(master,text="Submit",command=sequence(nex,mar))
            sub = Button(master, text="Submit", command=nex, bg="white", font="arial")
            sub.pack()
            # chk(results[x[0][7]],var.get())

            x[0] += 1


        nex()
        # scrollbar.config(command=listbox.yview)
        # marks=112
        # tkMessageBox.showinfo("Title",marks)

        # while(x<len(results)):
    except:
        print "Error!"


def slct_quiz():
    tkinter = Tk()

    tkinter.maxsize(800, 500)
    tkinter.minsize(800, 500)
    tkinter.geometry("500x500")
    tkinter.title("Quiz Choices")
    tkinter.configure(background='sky blue')
    op = Label(text="\n Available Quizzes \n", font=("arial", 22 , "bold"),bg = 'sky blue')
    op.pack()

    op2 = Label(text="Courses and their IDs \n", font=("arial", 14) ,bg = 'sky blue')
    op2.pack()


    try:
        cursor.execute("select distinct qid,_cour from question")
        res = cursor.fetchall()
        for row in res:
            opt = Label(tkinter, text=" ID = %s , Course = %s \n " % row , font=("arial", 11) ,bg = 'sky blue')
            opt.pack()
    except:
        print "ERROR!!!!"


    atmt_quiz()

    mainloop()


def _log(ref):
    val1 = str(r0.get())
    val2 = int(r1.get())
    roll = (val1.upper())
    ref.destroy()
    if (roll == "INSTRUCTOR") and (val2 == 1234):   #if user is an instructor
        make_quiz()
    elif (roll == "STUDENT") and (val2 == 4321): #if user is a student
        slct_quiz()


#class SimpleTest(unittest.TestCase):
    # Returns True or False.
 #   def test(self):
  #      self.assertTrue(True)

if __name__ == '__main__':

    tkinter = Tk()
    tkinter.maxsize(900, 600)
    tkinter.minsize(900, 600)
    tkinter.geometry("700x700")
    tkinter.title("Login page")
    tkinter.configure(background='sky blue')
    Label(tkinter, text="\n Quizzing application",font=(None, 20, 'bold'),pady=20,bg = 'sky blue').grid(row=0, columnspan=2)
    Label(tkinter, text="Welcome to the login page", font=("arial",12, 'bold'), pady=20 ,bg = 'medium sea green').grid( row=1, columnspan=10, padx = 10)
   # Label(master, text="Login as Student or Instructor? \n Type Student or Instructor \n", font="arial", pady=20).grid(row=1, columnspan=2)

    Label(tkinter, text="Username: ", font="arial", pady=6 ,bg = 'sky blue').grid(row=2, column=0, padx = 15 , pady = 15) #username label
    #Label(tkinter, text="(Student/Instructor) ", font="arial", pady=10, bg='royal blue').grid(row=2, column=2, padx=15, pady=15)
    r0 = Entry(tkinter, bg="white", width=40)
    r0.grid(row=2, column=1, sticky=W)
    Label(tkinter, text="Password: ", font="arial", pady=6 ,bg = 'sky blue').grid(row=3, column=0, padx = 15 , pady = 15) #password label
    r1 = Entry(tkinter, bg="white", show="*", width=40)
    r1.grid(row=3, column=1, sticky=W)
  #  v = Intvar()
   # Radiobutton(tkinter,
    #            text="Python",
     #           padx=20,
      #          variable=v,
       #         value=1).pack(anchor=W)
    #Radiobutton(tkinter,
     #           text="Perl",
      #          padx=20,
       #         variable=v,
        #        value=2).pack(anchor=W)
    Button(tkinter, text="Log in", command=lambda: _log(tkinter), font="arial", bg="orange").grid(row=9, padx = 15 , pady = 15 ,columnspan=2) #the login button
    tkinter.grid_columnconfigure(0, weight=1)
    tkinter.grid_columnconfigure(1, weight=1)

   # unittest.main()
    mainloop() #main loop

