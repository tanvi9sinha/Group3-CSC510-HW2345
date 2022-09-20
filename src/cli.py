import sys
import re

help = """ 
 CSV : summarized csv file
(c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license

 USAGE: lua seen.lua [OPTIONS]
 OPTIONS
 -e  --eg        start-up example                      = nothing
 -d  --dump      on test failure, exit with stack dump = false
 -f  --file      file with csv data                    = ../data/auto93.csv
 -h  --help      show help                             = false
 -n  --nums      number of nums to keep                = 512
 -s  --seed      random number seed                    = 10019 
 -S  --seperator feild seperator                       = , """

def gsub(the, help):
    for k, x in re.findall('\n [-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)', help):
        the[k] = coerce(x)
    return the
def coerce(s):
  def fun(s1):
    if s1 == "true":
      return True
    elif s1 == "false":
      return False
    else:
      return s1

  if s.isnumeric():
    return int(s)
  else:
    return fun(re.search('^[\s]*[\S+]*[\s]*$', s).group(0))

def cli_func(command_line):
  the = {}
  the = gsub(the, help)
  for slot,v in the.items():
      v = str(v)
      for i, x in enumerate(command_line):
          if x=="-"+slot[0] or x=="--"+slot :
            if v == "false":
                v = "true"
            elif v == "true":
                v = "false"
            else:
                v = command_line[i+1]
            the[slot] = coerce(v)
  if the["help"]: exit (print("\n" + str(help) + "\n"))

  return the



