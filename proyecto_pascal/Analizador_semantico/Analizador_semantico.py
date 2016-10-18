txt = " "
cont = 0

def incrementar_contador():
    global cont
    cont += 1
    return "%d" %cont

class Node ():
    pass

class Null (Node):
    def __init__(self):
        self.type = 'void'

    def imprimir (self, ident):
        print ident + "nodo nulo"

    def Traducir(self):
        global txt
        id = incrementar_contador
        txt += id + "[label= "+"nodo_nulo"+"]"+"\n\t"

        return id

class program (Node):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)

        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"

        return "digraph G {\n\t"+txt+"}"

class program2 (Node):
    def __init__(self,son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()

        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"

        return id

class function (Node):
    def __init__(self,son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)
        print ident + "Node: " + self.name


    def Traducir (self):
        global txt
        id = incrementar_contador()

        son1 = self.son1.Traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].Traducir()
        else:
            son2 = self.son2.Traducir()

        son3 = self.son3.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        txt += id + "->"+son3+"\n\t"
        return id

class arguments (Node):
    def __init__(self,son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    def imprimir(self, ident):
        print ident + "Nodo: "+self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        return id

class arguments2 (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id

class declaration_variables (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id

class declaration_variables2 (Node):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        return id

class param (Node):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        return id

class param2 (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id

class locals0 (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id

class dec_list (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id


class dec_list2 (Node):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        return id

class var_dec (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id

class var_dec2 (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id

class type0 (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1
    def imprimir(self, ident):
        print ident + "Nodo: "+self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        return id

class type2 (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1
    def imprimir(self, ident):
        print ident + "Nodo: "+self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        return id

class type3 (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id


class type4 (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id


class staments (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id


class staments2 (Node):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        return id


class stament (Node):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        return id


class stament2 (Node):
    def __init__(self,son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)

        print ident + "Node: " + self.name


    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        if type(self.son2) == type(tuple()):
            self.son2[0].Traducir()
        else:
            self.son2.Traducir
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        txt += id + "->"+son3+"\n\t"
        return id

class stament3 (Node):
    def __init__(self,son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)
        print ident + "Node: " + self.name


    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        son3 = self.son3.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        txt += id + "->"+son3+"\n\t"
        return id

class stament4 (Node):
    def __init__(self,son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    def imprimir(self, ident):
        print ident + "Nodo: "+self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        return id

class stament5 (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id

class stament6 (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id

class stament7 (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id

class stament8 (Node):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        return id


class stament9 (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        print ident + "Nodo: "+self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        return id

class stament10 (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        print ident + "Nodo: "+self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        return id

class stament11 (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id


class else0 (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id

class location_read (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id


class location_read2 (Node):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        return id


class expression (Node):
    def __init__(self,son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)
        print ident + "Node: " + self.name


    def Traducir (self):
        global txt
        id = incrementar_contador()

        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        son3 = self.son3.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        txt += id + "->"+son3+"\n\t"
        return id

class expression2 (Node):
    def __init__(self,son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)
        print ident + "Node: " + self.name


    def Traducir (self):
        global txt
        id = incrementar_contador()

        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        son3 = self.son3.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        txt += id + "->"+son3+"\n\t"
        return id

class expression3 (Node):
    def __init__(self,son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)
        print ident + "Node: " + self.name


    def Traducir (self):
        global txt
        id = incrementar_contador()

        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        son3 = self.son3.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        txt += id + "->"+son3+"\n\t"
        return id

class expression4 (Node):
    def __init__(self,son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()

        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        son3 = self.son3.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        txt += id + "->"+son3+"\n\t"
        return id

class expression5 (Node):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        return id

class expression6 (Node):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        return id

class expression7 (Node):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)

        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        if type(self.son2) == type(tuple()):
            self.son2[0].Traducir()
        else:
            self.son2.Traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        return id

class expression8 (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id

class expression9 (Node):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        return id


class expression10 (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id


class expression11 (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id


class expression12 (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id


class expression13 (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id


class expression_list (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id


class expression_list2 (Node):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        return id


class relation (Node):
    def __init__(self,son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)
        print ident + "Node: " + self.name


    def Traducir (self):
        global txt
        id = incrementar_contador()

        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        son3 = self.son3.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        txt += id + "->"+son3+"\n\t"
        return id

class relation2 (Node):
    def __init__(self,son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)
        print ident + "Node: " + self.name


    def Traducir (self):
        global txt
        id = incrementar_contador()

        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        son3 = self.son3.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        txt += id + "->"+son3+"\n\t"
        return id

class relation3 (Node):
    def __init__(self,son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)
        print ident + "Node: " + self.name


    def Traducir (self):
        global txt
        id = incrementar_contador()

        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        son3 = self.son3.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        txt += id + "->"+son3+"\n\t"
        return id

class relation4 (Node):
    def __init__(self,son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)
        print ident + "Node: " + self.name


    def Traducir (self):
        global txt
        id = incrementar_contador()

        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        son3 = self.son3.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        txt += id + "->"+son3+"\n\t"
        return id

class relation5 (Node):
    def __init__(self,son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)
        print ident + "Node: " + self.name


    def Traducir (self):
        global txt
        id = incrementar_contador()

        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        son3 = self.son3.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        txt += id + "->"+son3+"\n\t"
        return id

class relation6 (Node):
    def __init__(self,son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)
        print ident + "Node: " + self.name


    def Traducir (self):
        global txt
        id = incrementar_contador()

        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        son3 = self.son3.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        txt += id + "->"+son3+"\n\t"
        return id

class relation7 (Node):
    def __init__(self,son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)
        print ident + "Node: " + self.name


    def Traducir (self):
        global txt
        id = incrementar_contador()

        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        son3 = self.son3.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        txt += id + "->"+son3+"\n\t"
        return id

class relation8 (Node):
    def __init__(self,son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)
        print ident + "Node: " + self.name


    def Traducir (self):
        global txt
        id = incrementar_contador()

        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        son3 = self.son3.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        txt += id + "->"+son3+"\n\t"
        return id

class relation9 (Node):
    def __init__(self,son1,son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        son2 = self.son2.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        txt += id + "->"+son2+"\n\t"
        return id

class relation10 (Node):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Node: " + self.name

    def Traducir (self):
        global txt
        id = incrementar_contador()
        son1 = self.son1.Traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id

class Id(Node):
	def __init__(self, name):
		self.name = name

	def imprimir(self, ident):
		print ident + "ID: "+ self.name

	def Traducir(self):
		global txt
		id = incrementar_contador()
		txt += id+"[label= "+self.name+"]"+"\n\t"
		return id

class IntNumber(Node):
	def __init__(self, name):
		self.name = name

	def imprimir(self, ident):
		print ident + "NUM: "+ str(int(self.name))

	def Traducir(self):
		global txt
		id = incrementar_contador()
		txt += id+"[label= "+str(int(self.name))+"]\n\t"
		return id


class FloatNumber(Node):
	def __init__(self, name):
		self.name = name

	def imprimir(self, ident):
		print ident + "FloatNumber: "+ str(self.name)

	def Traducir(self):
		global txt
		id = incrementar_contador()
		txt += id+"[label= "+str(self.name)+"]\n\t"
		return id

class Greater(Node):
	def __init__(self, name):
		self.name = name

	def imprimir(self, ident):
		print ident + "Greater: "+ self.name
	def Traducir(self):
		global txt
		id = incrementar_contador()
		txt += id+"[label= "+self.name+"]\n\t"
		return id

class Less(Node):
	def __init__(self, name):
		self.name = name

	def imprimir(self, ident):
		print ident + "Less: "+ self.name
	def Traducir(self):
		global txt
		id = incrementar_contador()
		txt += id+"[label= "+self.name+"]\n\t"
		return id

class GreaterEqueal(Node):
	def __init__(self, name):
		self.name = name

	def imprimir(self, ident):
		print ident + "GreaterEqueal: "+ self.name
	def Traducir(self):
		global txt
		id = incrementar_contador()
		txt += id+"[label= "+self.name+"]\n\t"
		return id

class LessEqueal(Node):
	def __init__(self, name):
		self.name = name

	def imprimir(self, ident):
		print ident + "LessEqueal: "+ self.name
	def Traducir(self):
		global txt
		id = incrementar_contador()
		txt += id+"[label= "+self.name+"]\n\t"
		return id

class Slash(Node):
	def __init__(self, name):
		self.name = name

	def imprimir(self, ident):
		print ident + "Slash: "+ self.name
	def Traducir(self):
		global txt
		id = incrementar_contador()
		txt += id+"[label= "+self.name+"]\n\t"
		return id

class Asterik(Node):
	def __init__(self, name):
		self.name = name

	def imprimir(self, ident):
		print ident + "Asterik: "+ self.name
	def Traducir(self):
		global txt
		id = incrementar_contador()
		txt += id+"[label= "+self.name+"]\n\t"
		return id

class Plus(Node):
	def __init__(self, name):
		self.name = name

	def imprimir(self, ident):
		print ident + "Plus: "+ self.name
	def Traducir(self):
		global txt
		id = incrementar_contador()
		txt += id+"[label= "+self.name+"]\n\t"
		return id

class Minus(Node):
	def __init__(self, name):
		self.name = name

	def imprimir(self, ident):
		print ident + "Minus: "+ self.name
	def Traducir(self):
		global txt
		id = incrementar_contador()
		txt += id+"[label= "+self.name+"]\n\t"
		return id

class Assigment(Node):
	def __init__(self, name):
		self.name = name

	def imprimir(self, ident):
		print ident + "Assigment: "+ self.name
	def Traducir(self):
		global txt
		id = incrementar_contador()
		txt += id+"[label= "+self.name+"]\n\t"
		return id

class empty (Node):
    def __init__(self,name):
        pass
