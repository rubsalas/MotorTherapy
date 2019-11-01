
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightDECBALLOONFORIFDOWRANDOMIDrightASSIGNleftNEleftLESSEQLESSGREATEREQGREATERleftPLUSMINUSleftMULTDIVIDEleftLPARENRPARENSLPARENSRPARENARRAY ASIGNWORD ASSIGN BALLOON COLON COMMENT DEC DIVIDE DO DOW ELEVATE ELSE ENDDO EQGREATER EQLESS EQUAL FEND FLOAT FOR FORASIGNWORD FOREND GREATER ID IF INC INT LESS LPAREN MINUS MULT NE NUMBER OBJECT PERCENT PLUS PROCEDURE QUOTE RANDOM RPAREN SEMICOLON SLASH SLPAREN SPACE SRPAREN STRING TELARANA TEXTO TIMES USING WHILEprogram : blockblock :  varDecl valueAsign statementvalueAsign :  BALLOON LPAREN numberType COLON numberType RPAREN SEMICOLONvalueAsign :  ID ASSIGN STRING SEMICOLONvalueAsign :  ID SLPAREN NUMBER SRPAREN ASSIGN STRING SEMICOLONvalueAsign : ID SLPAREN NUMBER SRPAREN ASSIGN NUMBER SEMICOLONvarDecl : identList SEMICOLONvarDecl : INT ID ASSIGN NUMBER SEMICOLONvarDecl : TEXTO ID ASSIGN STRING SEMICOLONvarDecl : TEXTO LPAREN NUMBER RPAREN ID SLPAREN NUMBER SRPAREN SEMICOLONvarDecl : INT ID SLPAREN NUMBER SRPAREN SEMICOLONvarDecl : emptyidentList : variableType IDidentList : identList COLON IDvariableType : INTvariableType : TEXTOstatement : DOW LPAREN numberType RPAREN statementList ENDDO SEMICOLONstatement : RANDOM LPAREN ID COLON ID COLON ID RPARENstatement : IF LPAREN condition RPAREN SEMICOLON  statementListstatement : INC LPAREN ID COLON NUMBER RPAREN SEMICOLONstatement : DEC LPAREN ID COLON NUMBER RPAREN SEMICOLONstatement : FOR NUMBER TIMES USING ID randomInFor statementList FOREND SEMICOLONstatement : FORASIGNWORD LPAREN numberType COLON numberType RPAREN DO ASIGNWORD LPAREN arrayType COLON arrayType RPAREN SEMICOLONstatement : TELARANA LPAREN numberType COLON numberType RPAREN SEMICOLONstatement : OBJECT LPAREN numberType COLON numberType COLON numberType RPAREN SEMICOLONstatement : emptystatementList : statementstatementList : statementList statementrandomInFor : LPAREN ID COLON ID RPAREN SEMICOLONcondition : expression relation expressionrelation : ASSIGNrelation : NErelation : LESSrelation : GREATERrelation : EQLESSrelation : EQGREATERrelation : EQUALexpression : termexpression : addingOperator termexpression : expression addingOperator termaddingOperator : PLUSaddingOperator : MINUSterm : factorterm : term multiplyingOperator factormultiplyingOperator : MULTmultiplyingOperator : DIVIDEfactor : IDfactor : NUMBERfactor : ID SLPAREN NUMBER SRPARENnumberType : NUMBERnumberType : INT IDarrayType : TEXTO LPAREN NUMBER RPAREN ID SLPAREN NUMBER SRPAREN SEMICOLONarrayType : ARRAY IDempty :'
    
_lr_action_items = {'INT':([0,29,37,43,44,45,72,100,101,102,136,],[5,48,48,48,48,48,48,48,48,48,48,]),'TEXTO':([0,158,165,],[6,162,162,]),'BALLOON':([0,3,7,12,76,78,105,150,],[-54,10,-12,-7,-8,-9,-11,-10,]),'ID':([0,3,5,6,7,8,12,13,38,39,40,41,48,54,60,62,63,76,78,81,83,84,85,86,87,88,89,90,91,92,93,94,99,105,127,133,150,153,163,171,],[-54,11,14,15,-12,17,-7,32,56,64,66,67,73,79,64,-41,-42,-8,-9,109,64,64,-31,-32,-33,-34,-35,-36,-37,64,-45,-46,117,-11,142,146,-10,157,167,173,]),'$end':([1,2,9,18,28,74,108,110,126,128,137,138,139,141,143,144,148,151,156,159,172,],[0,-1,-54,-2,-26,-4,-27,-54,-28,-19,-3,-6,-5,-17,-20,-21,-24,-18,-22,-25,-23,]),'SEMICOLON':([4,17,32,49,51,53,77,82,121,122,123,125,130,131,135,140,152,155,160,170,176,],[12,-13,-14,74,76,78,105,110,137,138,139,141,143,144,148,150,156,159,164,172,177,]),'COLON':([4,17,32,46,47,56,66,67,69,70,71,73,109,120,146,161,167,177,],[13,-13,-14,72,-50,81,97,98,100,101,102,-51,127,136,153,165,-53,-52,]),'LPAREN':([6,10,19,20,21,22,23,25,26,27,117,154,162,],[16,29,37,38,39,40,41,43,44,45,133,158,166,]),'DOW':([9,28,74,80,107,108,110,126,128,132,137,138,139,141,143,144,145,148,151,156,159,164,172,],[19,-26,-4,19,19,-27,19,-28,19,19,-3,-6,-5,-17,-20,-21,19,-24,-18,-22,-25,-29,-23,]),'RANDOM':([9,28,74,80,107,108,110,126,128,132,137,138,139,141,143,144,145,148,151,156,159,164,172,],[20,-26,-4,20,20,-27,20,-28,20,20,-3,-6,-5,-17,-20,-21,20,-24,-18,-22,-25,-29,-23,]),'IF':([9,28,74,80,107,108,110,126,128,132,137,138,139,141,143,144,145,148,151,156,159,164,172,],[21,-26,-4,21,21,-27,21,-28,21,21,-3,-6,-5,-17,-20,-21,21,-24,-18,-22,-25,-29,-23,]),'INC':([9,28,74,80,107,108,110,126,128,132,137,138,139,141,143,144,145,148,151,156,159,164,172,],[22,-26,-4,22,22,-27,22,-28,22,22,-3,-6,-5,-17,-20,-21,22,-24,-18,-22,-25,-29,-23,]),'DEC':([9,28,74,80,107,108,110,126,128,132,137,138,139,141,143,144,145,148,151,156,159,164,172,],[23,-26,-4,23,23,-27,23,-28,23,23,-3,-6,-5,-17,-20,-21,23,-24,-18,-22,-25,-29,-23,]),'FOR':([9,28,74,80,107,108,110,126,128,132,137,138,139,141,143,144,145,148,151,156,159,164,172,],[24,-26,-4,24,24,-27,24,-28,24,24,-3,-6,-5,-17,-20,-21,24,-24,-18,-22,-25,-29,-23,]),'FORASIGNWORD':([9,28,74,80,107,108,110,126,128,132,137,138,139,141,143,144,145,148,151,156,159,164,172,],[25,-26,-4,25,25,-27,25,-28,25,25,-3,-6,-5,-17,-20,-21,25,-24,-18,-22,-25,-29,-23,]),'TELARANA':([9,28,74,80,107,108,110,126,128,132,137,138,139,141,143,144,145,148,151,156,159,164,172,],[26,-26,-4,26,26,-27,26,-28,26,26,-3,-6,-5,-17,-20,-21,26,-24,-18,-22,-25,-29,-23,]),'OBJECT':([9,28,74,80,107,108,110,126,128,132,137,138,139,141,143,144,145,148,151,156,159,164,172,],[27,-26,-4,27,27,-27,27,-28,27,27,-3,-6,-5,-17,-20,-21,27,-24,-18,-22,-25,-29,-23,]),'ASSIGN':([11,14,15,58,59,61,64,65,75,95,112,113,129,],[30,33,35,85,-38,-43,-47,-48,104,-39,-40,-44,-49,]),'SLPAREN':([11,14,64,79,173,],[31,34,96,106,174,]),'NUMBER':([16,24,29,31,33,34,37,39,43,44,45,60,62,63,72,83,84,85,86,87,88,89,90,91,92,93,94,96,97,98,100,101,102,104,106,136,166,174,],[36,42,47,50,51,52,47,65,47,47,47,65,-41,-42,47,65,65,-31,-32,-33,-34,-35,-36,-37,65,-45,-46,114,115,116,47,47,47,122,124,47,169,175,]),'ENDDO':([28,80,107,108,110,126,128,141,143,144,148,151,156,159,172,],[-26,-54,125,-27,-54,-28,-19,-17,-20,-21,-24,-18,-22,-25,-23,]),'FOREND':([28,108,110,126,128,132,141,143,144,145,148,151,156,159,164,172,],[-26,-27,-54,-28,-19,-54,-17,-20,-21,152,-24,-18,-22,-25,-29,-23,]),'STRING':([30,35,104,],[49,53,123,]),'RPAREN':([36,47,55,57,59,61,64,65,73,95,103,111,112,113,115,116,118,119,129,142,149,157,167,168,169,177,],[54,-50,80,82,-38,-43,-47,-48,-51,-39,121,-30,-40,-44,130,131,134,135,-49,151,155,160,-53,170,171,-52,]),'PLUS':([39,58,59,61,64,65,83,85,86,87,88,89,90,91,95,111,112,113,129,],[62,62,-38,-43,-47,-48,62,-31,-32,-33,-34,-35,-36,-37,-39,62,-40,-44,-49,]),'MINUS':([39,58,59,61,64,65,83,85,86,87,88,89,90,91,95,111,112,113,129,],[63,63,-38,-43,-47,-48,63,-31,-32,-33,-34,-35,-36,-37,-39,63,-40,-44,-49,]),'TIMES':([42,],[68,]),'SRPAREN':([50,52,114,124,175,],[75,77,129,140,176,]),'NE':([58,59,61,64,65,95,112,113,129,],[86,-38,-43,-47,-48,-39,-40,-44,-49,]),'LESS':([58,59,61,64,65,95,112,113,129,],[87,-38,-43,-47,-48,-39,-40,-44,-49,]),'GREATER':([58,59,61,64,65,95,112,113,129,],[88,-38,-43,-47,-48,-39,-40,-44,-49,]),'EQLESS':([58,59,61,64,65,95,112,113,129,],[89,-38,-43,-47,-48,-39,-40,-44,-49,]),'EQGREATER':([58,59,61,64,65,95,112,113,129,],[90,-38,-43,-47,-48,-39,-40,-44,-49,]),'EQUAL':([58,59,61,64,65,95,112,113,129,],[91,-38,-43,-47,-48,-39,-40,-44,-49,]),'MULT':([59,61,64,65,95,112,113,129,],[93,-43,-47,-48,93,93,-44,-49,]),'DIVIDE':([59,61,64,65,95,112,113,129,],[94,-43,-47,-48,94,94,-44,-49,]),'USING':([68,],[99,]),'DO':([134,],[147,]),'ASIGNWORD':([147,],[154,]),'ARRAY':([158,165,],[163,163,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'block':([0,],[2,]),'varDecl':([0,],[3,]),'identList':([0,],[4,]),'empty':([0,9,80,107,110,128,132,145,],[7,28,28,28,28,28,28,28,]),'variableType':([0,],[8,]),'valueAsign':([3,],[9,]),'statement':([9,80,107,110,128,132,145,],[18,108,126,108,126,108,126,]),'numberType':([29,37,43,44,45,72,100,101,102,136,],[46,55,69,70,71,103,118,119,120,149,]),'condition':([39,],[57,]),'expression':([39,83,],[58,111,]),'term':([39,60,83,84,],[59,95,59,112,]),'addingOperator':([39,58,83,111,],[60,84,60,84,]),'factor':([39,60,83,84,92,],[61,61,61,61,113,]),'relation':([58,],[83,]),'multiplyingOperator':([59,95,112,],[92,92,92,]),'statementList':([80,110,132,],[107,128,145,]),'randomInFor':([117,],[132,]),'arrayType':([158,165,],[161,168,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> block','program',1,'p_program','SintaticAnalizer.py',19),
  ('block -> varDecl valueAsign statement','block',3,'p_block','SintaticAnalizer.py',24),
  ('valueAsign -> BALLOON LPAREN numberType COLON numberType RPAREN SEMICOLON','valueAsign',7,'p_valueAsign1','SintaticAnalizer.py',28),
  ('valueAsign -> ID ASSIGN STRING SEMICOLON','valueAsign',4,'p_valueAsign2','SintaticAnalizer.py',32),
  ('valueAsign -> ID SLPAREN NUMBER SRPAREN ASSIGN STRING SEMICOLON','valueAsign',7,'p_valueAsign3','SintaticAnalizer.py',36),
  ('valueAsign -> ID SLPAREN NUMBER SRPAREN ASSIGN NUMBER SEMICOLON','valueAsign',7,'p_valueAsign4','SintaticAnalizer.py',40),
  ('varDecl -> identList SEMICOLON','varDecl',2,'p_varDecl1','SintaticAnalizer.py',44),
  ('varDecl -> INT ID ASSIGN NUMBER SEMICOLON','varDecl',5,'p_varDecl2','SintaticAnalizer.py',48),
  ('varDecl -> TEXTO ID ASSIGN STRING SEMICOLON','varDecl',5,'p_varDecl3','SintaticAnalizer.py',52),
  ('varDecl -> TEXTO LPAREN NUMBER RPAREN ID SLPAREN NUMBER SRPAREN SEMICOLON','varDecl',9,'p_varDecl4','SintaticAnalizer.py',56),
  ('varDecl -> INT ID SLPAREN NUMBER SRPAREN SEMICOLON','varDecl',6,'p_varDecl5','SintaticAnalizer.py',60),
  ('varDecl -> empty','varDecl',1,'p_varDeclEmpty','SintaticAnalizer.py',65),
  ('identList -> variableType ID','identList',2,'p_identList1','SintaticAnalizer.py',69),
  ('identList -> identList COLON ID','identList',3,'p_identList2','SintaticAnalizer.py',73),
  ('variableType -> INT','variableType',1,'p_variableType1','SintaticAnalizer.py',77),
  ('variableType -> TEXTO','variableType',1,'p_variableType2','SintaticAnalizer.py',81),
  ('statement -> DOW LPAREN numberType RPAREN statementList ENDDO SEMICOLON','statement',7,'p_statement2','SintaticAnalizer.py',89),
  ('statement -> RANDOM LPAREN ID COLON ID COLON ID RPAREN','statement',8,'p_statement3','SintaticAnalizer.py',93),
  ('statement -> IF LPAREN condition RPAREN SEMICOLON statementList','statement',6,'p_statement4','SintaticAnalizer.py',97),
  ('statement -> INC LPAREN ID COLON NUMBER RPAREN SEMICOLON','statement',7,'p_statement5','SintaticAnalizer.py',101),
  ('statement -> DEC LPAREN ID COLON NUMBER RPAREN SEMICOLON','statement',7,'p_statement6','SintaticAnalizer.py',105),
  ('statement -> FOR NUMBER TIMES USING ID randomInFor statementList FOREND SEMICOLON','statement',9,'p_statement7','SintaticAnalizer.py',109),
  ('statement -> FORASIGNWORD LPAREN numberType COLON numberType RPAREN DO ASIGNWORD LPAREN arrayType COLON arrayType RPAREN SEMICOLON','statement',14,'p_statement8','SintaticAnalizer.py',113),
  ('statement -> TELARANA LPAREN numberType COLON numberType RPAREN SEMICOLON','statement',7,'p_statement9','SintaticAnalizer.py',117),
  ('statement -> OBJECT LPAREN numberType COLON numberType COLON numberType RPAREN SEMICOLON','statement',9,'p_statement10','SintaticAnalizer.py',121),
  ('statement -> empty','statement',1,'p_statementEmpty','SintaticAnalizer.py',125),
  ('statementList -> statement','statementList',1,'p_statementList1','SintaticAnalizer.py',129),
  ('statementList -> statementList statement','statementList',2,'p_statementList2','SintaticAnalizer.py',133),
  ('randomInFor -> LPAREN ID COLON ID RPAREN SEMICOLON','randomInFor',6,'p_randomInFor','SintaticAnalizer.py',137),
  ('condition -> expression relation expression','condition',3,'p_condition1','SintaticAnalizer.py',141),
  ('relation -> ASSIGN','relation',1,'p_relation1','SintaticAnalizer.py',145),
  ('relation -> NE','relation',1,'p_relation2','SintaticAnalizer.py',149),
  ('relation -> LESS','relation',1,'p_relation3','SintaticAnalizer.py',153),
  ('relation -> GREATER','relation',1,'p_relation4','SintaticAnalizer.py',157),
  ('relation -> EQLESS','relation',1,'p_relation5','SintaticAnalizer.py',161),
  ('relation -> EQGREATER','relation',1,'p_relation6','SintaticAnalizer.py',165),
  ('relation -> EQUAL','relation',1,'p_relation7','SintaticAnalizer.py',169),
  ('expression -> term','expression',1,'p_expression1','SintaticAnalizer.py',173),
  ('expression -> addingOperator term','expression',2,'p_expression2','SintaticAnalizer.py',177),
  ('expression -> expression addingOperator term','expression',3,'p_expression3','SintaticAnalizer.py',181),
  ('addingOperator -> PLUS','addingOperator',1,'p_addingOperator1','SintaticAnalizer.py',185),
  ('addingOperator -> MINUS','addingOperator',1,'p_addingOperator2','SintaticAnalizer.py',189),
  ('term -> factor','term',1,'p_term1','SintaticAnalizer.py',193),
  ('term -> term multiplyingOperator factor','term',3,'p_term2','SintaticAnalizer.py',197),
  ('multiplyingOperator -> MULT','multiplyingOperator',1,'p_multiplyingOperator1','SintaticAnalizer.py',201),
  ('multiplyingOperator -> DIVIDE','multiplyingOperator',1,'p_multiplyingOperator2','SintaticAnalizer.py',205),
  ('factor -> ID','factor',1,'p_factor1','SintaticAnalizer.py',209),
  ('factor -> NUMBER','factor',1,'p_factor2','SintaticAnalizer.py',213),
  ('factor -> ID SLPAREN NUMBER SRPAREN','factor',4,'p_factor3','SintaticAnalizer.py',217),
  ('numberType -> NUMBER','numberType',1,'p_numberType1','SintaticAnalizer.py',221),
  ('numberType -> INT ID','numberType',2,'p_numberType2','SintaticAnalizer.py',225),
  ('arrayType -> TEXTO LPAREN NUMBER RPAREN ID SLPAREN NUMBER SRPAREN SEMICOLON','arrayType',9,'p_arrayType1','SintaticAnalizer.py',230),
  ('arrayType -> ARRAY ID','arrayType',2,'p_arrayType3','SintaticAnalizer.py',235),
  ('empty -> <empty>','empty',0,'p_empty','SintaticAnalizer.py',239),
]