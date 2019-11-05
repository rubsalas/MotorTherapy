import ply.lex as lex
import re
import codecs
import os
import sys

reservadas = ['IF', 'ELSE', 'DO', 'FOREND', 'FEND', 'BALLOON', 'WHILE', 'INC', 'DEC', 'FOR',
               'RANDOM', 'TELAARANA', 'FORASIGNWORD', 'OBJECT', 'ASIGNWORD', 'TIMES', 'USING', 'PROCEDURE',
                'INT','FLOAT','STRING','TEXTO','DOW','ENDDO', 'ARRAY', 'QUOTE', 'ENDIF']

tokens = reservadas + ['ID', 'NUMBER', 'PLUS', 'MINUS', 'DIVIDE', 'ASSIGN', 'LPAREN', 'RPAREN', 'SRPAREN', 'SLPAREN', 'EQUAL', 'COLON',
          'SEMICOLON', 'PERCENT', 'ELEVATE', 'SLASH', 'LESS', 'GREATER', 'EQLESS', 'EQGREATER', 'SPACE',
           'MULT', 'COMMENT', 'NE']


t_ignore = '\t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIVIDE = r'/'
t_PERCENT = r'\%'
#t_SPACE = "+"

t_QUOTE =r'\''
t_EQUAL = r'=='
t_ASSIGN = r'='
t_EQLESS = r'<='
t_EQGREATER = r'>='
t_LESS = r'<'
t_GREATER = r'>'
t_NE = r'!='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SLPAREN = r'\['
t_SRPAREN = r'\]'
t_SEMICOLON = r'\;'
t_COLON = r','

t_IF = r'If'
t_ELSE = 'else'
t_DO = r'DO'
t_FOREND = r'FOREND'
t_FEND = r'FEnd'
t_BALLOON = r'Balloon'
t_DOW = r'Dow'
t_ENDDO = r'Enddo'
t_INC = r'Inc'
t_DEC = r'Dec'
t_FOR = r'FOR'
t_RANDOM = r'Random'
t_TELAARANA = r'TelaArana'
t_FORASIGNWORD = r'ForAsignWord'
t_OBJECT = r'Object'
t_ASIGNWORD = r'AsignWord'
t_TIMES = r'times'
t_USING = r'using'
t_ENDIF = r'ENDIF'
t_ARRAY = r'Array'
t_INT = r'Int'
t_FLOAT = r'Float'
t_TEXTO = r'Texto'


#literals = {'{', '}', ';', ':','[',']','@','_','&','-'}


def t_ID(t):
    r'([a-z]+[a-zA-Z_][a-zA-Z0-9_]*[&@_-]*)+'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_STRING(t):
    r'([a-zA-Z_][a-zA-Z0-9_]*)'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_COMMENT(t):
    r'\//.*'
    pass


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_error(t):
    print("illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


cadena = ","
analizador = lex.lex()
# analizador.input(cadena)
#
# while True:
#    tok = analizador.token()
#    if not tok:
#        break
#    print(tok)

