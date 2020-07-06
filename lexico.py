import ply.lex as lex

reserved = {
    'if' : 'IF',
    'elif' : 'ELIF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'for' : 'FOR',
    'let' : 'LET',
    'var' : 'VAR',
    'const' : 'CONST',
    'number' : 'VARNUMBER',
    'string' : 'VARSTRING',
    'boolean' : 'VARBOOLEAN',
    'any' : 'ANY',
    'enum' : 'enum',
    'true' : 'TRUE',
    'false' : 'FALSE',
}

tokens = [
    'NUMBER',
    'FLOAT',
    'PLUS',
    'MINUS',
    'PRODUCT',
    'MOD',
    'POTENCIA',
    'DIVIDE',
    'GREATER',
    'LESS',
    'EQUALTO',
    'NOTEQUALTO',
    'LPAREN',
    'RPAREN',
    'VARIABLE',
    'EQUAL',
    'TWOPOINTS',
    'END',
] + list(reserved.values())

#Valores
t_NUMBER = r'[0-9]+'
t_FLOAT = r'[0-9]+\.[0-9]+'


#simbolos
t_PLUS = r'\+'
t_MINUS = r'-'
t_PRODUCT = r'\*'
t_POTENCIA = r'\*\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUAL = r'='
t_MOD = '%'
t_GREATER = r'>=?'
t_LESS = r'<=?'
t_EQUALTO = r'=='
t_NOTEQUALTO = r'!='
t_TWOPOINTS = r'\:'
t_END = r';'

#Reservados
t_IF = r'if'
t_ELIF = r'elif'
t_ELSE = r'else'
t_WHILE = r'while'
t_FOR = r'for'
t_LET = r'let'
t_VAR = r'var'
t_CONST = r'const'
t_VARNUMBER = r'number'
t_VARSTRING = r'string'
t_VARBOOLEAN = r'boolean'
t_ANY = r'any'
t_TRUE = r'true'
t_FALSE = r'false'


t_ignore = ' \t'

def t_VARIABLE(t):
    r'[a-z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'VARIABLE')    # Check for reserved words
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("No se ha reconocido el token '%s' " % t.value[0])
    t.lexer.skip(1)


# Build the lexer
cadena = "let x: boolean = true;"
lexer = lex.lex()
lexer.input(cadena)

while(True):
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)


