from misc_functions import *

class Row:
  def __init__(self, t):
    self.cells = t
    self.cooked = copy(t)
    self.isEvaled = False
