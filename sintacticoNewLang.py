import ply.yacc as yacc
import lexico_NewLang as mylexer
tokens = mylexer.tokens


# Statement(1 code line)
def p_statement(p):
    '''statement : statement_value
    | statement_value POINTCOMMA'''
    p[0] = p[1]


def p_statement_value(p):
    '''statement_value : expression
    | concatenate
    | declare
    | assign
    | expCond
    | expOpLog'''
    p[0] = p[1]


# Declaration of Variables, Array and Enum
def p_declare(p):
    '''declare : var_boolean
    | var_number
    | var_string
    | var_enum
    | declare_array
    | declare_enum
    | declare_generic'''
    p[0] = p[1]


# Declaration of enum
def p_declare_enum(p):
    'declare_enum : ENUM OBJECTNAME LKEY enums RKEY'
    p[0] = 500


def p_enums(p):
    '''enums : enums_numeric
    | enums_string'''


# For declarations of enums with numerics values
def p_enums_numeric(p):
    '''enums_numeric : enums_numeric COMMA enums_numeric_value
    | enums_numeric_value'''


def p_enums_numeric_value(p):
    '''enums_numeric_value : object_name EQUAL number
    | object_name'''


# For declarations of enums with string values
def p_enums_string(p):
    '''enums_string : enums_string COMMA enums_string_value
    | enums_string_value'''


def p_enums_string_value(p):
    'enums_string_value : object_name EQUAL string'


# Declaration of arrays
def p_declare_array(p):
    '''declare_array : declare_array_main_number
    | declare_array_main_boolean
    | declare_array_main_string
    | declare_generic_array'''
    p[0] = 400


# Declaration of array_number
def p_declare_array_main_number(p):
    '''declare_array_main_number : declare_array_number EQUAL list_number
    | declare_array_number'''


def p_declare_array_number(p):
    '''declare_array_number : declare_number LBRACKET RBRACKET
    | declare_any TWOPOINTS ARRAY LESS VARNUMBER GREATER'''


# Declaration of array_boolean
def p_declare_array_main_boolean(p):
    '''declare_array_main_boolean : declare_array_boolean EQUAL list_boolean
    | declare_array_boolean'''


def p_declare_array_boolean(p):
    '''declare_array_boolean : declare_boolean LBRACKET RBRACKET
    | declare_any TWOPOINTS ARRAY LESS VARBOOLEAN GREATER'''


# Declaration of array_string
def p_declare_array_main_string(p):
    '''declare_array_main_string : declare_array_string EQUAL list_string
    | declare_array_string'''

def p_declare_array_string(p):
    '''declare_array_string : declare_string LBRACKET RBRACKET
    | declare_any TWOPOINTS ARRAY LESS VARSTRING GREATER'''


# Declaration of generic array
def p_declare_generic_array(p):
    'declare_generic_array : declare_any EQUAL list_types'


# Declaration of variables
# Declaration of var_number
def p_var_number(p):
    '''var_number : declare_number EQUAL number_value
    | declare_number'''
    p[0] = 110


def p_declare_number(p):
    'declare_number : declare_any TWOPOINTS VARNUMBER'


# Declaration of var boolean
def p_var_boolean(p):
    '''var_boolean : declare_boolean EQUAL boolean_value
    | declare_boolean'''
    p[0] = 120


def p_declare_boolean(p):
    'declare_boolean : declare_any TWOPOINTS VARBOOLEAN'


# Declaration of var_string
def p_var_string(p):
    '''var_string : declare_string EQUAL string_value
    | declare_string'''
    p[0] = 130


def p_declare_string(p):
    'declare_string : declare_any TWOPOINTS VARSTRING'


# Declaration of var_enum
def p_var_enum(p):
    '''var_enum : declare_var_enum EQUAL enum_value
    | declare_var_enum'''
    p[0] = 140


def p_declare_var_enum(p):
    'declare_var_enum : declare_any TWOPOINTS object_name'


# General Declarator when data type is not specified
def p_declare_generic(p):
    '''declare_generic : declare_any EQUAL assign_value
    | declare_any'''
    p[0] = 100


# Can be used for all declarations
def p_declare_any(p):
    'declare_any : prefix VARIABLE'


# Assignments
def p_assign(p):
    '''assign : assign_variable
    | assign_array
    | assign_object_value'''
    p[0] = 50

# Assign variable
def p_assign_variable(p):
    '''assign_variable : variable EQUAL assign_value
    | variable EQUAL list_types'''


# Assign array_value
def p_assign_array(p):
    'assign_array : array_value EQUAL general_value'


# Assign object value
def p_assign_object_value(p):
    '''assign_object_value : object_value_form1 EQUAL general_value
    | object_value_form1 EQUAL list_types
    | object_value_form2 EQUAL general_value'''


# Valores posibles para variables
def p_assign_value(p):
    '''assign_value : general_value
    | object_definition'''


# Definicion de un objeto
def p_object_definition(p):
    'object_definition : LKEY attributes RKEY'


def p_attributes_line(p):
    '''attributes : attributes COMMA attribute
    | attribute'''


def p_attribute(p):
    '''attribute : variable TWOPOINTS general_value
    | variable TWOPOINTS list_types'''


# Valor: String, operacion matematica, boolean
def p_general_value(p):
    '''general_value : expression
    | boolean
    | string'''


# Lists_values
def p_list_types(p):
    '''list_types : list_number
    | list_boolean
    | list_string'''


# List number
def p_list_number(p):
    'list_number : LBRACKET numbers RBRACKET'


def p_numbers(p):
    '''numbers : numbers COMMA number_value
    | number_value'''


# List boolean
def p_list_boolean(p):
    'list_boolean : LBRACKET booleans RBRACKET'


def p_booleans(p):
    '''booleans : booleans COMMA boolean_value
    | boolean_value'''


# List string
def p_list_string(p):
    'list_string : LBRACKET strings RBRACKET'


def p_stringss(p):
    '''strings : strings COMMA string_value
    | string_value'''


# Declarations values
def p_number_value(p):
    'number_value : expression'


def p_declare_boolean_value(p):
    '''boolean_value : boolean
    | other_value'''


def p_string_value(p):
    '''string_value : string
    | other_value'''


# ConcatenationString--Review
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


# Math Operations
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


#Operaciones Condicionales
def p_expression_opLogico(p):
    '''expOpLog : expCond oplogico expCond
    | factor_exprlog  oplogico factor_exprlog
    | expression oplogico expression'''
    p[0] = 77.7


def p_exp_logica(p):
    'factor_exprlog : LPAREN expCond RPAREN'
    p[0] = p[2]


def p_expression_condicional(p):
    'expCond : expression operador expression'
    p[0]= 66.6


def p_term1_expr(p):
    '''term1 : LPAREN group RPAREN
    | group'''
    p[0] = 1


def p_group_expr(p):
    '''group : number
    | variable
    | array_value
    | object_value'''
    p[0] = p[1]


def p_term_factor(p):
    '''term : number
    | factor_expr
    | other_value'''
    p[0] = p[1]


def p_factor_expr(p):
    'factor_expr : LPAREN expression RPAREN'
    p[0] = p[2]


def p_other_value(p):
    '''other_value : variable
    | array_value
    | enum_value
    | object_value'''


# Object value
def p_object_value(p):
    '''object_value : object_value_form1
    | object_value_form2'''
    p[0] = 1


def p_object_value_form1(p):
    'object_value_form1 : variable POINT variable'


def p_object_value_form2(p):
    'object_value_form2 : variable POINT array_value'


# Array
def p_array_value(p):
    'array_value : variable LBRACKET expression RBRACKET'
    p[0] = 1


# Enum value
def p_enum_value(p):
    'enum_value : object_name POINT object_name'
    p[0] = 1


# Terminals
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
    '''string : NORMSTRING1
    | NORMSTRING2
    | MULTISTRING'''


def p_boolean_value(p):
    '''boolean : TRUE
    | FALSE'''


def p_variable(p):
    'variable : VARIABLE'
    p[0] = 1


def p_object_name(p):
    'object_name : OBJECTNAME'


def p_operador(p):
    '''operador : GREATER
      | LESS
      | GREATEREQUAL
      | LESSEQUAL
      | EQUALTO
      | NOTEQUALTO'''


def p_operadorlogico(p):
    '''oplogico : NEGATION
      | AND
      | OR'''


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