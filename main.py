from tkinter import *
from tkinter import messagebox 
import base64



#Function message decrypt
def decrypt():
    password = code.get()
    
    if password == "1234": # type: ignore
     myframe2 = Toplevel(myframe) # type: ignore
     myframe2.title("decryption") 
     myframe2.geometry("800x200")
     myframe2.configure(bg= "#00bd56")

     message = text1.get(1.0,END) # type: ignore
     Encode_message.encod("ascil") # type: ignore
     base64_bytes = base64.b64decode(decode_message) # type: ignore
     decrypt = base64_bytes.decode("ascil")

     Label(myframe2,text="DECRYOT",font="arial",fg = "white", bg= "#00bd56").place(x=10,y=0) # type: ignore
     text2 = Text(myframe2,font="Rpbote 10", bg = "white",relief = GROOVE, wrap=WORD, bd = 0)
     text2.place( x = 10, y = 40, width = 380, height=150)
    
     text2.insert(END,decrypt)
    elif password =="":
       messagebox.showerror("decryption","input password")
    elif password !="1234":
       messagebox.showerror("decryption","invalid password")

#Function message encrypt
def encrypt():
    password = code.get()

    if password == "1234": # type: ignore
     myframe1 = Toplevel(myframe) # type: ignore
     myframe1.title("encryption") 
     myframe1.geometry("400x200")
     myframe1.configure(bg = "#ed3833")

     message = text1.get(1.0,END) # type: ignore
     Encode_message.encod("ascil") # type: ignore
     base64_bytes = base64.b64encode(encode_message) # type: ignore
     encrypt = base64_bytes.decode("ascil")

     Label(myframe1,text="ENCRYOT",font="arial",fg = "white", bg= "#ed3833").place(x=10,y=0) # type: ignore
     text2 = Text(myframe1,font="Rpbote 10", bg = "white",relief = GROOVE, wrap=WORD, bd = 0)
     text2.place( x = 10, y = 40, width = 380, height=150)
    
     text2.insert(END,encrypt)
    elif password =="":
       messagebox.showerror("encryption","input password")
    elif password !="1234":
       messagebox.showerror("encryption","invalid password")

#Function message reset
def reset():
    code.get()
    text1.delete(1.0,END)
    



myframe = Tk()
#frame
myframe.title("Encryption app - تطبيق تشفير الرسائل") #عنوان النافذة
myframe.geometry("925x500+300+200") #قياسس عرض وطول النافذة
myframe.configure(bg="white")
myframe.resizable(False,False)

#img
img = PhotoImage(file ="pyy/guu.png" ) # type: ignore
Label(myframe , image = img , bg="white",bd=0).place (x=50 ,y=50)

#icon
img_icon = PhotoImage(file="pyy/iconn.png")
myframe.iconphoto(False,img_icon)

#label
myLabel = Label(myframe, text="Enter the text to be Encrypted or Decrypted :"
                , fg="#043054", font="@BatangChe 13 bold", bg="#e6e9fc").place( x = 500, y = 5)

#text
text1 = Text(font="Robote 20", bg="white", relief = GROOVE, wrap=WORD, bd = 5)
text1.place( x = 515, y = 45, width = 355, height=100)


#labe1
myLabell = Label(myframe, text="Enter the Encryption or decryption password : ",
                  fg="#043054", font="@BatangChe 11 bold", bg="#e6e9fc").place( x=520, y = 170)

#enter code
code = StringVar()
code = Entry(myframe,textvariable=code, width=19, bd = 3, font="arial 25", show="*" ).place (x=520,y=210)

#button##3d478f##86b366
mybutton = Button(myframe, text="Encrypt", bg= "#31358f", fg="white",width = 16, height=2, font="@BatangChe 13 bold",bd=2, command= encrypt).place ( x=520, y=270)
mybutton = Button(myframe, text="Decrypt", bg= "#31358f", fg="white",width = 16, height=2, font="@BatangChe 13 bold",bd=2, command= decrypt).place ( x=700, y=270)
mybutton = Button(myframe, text="Reset", bg= "#43a185", fg="white",width = 30, height=2, font="@BatangChe 13 bold", command = reset, bd=2).place ( x=545, y=350)

myframe.mainloop() #امر بجعل النافذة مفتوحة الى ان اغلقها من زر الاغلاق
