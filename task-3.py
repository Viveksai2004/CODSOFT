from tkinter import *

class list:
    def __init__(self,task):
        self.task=task
        self.task.title('To do list')  
        self.task.geometry('800x700')

        self.label1=Label(
                     self.task,text='To-do-list',font=("Times New Roman",50,"bold"),width=25,bg='orange')
        self.label1.pack()

   
        self.label2=Label(
                     self.task,text='ADD TASK',font=('calibri',25,"bold"),width=10,bg='orange')
        self.label2.place(x=30,y=100)

        self.label3=Label(
                      self.task,text="Tasks",font=('calibri',25,"bold"),width=10,bg='orange')
        self.label3.place(x=400,y=100)

        self.main_text=Listbox(self.task,height=15,width=30,font=('italic',20,"bold"),bg='light grey')
        self.main_text.place(x=310,y=150)

        self.text=Text(self.task,height=2,width=15,font=('italic',20,"bold"),bg='light grey')
        self.text.place(x=20,y=150)

        def add():
            content=self.text.get(1.0,END)
            self.main_text.insert(END,content)
            with open('data.txt','a') as file:
                file.write(content)
                file.seek(0)        
                file.close()
            self.text.delete(1.0,END)

        def delete():
            delete=self.main_text.curselection()
            look=self.main_text.get(delete)
            with open('data.txt','r+') as f:
                new_f=f.readlines()
                f.seek(0)
                for line in new_f:
                    item=str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete)

        with open('data.txt','r') as file:
            read=file.readlines()  
            for l in read:
                ready=l.split()
                self.main_text.insert(END, ready)
            file.close()

        self.button=Button(self.task,text='ADD',font=('calibri',25,"bold"),width=10,bg='orange',command=add)
        self.button.place(x=20,y=250)
 
        self.button2=Button(self.task,text='DELETE',font=('calibri',25,"bold"),width=10,bg='orange',command=delete)
        self.button2.place(x=20,y=350)   

def main():
    task=Tk()
    a=list(task)
    task.mainloop()             


if __name__=="__main__" :
    main()
    