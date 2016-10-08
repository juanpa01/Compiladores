import ply.yacc as yacc
import re
import sys
import codecs
import os
from analizador_lexico_pascal import tokens
from sys import stdin

#se define la precedencia de los operadores

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
    '''program : function'''
    print "program"

def p_program2 (p):
    '''program : program function'''
    print "program2"

def p_function (p):
    '''function : FUN ID arguments locals BEGIN staments END'''
    print "function"

def p_arguments (p):
    '''arguments : LPARENT RPARENT'''
    print "arguments"

def p_arguments2 (p):
    '''arguments : LPARENT declaration_variables RPARENT'''
    print "arguments2"

def p_declaration_variables (p):
    '''declaration_variables : param'''
    print "declaration_variables"

def p_declaration_variables2 (p):
    'declaration_variables : declaration_variables COMMA param'
    print "declaration_variables2"

def p_param (p):
    '''param : ID COLON type'''
    print "param"

def p_param2 (p):
    '''param : ID COLON'''
    print "param2"

def p_locals (p):
    '''locals : dec_list SEMICOLON'''
    print "locals"

def p_localsEmpty (p):
    '''locals : empty'''
    print "nulo"

def p_dec_list (p):
    '''dec_list : var_dec'''
    print "dec_list"

def p_dec_list2 (p):
    '''dec_list : dec_list SEMICOLON var_dec'''
    print "dec_list2"

def p_var_dec (p):
    '''var_dec : param'''
    print "var_dec"

def p_var_dec2 (p):
    '''var_dec : function'''
    print "var_dec2"

def p_type (p):
    '''type : INT'''
    print "type"

def p_type2 (p):
    '''type : FLOAT'''
    print "type2"

def p_type3 (p):
    '''type : INT LBRACKET expression RBRACKET'''
    print "type3"

def p_type4 (p):
    '''type : FLOAT LBRACKET expression RBRACKET'''
    print "type4"

def p_staments (p):
    '''staments : stament'''
    print "staments"

def p_staments2 (p):
    '''staments : staments SEMICOLON stament'''
    print "staments2"

def p_stament (p):
    '''stament : WHILE relation DO stament'''
    print "stament"

def p_stament2 (p):
    '''stament : IF relation THEN stament else'''
    print "stament2"

def p_stament3 (p):
    '''stament : ID ASSIGMENT expression'''
    print "stament3"

def p_stament4 (p):
    '''stament : PRINT LPARENT TEXT RPARENT'''
    print "stament4"

def p_stament5 (p):
    '''stament : WRITE LPARENT expression RPARENT'''
    print "stament5"

def p_stament6 (p):
    '''stament : READ LPARENT location_read RPARENT'''
    print "stament6"

def p_stament7 (p):
    '''stament : RETURN expression'''
    print "stament7"

def p_stament8 (p):
    '''stament : ID LPARENT expression RPARENT'''
    print "stament8"

def p_stament9 (p):
    '''stament : SKIP SEMICOLON'''
    print "stament9"

def p_stament10 (p):
    '''stament : BREAK SEMICOLON'''
    print "stament10"

def p_stament11 (p):
    '''stament : BEGIN staments END'''
    print "stament11"

def p_else (p):
    '''else : ELSE stament'''
    print "else"

def p_elseEmpty (p):
    '''else : empty'''
    print "nulo"

def p_location_read (p):
    '''location_read : ID'''
    print "location_read"

def p_location_read2 (p):
    '''location_read : ID LBRACKET expression RBRACKET'''
    print "location_read2"

def p_expression (p):
    '''expression : expression PLUS expression'''
    print "expression"

def p_expression2 (p):
    '''expression : expression SLASH expression'''
    print "expression2"

def p_expression3 (p):
    '''expression : expression ASTERIK expression'''
    print "expression3"

def p_expression4 (p):
    '''expression : expression MINUS expression'''
    print "expression4"

def p_expression5 (p):
    '''expression : MINUS expression'''
    print "expression5"

def p_expression6 (p):
    '''expression : LPARENT expression RPARENT'''
    print "expression6"

def p_expression7 (p):
    '''expression : ID LPARENT expression_list RPARENT'''
    print "expression7"

def p_expression8 (p):
    '''expression : ID'''
    print "expression8"

def p_expression9 (p):
    '''expression : ID LBRACKET expression RBRACKET'''
    print "expression9"

def p_expression10 (p):
    '''expression : INTNUMBER'''
    print "expression10"

def p_expression11 (p):
    '''expression : FLOATNUMBER'''
    print "expression11"

def p_expression12 (p):
    '''expression : INT LPARENT expression RPARENT'''
    print "expression12"

def p_expression13 (p):
    '''expression : FLOAT LPARENT expression RPARENT'''
    print "expression13"

def p_expression_list (p):
    '''expression_list : expression'''
    print "expression_list"

def p_expression_list2 (p):
    '''expression_list : expression COMMA expression'''
    print "expression_list2"

def p_expression_listEmpty (p):
    '''expression_list : empty'''
    print "nulo"

def p_relation (p):
    '''relation : expression GREATER expression'''
    print "relation"

def p_relation2 (p):
    '''relation : expression LESS expression'''
    print "relation2"

def p_relation3 (p):
    '''relation : expression GREATEREQUEAL expression'''
    print "relation3"

def p_relation4 (p):
    '''relation : expression LESSEQUAL expression'''
    print "relation4"

def p_relation5 (p):
    '''relation : expression DISTINT expression'''
    print "relation5"

def p_relation6 (p):
    '''relation : expression NOT expression'''
    print "relation6"

def p_relation7 (p):
    '''relation : expression OR expression'''
    print "relation7"

def p_relation8 (p):
    '''relation : expression AND expression'''
    print "relation8"

def p_relation9 (p):
    '''relation : NOT expression'''
    print "relation9"

def p_relation10 (p):
    '''relation : LPARENT expression RPARENT'''
    print "relation10"

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
directorio = "/home/juan/Escritorio/Compiladores/proyecto_pascal/Analizador_lexico/pruebas/"
archivo = buscarFichero(directorio) #guarda el archivo que selecciono en la funcion
test = directorio + archivo     #concatena la ruta de prueba con la ubicacion del archivo
fp = codecs.open(test,"r", "utf-8") #abre el archivo
cadena = fp.read()  #lee el archivo y lo guarda en una cadena
fp.close()          #cierra el archivo

parser = yacc.yacc()
result = parser.parse(cadena)

print result
