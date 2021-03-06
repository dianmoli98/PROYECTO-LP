#Molina Diana
#Marlon Lindao
#Dennys Lopez
#GRUPO NEWLANG

import ply.lex as lex

list_errors = []

reserved = {
    'let' : 'LET',
    'var' : 'VAR',
    'const' : 'CONST',
    'number' : 'VARNUMBER',
    'string' : 'VARSTRING',
    'String' : 'OBJECTSTRING',
    'boolean' : 'VARBOOLEAN',
    'enum' : 'ENUM',
    'null' : 'NULL',
    'undefined' : 'UNDEFINED',
    'static' : 'STATIC',
    'instanceof' : 'INSTANCEOF',

    'if' : 'IF',
    'elif' :'ELIF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'for' : 'FOR',
    'in' : 'IN',

    'any' : 'ANY',
    'true' : 'TRUE',
    'false' : 'FALSE',

    'new' : 'NEW',
    'object' : 'VAROBJECT',
    'Array' : 'ARRAY',
    'Set' : 'SET',

    #FUNCIONES
    'Math': 'FUNMATH',
    'abs' : 'ABS',
    'round': 'ROUND',
    'pow':'POW',

    #FUNCIONES Strings
    'charAt': 'FUNCTIONCHARAT',
    'concat': 'FUNCTIONCONCAT',
    'split': 'FUNCTIONSPLIT',

    #FUNCIONES Arrays
    'join': 'FUNCTIONJOIN',
    'filter': 'FUNCTIONFILTER',

    #FUNCIONES Conjuntos
    'add': 'FUNCTIONADD',
    'has': 'FUNCTIONHAS',

    'function': 'FUNCTION'
}

tokens = [
    'NUMBER',
    'FLOAT',
    'VARIABLE',
    'NORMSTRING1',
    'NORMSTRING2',
    'MULTISTRING',
    'OBJECTNAME',
    'POINT',

    'PLUS',
    'MINUS',
    'PRODUCT',
    'MOD',
    'DIVIDE',

    'LBRACKET',
    'RBRACKET',
    'LPAREN',
    'RPAREN',
    'LKEY',
    'RKEY',

    'GREATER',
    'LESS',
    'GREATEREQUAL',
    'LESSEQUAL',
    'EQUAL',
    'EQUALTO',
    'NOTEQUALTO',
    'INCREMENT',
    'DECREMENT',

    'NEGATION',
    'AND',
    'OR',

    'TWOPOINTS',
    'COMMA',
    'POINTCOMMA',
    'SPECIAL',
    'PRINT',
    'COMMENT',
    'MULTICOMMENT'

] + list(reserved.values())

#Valores
t_NUMBER = r'[0-9]+'
t_FLOAT = r'[0-9]+\.[0-9]+'
t_NORMSTRING1 = r'\".*\"' #Falta arreglar los dos norm y el multi
t_NORMSTRING2 = r'\'.*\''
t_MULTISTRING = r'`(.* |\n | \$\{.*\})*`'
t_POINT = r'\.'

#simbolos
t_PLUS = r'\+'
t_MINUS = r'-'
t_PRODUCT = r'\*'
t_MOD = '%'
t_DIVIDE = r'/'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LKEY = r'\{'
t_RKEY = r'\}'

t_GREATER = r'>'
t_LESS = r'<'
t_GREATEREQUAL = r'>='
t_LESSEQUAL = r'<='
t_EQUAL = r'='
t_EQUALTO = r'=='
t_NOTEQUALTO = r'!='
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_NEGATION = r'!'

t_AND = r'&&'
t_OR = r'\|\|'

t_TWOPOINTS = r'\:'
t_COMMA = r','
t_POINTCOMMA = r';'
t_SPECIAL = r'`'


#Reservados
t_LET = r'let'
t_VAR = r'var'
t_CONST = r'const'
t_VARNUMBER = r'number'
t_VARSTRING = r'string'
t_VARBOOLEAN = r'boolean'
t_OBJECTSTRING = r'String'
t_ENUM = r'enum'
t_NULL = r'null'
t_UNDEFINED = r'undefined'
t_STATIC = r'static'
t_INSTANCEOF = r'instanceof'

t_IF = r'if'
t_ELSE = r'else'
t_ELIF = r'elif'
t_WHILE = r'while'
t_FOR = r'for'
t_IN = r'in'


t_ANY = r'any'
t_TRUE = r'true'
t_FALSE = r'false'

t_NEW = r'new'
t_VAROBJECT = r'object'
t_ARRAY = r'Array'
t_SET = r'Set'

#FUNCIONES
t_FUNMATH = r'Math'
t_ABS = r'abs'
t_ROUND = r'round'
t_POW = r'pow'

#FUNCIONES Strings

t_FUNCTIONCHARAT= r'charAt' # Tambien para Arrays
t_FUNCTIONCONCAT= r'concat'
t_FUNCTIONSPLIT= r'split'

#FUNCIONES Arrays
t_FUNCTIONJOIN= r'join'
t_FUNCTIONFILTER= r'filter'

#FUNCIONES Conjuntos
t_FUNCTIONADD= r'add'
t_FUNCTIONHAS= r'has'

t_FUNCTION= r'function'


t_ignore = ' \t'


def t_PRINT(t):
    r'console.log'
    t.type = reserved.get(t.value,'PRINT')    # Check for reserved words
    return t

def t_COMMENT(t):
    r'\/\/[a-zA-Z_0-9\s]*'
    t.type = reserved.get(t.value,'COMMENT')    # Check for reserved words
    return t

def t_MULTICOMMENT(t):
    r'\/\*(.|\n|\s)*\*\/'
    t.type = reserved.get(t.value,'MULTICOMMENT')    # Check for reserved words
    return t

def t_VARIABLE(t):
    r'[a-z_$][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'VARIABLE')    # Check for reserved words
    return t

def t_OBJECTNAME(t):
    r'([A-Z][a-z]*)+'
    t.type = reserved.get(t.value,'OBJECTNAME')    # Check for reserved words
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    #print("No se ha reconocido el token '%s' " % t.value[0])
    list_errors.append(("No se ha reconocido el token '%s' " % t.value[0], t.lexer.lineno))
    t.lexer.skip(1)


lexer = lex.lex()

def compile_lexico():
    return lex.lex()
#Test - Dennys Lopez

test1_assignacion="var arreglo1 = [\"Ana\",\"Juan\"];"

test_has="let set1 = new Set();" + "\nlet result:boolean =set1.has(1);"

test_join="var arreglo1 = [\"Ana\",\"Juan\"];"+ "\nvar result = arreglo1.join(\",\");"

test_concat="var str1: string = \"Ana\";"+ "\nvar str2: string = \"Maria\";"+ "\nvar str3: string = str1.concat(str2);"

test_for="for (let i = 0; i < 3; i++) {"+ "console.log (\"i:\" + i);" +"}"

test_multiLineaComment="/*" +"\nThis is multi line comment."+"\nI am a comment. :)"+"\n*/"




#test - Diana Molina T
test_enum="enum Color {Amarrillo, Azul, Rojo}"

test_set = "let set1 = new Set ();"

test_split = "var result = str.split(" "); "

test_comment = "//esto es un comentario de una linea"

test_while="let i: number=5;"+ "\nwhile (i==5) {"+  "\nconsole.log(\"I am an infinity while loop .\");" +"\n}"

test_suma= "56-8"


#test - Marlon Lindao
test_enum2= "enum Animal{Perro, Gato=1}" + "\nconst x: Animal = Animal.Perro"

test_tuple= "let x: [string,number] = [\"Hola mundo\",4.5]"

test_boolean = "static y: boolean = true"

test_boolean2 = "let b = (var1 <= 5)&&(var2 != 10)"



tests=[test1_assignacion,test_has,test_join,test_concat,test_for,test_while,test_enum,test_set,test_split,test_enum2,test_tuple,
       test_boolean,test_boolean2, test_comment,test_suma,test_multiLineaComment]


'''for i in tests:
    #print("\n"+i+"\n")
    lexer.input(i)
    while(True):
        tok = lexer.token()
        if not tok:
            break  # No more input
        #print(tok)'''



