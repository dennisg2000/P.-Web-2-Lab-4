def esUnitaria(m):
  return m[0][0] == 1 and esEscalar(m)


a=[[1,0,0],
  [0,1,0],
  [0,0,1]]

print(esUnitaria(a))