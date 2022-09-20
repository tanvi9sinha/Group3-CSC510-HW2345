from misc import *
from cli import *
import random


class Num:
  def __init__(self, the, c = 0, s = ""):
    self.the = the
    self.n = 0
    self.at = c
    self.name = s
    self._has = []
    self.lo = float('inf')
    self.hi = float('-inf')
    self.isSorted = True
    self.w = 1
    if(len(s) != 0): 
      self.w = -1 if (s[-1] == '-') else 1

  def nums(self):
    if(self.isSorted == False):
      self._has.sort()
      self.isSorted = True
    return self._has
  
  def add(self, v):
    if (v != '?'):
      self.n = self.n + 1
      self.lo = min(float(v), self.lo)
      self.hi = max(float(v), self.hi)
      pos = -1
      if (len(self._has) < self.the["nums"]):
        self._has.append(float(v))
      elif (random.randrange(0, self.n) < self.the["nums"]):
        pos = random.randrange(0, len(self._has) - 1)
      if (pos):
        self.isSorted = False
        self._has[pos] = float(v)

  def div(self):
    a = self.nums()
    return ((per(a, 0.9) - per(a, 0.1))/2.58)
  
  def mid(self):
     return per(self.nums(), 0.5)
