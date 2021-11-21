from tkinter import *
from tkinter import ttk,messagebox
import googletrans
from googletrans import Translator



# import googletrans

# from googletrans import Translator

root=Tk()
root.geometry("1080x400")
root.title("@Avk Translator")
root.wm_iconbitmap("Translator.ico")
root.resizable(False,False)
root.configure(background="black")

def label_language():
    x1=combo1.get()
    x2=combo2.get()
    label1.configure(text=x1)
    label2.configure(text=x2)
    root.after(100,label_language)


def translate_now():
  input_text=text1.get(1.0,END)
  t1=Translator()
  trans_text=t1.translate(input_text,src=combo1.get(),dest=combo2.get())
  trans_text=trans_text.text

  text2.delete(1.0,END)
  text2.insert(END,trans_text)



# Arrow image
# arrow_image=PhotoImage(file="arrow.png")
# image_label=Label(root,image=arrow_image,width=550)
# image_label.place(x=460,y=50)
languages=googletrans.LANGUAGES
languageV=list(languages.values())
lang1=languages.keys()


# 1st  combobox
combo1=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo1.place(x=110,y=20)
combo1.set("English")

label1=Label(root,text="ENGLISH",font="segoe 30 bold",bg="black",fg="cyan",width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=50)

# 2nd  comboBox
combo2=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo2.place(x=730,y=20)
combo2.set("Select Language")

label2=Label(root,text="ENGLISH",font="segoe 30 bold",bg="black",fg="orange",width=18,bd=5,relief=GROOVE)
label2.place(x=630,y=50)


# 1st frame
f=Frame(root,bg="white",bd=5)
f.place(x=10,y=118,width=440,height=200)

text1=Text(f,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)


scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# 2ND frame
f=Frame(root,bg="white",bd=5)
f.place(x=630,y=118,width=440,height=200)

text2=Text(f,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)


scrollbar2=Scrollbar(f)
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Translate Button
translate=Button(root,text="Translate",font="Roboto 15 ",activebackground="White",cursor="hand2",bd=1,width=10,height=2,fg="cyan",bg='black',command=translate_now)
translate.place(x=476,y=170)



label_language()


root.mainloop()