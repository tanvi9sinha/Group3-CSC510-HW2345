def per (t, p = 0.5):
  p = int(p * len(t) + 0.5)
  return t[max(1, min(len(t), p))]

def o(t):
  if type(t) !=  dict:
    return str(t)
  def show(k,v):
    first = k[0]
    if(str(first)!="_"):
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

def oo(t):
  print(o(t))
  #  return t

import re

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

the = {}

def gsub(help):
    pattern = re.compile(r"-[\S+]\s+--[\S+]+\s+[\S+]+\s+=\s[\S+]+", re.IGNORECASE)
    mo = pattern.findall(help)
    for e in mo:
      pattern1 = re.compile(r"-[\S+]\s+--[\S+]+\s+[\S+]+\s+", re.IGNORECASE)
      pattern2 = re.compile(r"=\s[\S+]+", re.IGNORECASE)
      val = pattern2.search(e).group()[2:]
      the[pattern1.search(e).group()] = coerce(val) #passing values to coerce function
    print(the)
gsub(help)

def test_the():
  oo(the)
  return True


def rnd(x, places=2):
  return round(x, places)