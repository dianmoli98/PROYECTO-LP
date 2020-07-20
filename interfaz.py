from tkinter import *
#import sintacticoNewLang
import parser
root=Tk()
root.geometry("400x400")
root.title("GUI-NEWLANGS")

entrada=Entry(root)
entrada.grid(row=0,columnspan=6,sticky=W+E)#izq a derecha y ocupe toda la celda


resultado=StringVar()
resultado.set("aqui va el resultado")
salida=Label(root)
salida.config(textvariable=resultado)
salida.grid(row=1,columnspan=6,sticky=SE)#derecha

def clear_all():
    entrada.delete(0,END)
    resultado.set("")


def probar_expression():
    entrada_exp=entrada.get()
    try:
        exp_input=parser.expr(entrada_exp).compile() #expresion ingresada para compilarse+
        result= eval(exp_input)
        #salida.salida.insert(0,str(result))
        resultado.set(result)
        #resultado.set("bien")
    except:
        resultado.set("ERROR")


#ACCIONES
Button(root,text="PROBAR",width=20,height=2,command=lambda:probar_expression()).grid(row=2,column=0,sticky=SE)

Button(root,text="BORRAR",width=20,height=2,command=lambda:clear_all()).grid(row=2,column=1,sticky=SE)
root.mainloop()