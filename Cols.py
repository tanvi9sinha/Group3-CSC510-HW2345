from misc_functions import *
from Sym import *
from Num import *
import re

class Cols:
  def __init__(self, names):
    self.names = names
    self.all = {}
    self.klass = None
    self.x = {}
    self.y = {}
    for c, s in names.items():
      column = None
      if(re.match('^[A-Z]+', s) == None):
        column = Sym(c, s)
      else: 
        column = Num(c, s)
      col = push(self.all, column)
      if(s[-1] != ':'):
        toPush = None
        if(s[-1] == '+' or s[-1] == '-'):
          toPush = self.y
        elif(s[-1] == '!'):
          self.klass = col
        else: 
          toPush = self.x
        push(toPush, col)
