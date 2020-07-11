import ply.yacc as yacc
import lexico_NewLang as mylexer
tokens = mylexer.tokens


#Statement(1 linea de codigo)
def p_statement(p):
    '''statement : statement_value
    | statement_value POINTCOMMA'''
    p[0] = p[1]


def p_statement_value(p):
    '''statement_value : expression
    | concatenate
    | declare
    | assign'''
    p[0] = p[1]


#Declaration of Variables
def p_declare(p):
    '''declare : var_boolean
    | var_number
    | var_string
    | declare_generic'''
    p[0] = p[1]


#Declaration of var_number
def p_var_number(p):
    'var_number : declare_number EQUAL number_value'
    p[0] = 110


def p_declare_number(p):
    'declare_number : declare_any TWOPOINTS VARNUMBER'


def p_number_value(p):
    'number_value : expression'


#Declaration of var boolean
def p_var_boolean(p):
    'var_boolean : declare_boolean EQUAL boolean_value'
    p[0] = 120


def p_declare_boolean(p):
    'declare_boolean : declare_any TWOPOINTS VARBOOLEAN'


def p_declare_boolean_value(p):
    '''boolean_value : boolean
    | variable'''


#Declaration of var_string
def p_var_string(p):
    'var_string : declare_string EQUAL string_value'
    p[0] = 130


def p_declare_string(p):
    'declare_string : declare_any TWOPOINTS VARSTRING'


def p_string_value(p):
    '''string_value : string
    | variable'''


#General Declarator when data type is not specified
def p_declare_generic(p):
    'declare_generic : declare_any EQUAL assign_value'
    p[0] = 100


#Can be used for all declarations
def p_declare_any(p):
    'declare_any : prefix VARIABLE'


#Assignments
def p_assign(p):
    'assign : VARIABLE EQUAL assign_value'
    p[0] = 50


def p_assign_value(p):
    '''assign_value : expression
    | boolean
    | string'''


#ConcatenationString--Review
def p_concatenate(p):
    'concatenate : termS'
    p[0] = 300


def p_concatenate_term(p):
    'termS : string PLUS chain'
    p[0] = 1.0


def p_chain(p):
    '''chain : termS PLUS value
    | value'''


def p_value(p):
    '''value : expression
    | string'''


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
    'term : term PRODUCT term'
    p[0] = p[1] * p[3]


def p_term_div(p):
    'term : term DIVIDE term'
    if p[3] != 0:
        p[0] = p[1] / p[3]


def p_expression_increment(p):
    '''term : term1 INCREMENT
    | INCREMENT  term1'''
    p[0]= None

def p_expression_decrement(p):
    '''term : term1 DECREMENT
     | DECREMENT  term1'''
    p[0] = None

def p_term1(p):
    '''term1 : number
    | variable
    | group'''
    p[0] = p[1]

def p_group_expr(p):
    '''group : LPAREN variable RPAREN
        | LPAREN  number  RPAREN'''
    p[0] = p[2]

def p_term_factor(p):
    '''term : number
    | factor_expr
    | variable'''
    p[0] = p[1]


def p_factor_expr(p):
    'factor_expr : LPAREN expression RPAREN'
    p[0] = p[2]



#Terminals
def p_prefix(p):
    '''prefix : LET
    | VAR
    | STATIC
    | CONST'''


def p_number(p):
    '''number : NUMBER
    | FLOAT'''
    p[0] = float(p[1])


def p_string(p):
    'string : NORMSTRING1'


def p_boolean_value(p):
    '''boolean : TRUE
    | FALSE'''


def p_variable(p):
    'variable : VARIABLE'
    p[0] = 1


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