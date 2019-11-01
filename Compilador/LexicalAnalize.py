
from sly import Lexer,Parser

class CalcLexer(Lexer):
    #
    tokens = {ID, NUMBER, PLUS, MINUS, TIMES, DIVIDE, ASSIGN, LPAREN, RPAREN, EQUAL, COLON,
              SEMICOLON, PERCENT, ELEVATE, SLASH, LESS, GREATER, EQLESS, EQGREATER, SPACE, KEYWORDS, IF, ELSE, FUNCTION,
              BALLOON, BREAK, WHILE, INC, DEC, FOR, FOREND, RANDOM, MULT, USING, FORASIGNWORD,TELARAÑA,DO, ASIGNWORD, OBJECT, FEND,COMMENT}




    literals = {'(', ')', '{', '}', ';', ':','[',']','@','_','&','-'}
    ignore= '\t'
    FUNCTION = r'def [A-Z][a-zA-Z_]*'
    KEYWORDS = r'([a-zA-Z_][a-zA-Z0-9_]*[&@_-]*)+'
    NUMBER=r'\d+'


    PLUS= r'\+'
    MINUS=r'-'
    MULT=r'\*'
    COMMENT='//'
    DIVIDE=r'/'
    PERCENT = r'\%'
    SPACE=' '


    EQUAL= r'=='
    ASSIGN = r'='
    EQLESS=r'<='
    EQGREATER=r'>='
    LESS=r'<'
    GREATER=r'>'

    #Special tokens(Keywords)


    KEYWORDS['if'] = IF
    KEYWORDS['else'] = ELSE
    KEYWORDS['DO'] = DO
    KEYWORDS['FOREND'] = FOREND
    KEYWORDS['FEnd']=FEND
    FUNCTION['Balloon'] = BALLOON
    FUNCTION['Dow'] = WHILE
    FUNCTION['Enddo'] = BREAK
    FUNCTION['Inc'] = INC
    FUNCTION['Dec'] = DEC
    FUNCTION['FOR'] = FOR
    FUNCTION['Random'] = RANDOM
    FUNCTION['TelaAraña'] = TELARAÑA
    FUNCTION['ForAsignWord'] = FORASIGNWORD
    FUNCTION['Object']=OBJECT
    FUNCTION['AsignWord'] = ASIGNWORD
    KEYWORDS['times'] = TIMES
    KEYWORDS['using'] = USING



if __name__ == '__main__':
    data ='times'

    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        print(tok)