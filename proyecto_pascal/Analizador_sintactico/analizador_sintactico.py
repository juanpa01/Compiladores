import ply.yacc as yacc
import re
import sys
import codecs
import os
from analizador_lexico_pascal import tokens
from sys import stdin

precedence = (
            #derecha a izquierda
            ('rigth','ASSIGMENT'),
            ('rigth','ELSE'),
            #izquierda a derecha
            ('left','MINUS','PLUS'),
            ('left','AND','OR'),
            ('left','NOT'),
            ('left','LESS','LESSEQUAL','GREATER','GREATEREQUEAL'),
            ('left','ASTERIK','SLASH'),
            ('left','LPARENT','RPARENT')
            )

def p_program (p):
    '''program : PROGRAM ID SEMICOLON block PERIOD'''
    print "program"

def p_block (p):
    '''block : constant_definition_part variable_declaration_part function_declaration_part stament_part'''
    print "block"

def p_constant_definition_part (p):
    '''constant_definition_part : constant_definition_part CONST constant_definition SEMICOLON'''
    print "constant_definition_part"

def p_constant_definition_part2 (p):
    '''constant_definition_part : empty'''
    print "nulo"

def p_constant_definition (p):
    '''constant_definition : ID constant_definition'''
    print "constant_definition"

def p_constant_definition2 (p):
    '''constant_definition : COMMA ID constant_definition'''
    print "constant_definition2"

def p_constant_definition3 (p):
    '''constant_definition : EQUAL INTNUMBER constant_definition'''
    print "constant_definition3"

def p_constant_definition4 (p):
    '''constant_definition : EQUAL FLOATNUMBER constant_definition'''
    print "constant_definition4"

def p_constant_definition5 (p):
    '''constant_definition : empty'''
    print "nulo"

def p_variable_declaration_part (p):
    '''variable_declaration_part : variable_declaration_part VAR id_list COLON type SEMICOLON'''
    print "variable_declaration_part"

def p_variable_declaration_part2 (p):
    '''variable_declaration_part : empty'''
    print "nulo"

def p_id_list (p):
    '''id_list : ID'''
    print "id_list"

def p_id_list2 (p):
    '''id_list : id_list COMMA ID'''
    print "id_list2"

def p_type (p):
    '''type : INT'''
    print "type"

def p_type2 (p):
    '''type : FLOAT'''
    print "type2"

def p_type3 (p):
    '''type : STRING'''
    print ""

def p_type4 (p):
    '''type : CHAR'''
    print "type4"

def p_type5 (p):
    '''type : BOOLEAN'''
    print "type5"

def p_function_declaration_part (p):
    '''function_declaration_part : FUN ID arguments COLON type SEMICOLON block '''
    print "function_declaration_part"

def p_function_declaration_part2 (p):
    '''function_declaration_part : empty'''
    print "nulo"

def p_arguments (p):
    '''arguments : LPARENT parameter_list RPARENT'''
    print "arguments"

def p_arguments2 (p):
    '''arguments : empty'''
    print "nulo"

def p_parameter_list (p):
    '''parameter_list : id_list COLON type'''
    print "parameter_list"

def p_parameter_list2 (p):
    '''parameter_list : parameter_list SEMICOLON id_list COLON type'''
    print "parameter_list2"

def p_stament_part (p):
    '''stament_part : compound_stament'''
    print "stament_part"

def p_compound_stament (p):
    '''compound_stament : BEGIN staments SEMICOLON END'''
    print "compound_stament"

def p_staments (p):
    '''staments : stament'''
    print "staments"

def p_staments2 (p):
    '''staments : staments SEMICOLON stament'''
    print "staments2"

def p_stament (p):
    '''stament : simple_stament'''
    print "stament"

def p_stament2 (p):
    '''stament : structured_stament'''
    print "stament"

def p_simple_stament (p):
    '''simple_stament : assigment_stament'''
    print "simple_stament"

def p_simple_stament2 (p):
    '''simple_stament : procedure_stament'''
    print "simple_stament2"

def p_simple_stament3 (p):
    '''simple_stament : aplication'''
    print "simple_stament3"

def p_simple_stament4 (p):
    '''simple_stament : read_stament'''
    print "simple_stament4"

def p_simple_stament5 (p):
    '''simple_stament : write_stament'''
    print "simple_stament5"

def p_simple_stament6 (p):
    '''simple_stament : writeln_stament'''
    print "simple_stament6"

def p_assigment_stament (p):
    '''assigment_stament : ID LBRACKET expression RBRACKET ASSIGMENT expression'''
    print "assigment_stament"

def p_assigment_stament2 (p):
    '''assigment_stament : ID ASSIGMENT expression'''
    print "assigment_stament2"

def p_procedure_stament (p):
    '''procedure_stament : procedure_id'''
    print "procedure_stament"

def p_aplication (p):
    '''aplication : ID LPARENT output_value RPARENT'''
    print "aplication"

def p_read_stament (p):
    '''read_stament : READ LPARENT id_list RPARENT'''
    print "read_stament"

def p_read_stament2 (p):
    '''read_stament : READLN LPARENT id_list RPARENT'''
    print "read_stament2"

def p_write_stament (p):
    '''write_stament : WRITE LPARENT output_value RPARENT'''
    print "write_stament"

def p_writeln_stament (p):
    '''writeln_stament : WRITELN'''
    print "writeln_stament"

def p_writeln_stament2 (p):
    '''writeln_stament : WRITELN LPARENT output_value RPARENT'''
    print "writeln_stament2"

def p_procedure_id (p):
    '''procedure_id : ID'''
    print "procedure_id"

def p_output_value (p):
    '''output_value : expression'''
    print "output_value"

def p_output_value2 (p):
    '''output_value : output_value COMMA expression'''
    print "output_value2"

def p_output_value3 (p):
    '''output_value : empty'''
    print "nulo"

def p_structured_stament (p):
    '''structured_stament : compound_stament'''
    print "structured_stament"

def p_structured_stament2 (p):
    '''structured_stament : if_stament'''
    print "structured_stament2"

def p_structured_stament3 (p):
    '''structured_stament : while_stament'''
    print "structured_stament3"

def p_structured_stament4 (p):
    '''structured_stament : for_stament'''
    print "structured_stament4"

def p_if_stament (p):
    '''if_stament : IF expression THEN stament'''
    print "if_stament"

def p_if_stament2 (p):
    '''if_stament : IF expression THEN stament ELSE stament'''
    print "if_stament2"

def p_while_stament (p):
    '''while_stament : WHILE expression DO stament'''
    print "while_stament"

def p_for_stament (p):
    '''for_stament : FOR ID ASSIGMENT expression TO expression DO stament'''
    print "for_stament"

def p_for_stament2 (p):
    '''for_stament : FOR ID ASSIGMENT expression DOWNTO expression DO stament'''
    print "for_stament2"

def p_expression (p):
    '''expression : simple_expression'''
    print "expression"

def p_expression2 (p):
    '''expression : simple_expression relational_operator simple_expression'''
    print "expression2"

def p_simple_expression (p):
    '''simple_expression : term adding_operator'''
    print "simple_expression"

def p_adding_operator (p):
    '''adding_operator : operator term'''
    print "adding_operator"

def p_adding_operator2 (p):
    '''adding_operator : adding_operator operator term'''
    print "adding_operator2"

def p_adding_operator3 (p):
    '''adding_operator : empty'''
    print "nulo"

def p_term (p):
    '''term : factor multiplying_operator'''
    print "term"

def p_multiplying_operator (p):
    '''multiplying_operator : multiplying factor'''
    print "multiplying_operator"

def p_multiplying_operator2 (p):
    '''multiplying_operator : multiplying_operator multiplying factor  '''
    print "multiplying_operator2"

def p_multiplying_operator3 (p):
    '''multiplying_operator : empty'''
    print "multiplying_operator3"

def p_factor (p):
    '''factor : aplication'''
    print "factor"

def p_factor2 (p):
    '''factor : variable'''
    print "factor2"

def p_factor3 (p):
    '''factor : constant'''
    print "factor3"

def p_factor4 (p):
    '''factor : LPARENT expression RPARENT'''
    print "factor4"

def p_factor5 (p):
    '''factor : NOT factor'''
    print "factor5"

def p_relational_operator (p):
    '''relational_operator : EQUAL'''
    print "relational_operator"

def p_relational_operator2 (p):
    '''relational_operator : GREATER'''
    print "relational_operator2"

def p_relational_operator3 (p):
    '''relational_operator : GREATEREQUEAL'''
    print "relational_operator3"

def p_relational_operator4 (p):
    '''relational_operator : LESS'''
    print "relational_operator4"

def p_relational_operator5 (p):
    '''relational_operator : LESSEQUAL'''
    print "relational_operator"

def p_relational_operator6 (p):
    '''relational_operator : LESSGREATER'''
    print "relational_operator6"

def p_operator (p):
    '''operator : PLUS'''
    print "operator"

def p_operator2 (p):
    '''operator : MINUS'''
    print "operator2"

def p_operator3 (p):
    '''operator : OR'''
    print "operator3"

def p_multiplying (p):
    '''multiplying : ASTERIK'''
    print "multiplying"

def p_multiplying2 (p):
    '''multiplying : SLASH'''
    print "multiplying"

def p_multiplying3 (p):
    '''multiplying : AND'''
    print "multiplying3"

def p_variable (p):
    '''variable : ID'''
    print "variable"

def p_variable2 (p):
    '''variable : ID LPARENT expression RPARENT'''
    print "variable2"

def p_constant (p):
    '''constant : INTNUMBER'''
    print "constant"

def p_constant2 (p):
    '''constant : FLOATNUMBER'''
    print "constant2"

def p_constant3 (p):
    '''constant : ID'''
    print "constant3"

def p_constant4 (p):
    '''constant : CHAR'''
    print "constant4"

def p_constant5 (p):
    '''constant : STRING'''
    print "constant5"

def p_empty (p):
    '''empty :'''
    pass

def p_error (p):
    print "error de sintaxis",p
    print "error en la linea "+str(p.lineno)


#BBusca y muestra los archivos de una ubicacion
def buscarFichero(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print str(cont)+". "+file
        cont += 1

    while respuesta == False:
        numArchivo = raw_input("\nNumero del test: ")
        for file in files:
            if file == files[int(numArchivo)-1]:
                respuesta = True
                break

    return files[int(numArchivo)-1]

#ruta donde se ecuentra los archvos de prueba
directorio = "/home/juan/Escritorio/Compiladores/proyecto_pascal/Analizador_sintactico/pruebas/"
archivo = buscarFichero(directorio) #guarda el archivo que selecciono en la funcion
test = directorio + archivo     #concatena la ruta de prueba con la ubicacion del archivo
fp = codecs.open(test,"r", "utf-8") #abre el archivo
cadena = fp.read()  #lee el archivo y lo guarda en una cadena
fp.close()          #cierra el archivo

parser = yacc.yacc()
result = parser.parse(cadena)

print result
