from __builtin__ import sum

txt = ""
cont = 0


def sumContador():
    global cont
    cont +=1
    return "%d" % cont


class Nodo():
    pass


class Null(Nodo):
    def __init__(self):
        self.type = 'void'

    def imprimir(self,ident):
        print ident+ "nodo nulo"

    def traducir(self):
        global txt
        id = sumContador()
        txt += id+"[label="+"nodo_nulo"+"]" +"\n\t"
        return id


class program(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print ident + "Nodo: " +self.name

    def traducir(self):
        global txt
        id = sumContador()
        son1 = self.son1.traducir()

        txt += id + "[label="+self.name+"]" + "\n\t"
        txt += id + "->"+son1
        return "digraph G {\n\t"+txt+"}"


class block(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):

        if isinstance(self.son1,tuple):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if isinstance(self.son2, tuple):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)

        if isinstance(self.son3, tuple):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        if isinstance(self.son1, tuple):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if isinstance(self.son2, tuple):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if isinstance(self.son3, tuple):
            son3 = self.son2[0].traducir()
        else:
            son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class variableDec(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

        return id

class statementlist(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):

        if isinstance(self.son1, tuple):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if isinstance(self.son2, tuple):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        if isinstance(self.son1, tuple):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if isinstance(self.son2, tuple):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()


        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id
    

class initiateVar(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class arrayStruct(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id


class variableType1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class variableType2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class value1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class value2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class statement1(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        if isinstance(self.son1, tuple):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if isinstance(self.son2, tuple):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        if isinstance(self.son1, tuple):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if isinstance(self.son2, tuple):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class statement2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        if isinstance(self.son2, tuple):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class statement3(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id


class statement4(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        if isinstance(self.son2, tuple):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class statement5(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class statement6(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class statement7(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        if isinstance(self.son4, tuple):
            self.son4[0].imprimir(" " + ident)
        else:
            self.son4.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"


        return id


class statement8(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son4.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

        return id


class statement9(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class statement10(Nodo):

    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class statementList1(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class statementList2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class randomInFor(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class condition1(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id


class relation1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class relation2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class relation3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class relation4(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class relation5(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class relation6(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class relation7(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class expression1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class expression2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class expression3(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id



class addingOperator1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class addingOperator2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class term1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class term2(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id



class multiplyingOperator1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class multiplyingOperator2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class factor1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class factor2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class factor3(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class numberType1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class numberType2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class arrayType(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class ID(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print ident + "ID: " + self.name

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= " + self.name + "]" + "\n\t"

        return id


class ASSING(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print ident + "Assign: " + self.name

    def traducir(self):
        global txt
        id = sumContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class EQUAL(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print ident + "Equal: " + self.name

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class NE(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print ident + "NE: " + self.name

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class LESS(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print ident + "Less: " + self.name

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class GREATER(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print ident + "Greater: " + self.name

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class EQLESS(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print ident + "Lessequal: " + self.name

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class EQGREATER(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print ident + "Greaterequal: " + self.name

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class PLUS(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print ident + "Plus: " + self.name

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class MINUS(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print ident + "Minus: " + self.name

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class MULT(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print ident + "Times: " + self.name

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class DIVIDE(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print ident + "Divide: " + self.name

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class NUMBER(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print ident + "Number: " + str(self.name)

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id


class ARRAY(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print ident + "Array: " + str(self.name)

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id

class INT(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print ident + "Int: " + str(self.name)

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id


class TEXTO(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print ident + "Texto: " + str(self.name)

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id


class STRING(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print ident + "String: " + str(self.name)

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id
#class error(Nodo):
#    def _init_(self, name):
#        self.name = name
#
#    def imprimir(self, ident):
#        self.son1.imprimir(" "+ident)
#        print ident + "Nodo: "+self.name

#    def traducir(self):
#        global txt
#        id = sumContador()
#        return id

