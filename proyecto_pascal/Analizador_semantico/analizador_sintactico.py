import ply.yacc as yacc
import os
import codecs
import re
from analizador_lexico_pascal import tokens
from Analizador_semantico import *
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
    p[0] = program(p[1],"program")
    #print "program"

def p_program2 (p):
    '''program : program function'''
    p[0] = program2(p[1], p[2], "program2")
    #print "program2"

def p_function (p):
    '''function : FUN ID arguments locals BEGIN staments END'''
    p[0] = function( p[3], p[4], p[6], "function")
    #print "function"

def p_arguments (p):
    '''arguments : LPARENT RPARENT'''
    p[0] = arguments(p[1], p[2], "arguments")
    #print "arguments"

def p_arguments2 (p):
    '''arguments : LPARENT declaration_variables RPARENT'''
    p[0] =arguments2( p[2], "arguments2")
    #print "arguments2"

def p_declaration_variables (p):
    '''declaration_variables : param'''
    p[0] =declaration_variables(p[1], "declaration_variables")
    #print "declaration_variables"

def p_declaration_variables2 (p):
    'declaration_variables : declaration_variables COMMA param'
    p[0] =declaration_variables2(p[1], p[3], "declaration_variables2")
    #print "declaration_variables2"

def p_param (p):
    '''param : ID COLON type'''
    p[0] = param(Id(p[1]) , p[3], "param")
    #print "param"

def p_param2 (p):
    '''param : ID COLON'''
    p[0] =param2(Id(p[1]),"param2")
    #print "param2"

def p_locals0 (p):
    '''locals : dec_list SEMICOLON'''
    p[0] = locals0(p[1], "locals0")
    #print "locals0"

def p_localsEmpty (p):
    '''locals : empty'''
    p[0] = Null()
    #print "nulo"

def p_dec_list (p):
    '''dec_list : var_dec'''
    p[0] = dec_list(p[1], "dec_list")
    #print "dec_list"

def p_dec_list2 (p):
    '''dec_list : dec_list SEMICOLON var_dec'''
    p[0] = dec_list2(p[1], p[3], "dec_list2")
    #print "dec_list2"

def p_var_dec (p):
    '''var_dec : param'''
    p[0] = var_dec(p[1], "var_dec")
    #print "var_dec"

def p_var_dec2 (p):
    '''var_dec : function'''
    p[0] =var_dec2(p[1], "var_dec2")
    #print "var_dec2"

def p_type0 (p):
    '''type : INT'''
    p[0] = type0(p[1], "type0")
    #print "type"

def p_type2 (p):
    '''type : FLOAT'''
    p[0] =type2(p[1], "type2")
    #print "type2"

def p_type3 (p):
    '''type : INT LBRACKET expression RBRACKET'''
    p[0] =type3(p[3], "type3")
    #print "type3"

def p_type4 (p):
    '''type : FLOAT LBRACKET expression RBRACKET'''
    p[0] =type4(p[3], "type4")
    #print "type4"

def p_staments (p):
    '''staments : stament'''
    p[0] =staments(p[1], "staments")
    #print "staments"

def p_staments2 (p):
    '''staments : staments SEMICOLON stament'''
    p[0] =staments2(p[1], p[3], "staments2")
    #print "staments2"

def p_stament (p):
    '''stament : WHILE relation DO stament'''
    p[0] =stament(p[2], p[4], "stament")
    #print "stament"

def p_stament2 (p):
    '''stament : IF relation THEN stament else'''
    p[0] =stament2(p[2], p[4], p[5], "stament2")
    #print "stament2"

def p_stament3 (p):
    '''stament : ID ASSIGMENT expression'''
    p[0] =stament3(Id(p[1]),Assigment(p[2]),p[3], "stament3")
    #print "stament3"

def p_stament4 (p):
    '''stament : PRINT LPARENT TEXT RPARENT'''
    p[0] =stament4(p[1], p[2],"stament4")
    #print "stament4"

def p_stament5 (p):
    '''stament : WRITE LPARENT expression RPARENT'''
    p[0] =stament5(p[3], "stament5")
    #print "stament5"

def p_stament6 (p):
    '''stament : READ LPARENT location_read RPARENT'''
    p[0] =stament6(p[3], "stament6")
    #print "stament6"

def p_stament7 (p):
    '''stament : RETURN expression'''
    p[0] =stament7(p[2], "stament7")
    #print "stament7"

def p_stament8 (p):
    '''stament : ID LPARENT expression RPARENT'''
    p[0] =stament8(Id(p[1]), p[3], "stament8")
    #print "stament8"

def p_stament9 (p):
    '''stament : SKIP SEMICOLON'''
    p[0] =stament9(p[1],"stament9")
    #print "stament9"

def p_stament10 (p):
    '''stament : BREAK SEMICOLON'''
    p[0] =stament10( p[1],"stament10")
    #print "stament10"

def p_stament11 (p):
    '''stament : BEGIN staments END'''
    p[0] =stament11(p[2], "stament11")
    #print "stament11"

def p_else0 (p):
    '''else : ELSE stament'''
    p[0] =else0(p[2], "else0")
    #print "else0"

def p_elseEmpty (p):
    '''else : empty'''
    p[0] =Null()
    #print "nulo"

def p_location_read (p):
    '''location_read : ID'''
    p[0] =location_read(Id(p[1]),"location_read")
    #print "location_read"

def p_location_read2 (p):
    '''location_read : ID LBRACKET expression RBRACKET'''
    p[0] =location_read2(Id(p[1]), p[3], "location_read2")
    #print "location_read2"

def p_expression (p):
    '''expression : expression PLUS expression'''
    p[0] =expression(p[1], Plus(p[2]),p[3], "expression")
    #print "expression"

def p_expression2 (p):
    '''expression : expression SLASH expression'''
    p[0] =expression2(p[1],Slash(p[2]), p[3], "expression2")
    #print "expression2"

def p_expression3 (p):
    '''expression : expression ASTERIK expression'''
    p[0] =expression3(p[1],Asterik(p[2]), p[3], "expression3")
    #print "expression3"

def p_expression4 (p):
    '''expression : expression MINUS expression'''
    p[0] =expression4(p[1],Minus(p[2]), p[3], "expression4")
    #print "expression4"

def p_expression5 (p):
    '''expression : MINUS expression'''
    p[0] =expression5(Minus(p[1]),p[2], "expression5")
    #print "expression5"

def p_expression6 (p):
    '''expression : LPARENT expression RPARENT'''
    p[0] =expression6(p[2], "expression6")
    #print "expression6"

def p_expression7 (p):
    '''expression : ID LPARENT expression_list RPARENT'''
    p[0] =expression7(Id(p[1]), p[3], "expression7")
    #print "expression7"

def p_expression8 (p):
    '''expression : ID'''
    p[0] =expression8(Id(p[1]),"expression8")
    #print "expression8"

def p_expression9 (p):
    '''expression : ID LBRACKET expression RBRACKET'''
    p[0] =expression9(Id(p[1]), p[3], "expression9")
    #print "expression9"

def p_expression10 (p):
    '''expression : INTNUMBER'''
    p[0] =expression10(IntNumber(p[1]),"expression10")
    #print "expression10"

def p_expression11 (p):
    '''expression : FLOATNUMBER'''
    p[0] =expression11(FloatNumber(p[1]),"expression11")
    #print "expression11"

def p_expression12 (p):
    '''expression : INT LPARENT expression RPARENT'''
    p[0] =expression12(p[3], "expression12")
    #print "expression12"

def p_expression13 (p):
    '''expression : FLOAT LPARENT expression RPARENT'''
    p[0] =expression13(p[3], "expression13")
    #print "expression13"

def p_expression_list (p):
    '''expression_list : expression'''
    p[0] =expression_list(p[1], "expression_list")
    #print "expression_list"

def p_expression_list2 (p):
    '''expression_list : expression COMMA expression'''
    p[0] =expression_list2(p[1], p[3], "expression_list2")
    #print "expression_list2"

def p_expression_listEmpty (p):
    '''expression_list : empty'''
    p[0] =Null()
    #print "nulo"

def p_relation (p):
    '''relation : expression GREATER expression'''
    p[0] =relation(p[1],Greater(p[2]), p[3], "relation")
    #print "relation"

def p_relation2 (p):
    '''relation : expression LESS expression'''
    p[0] =relation2(p[1],Less(p[2]), p[3], "relation2")
    #print "relation2"

def p_relation3 (p):
    '''relation : expression GREATEREQUEAL expression'''
    p[0] =relation3(p[1],GreaterEqueal(p[2]), p[3], "relation3")
    #print "relation3"

def p_relation4 (p):
    '''relation : expression LESSEQUAL expression'''
    p[0] =relation4(p[1],LessEqual(p[2]), p[3], "relation4")
    #print "relation4"

def p_relation5 (p):
    '''relation : expression DISTINT expression'''
    p[0] =relation5(p[1],Distint(p[2]), p[3], "relation5")
    #print "relation5"

def p_relation6 (p):
    '''relation : expression NOT expression'''
    p[0] =relation6(p[1],Not(p[2]), p[3], "relation6")
    #print "relation6"

def p_relation7 (p):
    '''relation : expression OR expression'''
    p[0] =relation7(p[1],Or(p[2]), p[3], "relation7")
    #print "relation7"

def p_relation8 (p):
    '''relation : expression AND expression'''
    p[0] =relation8(p[1],And(p[2]), p[3], "relation8")
    #print "relation8"

def p_relation9 (p):
    '''relation : NOT expression'''
    p[0] =relation9(Not(p[1]),p[2], "relation9")
    #print "relation9"

def p_relation10 (p):
    '''relation : LPARENT expression RPARENT'''
    p[0] =relation10( p[2],  "relation10")
    #print "relation10"

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
directorio = "/home/juan/Escritorio/Compiladores/proyecto_pascal/Analizador_semantico/pruebas/"
archivo = buscarFichero(directorio) #guarda el archivo que selecciono en la funcion
test = directorio + archivo     #concatena la ruta de prueba con la ubicacion del archivo
fp = codecs.open(test,"r", "utf-8") #abre el archivo
cadena = fp.read()  #lee el archivo y lo guarda en una cadena
fp.close()          #cierra el archivo

yacc.yacc()
result = yacc.parse(cadena, debug = 1)

#result.imprimir(" ")
result.Traducir()

graphFile = open('graphviztrhee.vez','w')
graphFile.write(result.Traducir())
graphFile.close()
#print result
