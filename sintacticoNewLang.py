import ply.yacc as yacc
import lexico_NewLang as mylexer
tokens = mylexer.tokens

#All
def p_all(p):
    '''all : statement
    | concatenate
    | assign'''
    p[0] = p[1]

#Declaration of Variables
def p_assign(p):
    '''assign : var_boolean'''
    p[0] = p[1]

#Declaration of var boolean
def p_var_boolean(p):
    '''var_boolean : declare_any EQUAL boolean
    | declare_boolean EQUAL boolean'''
    p[0] = 10000

def p_declare_boolean(p):
    'declare_boolean : prefix VARIABLE TWOPOINTS VARBOOLEAN'

#Can be used for all declarations
def p_declare_any(p):
    'declare_any : prefix VARIABLE'

#ConcatenationString--Review
def p_concatenate(p):
    'concatenate : termS'
    p[0] = 20000

def p_concatenate_termS(p):
    'termS : string PLUS chain'
    p[0] = 1.0

def p_chain(p):
    '''chain : termS PLUS value
    | value'''

def p_value(p):
    '''value : expression
    | string'''

#Statement
def p_statement_expression(p):
    'statement : expression'
    p[0] = p[1]

#Math Operations
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_product(p):
    'term : term PRODUCT factor'
    p[0] = p[1] * p[3]


def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

#Terminals
def p_prefix(p):
    '''prefix : LET
    | VAR
    | STATIC
    | CONST'''

def p_string(p):
    'string : NORMSTRING1'

def p_boolean_value(p):
    '''boolean : TRUE
    | FALSE'''

def p_factor_num(p):
    '''factor : NUMBER
    | FLOAT'''
    p[0] = float(p[1])

def p_factor_var(p):
    'factor : VARIABLE'
    p[0] = 1

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!: "+str(p))


# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('Typescript > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)