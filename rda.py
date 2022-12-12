import re

# Syntax Analyzer
class RDA:
  def __init__(self, tokens) :
    self.tokens = tokens
    self.current = 0
    self.currentToken = tokens[self.current]

  def start(self):
    if self.currentToken == 'INIT':
      self.getNextToken()
      self.stmt()
    else:
      self.error()

  def getNextToken(self):
    if self.current < len(self.tokens):
      self.current += 1
    self.currentToken = self.tokens[self.current]

  def stmt(self):
    match self.currentToken:
      case 'DRNG':
        self.during()
      case 'GIVN':
        self.given()
      case 'id':
        self.var_op()
      case 'BRKS':
        self.block()
      case _:
        self.error()

  def block(self):
    if self.currentToken == '{':
      self.getNextToken()
      while self.currentToken == 'DRNG' or self.currentToken == 'GIVN' or self.currentToken == 'id' or self.currentToken == 'BRKS':
        self.stmt()
        if self.currentToken == 'BLKE':
          self.getNextToken()
          self.stmt()
        else:
          self.error()
      if self.currentToken == 'BRKE':
        self.getNextToken()
      else:
        self.error()
    else:
      self.error()
    
  def during(self):
    if self.currentToken == 'DRNG':
      self.getNextToken()
      if self.currentToken == 'STRP':
        self.getNextToken()
        self.boolexpr()
        if self.currentToken == 'ENDP':
          self.getNextToken()
          self.block()
        else:
          self.error()
      elif self.currentToken == 'int':
        self.getNextToken()
        self.block()
      else:
        self.error()
      pass
    else:
      self.error()

  def given(self):
    if self.currentToken == 'GIVN':
      self.getNextToken()
      if self.currentToken == 'STRP':
        self.getNextToken()
        self.boolexpr()
        if self.currentToken == 'ENDP':
          self.getNextToken()
          self.block()
          if self.currentToken == 'IFNO':
            self.getNextToken()
            self.block()
        else:
          self.error()
      else:
        self.error()
    else:
      self.error()
      
  def boolexpr(self):
    self.bor()
    while self.currentToken == 'AND':
      self.getNextToken()
      self.bor()

  def bor(self):
    self.beq()
    while self.currentToken == 'OR':
      self.getNextToken()
      self.beq()

  def beq(self):
    self.brel()
    while self.currentToken == 'EQTO' or self.currentToken == 'NOEQ':
      self.getNextToken()
      self.brel()

  def brel(self):
    self.bexpr()
    while self.currentToken == 'LESS' or self.currentToken == 'MORE' or self.currentToken == 'LEEQ' or self.currentToken == 'MOEQ':
      self.getNextToken()
      self.bexpr()

  def bexpr(self):
    self.bterm()
    while self.currentToken == 'MULT' or self.currentToken == 'DIVS':
      self.getNextToken()
      self.bterm()

  def bterm(self):
    self.bfactor()
    while self.currentToken == 'PLUS' or self.currentToken == 'MNUS' :
      self.getNextToken()
      self.bfactor()

  def bfactor(self):
    if self.currentToken == 'id' or self.currentToken == 'int':
      self.getNextToken()
    elif self.currentToken == 'STRP':
      self.getNextToken()
      self.bexpr()
      if self.currentToken == 'ENDP':
        self.getNextToken()
      else:
        self.error()
    else:
      self.error()

  def var_op(self):
    if self.currentToken == 'SNUM'or self.currentToken =='INUM'or self.currentToken =='LNUM':
      self.getNextToken()
      if self.currentToken == 'id':
        self.getNextToken()
      elif self.currentToken == 'SIGN':
        self.getNextToken()
        self.expr()
      else:
        self.error()

  def expr(self):
    self.term()
    while self.currentToken == 'MULT' or self.currentToken == 'DIVS':
      self.getNextToken()
      self.term()

  def term(self):
    self.factor()
    while self.currentToken == 'PLUS' or self.currentToken == 'MNUS' :
      self.getNextToken()
      self.factor()

  def error(self):
    print("Syntax Error.")
    StopIteration

  def factor(self):
    if self.currentToken == 'id' or self.currentToken == 'int':
      self.getNextToken()
    elif self.currentToken == 'STRP':
      self.getNextToken()
      self.expr()
      if self.currentToken == 'ENDP':
        self.getNextToken()
      else:
        self.error()
    else:
      self.error()