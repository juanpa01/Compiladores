import ply.lex as lex
import re
import sys
import codecs
import os

#Palabras reservadas del sistema
reservadas = ['SI','MIENTRAS','PARA','ENTONCES','SINO','ASIGNAR','IMPRIMIR',
            'ENTERO','FLOTANTE','CADENA','CARACTER','DOBLE']

tokens = reservadas + ['ID','NUMERO','ADD','SUB','MULT','DIV','MOD','EQUAL',
        'NE','LT', 'LTE', 'GT', 'GTE','LPARENT','RPARENT','COMMA','SEMICOLON',
        'TEXTO']

#Tabla de simbolos
t_ignore = ' \t'
t_ADD = r'\+'
t_SUB = r'\-'
t_MULT = r'\*'
t_DIV = r'/'
t_MOD = r'%'
t_EQUAL = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMICOLON = r';'

def t_ID (t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_COMENTARIO (t):
    r'\//.*'
    pass  #reconoce el comentario pero no va hacer nada

def t_NUMERO (t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_TEXTO (t):
    r'"[a-zA-Z0-9 _+*-]*"'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_error (t):
    print "caracter ilegal '%s'" % t.value[0]
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

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

directorio = "/home/juan/Escritorio/Compiladores/pruebas/"
archivo = buscarFichero(directorio)
test = directorio + archivo
fp = codecs.open(test,"r", "utf-8")
cadena = fp.read()
fp.close()
analizador = lex.lex()
analizador.input(cadena)


while True:
    tok = analizador.token()
    if not tok :
        break
    print tok
