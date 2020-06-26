from tkinter import*
import smtplib
mailid=""
password=""
root=Tk()
root.geometry("400x300")
root.resizable(0,0)
l11=Label(root,text="Email Sender",font="Helvetica 25 bold").place(x=100,y=0)
l21=Label(root,text="From:").place(x=0,y=70)
e11=Entry(root,width="30")
e11.place(x=100,y=70)

l22=Label(root,text="Password:").place(x=0,y=100)
e12=Entry(root,width="30",show="*")
e12.place(x=100,y=100)

l2=Label(root,text="To:").place(x=0,y=130)
e1=Entry(root,width="30")
e1.place(x=100,y=130)
l3=Label(root,text="Message:").place(x=0,y=160)
e2=Entry(root,width="40")
e2.place(x=100,y=160)
l4=Label(root)
l4.place(x=0,y=210)
def sendemail():
    try:
        mailid=str(e11.get())
        password=str(e12.get())
        recipnt=str(e1.get())
        msg=str(e2.get())
        server=smtplib.SMTP('smtp.gmail.com',587)
        
        server.starttls()
        server.login(mailid,password)
        server.sendmail(mailid,recipnt,msg)
        server.quit()
        l4.configure(text="Email Succesfully send",font="Helvetica 15 bold")
    except:    
        l4.configure(text="Email not send,failed network",font="Helvetica 10 bold")
    
b1=Button(root,text="Send",command=sendemail,width="8").place(x=170,y=250)

root.mainloop()
