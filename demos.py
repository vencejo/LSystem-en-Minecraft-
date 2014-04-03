from Lsystem3D import *

# Some demo functions, which make it relatively easy to use

def interactive_demo():
   def show_demo(name, action):
      print(name)
      action()
      input = raw_input("Press any key to continue or q/Q to quit: ")
      if input.lower() == 'q':
         sys.exit(0)
  
   show_demo("Pruebas Simples",demo_i)
   show_demo("Bushy tree", demo1)
   show_demo("Twiggy tree", demo2)
   show_demo("Peano Gosper curve", demo5)
   show_demo("Conifer-like tree", demo6)
   show_demo("Tiles", demo7)
   show_demo("Cristal", demo8)
   show_demo("Peano curve", demo9)
   show_demo("Hilbert curve", demo10)
   show_demo("Hilbert 3D v2", demo11)
  

def demo_i():
   def init():
      initPosition(0,-45,0)
   vis = Visualise(basic_actions(60,60,2), init)
   basico().run(4,vis)

def basico():
    return LSystem(['A -> FFFFFFFFX ',   
                     'X -> [+FFFFY][-FFFFY]',
                     'Y -> [+FFY][-FFY]',
                     'F -> F']) 
def demo1():
   def init():
      initPosition(0,-50,0)
   vis = Visualise(basic_actions(25,25,5), init)
   bushy_tree().run(5,vis)

def bushy_tree():
    return LSystem(['F -> [FF-[-F+F+F]+[+F-F-F]] FF{[{F}F}F]}[}F{F{F]'])  # Regla en 1D: 'F -> FF-[-F+F+F]+[+F-F-F]'

def demo2():
   def init():
      initPosition(0,-45,0)
   vis = Visualise(basic_actions(25,25,2), init)
   twiggy_tree().run(4,vis)

def twiggy_tree():
    rules = ['X -> F-[[X]+X]+F[+FX]-X F{[[X]}X]}F[}FX]{X', 'F -> FF'] 
    return LSystem(rules)


def demo5():
   def init():
      initPosition(lambda width, height : (width/4, 3*height/8))
   actions = basic_actions(60,60,4)
   vis = Visualise(actions, init)
   peano_gosper().run(5,vis)


def demo5():
   def init():
      initPosition(0,0,0)
   actions = basic_actions(60,60,4)
   vis = Visualise(actions, init)
   peano_gosper().run(3,vis)

def peano_gosper():
   rules = [ 'X -> X+YF++YF-FX--FXFX-YF+'
           , 'Y -> -FX+YFYF++YF+FX--FX-Y'
           , 'F -> F' ]
   return LSystem(rules)

def demo6():
   def init():
      initPosition(0,-50,0)
   actions = basic_actions(20,20,11)
   vis = Visualise(actions, init)
   conifer().run(5,vis)
   
def conifer():
   rules = [ 'I -> VZFFF'
           , 'V -> [[+++W][---W]YV][}}}W][{{{W]YV '
           , 'W -> [+X[-W]Z]}X[{W]Z'
           , 'X -> [-W[+X]Z]{W[}X]Z'
           , 'Y -> [YZ]YZ'
           , 'Z -> [[-FFF][+FFF]F][{FFF][}FFF]F'
           , 'F -> F' ]
   return LSystem(rules)

def demo7():
   def init():
      initPosition(0,0,0)
   actions = basic_actions(90,90,4)
   vis = Visualise(actions, init)
   tiles().run(4,vis)

def tiles():
   rules = [ 'I -> [F+F+F+F]F}F}F}F'
           , 'F -> [FF+F-F+F+FF]FF}F{F}F}FF' ]
   return LSystem(rules)
   
def demo8():
   def init():
      initPosition(0,-45,0)
   actions = basic_actions(90,90,4)
   vis = Visualise(actions, init)
   crystal().run(4,vis)

def crystal():
   rules = ['I -> [F+F+F+F] F}F}F}F', 
            'F -> [FF+F++F+F] FF}F}}F}F']
   return LSystem(rules)

def demo9():
   def init():
      initPosition(0,-50,0)
      tortuga = setup()
      tortuga.roll(-90)
   actions = basic_actions(90,90,2)
   vis = Visualise(actions, init)
   peano_curve().run(4,vis)

def peano_curve():
   rules = [ 'X -> XFYFX+F+YFXFY-F-XFYFX'
           , 'Y -> YFXFY-F-XFYFX+F+YFXFY'
           , 'F -> F' ]
   return LSystem(rules)
   
def demo10():
   def init():
      initPosition(0,-40,0)
      tortuga = setup()
      tortuga.roll(90)
   actions = basic_actions(90,90,2)
   vis = Visualise(actions, init)
   hilbert().run(5,vis)

def hilbert():
   rules = [ 'A -> -BF+AFA+FB-','B -> +AF-BFB-FA+', 'F -> F']
   return LSystem(rules)
   

def demo11():
   def init():
      initPosition(0,-45,0)
      #tracer(1,1)
     
   actions = basic_actions2(90,90,6)
   vis = Visualise(actions, init)
   hilbert3d().run( 5,vis)


def hilbert3d():
   rules = [ 'X -> ^ < X F ^ < X F X - F ^ > > X F X & F + > > X F X - F > X - >',  # ^ < X F ^ < X F X - F ^ > > X F X & F + > > X F X - F > X - >
             'F -> F']
   return LSystem(rules)
   

   
if __name__ == "__main__":
   interactive_demo() 

