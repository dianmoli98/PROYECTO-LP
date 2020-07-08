#Molina Diana
#Marlon Lindao
#Dennys Lopez

import ply.lex as lex

reserved = {
    'let' : 'LET',
    'var' : 'VAR',
    'const' : 'CONST',
    'number' : 'VARNUMBER',
    'string' : 'VARSTRING',
    'boolean' : 'VARBOOLEAN',
    'enum' : 'ENUM',
    'null' : 'NULL',
    'undefined' : 'UNDEFINED',
    'static' : 'STATIC',
    'typeof' : 'TYPEOF',
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
    'charAt': 'FUNCTIONCHARAT',
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
    'LCOMILLA',
    'RCOMILLA',

    'GREATER',
    'LESS',
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
    'DOLLAR',
    'PRINT',
    'COMMENT',

] + list(reserved.values())

#Valores
t_NUMBER = r'[0-9]+'
t_FLOAT = r'[0-9]+\.[0-9]+'
t_NORMSTRING1 = r'\".*\"' #Falta arreglar los dos norm y el multi
t_NORMSTRING2 = r'\'.*\''
t_MULTISTRING = r'`(.*\n?)*`'
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
t_LCOMILLA = r'“'
t_RCOMILLA = r'”'

t_GREATER = r'>=?'
t_LESS = r'<=?'
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
t_DOLLAR = r'\$'


#Reservados
t_LET = r'let'
t_VAR = r'var'
t_CONST = r'const'
t_VARNUMBER = r'number'
t_VARSTRING = r'string'
t_VARBOOLEAN = r'boolean'
t_ENUM = r'enum'
t_NULL = r'null'
t_UNDEFINED = r'undefined'
t_STATIC = r'static'
t_INSTANCEOF = r'instanceof'
t_TYPEOF = r'typeof'

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
t_FUNCTIONCHARAT= r'charAt'


t_ignore = ' \t'


def t_PRINT(t):
    r'console.log'
    t.type = reserved.get(t.value,'PRINT')    # Check for reserved words
    return t

def t_COMMENT(t):
    r'\/\/[a-z_][a-zA-Z_0-9\s]*'
    t.type = reserved.get(t.value,'COMMENT')    # Check for reserved words
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
    print("No se ha reconocido el token '%s' " % t.value[0])
    t.lexer.skip(1)


# Build the lexer
cadena = "//esto es un comentario  "

lexer = lex.lex()
lexer.input(cadena)

while(True):
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)


