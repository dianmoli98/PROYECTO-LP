from tkinter import *
import parser
root=Tk()
root.title("GUI-NEWLANGS")

entrada=Entry(root)
entrada.grid(row=0,columnspan=6,sticky=W+E)#izq a derecha y ocupe toda la celda


resultado=StringVar()
resultado.set("0")
salida=Label(root)
salida.config(textvariable=resultado)
salida.grid(row=1,columnspan=6,sticky=SE)#derecha

Button(root,text="PROBAR").grid(row=2,column=0,sticky=SE)
root.mainloop()