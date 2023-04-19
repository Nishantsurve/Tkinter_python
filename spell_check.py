import tkinter
from tkinter import *
from textblob import TextBlob

    
root = Tk()
root.title("My spell checker")
root.geometry("700x400")
root.config(background="#dae6f6")


def check_sp():
    word= spell_chk.get()
    a = TextBlob(word)
    right = str(a.correct())
    
    cs =  Label(root, text ="Correct Text is : ",font=("poppins" ,20,"bold"),bg="#dae6f6",fg = "#364971")
    cs.place(x=100,y=250)
    spell.config(text = right)


text_heading=Label(root, text ="Spelling checker",font= ("Trebuchet MS",30,"bold"), bg="#dae6f6",fg ="#364971")
text_heading.pack(pady=(50,0))

text_check = Label(root, text ="Enter the spelling", font= ("Trebuchet",20,"bold"), bg= "#dae6f6",fg="#364971")
text_check.pack()

spell_chk = Entry(root,justify="center", font= ("poppins",25), width= 30 , border=2, bg="white")
spell_chk.pack(pady=10)
spell_chk.focus()

check_btn = Button(root, text ="Check",  font= ("arial",20,"bold"),fg="white",bg="red", command= check_sp)
check_btn.pack()

spell = Label(root , font =("poppins",20),fg = "#364971",bg ="#dae6f6")
spell.place(x=350, y=250)

root.mainloop()
