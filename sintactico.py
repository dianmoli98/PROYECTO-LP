import ply.yacc as yacc
import lexico as mylexer
tokens = mylexer.tokens

def p_all(p):
    ''' all : statement'''
    p[0] = p[1]

def p_statement_expression(p):
    'statement : expression'
    p[0] = p[1]

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