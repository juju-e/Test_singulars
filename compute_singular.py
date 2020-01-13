import numpy.linalg as lin
def is_singular(mat):
  return round(lin.det(mat))==0
def is_regular(mat):
  return round(lin.det(mat))!=0

