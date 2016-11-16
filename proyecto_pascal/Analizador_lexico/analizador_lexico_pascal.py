import ply.lex as lex
import re
import sys
import codecs
import os

#Palabras reservadas del sistema
reservadas = ['ELSE','IF','INT','FLOAT','RETURN','WHILE','FUN','BEGIN','DO','THEN',
            'END','PRINT','READ','WRITE','SKIP','BREAK','AND','OR','NOT',]
                        #simbolos
tokens = reservadas + ['PLUS','MINUS','ASTERIK','SLASH','EQUAL','LESS',
                    'GREATER','LBRACKET','RBRACKET','PERIOD','COMMA','COLON','SEMICOLON',
                    'POINTER','LPARENT','RPARENT','LESSGREATER','LESSEQUAL','GREATEREQUEAL',
                    'ASSIGMENT',
                    #otros
                    'ID','INTNUMBER','FLOATNUMBER','TEXT']

#Tabla de simbolos
t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_ASTERIK = r'\*'
t_SLASH = r'/'
t_EQUAL = r'='
t_LESS = r'<'
t_LESSEQUAL = r'<='
t_GREATER = r'>'
t_GREATEREQUEAL = r'>='
t_LESSGREATER = r'<>'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_PERIOD = r'\.'
t_COMMA = r','
t_COLON = r':'
t_SEMICOLON = r';'
t_POINTER = r'\^'
t_ASSIGMENT = r':='


def t_ID (t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_malformed_id(t):
    r'(\d+)[A-Za-z]'
    print "Linea "+str(t.lineno) + " ID no valido "+t.value

def t_COMENT1 (t):
    r'\(\*(.|\n)*\*\)'
    pass  #reconoce el comentario pero no va hacer nada


def t_COMENT2 (t):
    r'\{(.|\n)*\}'
    pass  #reconoce el comentario pero no va hacer nada


def t_FLOATNUMBER (t):
    r'\d+(\.\d+(e(\+|-)?\d+)?|e[\+|-]?\d+)'
    t.value = float(t.value)
    return t

def t_INTNUMBER (t):
    r'0(?!\d)|([1-9]\d*)'
    t.value = int(t.value)
    return t

def t_TEXT (t):
    r'"[^\n]*?(?<!\\)"'
    temp_str = t.value.replace(r'\\', '')
    m = re.search(r'\\[^n"]', temp_str)
    if m != None:
        print "Linea %d. Caracter de escape no soportado %s en string." % (t.lineno, m.group(0))
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error (t):
    print "caracter ilegal '%s'" % t.value[0]
    t.lexer.skip(1)

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
analizador = lex.lex()
analizador.input(cadena)   #se ingresa como entrada la cadena para ser analizado


while True:
    tok = analizador.token()
    if not tok :
        break
    print tok
