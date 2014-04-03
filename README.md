Lsystems in the Raspberry Pi Minecraft
======================================

Interpreta cadenas en forma de reglas L y dibuja sus interacciones en el mundo tridimensinal de Minecraft en la Raspberry Pi


Funcionamiento
--------------
* Si el programa se ejecuta en una computadora conectada a la misma red de la Raspberry:
	Poner la ip de tu raspberry en la linea ("mc = minecraft.Minecraft.create("192.168.1.253") ") al principio de tortuga3D.py
* Si el programa se ejecuta en la propia raspberry:
	Poner "mc = minecraft.Minecraft.create() " al principio de tortuga3D.py
* Ejecutar demos.py


Modulos
-------
* demos.py -> programa de inicio que lanza todos los demos interactivamente , uno tras otro
* Lsystem3D.py -> Interpretador de las cadenas de texto como reglas L
* tortuga3D.py -> programa propio que adapta los movientos de la tortuga de logo a un entorno 3D
* minecraftstuff.py  -> para dibujar figuras geometricas simples 
* math3D.py -> gestiona las operaciones matematicas geometricas en 3D

Creditos
--------
* demos.py y Lsystem3D.py , programas basado en el trabajo de Bernie Pope www.cs.mu.oz.au/~bjpop/ cuyo codigo puede verse en: http://www.berniepope.id.au/html/pycol/lsystem.py.html
* minecraftstuff.py ,programa de Martin O'Hanlon www.stuffaboutcode.com para dibujar en Minecraft Pi
* math3D.py , programa basado en el trabajo de Daniel Bates http://www.cl.cam.ac.uk/~db434/ cuyo codigo fuente se puede ver en: http://www.cl.cam.ac.uk/~db434/files/setblockdemo.py


Licencia
--------
GNU GENERAL PUBLIC LICENSE
Version 2, June 1991
