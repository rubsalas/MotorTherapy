import ply.yacc as yacc
import os
import codecs
import re
from LexicalAnalizer import tokens
from sys import stdin
from SemacticAnalizer import *

precedence = (
    ('right','ID','DEC','BALLOON','FOR','IF','DOW','RANDOM'),
    ('right', 'ASSIGN'),
    ('left', 'NE'),
    ('left', 'LESS', 'EQLESS', 'GREATER', 'EQGREATER'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIVIDE'),
    ('left', 'LPAREN', 'RPAREN', 'SLPAREN', 'SRPAREN'),
)

def p_program(p):
    '''program : block'''
    print("program")
    p[0] = program(p[1], "program")

def p_block(p):
    '''block : variableDec statement'''
    p[0] = block(p[1], p[2], "block")
    print("block")

def p_variableDec(p):
    '''variableDec : variableType ID arrayStruct initiateVar SEMICOLON'''
    p[0] =variableDec(p[1], ID(p[2]), p[3], p[4], "variableDec")
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
    '''arrayStruct : SLPAREN NUMBER SRPAREN '''
    p[0] = arrayStruct(p[1], NUMBER(p[2]), p[3],"arrayStruct")
    print("arrayStruct ")

def p_arrayStructEmpty(p):
    '''arrayStruct : empty'''
    p[0] = Null()
    print("nulo")

def p_variableType1(p):
    '''variableType : INT'''
    p[0] = variableType1(INT(p[1]),"variableType1")
    print("variableType 1")

def p_variableType2(p):
    '''variableType : TEXTO LPAREN NUMBER RPAREN'''
    p[0] = variableType2(TEXTO(p[1]), NUMBER(p[3]), "variableType2")
    print("variableType 2")

def p_variableTypeEmpty(p):
    '''variableType : empty'''
    p[0] = Null()
    print("nulo")

def p_value1(p):
    '''value : NUMBER'''
    p[0] = value1(NUMBER(p[1]), "value1")
    print("value 1")

def p_value2(p):
    '''value : STRING'''
    p[0] = value1(STRING(p[1]), "value2")
    print("value 2")

def p_statement1(p):
    '''statement : BALLOON LPAREN numberType COLON numberType RPAREN SEMICOLON'''
    p[0] = statement1(p[3], p[5], "statement1")
    print("statement 1")

def p_statement2(p):
    '''statement : DOW LPAREN numberType RPAREN statement ENDDO SEMICOLON'''
    p[0] = statement2(p[3], p[5], "statement2")
    print ("statement 2")

def p_statement3(p):
    '''statement : RANDOM LPAREN arrayType COLON numberType COLON numberType RPAREN SEMICOLON'''
    p[0] = statement3(p[3], p[5], p[7], "statement3")
    print ("statement 3")

def p_statement4(p):
    '''statement : IF LPAREN condition RPAREN SEMICOLON  statement  ENDIF SEMICOLON'''
    p[0] = statement4(p[3], p[5], "statement4")
    print ("statement 4")

def p_statement5(p):
    '''statement : INC LPAREN numberType COLON numberType RPAREN SEMICOLON'''
    p[0] = statement5(p[3], p[5], "statement5")
    print("statement5")

def p_statement6(p):
    '''statement : DEC LPAREN numberType COLON numberType RPAREN SEMICOLON'''
    p[0] = statement6(p[3], p[5], "statement6")
    print("statement6")

def p_statement7(p):
    '''statement : FOR numberType TIMES USING arrayType randomInFor statement FOREND SEMICOLON'''
    p[0] = statement7(p[2], p[5], p[6], p[7], "statement7")
    print("statement7")

def p_statement8(p):
    '''statement : FORASIGNWORD LPAREN numberType COLON numberType RPAREN DO ASIGNWORD LPAREN arrayType COLON arrayType RPAREN SEMICOLON'''
    p[0] = statement1(p[3], p[5], p[10], p[12], "statement8")
    print("statement8")

def p_statement9(p):
    '''statement : TELAARANA LPAREN numberType COLON numberType RPAREN SEMICOLON'''
    p[0] = statement9(p[3], p[5], "statement9")
    print("statement9")

def p_statement10(p):
    '''statement : OBJECT LPAREN numberType COLON numberType COLON numberType RPAREN SEMICOLON'''
    p[0] = statement10(p[3], p[5], p[7], "statement10")
    print("statement10")

def p_statementEmpty(p):
    '''statement : empty'''
    p[0] = Null()
    print("nulo")

# def p_statementList1(p):
#     '''statementList : statement'''
#     print ("statementList 1")
#
# def p_statementList2(p):
#     '''statementList : statementList  statement'''
#     print ("statementList 2")

def p_randomInFor(p):
    '''randomInFor : RANDOM LPAREN numberType COLON numberType RPAREN SEMICOLON'''
    p[0] = randomInFor(p[3], p[5], "randomInFor")
    print("randomInFor")


def p_condition1(p):
    '''condition : expression relation expression'''
    p[0] = condition1(p[1], p[2], p[3], "condition1")
    print ("condition 1")

def p_relation1(p):
    '''relation : ASSIGN'''
    p[0] = relation1(ASSING(p[1]), "relation1")
    print ("relation 1")

def p_relation2(p):
    '''relation : NE'''
    p[0] = relation2(NE(p[1]), "relation2")
    print ("relation 2")

def p_relation3(p):
    '''relation : LESS'''
    p[0] = relation3(LESS(p[1]), "relation3")
    print ("relation 3")

def p_relation4(p):
    '''relation : GREATER'''
    p[0] = relation4(GREATER(p[1]), "relation4")
    print ("relation 4")

def p_relation5(p):
    '''relation : EQLESS'''
    p[0] = relation5(EQLESS(p[1]), "relation5")
    print ("relation 5")

def p_relation6(p):
    '''relation : EQGREATER'''
    p[0] = relation6(EQGREATER(p[1]), "relation6")
    print ("relation 6")

def p_relation7(p):
    '''relation : EQUAL'''
    p[0] = relation7(EQUAL(p[1]), "relation7")
    print ("relation 7")

def p_expression1(p):
    '''expression : term'''
    p[0] = expression1(p[1], "expression1")
    print ("expresion 1")

def p_expression2(p):
    '''expression : addingOperator term'''
    p[0] = expression2(p[1], p[2], "expression2")
    print ("expresion 2")

def p_expression3(p):
    '''expression : expression addingOperator term'''
    p[0] = expression3(p[1], p[2], p[3], "expression3")
    print ("expresion 3")

def p_addingOperator1(p):
    '''addingOperator : PLUS'''
    p[0] = addingOperator1(PLUS(p[1]), "addingOperator1")
    print ("addingOperator 1")

def p_addingOperator2(p):
    '''addingOperator : MINUS'''
    p[0] = addingOperator2(MINUS(p[1]), "addingOperator2")
    print ("addingOperator 1")

def p_term1(p):
    '''term : factor'''
    p[0] = term1(p[1], "factor1")
    print ("term 1")

def p_term2(p):
    '''term : term multiplyingOperator factor'''
    p[0] = term2(p[1], p[2], p[3], "factor2")
    print ("term 2")

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
    print("numberType2")

def p_arrayType(p):
    '''arrayType : ARRAY ID'''
    p[0] = arrayType(ARRAY(p[1]), ID(p[2]), "arrayType")
    print("arrayType")

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    print ("Error de sintaxis ", p)

#print "Error en la linea "+str(p.lineno)

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
        print (str(cont)+". "+file)
        cont = cont+1

    while respuesta == False:
        numArchivo = input('\nNumero del test: ')
        for file in files:
            if file == files[int(numArchivo)-1]:
                respuesta = True
                break

    print ("Has escogido \"%s\" \n" %files[int(numArchivo)-1])

    return files[int(numArchivo)-1]


def traducir(result):
    graphFile = open('graphviztrhee.vz','w')
    graphFile.write(result.traducir())
    graphFile.close()
    print "El programa traducido se guardo en \"graphviztrhee.vz\""

directorio = '/home/josu/Downloads/plyCompiler/test/'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

yacc.yacc()
result = yacc.parse(cadena,debug=1)

#result.imprimir(" ")
#print result.traducir()
traducir(result)