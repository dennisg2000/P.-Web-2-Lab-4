def esEscalar(m):
  d = m[0][0]
  for i in range(len(m)):
    for j in range(len(m)):
      if i != j:
        if m[i][j] != 0:
          print(m[i][j])
          return False
      elif m[i][j] != d:
        print(m[i][j])
        return False
  return True

def esUnitaria(m):
  return m[0][0] == 1 and esEscalar(m)

a=[[1,0],[0,1]]

print(esEscalar(a))
print(esUnitaria(a))
