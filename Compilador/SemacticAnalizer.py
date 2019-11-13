
txt = ""
cont = 0
list= []
conta=-1
variables = []

var = False
def codeGenetor(x,y):
    global list
    global conta
    global var

    if (x=="statement" or x=="variableDec"):
        var = False
        if (x=="variableDec"):
            var = True
        list.append([])
        conta+=1
        list[conta].append(y)
        return
    else:
        if (x=="FOREND"):
            list.append(["FOREND"])
            conta+=1
        else:
            if (x== "ENNDO"):
                list.append(["ENNDO"])
                conta+=1
            else:
                if (x== "ENDIF"):
                    list.append(["ENDIF"])
                    conta+=1
                else:
                    if (var):
                        variables.append(x)
                    list[conta].append(x)


def sumContador():
    global cont
    cont +=1
    return "%d" % cont


class Node():
    pass


class Null(Node):
    def __init__(self):
        self.type = 'void'

    def imprimir(self,ident):
        print (ident+ "nodo nulo")

    def traducir(self):
        global txt
        id = sumContador()
        txt += id+"[label="+"nodo_nulo"+"]" +"\n\t"
        return id


class program(Node):
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
        print (ident + "Node: " +self.name)

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

        txt += id + "[label="+self.name+"]" + "\n\t"
        txt += id + "->"+son1
        txt += id + "->" + son2
        return "digraph G {\n\t"+txt+"}"


class blocklist(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if isinstance(self.son1, tuple):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        print (ident + "Node: " +self.name)

    def traducir(self):
        global txt
        id = sumContador()
        if isinstance(self.son1, tuple):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()



        txt += id + "[label="+self.name+"]" + "\n\t"
        txt += id + "->"+son1
        return id

class block(Node):
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

        print (ident + "Node: " + self.name)

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
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id


class variableDec(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        codeGenetor("variableDec",0)
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print (ident + "Node: " + self.name)


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

class statementlist(Node):
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

        print (ident + "Node: " + self.name)

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


class initiateVar(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print (ident + "Node: " + self.name)


    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class arrayStruct(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class variableType1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class variableType2(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class value1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class value2(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class statement1(Node):
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
            codeGenetor("statement", 1)
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if isinstance(self.son2, tuple):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)

        print (ident + "Node: " + self.name)


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


class statement2(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        codeGenetor("statement", 2)
        self.son1.imprimir(" " + ident)
        if isinstance(self.son2, tuple):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print (ident + "Node: " + self.name)


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


class statement3(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        codeGenetor("statement", 3)
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print (ident + "Node: " + self.name)


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


class statement4(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        codeGenetor("statement", 4)
        self.son1.imprimir(" " + ident)
        if isinstance(self.son2, tuple):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print (ident + "Node: " + self.name)


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


class statement5(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        codeGenetor("statement", 5)
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print (ident + "Node: " + self.name)


    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class statement6(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        codeGenetor("statement", 6)
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print (ident + "Node: " + self.name)


    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class statement7(Node):
    def __init__(self, son1, son2, son3, son4, son5, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5

    def imprimir(self, ident):
        codeGenetor("statement", 7)
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        if isinstance(self.son4, tuple):
            self.son4[0].imprimir(" " + ident)
        else:
            self.son4.imprimir(" " + ident)
        self.son5.imprimir(" "+ ident)

        print (ident + "Node: " + self.name)


    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()
        son5 = self.son5.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"


        return id


class statement8(Node):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):
        codeGenetor("statement", 8)
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son4.imprimir(" " + ident)

        print (ident + "Node: " + self.name)


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


class statement9(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        codeGenetor("statement", 9)
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print (ident + "Node: " + self.name)


    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class statement10(Node):

    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        codeGenetor("statement", 10)
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print (ident + "Node: " + self.name)


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

class statementList1(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print (ident + "Node: " + self.name)


    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id



class statementList2(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print (ident + "Node: " + self.name)


    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id



class randomInFor(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        codeGenetor(self.name, 0)
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print (ident + "Node: " + self.name)


    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class condition1(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

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


class relation1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class relation2(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class relation3(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class relation4(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class relation5(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class relation6(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class relation7(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class expression1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class expression2(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class expression3(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

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



class addingOperator1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class addingOperator2(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class term1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class term2(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

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



class multiplyingOperator1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class multiplyingOperator2(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class factor1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class factor2(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class factor3(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class numberType1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class numberType2(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class arrayType(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print (ident + "Node: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class ID(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print (ident + "ID: " + self.name)
        codeGenetor(self.name, 0)

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= " + self.name + "]" + "\n\t"

        return id


class ASSING(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print (ident + "Assign: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class EQUAL(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print (ident + "Equal: " + self.name)
        codeGenetor(self.name, 0)

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class NE(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print (ident + "NE: " + self.name)
        codeGenetor(self.name, 0)

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class LESS(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print (ident + "Less: " + self.name)
        codeGenetor(self.name, 0)

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class GREATER(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print (ident + "Greater: " + self.name)
        codeGenetor(self.name, 0)

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class EQLESS(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print (ident + "Lessequal: " + self.name)
        codeGenetor(self.name, 0)

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class EQGREATER(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print (ident + "Greaterequal: " + self.name)
        codeGenetor(self.name, 0)

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class PLUS(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print (ident + "Plus: " + self.name)
        codeGenetor(self.name, 0)

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class MINUS(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print (ident + "Minus: " + self.name)
        codeGenetor(self.name, 0)

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class MULT(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print (ident + "Times: " + self.name)
        codeGenetor(self.name, 0)

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class DIVIDE(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print (ident + "Divide: " + self.name)
        codeGenetor(self.name, 0)

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class NUMBER(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print (ident + "Number: " + str(self.name))
        codeGenetor(self.name, 0)

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id


class ARRAY(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print (ident + "Array: " + str(self.name))
        codeGenetor(self.name, 0)

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id

class INT(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print (ident + "Int: " + str(self.name))
        codeGenetor(self.name, 0)

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id


class TEXTO(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print (ident + "Texto: " + str(self.name))
        codeGenetor(self.name, 0)

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id


class STRING(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print (ident + "String: " + str(self.name))
        codeGenetor(self.name, 0)

    def traducir(self):
        global txt
        id = sumContador()
        txt += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id

class ENDDO(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        codeGenetor("ENDDO", 0)
        print (ident + "Enddo: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class ENDIF(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        codeGenetor("ENDIF", 0)
        print (ident + "Endif: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class FOREND(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        codeGenetor("FOREND", 0)
        print (ident + "Forend: " + self.name)

    def traducir(self):
        global txt
        id = sumContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

#class error(Node):
#    def _init_(self, name):
#        self.name = name
#
#    def imprimir(self, ident):
#        self.son1.imprimir(" "+ident)
#        print (ident + "Node: "+self.name

#    def traducir(self):
#        global txt
#        id = sumContador()
#        return id

