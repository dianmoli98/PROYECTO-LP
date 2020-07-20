import ply.yacc as yacc
import lexico_NewLang as mylexer
tokens = mylexer.tokens


# Statement(1 code line)
def p_statement(p):
    '''statement : atomicstatement
    | atomicstatement statement'''
    p[0] = 1

def p_atomicStatement(p):
    '''atomicstatement : statement_value
    | statement_value POINTCOMMA'''
    p[0] = 1


def p_statement_value(p):
    '''statement_value : concatenate
    | expression
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
    | functionStatement
    | consoleLog'''
    p[0] = 1


def p_statement_control(p):
    '''statement_control : funcionif
    | funcionwhile
    | funcionfor'''
    p[0] = 1


def p_consoleLog(p):
    '''consoleLog : PRINT LPAREN RPAREN
    | PRINT LPAREN VARIABLE RPAREN
    | PRINT LPAREN string RPAREN'''
    p[0] = 1


# comentarios
def p_declarationcomments(p):
    '''comments : COMMENT
    | MULTICOMMENT'''
    p[0] = 1


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
    | declare_tuples
    | declare_generic'''
    p[0] = 1


# Declaration of enum
def p_declare_enum(p):
    'declare_enum : ENUM OBJECTNAME LKEY enums RKEY'
    p[0] = 1


def p_enums(p):
    '''enums : enums_numeric
    | enums_string'''
    p[0] = 1



# For declarations of enums with numerics values
def p_enums_numeric(p):
    '''enums_numeric : enums_numeric COMMA enums_numeric_value
    | enums_numeric_value'''
    p[0] = 1



def p_enums_numeric_value(p):
    '''enums_numeric_value : object_name EQUAL number
    | object_name'''
    p[0] = 1



# For declarations of enums with string values
def p_enums_string(p):
    '''enums_string : enums_string COMMA enums_string_value
    | enums_string_value'''
    p[0] = 1


def p_enums_string_value(p):
    'enums_string_value : object_name EQUAL string'
    p[0] = 1

# FUNCTION
def p_functionDeclarar(p):
    '''functionStatement : FUNCTION VARIABLE LPAREN RPAREN substatement
    | FUNCTION VARIABLE LPAREN funcParametres RPAREN substatement'''
    p[0] = 1


def p_funtionParametres(p):
    '''funcParametres : VARIABLE
    | VARIABLE COMMA funcParametres'''
    p[0] = 1

# if
def p_condicionIf(p):
    '''funcionif : IF LPAREN formLog RPAREN substatement
    | IF LPAREN formLog RPAREN substatement funcionelif
    | IF LPAREN formLog RPAREN substatement funcionelif funcionelse
    | IF LPAREN formLog RPAREN substatement funcionelse
    | IF LPAREN VARIABLE INSTANCEOF OBJECTNAME RPAREN substatement

    '''
    p[0] = 1

# elif
def p_condicionElif(p):
    '''funcionelif : ELIF LPAREN formLog RPAREN substatement
    | ELIF LPAREN formLog RPAREN substatement funcionelif '''
    p[0] = 1


# else
def p_condicionElse(p):
    '''funcionelse : ELSE substatement'''
    p[0] = 1


# for
def p_condicionFor(p):
    '''funcionfor : FOR LPAREN LET VARIABLE EQUAL number_value POINTCOMMA formLog POINTCOMMA term RPAREN substatement
    | FOR LPAREN VARIABLE EQUAL number_value POINTCOMMA formLog POINTCOMMA term RPAREN substatement
    | FOR LPAREN LET VARIABLE IN VARIABLE RPAREN substatement
    | FOR LPAREN VARIABLE IN VARIABLE RPAREN substatement
    '''
    p[0] = 1


# While
def p_condicionWhile(p):
    'funcionwhile : WHILE LPAREN formLog RPAREN substatement'
    p[0] = 1


def p_subStatement(p):
    '''substatement : LKEY statement RKEY
    | LKEY RKEY'''
    p[0] = 1

# Declaration of set
def p_declare_Set(p):
    'exp_set : declare_any EQUAL NEW SET LPAREN RPAREN'
    p[0] = 1

# Declaration of tuples
def p_declare_tuples(p):
    '''declare_tuples : declare_any TWOPOINTS tuples_2_variables
    | declare_any TWOPOINTS tuples_2_variables EQUAL tuples_2_values
    | declare_any TWOPOINTS tuples_3_variables
    | declare_any TWOPOINTS tuples_3_variables EQUAL tuples_3_values
    | declare_any TWOPOINTS tuples_4_variables
    | declare_any TWOPOINTS tuples_4_variables EQUAL tuples_4_values'''
    p[0] = 1


def p_declare_tuples_2_variables(p):
    'tuples_2_variables : LBRACKET types COMMA types RBRACKET'
    p[0] = 1


def p_declare_tuples_3_variables(p):
    'tuples_3_variables : LBRACKET types COMMA types COMMA types RBRACKET'
    p[0] = 1


def p_declare_tuples_4_variables(p):
    'tuples_4_variables : LBRACKET types COMMA types COMMA types COMMA types RBRACKET'
    p[0] = 1


def p_declare_tuples_2_values(p):
    'tuples_2_values : LBRACKET general_value COMMA general_value RBRACKET'
    p[0] = 1


def p_declare_tuples_3_values(p):
    'tuples_3_values : LBRACKET general_value COMMA general_value COMMA general_value RBRACKET'
    p[0] = 1


def p_declare_tuples_4_values(p):
    'tuples_4_values : LBRACKET general_value COMMA general_value COMMA general_value COMMA general_value RBRACKET'
    p[0] = 1


# Declaration of arrays
def p_declare_array(p):
    '''declare_array : declare_array_main_number
    | declare_array_main_boolean
    | declare_array_main_string
    | declare_generic_array'''
    p[0] = 1

# Declaration of array_number
def p_declare_array_main_number(p):
    '''declare_array_main_number : declare_array_number EQUAL list_number
    | declare_array_number EQUAL LBRACKET RBRACKET
    | declare_array_number'''
    p[0] = 1


def p_declare_array_number(p):
    '''declare_array_number : declare_number LBRACKET RBRACKET
    | declare_any TWOPOINTS ARRAY LESS VARNUMBER GREATER'''
    p[0] = 1


# Declaration of array_boolean
def p_declare_array_main_boolean(p):
    '''declare_array_main_boolean : declare_array_boolean EQUAL list_boolean
    | declare_array_boolean EQUAL LBRACKET RBRACKET
    | declare_array_boolean'''
    p[0] = 1


def p_declare_array_boolean(p):
    '''declare_array_boolean : declare_boolean LBRACKET RBRACKET
    | declare_any TWOPOINTS ARRAY LESS VARBOOLEAN GREATER'''
    p[0] = 1


# Declaration of array_string
def p_declare_array_main_string(p):
    '''declare_array_main_string : declare_array_string EQUAL list_string
    | declare_array_string EQUAL LBRACKET RBRACKET
    | declare_array_string'''
    p[0] = 1


def p_declare_array_string(p):
    '''declare_array_string : declare_string LBRACKET RBRACKET
    | declare_any TWOPOINTS ARRAY LESS VARSTRING GREATER'''
    p[0] = 1


# Declaration of generic array
def p_declare_generic_array(p):
    'declare_generic_array : declare_any EQUAL list_types'
    p[0] = 1


# Declaration of variables
def p_declare_null(p):
    'var_null : declare_any EQUAL NULL'
    p[0] = 1


def p_declare_undefined(p):
    'var_undefined : declare_any EQUAL UNDEFINED'
    p[0] = 1

# Declaration of var_number add funcionmath
def p_var_number(p):
    '''var_number : declare_number EQUAL number_value
    | declare_number EQUAL funcionmath
    | declare_number
    | declare_number EQUAL expression'''
    p[0] = 1


def p_declare_number(p):
    'declare_number : declare_any TWOPOINTS VARNUMBER'
    p[0] = 1


# Declaration of var boolean
def p_var_boolean(p):
    '''var_boolean : declare_boolean EQUAL boolean_value
    | declare_boolean'''
    p[0] = 1


def p_declare_boolean(p):
    'declare_boolean : declare_any TWOPOINTS VARBOOLEAN'
    p[0] = 1


# Declaration of var_string
def p_var_string(p):
    '''var_string : declare_string EQUAL string_value
    | declare_string'''
    p[0] = 1


def p_declare_string(p):
    'declare_string : declare_any TWOPOINTS VARSTRING'
    p[0] = 1


# Declaration of var_enum
def p_var_enum(p):
    '''var_enum : declare_var_enum EQUAL enum_value
    | declare_var_enum'''
    p[0] = 1


def p_declare_var_enum(p):
    'declare_var_enum : declare_any TWOPOINTS object_name'
    p[0] = 1


# General Declarator when data type is not specified
def p_declare_generic(p):
    '''declare_generic : declare_any EQUAL assign_value
    | declare_any'''
    p[0] = 1


# Can be used for all declarations
def p_declare_any(p):
    '''declare_any : prefix VARIABLE'''
    p[0] = 1


# Assignments
def p_assign(p):
    '''assign : assign_variable
    | assign_array
    | assign_object_value'''
    p[0] = 1

# Assign variable
def p_assign_variable(p):
    '''assign_variable : variable EQUAL assign_value
    | variable EQUAL funciones
    | variable EQUAL list_types'''
    p[0] = 1


# Assign array_value
def p_assign_array(p):
    'assign_array : array_value EQUAL general_value'
    p[0] = 1


# Assign object value
def p_assign_object_value(p):
    '''assign_object_value : object_value_form1 EQUAL general_value
    | object_value_form1 EQUAL list_types
    | object_value_form2 EQUAL general_value'''
    p[0] = 1


# Valores posibles para variables
def p_assign_value(p):
    '''assign_value : general_value
    | object_definition
    | tuples_list'''
    p[0] = 1


def p_tuples_list(p):
    'tuples_list : LBRACKET tuples_values RBRACKET'
    p[0] = 1


def p_tuples_values(p):
    '''tuples_values : tuples_values COMMA general_value
    | general_value'''
    p[0] = 1

# Definicion de un objeto
def p_object_definition(p):
    '''object_definition : LKEY attributes RKEY
    | LKEY RKEY '''
    p[0] = 1


def p_attributes_line(p):
    '''attributes : attributes COMMA attribute
    | attribute'''
    p[0] = 1


def p_attribute(p):
    '''attribute : variable TWOPOINTS general_value
    | variable TWOPOINTS list_types'''
    p[0] = 1


# Valor: String, operacion matematica, boolean
def p_general_value(p):
    '''general_value : expression
    | boolean
    | string
    | concatenate
    | string_object
    | expCond
    | expOpLog
    | expNeg
    | expEq
    | expNotEq'''
    p[0] = 1


# Lists_values
def p_list_types(p):
    '''list_types : list_number
    | list_boolean
    | list_string
    | LBRACKET RBRACKET'''
    p[0] = 1


# List number
def p_list_number(p):
    'list_number : LBRACKET numbers RBRACKET'
    p[0] = 1


def p_numbers(p):
    '''numbers : numbers COMMA number_value
    | number_value'''
    p[0] = 1


# List boolean
def p_list_boolean(p):
    'list_boolean : LBRACKET booleans RBRACKET'
    p[0] = 1


def p_booleans(p):
    '''booleans : booleans COMMA boolean_value
    | boolean_value'''
    p[0] = 1


# List string
def p_list_string(p):
    'list_string : LBRACKET strings RBRACKET'
    p[0] = 1


def p_stringss(p):
    '''strings : strings COMMA string_value
    | string_value'''


# Declarations values
def p_number_value(p):
    'number_value : expression'
    p[0] = 1


def p_declare_boolean_value(p):
    '''boolean_value : boolean
    | other_value
    | expCond
    | expOpLog
    | expNeg
    | expEq
    | expNotEq'''
    p[0] = 1


def p_string_value(p):
    '''string_value : string
    | other_value
    | string_object
    | concatenate'''
    p[0] = 1


# ConcatenationString--Review
def p_concatenate(p):
    '''concatenate : string PLUS termS'''
    p[0] = 1


def p_concatenate_term(p):
    '''termS : termS PLUS value
    | value'''
    p[0] = 1


def p_value(p):
    '''value : expression
    | string'''
    p[0] = 1


# Math Operations
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = 1


def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = 1


def p_expression_term(p):
    'expression : term'
    p[0] = 1


def p_term_product(p):
    'expression : expression PRODUCT expression'
    p[0] = 1


def p_term_div(p):
    'expression : expression DIVIDE expression'
    p[0] = 1

def p_term_mod(p):
    'expression : expression MOD expression'
    p[0] = 1

def p_expression_increment(p):
    '''term : term1 INCREMENT
    | INCREMENT  term1'''
    p[0] = 1


def p_expression_decrement(p):
    '''term : term1 DECREMENT
     | DECREMENT  term1'''
    p[0] = 1


def p_negation(p):
    '''expNeg : NEGATION expOpLog
        | NEGATION factor_exprlog
        | NEGATION boolean
        | NEGATION LPAREN expOpLog RPAREN
        | NEGATION VARIABLE
        '''
    p[0] = 1


def p_equalto(p):
    '''expEq : expCond EQUALTO expCond
    | factor_exprlog  EQUALTO factor_exprlog
    | expression EQUALTO expression  '''
    p[0] = 1


def p_notequal(p):
    '''expNotEq : expCond NOTEQUALTO expCond
    | factor_exprlog  NOTEQUALTO factor_exprlog
    | expression NOTEQUALTO expression  '''
    p[0] = 1


# Operaciones Condicionales
def p_expression_opLogico(p):
    '''expOpLog : expCond oplogico expCond
    | factor_exprlog  oplogico factor_exprlog
    | expression oplogico expression
    | boolean oplogico boolean'''
    p[0] = 1


def p_exp_logica(p):
    'factor_exprlog : LPAREN expCond RPAREN'
    p[0] = 1


def p_expression_condicional(p):
    '''expCond : expression operador expression
    | LPAREN expression operador expression RPAREN'''
    p[0] = 1


def p_term1_expr(p):
    '''term1 : LPAREN group RPAREN
    | group'''
    p[0] = 1


def p_group_expr(p):
    '''group : number
    | variable
    | array_value
    | object_value'''
    p[0] = 1


def p_term_factor(p):
    '''term : number
    | factor_expr
    | other_value'''
    p[0] = 1


def p_factor_expr(p):
    'factor_expr : LPAREN expression RPAREN'
    p[0] = 1


def p_other_value(p):
    '''other_value : variable
    | funciones
    | array_value
    | enum_value
    | object_value'''
    p[0] = 1

# FUNCIONES IF
def p_funcionLog(p):
    '''formLog : expCond
       | expOpLog'''
    p[0] = 1

# Object value
def p_object_value(p):
    '''object_value : object_value_form1
    | object_value_form2'''
    p[0] = 1

def p_string_object(p):
    'string_object : NEW OBJECTSTRING LPAREN string RPAREN'
    p[0] = 1

def p_object_value_form1(p):
    'object_value_form1 : variable POINT variable'
    p[0] = 1

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
    p[0] = 1

def p_typedate(p):
    '''typedate : types
        | ENUM'''
    p[0] = 1

def p_types(p):
    '''types : VARNUMBER
        | VARSTRING
        | VARBOOLEAN'''
    p[0] = 1

def p_number(p):
    '''number : NUMBER
    | FLOAT'''
    p[0] = 1

def p_string(p):
    '''string : NORMSTRING1
    | NORMSTRING2
    | MULTISTRING'''
    p[0] = 1

def p_boolean_value(p):
    '''boolean : TRUE
    | FALSE'''
    p[0] = 1

def p_variable(p):
    'variable : VARIABLE'
    p[0] = 1

def p_object_name(p):
    'object_name : OBJECTNAME'
    p[0] = 1

def p_operador(p):
    '''operador : GREATER
      | LESS
      | GREATEREQUAL
      | LESSEQUAL
      | EQUALTO
      | NOTEQUALTO'''
    p[0] = 1

def p_operadorlogico(p):
    '''oplogico : AND
      | OR'''
    p[0] = 1

# funciones
def p_funciones(p):
    '''funciones : funcionmath
    | funcionString
    | funcionArray
    | funcionConjunto'''
    p[0] = 1

# Math Funciones
def p_funcionMath(p):
    '''funcionmath : mathAbs
    | mathRound
    | mathPow'''
    p[0] = 1


def p_math_abs_declare(p):
    'mathAbs : declare_any EQUAL mathAbs'
    p[0] = 1


def p_math_abs(p):
    '''mathAbs : FUNMATH POINT  ABS LPAREN VARIABLE RPAREN
    | FUNMATH POINT  ABS LPAREN number_value RPAREN
    | FUNMATH POINT  ABS LPAREN MINUS  number_value RPAREN'''
    p[0] = 1


def p_math_round(p):
    '''mathRound : FUNMATH POINT  ROUND LPAREN VARIABLE RPAREN
    | FUNMATH POINT  ROUND LPAREN number_value RPAREN'''
    p[0] = 1


def p_math_pow(p):
    '''mathPow : FUNMATH POINT  POW LPAREN VARIABLE COMMA VARIABLE RPAREN
    | FUNMATH POINT  POW LPAREN number_value COMMA number_value RPAREN
    | FUNMATH POINT  POW LPAREN VARIABLE COMMA number_value RPAREN
    | FUNMATH POINT  POW LPAREN number_value COMMA VARIABLE RPAREN'''
    p[0] = 1

# String Funciones
def p_funcionesString(p):
    '''funcionString : stringCharAt
    | stringConcat
    | stringSplit'''
    p[0] = 1


def p_string_charAt(p):
    '''stringCharAt : VARIABLE POINT FUNCTIONCHARAT LPAREN VARIABLE RPAREN
    | VARIABLE POINT FUNCTIONCHARAT LPAREN number_value RPAREN'''
    p[0] = 1


def p_string_concat(p):
    '''stringConcat : VARIABLE POINT FUNCTIONCONCAT LPAREN VARIABLE RPAREN
    | VARIABLE POINT FUNCTIONCONCAT LPAREN string RPAREN
    '''
    p[0] = 1


def p_string_split(p):
    '''stringSplit : VARIABLE POINT FUNCTIONSPLIT LPAREN VARIABLE RPAREN
    | VARIABLE POINT FUNCTIONSPLIT LPAREN string RPAREN
    '''
    p[0] = 1

# Arrays funciones
def p_funcionesArray(p):
    '''funcionArray : arrayFilter
    | arrayConcat
    | arrayJoin'''
    p[0] = 1


def p_array_concat(p):
    '''arrayConcat : VARIABLE POINT FUNCTIONCONCAT LPAREN VARIABLE RPAREN
    | VARIABLE POINT FUNCTIONCONCAT LPAREN list_types RPAREN'''
    p[0] = 1


def p_array_join_declare(p):
    '''arrayJoin : declare_any arrayJoin
    | declare_any arrayJoin POINTCOMMA'''
    p[0] = 1


def p_array_join(p):
    '''arrayJoin : VARIABLE POINT FUNCTIONJOIN LPAREN VARIABLE RPAREN
    | VARIABLE POINT FUNCTIONJOIN LPAREN string RPAREN
    '''
    p[0] = 1


def p_array_filter(p):
    '''arrayFilter : VARIABLE POINT FUNCTIONFILTER LPAREN VARIABLE RPAREN'''
    p[0] = 1

# conjuntos Funciones
def p_funcionesConjuntos(p):
    '''funcionConjunto : conjuntoAdd
    | conjuntoHas'''
    p[0] = 1


def p_conjunto_add(p):
    '''conjuntoAdd : VARIABLE POINT FUNCTIONADD LPAREN VARIABLE RPAREN
    | VARIABLE POINT FUNCTIONADD LPAREN number_value RPAREN
    | VARIABLE POINT FUNCTIONADD LPAREN boolean_value RPAREN
    | VARIABLE POINT FUNCTIONADD LPAREN string RPAREN'''
    p[0] = 1


def p_conjunto_has(p):
    '''conjuntoHas : VARIABLE POINT FUNCTIONHAS LPAREN VARIABLE RPAREN
    | VARIABLE POINT FUNCTIONHAS LPAREN number_value RPAREN
    | VARIABLE POINT FUNCTIONHAS LPAREN boolean_value RPAREN
    | VARIABLE POINT FUNCTIONHAS LPAREN string RPAREN'''
    p[0] = 1

# Error rule for syntax errors

lineaError=None
list_Errors = []
NoError=[True]

def p_error(p):
    global flag_for_error
    flag_for_error=1

    NoError[0]=False

    if p is not None:
        #print("Error de syntax linea %s, en \'%s\'."%(str(lineaError),str(p.type)))
        #print("ValueError: Nombre \'%s\' no es definido."%(str(p.value)))
        var1 = "Error de syntax linea %s, en \'%s\'."%(str(lineaError),str(p.type))
        var2 = "ValueError: Nombre \'%s\' no es definido."%(str(p.value))
        list_Errors.append((var1, var2))
        # #print(dir(p))

    #else:
        #print("Fin de entrada inesperado.")


#PRUEBAS REALIZADAS POR DIANA MOLINA, DENNYS LOPEZ Y MARLON LINDAO

# var tupla: [string, number] = ["Hola",4];
# tipo de dato.
# var nombre2 = "Nombre:" + name + "Apellido:" + lastname;
# var age = "Edad:" + (edad +1);
#var str = new String("Ana");  
#var s:string=`Hola ${name}`
# function isLess(element, index, array) {var i:number =1;}

# console.log("Prueba\n");

# PRUEBASS CON DECLARACION DE VARIABLES
# let color;
# let color

# let eye = 10;
# let eye = 10
# var numero=18;
# let color=null
# let color=undefined;

# let eye: number = 10;
# let x: number = 40;
# let var1: number= 50;
# let var1: number= 9;
# var eye = 10;
# let color: string = "blue";
# var color2 = 'red';
# let name: string='Hola';
# var str1: string = "Ana";
# let va2r: boolean = true;
# let result: boolean = !var1;
# let result:boolean= var1>var2||var1<=var3;

# DECLARACION  DE ARREGLOS
# let miarray: number[];
# let miarray: number[] = [1,2,3,4,5];
# let x: Array<string> = ["Hola","Hola2"]
# var arreglo= [ 1 , 2,3,4,8];
# var arreglo2 = ["Lopez","Damian"];

# DECLARACION DE ENUM
# enum Color {Amarrillo, Azul, Rojo}
# enum Animal {Perro =1, Gato=23}
# let c: Color = Color.Rojo;
# let a: Animal = Animal. Perro;

# CONJUNTOS
# let set1 = new Set ();

# OPERACIONES MATEMATICAS
# let result: number= var1-var2;
# let result: number= var1-var2+var3;
# let result: number= (var1-var2)+var3;
# (4-5)+9;
# 5-6
# (8+9)-(4*5)
# (8+9)/var3
# let result:number=(var1-var2)+var3;

# CONTADOR
# contador++;
# --numero;
# index--;

# CONCATENACION
# var nombre = "Marlon" + "Lindao";
# var name = "Marlon"

# FUNCIONES MATEMIATICAS
# var numberAbs = Math.abs(-3);
# var numberRound = Math.round(2.6);
# var numberPow = Math.pow (4,2);
# Math.abs(-3);

# CONDICIONES
# 1 < 5 && 7>=6
# (1 < 5)&&(7>=6)
#! (1 < 5 && 7>=6)
# !var3
# let result: boolean= var1== v2ar;
# var1 || va3
# (var3-var8)&&(4-5)
# 3||(var7+ver5)

# FUNCIONES PARA STRINGS
# var str3: string = str1.concat(str2);
# str.charAt(0ErrorDetect
# FUNCIONES PARA ARREGLOS
# var result = arreglo1.concat(arreglo2);
# var result = arreglo.filter(isLess);
# arreglo.filter(isLess);
# var result = arreglo1.join(",");

# FUNCIONES PARA CONJUNTOS
# set1.add(1);
# let result:boolean =set1.has(1);
# FUNCIONES IF, FOR Y WHILE
# if (5>6) { }
# if (5>6) { } elif(i==1){}else{}
# if (5>6) { } elif(i==1){}elif(i==1){console.log("F")}else{}
# for (let i = 0; i < 3; i++) { var i:number= 1; }
# for(let i = 0; i < 3; i++) {if (5>6) { } elif(i==1){}elif(i==1){console.log("F")}else{}}
# for(let i in list) {if (5>6) { } elif(i==1){}elif(i==1){console.log("F")}else{} while (i==5) {str.charAt(0); console.log (x);}}
# while (i==5) {str.charAt(0); console.log (x);}
#console.log (x);

#Example multiline
"""

linea = '''while (i==5) {
    \nstr.charAt(0);
    \nconsole.log (x);}
    \nif (5>6) {var a=9; }
    \nelif(i==1){}
    \nelif(i==1){console.log(\"F\")}
    \nelse{}'''

resultado = parser.parse(linea)
print(resultado)

"""

# Build the parser
parser = yacc.yacc()


def complle_sintactico():
    return yacc.yacc()
'''
while True:
    listaArg = []

    try:
        s = input('Typescript > ')
        listaArg = s.split("\\" + "n")
        NoError[0]=True

    except EOFError:
        break
    for i in range(len(listaArg)):
        lineaError = i + 1

        linea = listaArg[i]
        # p.lineno(i)
        if not linea:
            continue
        result = parser.parse(linea)
        
        if not NoError[0]:
            break

        if (i+1)==len(listaArg):
            print("Compilacion Exitosa")
            #print(result)
'''
