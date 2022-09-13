import sys
import re
from csv import reader

the = {"seed": 2022, "dump": False, "nums": 100}

def csv(fname, fun):
  sep = "([^" + "\," + "]+" # Replace comma with the.separator!
  with open(fname) as file_obj:
    reader_obj = reader(file_obj)
    for row in reader_obj:
      t = {}
      for element in row:
        t[str(1 + len(t))] = coerce(element)
      fun(t)
      
def per (t, p = 0.5):
  p = int(p * len(t) + 0.5)
  return t[max(1, min(len(t), p))]


def o(t):
  if (type(t) !=  dict and type(t).__module__ == "__builtin__"):
    return str(t)
  if(type(t).__module__ != "__builtin__" and type(t) != dict):
    newDictionary = (vars(t))
    newDictionary.pop('_has')
    return newDictionary

  print(t)
  def show(k,v):
    first = k[0]
    if(str(first)!="_"):
      if(type(v) == dict):
        v = o(v)
        if(len(t) == 0):
          return ":"+str(k)+str(v)
        else:
          return str(v)
  u={}
  for k,v in t.items():
    u_len = len(u)
    u[k] = show(k,v)
  if len(t)==0:
    u = sorted(u)
  output = ""
  for key in u:
    output = output + ":" + key + " " + str(u[key]) + " "
  return "{" + output + "}"

def o_2(t):
  if type(t) !=  dict and type(t).__module__ == "__builtin__":
    return str(t)

  if(type(t).__module__ != "__builtin__" and type(t) != dict):
    newDictionary = (vars(t))
    newDictionary.pop('_has')
    return newDictionary

  def show(k,v):
    first = k[0]
    if(str(first)!="_"):
      if(type(v) == dict): 
        v = o_2(v)
        if(len(t) == 0):
          return ":"+str(k)+str(v)
        else:
          return str(v)
      else:
        return str(v)
  u={}
  for k,v in t.items():
    u_len = len(u)
    u[k] = show(k,v)
  if len(t)==0:
    u = sorted(u)
  output = "{"
  for key in u:
    output = output+str(u[key])+" "
  output = output+"}"
  return output

def oo_2(t):
   print(o_2(t)) 
   return t

def oo(t):
   print(o(t)) 
   return t

help = """ 
 CSV : summarized csv file
(c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license

 USAGE: lua seen.lua [OPTIONS]
 OPTIONS
 -e  --eg        start-upexample                      = nothing
 -d  --dump      ontestfailure,exitwithstackdump = false
 -f  --file      filewithcsvdata                    = ../data/auto93.csv
 -h  --help      show help                             = false
 -n  --nums      numberofnumstokeep                = 512
 -s  --seed      randomnumberseed                    = 10019 
 -S  --seperator feildseperator                       = , """


def coerce(s):
  def fun(s1):
    if s1 == "true":
      print("here")
      return True
    elif s1 == "false":
      return False
    else:
      return s1

  if s.isnumeric():
    return int(s)
  else:
    return fun(re.search('^[\s]*[\S+]*[\s]*$', s).group(0))


# def gsub(help):
#     pattern = re.compile(r"-[\S+]\s+--[\S+]+\s+[\S+]+\s+=\s[\S+]+", re.IGNORECASE)
#     mo = pattern.findall(help)
#     for e in mo:
#       pattern1 = re.compile(r"-[\S+]\s+--[\S+]+\s+[\S+]+\s+", re.IGNORECASE)
#       pattern2 = re.compile(r"=\s[\S+]+", re.IGNORECASE)
#       val = pattern2.search(e).group()[2:]
#       the[pattern1.search(e).group()] = coerce(val) #passing values to coerce function
#     print(the)
# gsub(help)

# def test_the():
#   oo(the)
#   return True


def rnd(x, places=2):
  return round(x, places)

def copy(t):
  if(type(t)!= "dict"):
    return t
  u = {}
  for k, v in t.items():
    u[k] = copy(v)
  return u

def push(t, x):
  t[1 + len(t)] = x
  return x

