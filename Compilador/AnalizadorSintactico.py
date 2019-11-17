import ply.yacc as yacc
import os
import codecs
from Compilador.Interpretador import *
import re
from Compilador.AnalizadorLexico import tokens
from sys import stdin
from Compilador.AnalizadorSemantico import *
listfor = []

varsintac = []
flag1 = False;
flag2 = False;
flag3 = False;

precedence = (
    ('right', 'ID', 'DEC', 'BALLOON', 'FOR', 'IF', 'DOW', 'RANDOM'),
    ('right', 'ASSIGN'),
    ('left', 'NE'),
    ('left', 'LESS', 'EQLESS', 'GREATER', 'EQGREATER'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIVIDE'),
    ('left', 'LPAREN', 'RPAREN', 'SLPAREN', 'SRPAREN'),
)


def p_program(p):
    '''program : BEGIN subB END SEMICOLON'''
    print("program")
    p[0] = program(p[2], "program")


def p_subB(p):
    '''subB : subB ID LC block RC'''
    print("subB")
    p[0] = subB(p[1], FUNC(p[2]), p[4], END(p[5]), "subB")


def p_subBEmpty(p):
    '''subB : empty'''
    p[0] = Null()
    print("nulo")


def p_block(p):
    """block : statementList variableDec statement"""
    p[0] = block(p[1], p[2], p[3], "block")
    print("block")


def p_blockEmpty(p):
    '''block : empty'''
    p[0] = Null()
    print("nulo")


def p_statementList(p):
    '''statementList : statementList1 statementList2'''
    p[0] = statementlist(p[1], p[2], "statementlist")
    print("statementlist")


def p_statementlistEmpty(p):
    '''statementList : empty'''
    p[0] = Null()
    print("nulo")


def p_variableDec(p):
    '''variableDec : variableType ID arrayStruct initiateVar SEMICOLON'''
    varsintac.append(p[2])
    p[0] = variableDec(p[1], ID(p[2]), p[3], p[4], "variableDec")
    print("variableDec")


def p_variableDecEmpty(p):
    '''variableDec : empty'''
    p[0] = Null()
    print("nulo")


def p_initiateVar(p):
    '''initiateVar : ASSIGN value'''
    p[0] = initiateVar(ASSING(p[1]), p[2], "initiateVar")
    print("initiateVar")


def p_initiateVarEmpty(p):
    '''initiateVar : empty'''
    p[0] = Null()
    print("nulo")


def p_arrayStruct(p):
    '''arrayStruct : LPAREN NUMBER RPAREN '''
    varsintac.append(p[2])
    varsintac.append("Index")
    p[0] = arrayStruct(NUMBER(p[2]), "arrayStruct")
    print("arrayStruct ")


def p_arrayStructEmpty(p):
    '''arrayStruct : empty'''
    p[0] = Null()
    print("nulo")

def p_xType1(p):
    '''xType : numberType '''
    p[0] = xType1(p[1], "xType")
    print("xType")

def p_xType2(p):
    '''xType :  arrayType2'''
    p[0] = xType2(p[1], "xType")
    print("xType")

def p_variableType1(p):
    '''variableType : INT'''
    p[0] = variableType1(INT(p[1]), "variableType1")
    print("variableType 1")


def p_variableType2(p):
    '''variableType : TEXTO LPAREN NUMBER RPAREN'''
    global flag1
    flag1 = True
    varsintac.append(p[3])
    varsintac.append("Size")
    p[0] = variableType2(TEXTO(p[1]), NUMBER(p[3]), "variableType2")
    print("variableType 2")


def p_variableTypeEmpty(p):
    '''variableType : empty'''
    p[0] = Null()
    print("nulo")


def p_value1(p):
    '''value : NUMBER'''

    global flag1, flag2
    if flag2:
        varsintac.append("ArrayPart")
        flag2 = False

    if not flag1:
        varsintac.append(p[1])
    else:
        flag1 = False
        varsintac.append(p[1])

    p[0] = value1(NUMBER(p[1]), "value1")
    print("value 1")


def p_value2(p):
    '''value :  STRING'''
    global flag1, flag2
    if flag2:
        varsintac.append("ArrayPart")
        flag2 = False

    if not flag1:
        varsintac.append(p[1])
    else:
        flag1 = False
        varsintac.append(p[1])
    p[0] = value2(STRING(p[1]), "value2")
    print("value 2")


def p_statement1(p):
    '''statement : BALLOON LPAREN numberType COLON numberType RPAREN SEMICOLON'''
    p[0] = statement1(p[3], p[5], "statement1")
    print("statement 1")


def p_statement2(p):
    '''statement : DOW LPAREN numberType RPAREN statementList ENDDO SEMICOLON'''
    p[0] = statement2(p[3], p[5], ENDDO(p[6]), "statement2")
    print("statement 2")


def p_statement3(p):
    '''statement : RANDOM LPAREN arrayT COLON numberType COLON numberType RPAREN SEMICOLON'''
    p[0] = statement3(p[3], p[5], p[7], "statement3")
    print("statement 3")


def p_statement4(p):
    '''statement : IF LPAREN condition RPAREN SEMICOLON  statement ENDIF SEMICOLON'''
    p[0] = statement4(p[3], p[6], ENDIF(p[7]), "statement4")
    print("statement 4")


def p_statement5(p):
    '''statement : INC LPAREN numberType COLON numberType RPAREN SEMICOLON'''
    p[0] = statement5(p[3], p[5], "statement5")
    print("statement5")


def p_statement6(p):
    '''statement : DEC LPAREN numberType COLON numberType RPAREN SEMICOLON'''
    p[0] = statement6(p[3], p[5], "statement6")
    print("statement6")


def p_statement7(p):
    '''statement : FOR numberType TIMES USING arrayT randomInFor block FOREND SEMICOLON'''
    p[0] = statement7(p[2], p[5], p[6], p[7], FOREND(p[8]), "statement7")
    print("statement7")


def p_statement8(p):
    '''statement : FORASIGNWORD LPAREN numberType COLON numberType RPAREN DO ASIGNWORD LPAREN arrayT COLON arrayT RPAREN SEMICOLON'''
    p[0] = statement8(p[3], p[5], p[10], p[12], "statement8")
    print("statement8")


def p_statement9(p):
    '''statement : TELAARANA LPAREN numberType COLON numberType RPAREN SEMICOLON'''
    p[0] = statement9(p[3], p[5], "statement9")
    print("statement9")


def p_statement10(p):
    '''statement : OBJECT LPAREN numberType COLON xType COLON numberType RPAREN SEMICOLON'''
    p[0] = statement10(p[3], p[5], p[7], "statement10")
    print("statement10")


def p_statement11(p):
    '''statement : FOR numberType TIMES USING ID statementList FEND SEMICOLON'''
    global listfor
    listfor.append(p[5])
    p[0] = statement11(p[2], ID(p[5]), p[6], FEND(p[7]), "statement11")


def p_statement12(p):
    '''statement : ARRAY ID LPAREN numberType RPAREN initiateVar SEMICOLON'''
    print("statement12")
    global flag2
    flag2 = True
    p[0] = statement12(ID(p[2]), p[4], p[6], "statement12")


def p_statementEmpty(p):
    '''statement : empty'''
    p[0] = Null()
    print("nulo")


def p_statementList1(p):
    '''statementList1 : block statement'''
    p[0] = statementList1(p[1], p[2], "statementList1")
    print("statementList 1")


def p_statementList2(p):
    '''statementList2 :  block variableDec '''
    p[0] = statementList2(p[1], p[2], "statementList2")
    print("statementList 2")


def p_randomInFor(p):
    '''randomInFor : RANDOM LPAREN numberType COLON numberType RPAREN SEMICOLON'''
    p[0] = randomInFor(p[3], p[5], "randomInFor")
    print("randomInFor")


def p_condition1(p):
    '''condition : expression relation expression'''
    p[0] = condition1(p[1], p[2], p[3], "condition1")
    print("condition 1")


def p_relation1(p):
    '''relation : ASSIGN'''
    p[0] = relation1(ASSING(p[1]), "relation1")
    print("relation 1")


def p_relation2(p):
    '''relation : NE'''
    p[0] = relation2(NE(p[1]), "relation2")
    print("relation 2")


def p_relation3(p):
    '''relation : LESS'''
    p[0] = relation3(LESS(p[1]), "relation3")
    print("relation 3")


def p_relation4(p):
    '''relation : GREATER'''
    p[0] = relation4(GREATER(p[1]), "relation4")
    print("relation 4")


def p_relation5(p):
    '''relation : EQLESS'''
    p[0] = relation5(EQLESS(p[1]), "relation5")
    print("relation 5")


def p_relation6(p):
    '''relation : EQGREATER'''
    p[0] = relation6(EQGREATER(p[1]), "relation6")
    print("relation 6")


def p_relation7(p):
    '''relation : EQUAL'''
    p[0] = relation7(EQUAL(p[1]), "relation7")
    print("relation 7")


def p_expression1(p):
    '''expression : term'''
    p[0] = expression1(p[1], "expression1")
    print("expresion 1")


def p_expression2(p):
    '''expression : addingOperator term'''
    p[0] = expression2(p[1], p[2], "expression2")
    print("expresion 2")


def p_expression3(p):
    '''expression : expression addingOperator term'''
    p[0] = expression3(p[1], p[2], p[3], "expression3")
    print("expresion 3")


def p_addingOperator1(p):
    '''addingOperator : PLUS'''
    p[0] = addingOperator1(PLUS(p[1]), "addingOperator1")
    print("addingOperator 1")


def p_addingOperator2(p):
    '''addingOperator : MINUS'''
    p[0] = addingOperator2(MINUS(p[1]), "addingOperator2")
    print("addingOperator 1")


def p_term1(p):
    '''term : factor'''
    p[0] = term1(p[1], "factor1")
    print("term 1")


def p_term2(p):
    '''term : term multiplyingOperator factor'''
    p[0] = term2(p[1], p[2], p[3], "factor2")
    print("term 2")


def p_multiplyingOperator1(p):
    '''multiplyingOperator : MULT'''
    p[0] = multiplyingOperator1(MULT(p[1]), "multiplyingOperator1")
    print("multiplyingOperator 1")


def p_multiplyingOperator2(p):
    '''multiplyingOperator : DIVIDE'''
    p[0] = multiplyingOperator2(DIVIDE(p[1]), "multiplyingOperator2")
    print("multiplyingOperator 2")


def p_factor1(p):
    '''factor : ID'''
    p[0] = factor1(p[1], "factor1")
    print("factor 1")


def p_factor2(p):
    '''factor : NUMBER'''
    p[0] = factor2(NUMBER(p[1]), "factor2")
    print("factor 2")


def p_factor3(p):
    '''factor : ID SLPAREN NUMBER SRPAREN'''
    p[0] = factor3(ID(p[1]), NUMBER(p[3]), "factor3")
    print("factor 3")


def p_numberType1(p):
    '''numberType : NUMBER'''
    p[0] = numberType1(NUMBER(p[1]), "numberType1")
    print("numberType1")


def p_numberType2(p):
    '''numberType : INT ID'''
    p[0] = numberType2(INT(p[1]), ID(p[2]), "numberType2")
    flag = False
    for i in varsintac:
        if isinstance(i,int):
            pass
        else:
            if i.encode('ascii', 'ignore') == p[2].encode('ascii', 'ignore'):
                flag = True

    if not (flag):
        raise ValueError("ERROR SINTACTICO VARIABLE" )

    print("numberType2")


def p_arrayType(p):
    '''arrayType : ARRAY ID LPAREN numberType RPAREN'''
    for i in range(len(varsintac)):
        if isinstance(varsintac[i], int):
            pass
        else:
            if varsintac[i].encode('ascii', 'ignore') == p[2].encode('ascii', 'ignore'):
                print("peguense un sobo")
                print(p[4])
                if varsintac[i-1] == p[4]:
                    print("No pierdo nada")



    p[0] = arrayType(ARRAY(p[1]), ID(p[2]), p[4], "arrayType")
    print("arrayType")

def p_arrayType2(p):
    '''arrayType2 : ARRAY ID LPAREN ID RPAREN'''
    p[0] = arrayType2(ARRAY(p[1]), ID(p[2]), ID(p[4]), "arrayType")
    print("arrayType")

def p_arrayT(p):
    '''arrayT : ARRAY ID'''
    p[0] = arrayT(ARRAY(p[1]), ID(p[2]), "arrayT")
    print("arrayT")


def p_empty(p):
    '''empty :'''
    pass


def p_error(p):
    print("Error de sintaxis ", p)


# print "Error en la linea "+str(p.lineno)

# cadena = ('RANDOM (hola,hola,hola)')
# parser = yacc.yacc()
# result = parser.parse(cadena)


def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print(str(cont) + ". " + file)
        cont = cont + 1

    while respuesta == False:
        numArchivo = 1 #input('\nNumero del test: ')
        for file in files:
            if file == files[int(numArchivo) - 1]:
                respuesta = True
                break

    print("Has escogido \"%s\" \n" % files[int(numArchivo) - 1])

    return files[int(numArchivo) - 1]


def traducir(result):
    graphFile = open('graphviztrhee.vz', 'w')
    graphFile.write(result.traducir())
    graphFile.close()
    print("El programa traducido se guardo en \"graphviztrhee.vz\"")



