from tkinter import *
import lexico_NewLang as lexer
import sintacticoNewLang as parse
from tkinter import scrolledtext

import parser

lexico = lexer.compile_lexico()
sintactico = parse.complle_sintactico()

root=Tk()
root.geometry("580x660")
root.title("GUI-NEWLANGS")



titulo = StringVar()
titulo.set("Analizador Typescript")


title = Label(root,fg='blue', font=("Helvetica", 12))
title.config(textvariable=titulo)
title.grid(row=0,columnspan=6,sticky=W)

entrada = scrolledtext.ScrolledText(root,width=40,height=24)
#entrada=Text(root, height=20, width=20)
entrada.grid(row=1,columnspan=6,sticky=W+E) #izq a derecha y ocupe toda la celda


resultado=StringVar()
resultado.set("Resultado del Análisis")

salida=Label(root,fg='blue')
salida.config(textvariable=resultado)
salida.grid(row=3,columnspan=6,sticky=SE)#derecha

output=scrolledtext.ScrolledText(root, height=8, width=20)
output.grid(row=4,columnspan=6,sticky=W+E) #izq a derecha y ocupe toda la celda
output.config(state=DISABLED)

def clear_all():
    entrada.delete('1.0',END)
    lexer.list_errors.clear()
    parse.list_Errors.clear()
    lexico.lineno = 1
    parse.lineaError = 1
    output.config(state=NORMAL)
    output.delete('1.0',END)
    output.config(state=DISABLED)
    #resultado.set("")


def call_lexer():
    entrada_exp = entrada.get('1.0', END)
    lexer.list_errors.clear()
    lexico.lineno = 1
    listaArg = entrada_exp.split("\\" + "n")
    error = 0
    string_error = ""
    for i in listaArg:
        lexico.input(i)
        while (True):
            tok = lexico.token()
            if not tok:
                break  # No more input

    if len(lexer.list_errors) > 0:
        for e in lexer.list_errors:
            string_error += e[0] + "en la linea " + str(e[1]) + "\n"
            error += 1
    if error == 0:
        entrada_exp = "Todo el codigo ha sido reconocido"
    else:
        entrada_exp = "Su codigo tiene los siguientes errores:\n" + string_error

    output.config(state=NORMAL)
    output.delete('1.0', END)
    output.insert(INSERT, entrada_exp)
    output.config(state=DISABLED)


def call_sintactico():
    entrada_exp = entrada.get('1.0', END)

    salidaUI=parse.testUI(entrada_exp)
    if salidaUI==None:
        salidaUI=""

    output.config(state=NORMAL)
    output.delete('1.0', END)
    output.insert(INSERT, salidaUI)
    output.config(state=DISABLED)

def probar_expression():
    entrada_exp=entrada.get('1.0', END)
    try:
        exp_input=parser.expr(entrada_exp).compile() #expresion ingresada para compilarse+
        result= eval(exp_input)
        #salida.salida.insert(0,str(result))
        resultado.set(result)
        #resultado.set("bien")
    except:
        resultado.set("ERROR")


#ACCIONES
Button(root,text="LEXICO",bg='green', fg='white', font=('helvetica', 10, 'bold'),width=20,height=2,command=lambda: call_lexer()).grid(row=2,column=0,sticky=SE)

Button(root,text="SINTACTICO",bg='green', fg='white', font=('helvetica', 10, 'bold'),width=20,height=2,command=lambda:call_sintactico()).grid(row=2,column=1,sticky=SE)
Button(root,text="BORRAR",bg='red', fg='white', font=('helvetica', 10, 'bold'),width=20,height=2,command=lambda:clear_all()).grid(row=2,column=2,sticky=SE)
root.mainloop()