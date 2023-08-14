import tkinter as tk
from tkinter import *
import random 

questions=[
           " Which batsman has most international Centuries?",
           " Which batsman has hit 6 sixes in an over vs Srilanka?",
           " Who took most number of wickets in test Cricket'?",
           " Which team won the ICC World Cup in 2019'?",
           " What is highest score of kohli in ODI's'?"
             ]

answers_choice=[
    ["Ricky Ponting","Sachin Tendulkar","Sangakara","Virat Kohli"],
    ["Yuvraj Singh","Gibbs","Dhoni","Pollard"],
    ["Muralidharan","Anil Kumble","Jimmy Anderson","Shane Warne"],
    ["India","England","Newzealand","Australia"],
    ["145","179","183","195"],
]

answers = [1,3,0,1,2]

user_answer = []

indexes=[]
def generator():
    global indexes
    while(len(indexes)<5):
        x=random.randint(0,4)
        if x in indexes:
            continue
        else:
            indexes.append(x)
     #print(indexes)

def showresult(score):
    labelquestion.destroy()
    op1.destroy()
    op2.destroy()
    op3.destroy()
    op4.destroy()
    labelresult=Label(quiz,text=f'Your score is {score}/5 ', font=("Times New Roman",50,"bold"),bg="light green")
    labelresult.pack(pady=(100,50))
    labelpercent=Label(quiz,text= f'You secured {score/5*100}% ', font=("Times New Roman",50,"bold"),bg="light green")
    labelpercent.pack(pady=(100,50))


def calc():
    global indexes,user_answer,answers
    x=0
    score=0
    for i in indexes:
        if user_answer[x]==answers[i]:
            score=score+1
        x=x+1
    print(score)
    showresult(score)


ques=1
def selected():
    global option,user_answer
    global labelquestion,op1,op2,op3,op4
    global ques
    x=option.get()
    user_answer.append(x)
    option.set(-1)
    if ques<5:
        labelquestion.config(text=questions[indexes[ques]])
        op1['text']=answers_choice[indexes[ques]][0]
        op2['text']=answers_choice[indexes[ques]][1]
        op3['text']=answers_choice[indexes[ques]][2]
        op4['text']=answers_choice[indexes[ques]][3]
        ques+=1
        
    else:
        print(indexes)
        print(user_answer)
        print(answers)
        calc()

def startquiz():
    global labelquestion,op1,op2,op3,op4
    labelquestion = Label(quiz,
                          text = questions[indexes[0]],
                          font = ("Times New Roman",30),
                          width = 500,
                          justify = "left",
                          wraplength = 700,
                          bg='white')
    labelquestion.pack(pady=(100,30))

    global option
    option = IntVar()
    option.set(-1)

    op1 = Radiobutton(quiz,
                       text=answers_choice[indexes[0]][0],
                       font=("Times New Roman",25),
                       value=0,
                       variable=option,
                       command=selected,
                       bg='white')
    op1.pack(pady=5)

    op2 = Radiobutton(quiz,
                       text=answers_choice[indexes[0]][1],
                       font=("Times New Roman",25),
                       value=1,
                       variable=option,
                       command=selected,
                       bg='white')
    op2.pack(pady=5)

    op3 = Radiobutton(quiz,
                       text=answers_choice[indexes[0]][2],
                       font=("Times New Roman",25),
                       value=2,
                       variable=option,
                       command=selected,
                       bg='white')
    op3.pack(pady=5)

    op4 = Radiobutton(quiz,
                       text=answers_choice[indexes[0]][3],
                       font=("Times New Roman",25),
                       value=3,
                       variable=option,
                       command=selected,
                       bg='white')
    op4.pack(pady=5)


def startispressed():
    labeltext.destroy()
    labelinstruction.destroy()
    labelRules.destroy()
    btnStart.destroy()
    generator()
    startquiz()

quiz=tk.Tk()
quiz.geometry('800x600')
quiz.title('Quiz Game by Vivek sai')

quiz.config(bg='white')


labeltext = Label(quiz,text="Cricket Quiz", font=("Times New Roman",70,"bold"),bg="white")
labeltext.pack(pady=(0,50))

image1 = PhotoImage(file="start.png")

btnStart = Button(quiz,image=image1,relief=FLAT,border=0,command = startispressed)
btnStart.pack()

labelinstruction = Label(quiz,text='READ THE RULES AND\nClick Start Once You are Ready',bg='light green',font=("Times New Roman",25 ),justify='center')
labelinstruction.pack()

labelRules = Label(quiz,
                   text =  "1. This quiz contains 5 questions \n 2. You will get 20 seconds to solve a question. \n 3. Once you select an Option that will be the final answer \n  4. Hence, think before you answer",
                   width = 100,
                   font = ("Times New Roman",15))
labelRules.pack()

quiz.mainloop()