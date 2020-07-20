from tkinter import *
import lexico_NewLang as lexer
import sintacticoNewLang as parse

import parser

lexico = lexer.compile_lexico()

root=Tk()
root.geometry("500x400")
root.title("GUI-NEWLANGS")

titulo = StringVar()
titulo.set("Analizador Typescript")
title = Label(root)
title.config(textvariable=titulo)
title.grid(row=0,columnspan=6,sticky=SE)

entrada=Text(root, height=10, width=20)
entrada.grid(row=1,columnspan=6,sticky=W+E) #izq a derecha y ocupe toda la celda


resultado=StringVar()
resultado.set("aqui va el resultado")
salida=Label(root)
salida.config(textvariable=resultado)
salida.grid(row=2,columnspan=6,sticky=SE)#derecha

output=Text(root, height=10, width=20)
output.grid(row=3,columnspan=6,sticky=W+E) #izq a derecha y ocupe toda la celda
output.config(state=DISABLED)

def clear_all():
    entrada.delete('1.0',END)
    lexer.list_errors.clear()
    lexico.lineno = 1
    output.config(state=NORMAL)
    output.delete('1.0',END)
    output.config(state=DISABLED)
    #resultado.set("")


def call_lexer():
    entrada_exp = entrada.get('1.0', END)
    lexer.list_errors.clear()
    lexico.lineno = 1
    listaArg = entrada_exp.split("\\" + "n")
    linea = 0
    error = 0
    string_error = ""
    for i in listaArg:
        lexico.input(i)
        linea = linea + 1
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
Button(root,text="LEXICO",width=20,height=2,command=lambda: call_lexer()).grid(row=4,column=0,sticky=SE)
Button(root,text="SINTACTICO",width=20,height=2,command=lambda:probar_expression()).grid(row=4,column=1,sticky=SE)
Button(root,text="BORRAR",width=20,height=2,command=lambda:clear_all()).grid(row=4,column=2,sticky=SE)
root.mainloop()