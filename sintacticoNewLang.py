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
    | expOpLog
    | expNeg
    | expEq
    | expNotEq
    | exp_set
    | statement_control
    | comments
    | consoleLog'''
    p[0] = p[1]

def p_statement_control(p):
    '''statement_control : funcionif
    | funcionwhile
    | funcionfor'''

def p_consoleLog(p):
    '''consoleLog : PRINT LPAREN RPAREN
    | PRINT LPAREN VARIABLE RPAREN
    | PRINT LPAREN string RPAREN'''
    print("console.log")

#comentarios
def p_declarationcomments(p):
    '''comments : COMMENT
    | MULTICOMMENT'''

# Declaration of Variables, Array and Enum
def p_declare(p):
    '''declare : var_boolean
    | var_number
    | var_string
    | var_enum
    | var_null
    | var_undefined
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

#if
def p_condicionIf(p):
    '''funcionif : IF LPAREN formLog RPAREN substatement
    | IF LPAREN formLog RPAREN substatement funcionelif
    | IF LPAREN formLog RPAREN substatement funcionelif funcionelse
    | IF LPAREN formLog RPAREN substatement funcionelse
    '''
    p[0] = 1000

#elif
def p_condicionElif(p):
    '''funcionelif : ELIF LPAREN formLog RPAREN substatement
    | ELIF LPAREN formLog RPAREN substatement funcionelif '''

#else
def p_condicionElse(p):
    '''funcionelse : ELSE substatement'''

#for
def p_condicionFor(p):
    '''funcionfor : FOR LPAREN prefix VARIABLE EQUAL number_value POINTCOMMA formLog POINTCOMMA term RPAREN substatement
    | FOR LPAREN VARIABLE EQUAL number_value POINTCOMMA formLog POINTCOMMA term RPAREN substatement
    '''
    p[0] = 1000


#While
def p_condicionWhile(p):
    '''funcionwhile : WHILE LPAREN formLog RPAREN substatement
    '''
def p_subStatement(p):
    '''substatement : LKEY statement RKEY
    | LKEY RKEY'''

#Declaration of set
def p_declare_Set(p):
    'exp_set : declare_any EQUAL NEW SET LPAREN RPAREN'
    p[0] = 600


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
def p_declare_null(p):
    'var_null : declare_any EQUAL NULL'
    p[0] =110.10

def p_declare_undefined(p):
    'var_undefined : declare_any EQUAL UNDEFINED'
    p[0] =120.20

# Declaration of var_number add funcionmath
def p_var_number(p):
    '''var_number : declare_number EQUAL number_value
    | declare_number EQUAL funcionmath
    | declare_number
    | declare_number EQUAL expression'''
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
    | variable EQUAL funciones
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
    | string
    | expCond
    | expOpLog
    | expNeg
    | expEq
    | expNotEq'''


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
    | other_value
    | expCond
    | expOpLog
    | expNeg
    | expEq
    | expNotEq'''


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

def p_expression_minus(p):
    'expression : expression MINUS term'

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


def p_negation(p):
    '''expNeg : NEGATION expOpLog
        | NEGATION factor_exprlog
        | NEGATION boolean
        | NEGATION LPAREN expOpLog RPAREN
        '''
    p[0] = 88.8

def p_equalto(p):
    '''expEq : expCond EQUALTO expCond
    | factor_exprlog  EQUALTO factor_exprlog
    | expression EQUALTO expression  '''
    p[0] = 99.9

def p_notequal(p):
    '''expNotEq : expCond NOTEQUALTO expCond
    | factor_exprlog  NOTEQUALTO factor_exprlog
    | expression NOTEQUALTO expression  '''
    p[0] = 99.9


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
    '''expCond : expression operador expression
    | LPAREN expression operador expression RPAREN'''
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
    | funciones
    | array_value
    | enum_value
    | object_value'''

#FUNCIONES IF
def p_funcionLog(p):
    '''formLog : expCond
       | expOpLog'''

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

def p_typedate(p):
    '''typedate : VARNUMBER
        | VARSTRING
        | VARBOOLEAN
        | ENUM'''

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
    '''oplogico : AND
      | OR'''
#funciones
def p_funciones(p):
    '''funciones : funcionmath
    | funcionString
    | funcionArray
    | funcionConjunto'''

#Math Funciones
def p_funcionMath(p):
    '''funcionmath : mathAbs
    | mathRound
    | mathPow'''

def p_math_abs_declare(p):
    'mathAbs : declare_any EQUAL mathAbs'

def p_math_abs(p):
    '''mathAbs : FUNMATH POINT  ABS LPAREN VARIABLE RPAREN
    | FUNMATH POINT  ABS LPAREN number_value RPAREN
    | FUNMATH POINT  ABS LPAREN MINUS  number_value RPAREN'''

def p_math_round(p):
    '''mathRound : FUNMATH POINT  ROUND LPAREN VARIABLE RPAREN
    | FUNMATH POINT  ROUND LPAREN number_value RPAREN'''

def p_math_pow(p):
    '''mathPow : FUNMATH POINT  POW LPAREN VARIABLE COMMA VARIABLE RPAREN
    | FUNMATH POINT  POW LPAREN number_value COMMA number_value RPAREN
    | FUNMATH POINT  POW LPAREN VARIABLE COMMA number_value RPAREN
    | FUNMATH POINT  POW LPAREN number_value COMMA VARIABLE RPAREN'''

#String Funciones
def p_funcionesString(p):
    '''funcionString : stringCharAt
    | stringConcat
    | stringSplit'''

def p_string_charAt(p):
    '''stringCharAt : VARIABLE POINT FUNCTIONCHARAT LPAREN VARIABLE RPAREN
    | VARIABLE POINT FUNCTIONCHARAT LPAREN number_value RPAREN'''

def p_string_concat(p):
    '''stringConcat : VARIABLE POINT FUNCTIONCONCAT LPAREN VARIABLE RPAREN
    | VARIABLE POINT FUNCTIONCONCAT LPAREN string RPAREN
    '''
def p_string_split(p):
    '''stringSplit : VARIABLE POINT FUNCTIONSPLIT LPAREN VARIABLE RPAREN
    | VARIABLE POINT FUNCTIONSPLIT LPAREN string RPAREN
    '''

#Arrays funciones
def p_funcionesArray(p):
    '''funcionArray : arrayFilter
    | arrayConcat
    | arrayJoin'''

def p_array_concat(p):
    '''arrayConcat : VARIABLE POINT FUNCTIONCONCAT LPAREN VARIABLE RPAREN
    | VARIABLE POINT FUNCTIONCONCAT LPAREN list_types RPAREN'''

def p_array_join_declare(p):
    '''arrayJoin : declare_any arrayJoin
    | declare_any arrayJoin POINTCOMMA'''

def p_array_join(p):
    '''arrayJoin : VARIABLE POINT FUNCTIONJOIN LPAREN VARIABLE RPAREN
    | VARIABLE POINT FUNCTIONJOIN LPAREN string RPAREN
    '''

def p_array_filter(p):
    '''arrayFilter : VARIABLE POINT FUNCTIONFILTER LPAREN VARIABLE RPAREN'''

#conjuntos Funciones
def p_funcionesConjuntos(p):
    '''funcionConjunto : conjuntoAdd
    | conjuntoHas'''

def p_conjunto_add(p):
    '''conjuntoAdd : VARIABLE POINT FUNCTIONADD LPAREN VARIABLE RPAREN
    | VARIABLE POINT FUNCTIONADD LPAREN number_value RPAREN
    | VARIABLE POINT FUNCTIONADD LPAREN boolean_value RPAREN
    | VARIABLE POINT FUNCTIONADD LPAREN string RPAREN'''

def p_conjunto_has(p):
    '''conjuntoHas : VARIABLE POINT FUNCTIONHAS LPAREN VARIABLE RPAREN
    | VARIABLE POINT FUNCTIONHAS LPAREN number_value RPAREN
    | VARIABLE POINT FUNCTIONHAS LPAREN boolean_value RPAREN
    | VARIABLE POINT FUNCTIONHAS LPAREN string RPAREN'''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!: "+str(p))

#PRUEBASS
#let eye = 10;
#var numero=18;
#let eye: number = 10;
#let x: number = 40;
#let var1: number= 50;
#let var1: number= 9;
#let result: boolean= var1== var2;
#var eye = 10;
#let color: string = "blue";
#var color2 = 'red';
#let name: string='Hola';
#var str1: string = "Ana";

#let list: number [] = [1,2,3];
#let x: Array<string> = ["Hola","Hola2"]
#var arreglo2 = ["Lopez","Damian"];
#var arreglo= [ 1 , 2,3,4,8];
#let set1 = new Set ();
#enum Color {Amarrillo, Azul, Rojo}

#let c: Color = Color.Rojo;
#let a: Animal = Animal. Perro;

#contador++;
#--numero;
#index--;

#var nombre = "Marlon" + "Lindao";
#var name = "Marlon"

#var numberAbs = Math.abs(-3);
#var numberRound = Math.round(2.6);
#var numberPow = Math.pow (4,2);

#1 < 5 && 7>=6
#(1 < 5)&&(7>=6)
#! (1 < 5 && 7>=6)


#let result: number= var1-var2;
#let result: number= var1-var2+var3;
#let result: number= (var1-var2)+var3;
#let va2r: boolean = true;

# var tupla: [string, number] = ["Hola",4]                           NO coge
#enum Animal {enum Animal {Perro =1, Gato,}                          NO SALE
#var nombre2 = “Nombre:” + name + “\n” + “Apellido:” + lastname;      NOSALE
#var age = “Edad:” + (edad +1);                                      NO SALE                                                
#let result: boolean = var1 == var2 || var1>=var3;                   NO SALE
#let result: boolean =! var1;                                        NO SAEL
#var str = new String("Ana");  #                                      NO SALE
#function isLess(element, index, array)                              NO SALE

## Pruebas Dennys Lopez

# if (5>6) { }
# if (5>6) { } elif(i==1){}else{}
# if (5>6) { } elif(i==1){}elif(i==1){console.log("F")}else{}
#for (let i = 0; i < 3; i++) { }                                    
#while (i==5) {str.charAt(0);}                                              
#console.log (x);  

#str.charAt(0);
#var str3: string = str1.concat(str2);
#var result = arreglo1.join(",");
#var result = str.split(" ");
#var result = arreglo.filter(isLess);
#arreglo.filter(isLess);

#set1.add(1);
#let result:boolean =set1.has(1);

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

