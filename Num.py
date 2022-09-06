import random
from misc_functions import *

class Num:
  def __init__(self, c = 0, s = ""):
    self.n = 0
    self.at = c
    self.name = s
    self._has = []
    self.lo = float('inf')
    self.hi = float('-inf')
    self.isSorted = True
    self.w = -1 if ((s or "").find("-$") != -1) else 1

  def nums(self):
    if(self.isSorted == False):
      self._has.sort()
      self.isSorted = True
    return self._has
  
  def add(self, v):
    if (v != '?'):
      self.n = self.n + 1
      self.lo = min(v, self.lo)
      self.hi - max(v, self.hi)
      pos = -1
      if (len(self._has) < the["nums"]):
        self._has.append(int(v))
      elif (random.randrange(0, self.n) < the["nums"]):
        pos = random.randrange(0, len(self._has) - 1)
      if (pos):
        self.isSorted = False
        self._has[pos] = int(v)

  def div(self):
    a = self.nums()
    return ((per(a, 0.9) - per(a, 0.1))/2.58)
  
  def mid(self):
     return per(self.nums(), 0.5)
