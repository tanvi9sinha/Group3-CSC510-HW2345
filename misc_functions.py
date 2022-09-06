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