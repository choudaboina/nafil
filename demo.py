import tkinter  as tk



root =Tk()

root.title("ursq")
root.geometry("644*434")



label(root,text="enter your bank:").grid(row=5,column=4)
entry(root).grid(row=0,colum=1)



label(root,text = "enter your password:").grid(row=5,column=4)
entry(root).grid(row=1,colum=1)



root.mainloop()
























