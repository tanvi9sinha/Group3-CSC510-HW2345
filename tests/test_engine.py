from collections import OrderedDict
import random 
from src import *
# from src.Num import *
# from src.Sym import *
# from src.misc import *

eg_local = {}



def pcall(func, the): 
  try: 
    if func == "ALL" or func == "BIGNUM" or func == "NUM" or func=="DATA" or func=="STATS":
        retval = eg_local[func](the)
        return (True, retval)
    else:
        retval = eg_local[func]()
        return (True, retval)
  except Exception as e: 
    print("Exception"+str(e))
    return (False, e)

def runs(m, the):
  try:
    status = False
    out = False
    if not eg_local[m]:
      return
    random.seed(the["seed"])
    old = {}
    for key, val in the.items():
      old[key] = val
    
    if (the["dump"] == True):
        status, out = True, eg_local[m]()
    #   status, out = True, eg_local[m]()
    else:
       status, out = pcall(m, the)
    for key, val in old.items():
      the[key] = val
    if status == True:
      if out != False:
        msg = "PASS"
      else:
        msg = "FAIL"
    else:
      msg = "CRASH"
    print("!!!!!!" + str(msg) + " " + (m) + " " + str(status))
    return out 
  except:
    raise Exception("")


def BAD():
  print(eg_local["dont.have.this.field"])


def LIST():
  t = {}
  for k in eg_local.items():
    t[1 + len(t)] = k
    t = OrderedDict(sorted(t.items()))
  return t


def ALL(the):
  fails = 0
  for _, v in eg_local["LIST"]().items():
    if (v[0] != "ALL"):
      print("\n---------------------------------")
      if not runs(v[0], the):
        fails = fails + 1
  return True


def LS():
  print("\nExamples lua csv --e...")
  for _, v in eg_local["LIST"]().items():
    print(str(v[0]))
  return True

def SYM():
  print("----SYM TEST CASE-------")
  sym = Sym()
  pairs = ['a','a','a','a','b','b','c']
  for x in pairs:
    sym.add(x)
  mode = sym.mid()
  print("Mode: " + mode)

  entropy = sym.div()
  print("Entropy: " + str(entropy))

def NUM(the):
  print("----NUM TEST CASE-------")
  num = Num(the)
  for i in range(1, 101):
    num.add(i)
  mid = num.mid()
  div = num.div()
  print("Mid: " + str(mid))
  print("Div: " + str(div))

def BIGNUM(the): 
  print("----BIGNUM TEST CASE-------")
  num = Num(the)
  the["nums"] = 32
  for i in range(1, 1001): 
    num.add(i)
  print(num.nums())
  print("Number of numbers: " + str(len(num._has)))

def CSV():
  print("----CSV TEST CASE------")
  n=0
  def fun(row):
    nonlocal n
    n=n+1
    if(n<=10):
      oo_2(row)
    else:
      return
  csv("../data/data.csv", fun)
  return True

def DATA(the):
  print("----DATA TEST CASE------")
  d = Data("../data/data.csv", the)
  for _,col in d.cols.y.items():
     oo(col) 
  return True

def STATS(the):
  print("----STATS TEST CASE------")
  data = Data("../data/data.csv", the)
  div = lambda col: col.div()
  mid = lambda col: col.mid()
  print("xmid", o(data.stats(2, data.cols.x, mid)))
  print("xdiv", o(data.stats(3, data.cols.x, div)))
  print("ymid", o(data.stats(2, data.cols.y, mid)))
  print("ydiv", o(data.stats(3, data.cols.y, div)))


eg_local["BAD"] = BAD
eg_local["LIST"] = LIST
eg_local["ALL"] = ALL
eg_local["LS"] = LS
eg_local["SYM"] = SYM
eg_local["NUM"] = NUM
eg_local["BIGNUM"] = BIGNUM
eg_local["CSV"] = CSV
eg_local["DATA"] = DATA
eg_local["STATS"] = STATS
