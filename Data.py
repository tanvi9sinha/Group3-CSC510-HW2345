from misc_functions import *
from Cols import *
from Row import *

class Data:
  def __init__(self, src):
    self.cols = None
    self.rows = {}
    if(type(src) == str):
      csv(src,  lambda row : self.add(row)) 
    else:
      for _, row in src.items(): 
        self.add(row)

  def add(self, xs):
    if (not self.cols):
      self.cols = Cols(xs)
    else :
      row = push(self.rows, xs if "cells" in xs.items() else Row(xs)) 
      for _, v in self.cols.x.items():
        v.add(row.cells[v.at])
      for _, v in self.cols.y.items():
        v.add(row.cells[v.at])

  def stats(self, places, showCols, fun):
    showCols, fun = showCols or self.cols.y, fun or "mid"
    t = {}
    for _, col in showCols.items():
      v = fun(col)
      v = v if(type(v) == int) else rnd(v, places)
      t[col.name] = v
    return t
