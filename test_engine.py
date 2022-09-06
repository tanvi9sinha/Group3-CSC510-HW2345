from collections import OrderedDict
import random 
from Num import *
from Sym import *

eg = {}
the = {"seed": 2022, "dump": False, "nums": 100}

def pcall(func): 
  try: 
    retval = func()
    return (True, retval)
  except Exception as e: 
    return (False, e)

def runs(k):
  try:
    status = False
    out = False
    if not eg[k]:
      return
    random.seed(the["seed"])
    old = {}
    for key, val in the.items():
      old[key] = val
    
    if (the["dump"] == True):
      status, out = True, eg[k]()
    else:
      status, out = pcall(eg[k])
    for key, val in old.items():
      the[key] = val
    #print(out)
    if status == True:
      if out != False:
        msg = "PASS"
      else:
        msg = "FAIL"
    else:
      msg = "CRASH"
    print("!!!!!!" + str(msg) + " " + (k) + " " + str(status))
    return out 
  except:
    raise Exception("")


def BAD():
  print(eg["dont.have.this.field"])


def LIST():
  t = {}
  for k in eg.items():
    t[1 + len(t)] = k
    t = OrderedDict(sorted(t.items()))
  return t


def ALL():
  fails = 0
  for _, v in eg["LIST"]().items():
    if (v[0] != "ALL"):
      print("\n---------------------------------")
      if (not runs(v[0])):
        fails = fails + 1
  return True


def LS():
  print("\nExamples lua csv --e...")
  for _, v in eg["LIST"]().items():
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

def NUM():
  print("----NUM TEST CASE-------")
  num = Num()
  for i in range(1, 101):
    num.add(i)
  mid = num.mid()
  div = num.div()
  print("Mid: " + str(mid))
  print("Div: " + str(div))

def BIGNUM(): 
  print("----BIGNUM TEST CASE-------")
  num = Num()
  the["nums"] = 32
  for i in range(1, 1001): 
    num.add(i)
  print(num.nums())
  print("Number of numbers: " + str(len(num._has)))

eg["BAD"] = BAD
eg["LIST"] = LIST
eg["ALL"] = ALL
eg["LS"] = LS
eg["runs"] = runs
eg["SYM"] = SYM
eg["NUM"] = NUM
eg["BIGNUM"] = BIGNUM

eg["runs"]("ALL")