''' Programa basado en el trabajo de Daniel Bates http://www.cl.cam.ac.uk/~db434/
cuyo codigo fuente se puede ver en: http://www.cl.cam.ac.uk/~db434/files/setblockdemo.py '''


from math import sin, cos, radians,degrees, sqrt, pow , acos

class coordinate3d:
  """Class used to represent a point in 3D space."""
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z

  def __add__(self, other):
    return coordinate3d(self.x+other.x, self.y+other.y, self.z+other.z)
    
  def __mul__(self, other):
	  #Multiplicacion por un escalar
	  return coordinate3d(self.x*other, self.y*other, self.z*other)
  
  def __str__(self):
	  return str([self.x, self.y, self.z])	  
	  
  def modulo(self):
	  return sqrt(pow(self.x,2)+pow(self.y,2)+pow(self.z,2))


class transformation:
  """Representation of homogeneous matrices used to apply transformations to
coordinates - using a 4x4 matrix allows shifts as well as scales/rotations.
Transformations can be combined by multiplying them together."""
  def __init__(self, matrix):
    self.matrix = matrix

  def __mul__(self, other):
    if isinstance(other, transformation):
      return self.compose(other)
    elif isinstance(other, coordinate3d):
      return self.apply(other)
    else:
      print "Can't multiply transformation by {0}".format(type(other))

  def compose(self, other):
    """Compose this transformation with another, returning a new transformation."""
    newmatrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
      for j in range(4):
        for k in range(4):
          newmatrix[i][k] += self.matrix[i][j]*other.matrix[j][k]
    return transformation(newmatrix)

  def apply(self, point):
    """Apply this transformation to a coordinate, returning a new coordinate."""
    return coordinate3d(
        self.matrix[0][0]*point.x + self.matrix[0][1]*point.y + self.matrix[0][2]*point.z + self.matrix[0][3],
        self.matrix[1][0]*point.x + self.matrix[1][1]*point.y + self.matrix[1][2]*point.z + self.matrix[1][3],
        self.matrix[2][0]*point.x + self.matrix[2][1]*point.y + self.matrix[2][2]*point.z + self.matrix[2][3])
      
      
## Transformation functions

def identity():
  return transformation([[1,0,0,0],
                         [0,1,0,0],
                         [0,0,1,0],
                         [0,0,0,1]])

def shift(x,y,z):
  """Move by a given offset."""
  return transformation([[1,0,0,x],
                         [0,1,0,y],
                         [0,0,1,z],
                         [0,0,0,1]])

def rotationx(angle):
  """Rotate about the x axis by the given number of degrees."""
  angle = radians(angle)
  return transformation([[1,           0,          0, 0],
                         [0,  cos(angle), sin(angle), 0],
                         [0, -sin(angle), cos(angle), 0],
                         [0,           0,          0, 1]])

def rotationy(angle):
  """Rotate about the y axis by the given number of degrees."""
  angle = radians(angle)
  return transformation([[ cos(angle), 0, sin(angle), 0],
                         [          0, 1,          0, 0],
                         [-sin(angle), 0, cos(angle), 0],
                         [          0, 0,          0, 1]])

def rotationz(angle):
  """Rotate about the z axis by the given number of degrees."""
  angle = radians(angle)
  return transformation([[ cos(angle), sin(angle), 0, 0],
                         [-sin(angle), cos(angle), 0, 0],
                         [          0,          0, 1, 0],
                         [          0,          0, 0, 1]])


