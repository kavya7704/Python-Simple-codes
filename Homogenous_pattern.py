s = input()
def homogenous(s)
  layersize = 1
  count = 0
  i = 0
  
  while i + layersize <= len(s):
      
      layer = s[i:i+layersize]
      print(layer)
      if (len(set(layer))) == 1:
          count += 1
      i += layersize
      layersize += 1
  return count

print(homogenous(s))
