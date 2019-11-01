import ply.yacc as yacc
import os
import codecs
import re
from LexicalAnalizer import tokens
from sys import stdin

precedence = (
    ('right','DEC','BALLOON','FOR','IF','DOW','RANDOM','ID'),
    ('right', 'ASSIGN'),
    ('left', 'NE'),
    ('left', 'LESS', 'EQLESS', 'GREATER', 'EQGREATER'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIVIDE'),
    ('left', 'LPAREN', 'RPAREN', 'SLPAREN', 'SRPAREN'),
    )

def p_program(p):
    '''program : block'''
    print ("program")
#p[0] = program(p[1],"program")

def p_block(p):
    '''block :  varDecl valueAsign statement'''
    print ("block")

def p_valueAsign1(p):
    '''valueAsign :  BALLOON LPAREN numberType COLON numberType RPAREN SEMICOLON'''
    print ("valueAsign 1")

def p_valueAsign2(p):
    '''valueAsign :  ID ASSIGN STRING SEMICOLON'''
    print ("valueAsign 2")

def p_valueAsign3(p):
    '''valueAsign :  ID SLPAREN NUMBER SRPAREN ASSIGN STRING SEMICOLON'''
    print ("valueAsign 3")

def p_valueAsign4(p):
    '''valueAsign : ID SLPAREN NUMBER SRPAREN ASSIGN NUMBER SEMICOLON'''
    print ("valueAsign 4")

def p_varDecl1(p):
    '''varDecl : identList SEMICOLON'''
    print ("varDecl 1")

def p_varDecl2(p):
    '''varDecl : INT ID ASSIGN NUMBER SEMICOLON'''
    print ("varDecl 2")

def p_varDecl3(p):
    '''varDecl : TEXTO ID ASSIGN STRING SEMICOLON'''
    print ("varDecl 3")

def p_varDecl4(p):
    '''varDecl : TEXTO LPAREN NUMBER RPAREN ID SLPAREN NUMBER SRPAREN SEMICOLON'''
    print ("varDecl 4")

def p_varDecl5(p):
    '''varDecl : INT ID SLPAREN NUMBER SRPAREN SEMICOLON'''
    print ("varDecl 5")


def p_varDeclEmpty(p):
    '''varDecl : empty'''
    print ("nulo")

def p_identList1(p):
    '''identList : variableType ID'''
    print ("identList 1")

def p_identList2(p):
    '''identList : identList COLON ID'''
    print ("identList 2")

def p_variableType1(p):
    '''variableType : INT'''
    print("variableType1")

def p_variableType2(p):
    '''variableType : TEXTO'''
    print("variableType2")

# def p_statement1(p):
#     '''statement : BALLOON LPAREN numberType COLON numberType RPAREN SEMICOLON'''
#     print ("statement 1")

def p_statement2(p):
    '''statement : DOW LPAREN numberType RPAREN statementList ENDDO SEMICOLON'''
    print ("statement 2")

def p_statement3(p):
    '''statement : RANDOM LPAREN ID COLON ID COLON ID RPAREN'''
    print ("statement 3")

def p_statement4(p):
    '''statement : IF LPAREN condition RPAREN SEMICOLON  statementList'''
    print ("statement 4")

def p_statement5(p):
    '''statement : INC LPAREN ID COLON NUMBER RPAREN SEMICOLON'''
    print("statement5")

def p_statement6(p):
    '''statement : DEC LPAREN ID COLON NUMBER RPAREN SEMICOLON'''
    print("statement6")

def p_statement7(p):
    '''statement : FOR NUMBER TIMES USING ID randomInFor statementList FOREND SEMICOLON'''
    print("statement7")

def p_statement8(p):
    '''statement : FORASIGNWORD LPAREN numberType COLON numberType RPAREN DO ASIGNWORD LPAREN arrayType COLON arrayType RPAREN SEMICOLON'''
    print("statement8")

def p_statement9(p):
    '''statement : TELARANA LPAREN numberType COLON numberType RPAREN SEMICOLON'''
    print("statement9")

def p_statement10(p):
    '''statement : OBJECT LPAREN numberType COLON numberType COLON numberType RPAREN SEMICOLON'''
    print("statement10")

def p_statementEmpty(p):
    '''statement : empty'''
    print ("nulo")

def p_statementList1(p):
    '''statementList : statement'''
    print ("statementList 1")

def p_statementList2(p):
    '''statementList : statementList statement'''
    print ("statementList 2")

def p_randomInFor(p):
    '''randomInFor : LPAREN ID COLON ID RPAREN SEMICOLON'''
    print("randomInFor")

def p_condition1(p):
    '''condition : expression relation expression'''
    print ("condition 1")

def p_relation1(p):
    '''relation : ASSIGN'''
    print ("relation 1")

def p_relation2(p):
    '''relation : NE'''
    print ("relation 2")

def p_relation3(p):
    '''relation : LESS'''
    print ("relation 3")

def p_relation4(p):
    '''relation : GREATER'''
    print ("relation 4")

def p_relation5(p):
    '''relation : EQLESS'''
    print ("relation 5")

def p_relation6(p):
    '''relation : EQGREATER'''
    print ("relation 6")

def p_relation7(p):
    '''relation : EQUAL'''
    print ("relation 7")

def p_expression1(p):
    '''expression : term'''
    print ("expresion 1")

def p_expression2(p):
    '''expression : addingOperator term'''
    print ("expresion 2")

def p_expression3(p):
    '''expression : expression addingOperator term'''
    print ("expresion 3")

def p_addingOperator1(p):
    '''addingOperator : PLUS'''
    print ("addingOperator 1")

def p_addingOperator2(p):
    '''addingOperator : MINUS'''
    print ("addingOperator 1")

def p_term1(p):
    '''term : factor'''
    print ("term 1")

def p_term2(p):
    '''term : term multiplyingOperator factor'''
    print ("term 1")

def p_multiplyingOperator1(p):
    '''multiplyingOperator : MULT'''
    print("multiplyingOperator 1")

def p_multiplyingOperator2(p):
    '''multiplyingOperator : DIVIDE'''
    print("multiplyingOperator 2")

def p_factor1(p):
    '''factor : ID'''
    print("factor 1")

def p_factor2(p):
    '''factor : NUMBER'''
    print("factor 2")

def p_factor3(p):
    '''factor : ID SLPAREN NUMBER SRPAREN'''
    print("factor 3")

def p_numberType1(p):
    '''numberType : NUMBER'''
    print("numberType1")

def p_numberType2(p):
    '''numberType : INT ID'''
    print("numberType2")


def p_arrayType1(p):
    '''arrayType : TEXTO LPAREN NUMBER RPAREN ID SLPAREN NUMBER SRPAREN SEMICOLON'''
    print("arrayType1")


def p_arrayType3(p):
    '''arrayType : ARRAY ID'''
    print("arrayType3")

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

directorio = '/home/pablo/Documentos/Github/MotorTherapy/plyCompiler/test/'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)

print (result)