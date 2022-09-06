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