#Este programa simula el lenguaje de la tortuga de  logo en las 3 dimensiones de Minecraft

import mcpi.minecraft as minecraft
import mcpi.block as block
import minecraftstuff 
import time
from math3D import *

mc = minecraft.Minecraft.create("192.168.1.3") # <- Put Your ip here
#create drawing object
mcd = minecraftstuff.MinecraftDrawing(mc) 

class Tortuga:
	
	def __init__(self,paso,tipoBloque,tipoTortuga,mostrarTortuga):
        
		self.paso = paso
		self.tipoBloque = tipoBloque
		self.tipoTortuga = tipoTortuga
		self.mostrarTortuga = mostrarTortuga
		#Posicion inicial de la tortuga
		self.posicion = coordinate3d(0,0,0)
		#vector direccion de la tortuga
		self.vectorDireccion = coordinate3d(0,1,0)
		#Modo inicial de la tortuga 
		self.lapizArriba = False
		#Variables para depuracion
		self.pausaSegundos = 0
		self.intervaloIteraciones = 0
		self.contadorIteraciones = 0
		self.trazando  = False
      
      
	def hideturtle(self):
		self.mostrarTortuga = False

	def showturtle(self):
		self.mostrarTortuga = True	
		
	def up(self):
		self.lapizArriba = True
	
	def down(self):
		self.lapizArriba = False
	
	def initDirection(self):
		#vector direccion de la tortuga
		self.vectorDireccion = coordinate3d(0,1,0)
		
	def setDirection(self,x,y,z):
		#vector direccion de la tortuga
		self.vectorDireccion = coordinate3d(x,y,z)
	
	def position(self):
		return (self.posicion.x, self.posicion.y,self.posicion.z)
	
	def setheading(self,alpha, beta, gamma):
		""" Pone al vector direccion mirando en la direccion marcada por los angulos 
		alpha (con el eje x), beta (con el eje y) y gamma (con el eje z) """
		#Actualiza el vector direccion
		self.setDirection(cos(radians(alpha)),cos(radians(beta)),cos(radians(gamma)))
	
	def heading(self):
		return (degrees(acos(self.vectorDireccion.x)), 
				 degrees(acos(self.vectorDireccion.y)), 
				 degrees(acos(self.vectorDireccion.z)))
	
	def rotaDireccion(self,pitchAngle,yawAngle,rollAngle):
		self.vectorDireccion = rotationx(pitchAngle)*(rotationy(yawAngle)*(rotationz(rollAngle) * self.vectorDireccion))
	
	def yaw(self,angle):
		self.rotaDireccion(0 ,angle,0)
		
	def pitch(self, angle):
		self.rotaDireccion(angle, 0,0)
	
	def roll(self, angle):
		self.rotaDireccion(0, 0,angle)
		
	def goto(self,px,py,pz):
		
		#Borra la tortuga de su anterior posicion
		mc.setBlock(self.posicion.x,self.posicion.y,self.posicion.z,self.tipoBloque)
		#Cambia la posicion
		self.posicion = coordinate3d(px, py,pz)
		if self.mostrarTortuga :
			mc.setBlock(px,py,pz,self.tipoTortuga)
		if self.trazando:
			self.goTracer()
       
	def forward(self,distancia):
		 
		nuevaPos = self.posicion + self.vectorDireccion * distancia 
		
		if not self.lapizArriba: #Si el lapiz no esta arriba pinta una linea desde la antigua posicion a la nueva
			 mcd.drawLine( int(self.posicion.x), int(self.posicion.y), int(self.posicion.z), 
						   int(nuevaPos.x), int(nuevaPos.y), int(nuevaPos.z), self.tipoBloque)
		
		#Borra la tortuga de su anterior posicion
		mc.setBlock(self.posicion.x,self.posicion.y,self.posicion.z,self.tipoBloque)
		#La dibuja en la nueva
		if self.mostrarTortuga :
			mc.setBlock(nuevaPos.x,nuevaPos.y,nuevaPos.z,self.tipoTortuga)
		
		self.posicion = nuevaPos 
			
		if self.trazando:
			self.goTracer()
		
		
	## Funciones de depuracion de la tortuga

	def tracer(self, numIteraciones,segundos):
		# Muestra las posicion de la tortuga cada num de iteraciones con un retraso de los segundos marcados
		self.trazando = True
		self.intervaloIteraciones = numIteraciones
		self.pausaSegundos = segundos
		
	def goTracer(self):
		
		self.contadorIteraciones += 1
		
		if self.contadorIteraciones >= self.intervaloIteraciones:
			time.sleep(self.pausaSegundos)
			self.contadorIteraciones = 0
			print "angulos: " + str(self.heading()),  "posicion: " + str(self.posicion)
	

		
def setup(vectorDireccion=(0,1,0)):

	tortuga = Tortuga(4,block.LEAVES ,block.NETHER_REACTOR_CORE,False)
	tortuga.vectorDireccion = coordinate3d(vectorDireccion[0],vectorDireccion[1],vectorDireccion[2])
	tortuga.down()
	
	#Limpia el escenario
	mc.setBlocks(-100,-50,-50, 100, 50, 50,block.AIR)
	#Pone a el jugador cerca del origen
	mc.player.setTilePos(0,-40,-18) 
	#Muestra la tortuga
	mc.setBlock(0,0,0,tortuga.tipoTortuga)

	return tortuga
		 
if __name__ == "__main__":
    
    t = setup()
    t.tracer(1,1)
     
    #Imprime los ejes de coordenadas
    #Eje z
    print t.heading()
    t.goto(0,-40,0)
    t.setDirection(0,0,1)
    t.forward(4)
    #Eje y
    t.goto(0,-40,0)
    t.setDirection(0,1,0)
    t.forward(4)
    #Eje x
    t.goto(0,-40,0)
    t.setDirection(1,0,0)
    t.forward(4)
    
    
    
