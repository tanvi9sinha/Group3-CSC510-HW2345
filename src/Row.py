from misc import *
def copy(t):
  if(type(t)!= "dict"):
    return t
  u = {}
  for k, v in t.items():
    u[k] = copy(v)
  return u

class Row:
  def __init__(self, t):
    self.cells = t
    self.cooked = copy(t)
    self.isEvaled = False
