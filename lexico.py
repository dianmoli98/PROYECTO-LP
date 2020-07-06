import ply.lex as lex

reserved = {
    'if' : 'IF',
    'elif' : 'ELIF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'for' : 'FOR',
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

t_NUMBER = r'[0-9]+'
t_FLOAT = r'[0-9]+\.[0-9]+'
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
t_IF = r'if'
t_ELIF = r'elif'
t_ELSE = r'else'
t_WHILE = r'while'
t_FOR = r'for'
t_TWOPOINTS = r'\:'
t_END = r';'

t_ignore = r' \t'

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
cadena = "for if mds"
lexer = lex.lex()
lexer.input(cadena)

while(True):
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)


