import tkinter as tk
space_text=""
def add_to_space(self):
    global space_text
    space_text=space_text+str(self)
    space.delete("1.0","end")
    space.insert("1.0",space_text)
def calculate():
    global space_text
    result=str(eval(space_text))
    space.delete("1.0","end")
    space.insert("1.0",result)
def clear():
    global space_text
    space_text=""
    space.delete("1.0","end")

calculator=tk.Tk()
calculator.geometry("295x295")
space=tk.Text(calculator,height=2,width=21,font=("calibri",20))
space.grid(row=1,column=1,columnspan=4)
 
btn_1=tk.Button(calculator,text="1",command=lambda:add_to_space(1),width=5,font=("calibri",14))
btn_1.grid(row=4,column=1)

btn_2=tk.Button(calculator,text="2",command=lambda:add_to_space(2),width=5,font=("calibri",14))
btn_2.grid(row=4,column=2)

btn_3=tk.Button(calculator,text="3",command=lambda:add_to_space(3),width=5,font=("calibri",14))
btn_3.grid(row=4,column=3)

btn_4=tk.Button(calculator,text="4",command=lambda:add_to_space(4),width=5,font=("calibri",14))
btn_4.grid(row=3,column=1)

btn_5=tk.Button(calculator,text="5",command=lambda:add_to_space(5),width=5,font=("calibri",14))
btn_5.grid(row=3,column=2)

btn_6=tk.Button(calculator,text="6",command=lambda:add_to_space(6),width=5,font=("calibri",14))
btn_6.grid(row=3,column=3)

btn_7=tk.Button(calculator,text="7",command=lambda:add_to_space(7),width=5,font=("calibri",14))
btn_7.grid(row=2,column=1)

btn_8=tk.Button(calculator,text="8",command=lambda:add_to_space(8),width=5,font=("calibri",14))
btn_8.grid(row=2,column=2)

btn_9=tk.Button(calculator,text="9",command=lambda:add_to_space(9),width=5,font=("calibri",14))
btn_9.grid(row=2,column=3)

btn_0=tk.Button(calculator,text="0",command=lambda:add_to_space(0),width=5,font=("calibri",14))
btn_0.grid(row=5,column=1)

btn_plus=tk.Button(calculator,text="+",command=lambda:add_to_space("+"),width=5,font=("calibri",14))
btn_plus.grid(row=2,column=4)

btn_minus=tk.Button(calculator,text="-",command=lambda:add_to_space("-"),width=5,font=("calibri",14))
btn_minus.grid(row=3,column=4)

btn_multiply=tk.Button(calculator,text="*",command=lambda:add_to_space("*"),width=5,font=("calibri",14))
btn_multiply.grid(row=4,column=4)

btn_divide=tk.Button(calculator,text="/",command=lambda:add_to_space("/"),width=5,font=("calibri",14))
btn_divide.grid(row=5,column=4)

btn_clear=tk.Button(calculator,text="clear",command=lambda:clear(),width=5,font=("calibri",14))
btn_clear.grid(row=6,column=4)

btn_point=tk.Button(calculator,text=".",command=lambda:add_to_space("."),width=5,font=("calibri",14))
btn_point.grid(row=5,column=2)

btn_open_paranthesis=tk.Button(calculator,text="(",command=lambda:add_to_space("("),width=5,font=("calibri",14))
btn_open_paranthesis.grid(row=6,column=1)

btn_closed_paranthesis=tk.Button(calculator,text=")",command=lambda:add_to_space(")"),width=5,font=("calibri",14))
btn_closed_paranthesis.grid(row=6,column=2)

btn_equal=tk.Button(calculator,text="=",command=lambda:calculate(),width=5,font=("calibri",14))
btn_equal.grid(row=6,column=3)

btn_percentage=tk.Button(calculator,text="%",command=lambda:add_to_space("%"),width=5,font=("calibri",14))
btn_percentage.grid(row=5,column=3)

calculator.mainloop()
