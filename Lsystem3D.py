'''
Bernie's L System demo in Python.

This program implements a simple context free L System,
and renders two dimensional images in a window.
It needs (at least) python 2.6, and uses the turtle 
graphics library, which is based on TK graphics.

To try it out, either load into Python and run the 
demo functions, or run it from the command line:
  
   python lsystem.py

Author: Bernie Pope: www.cs.mu.oz.au/~bjpop/
Licence: unrestricted.

Feel free to play with the code as much as you like
and share your changes with the world.

Some remarks about the implementation:

An L-System is a term rewriting system made up of one or
more rules. Rules have the form:

   head -> body

where head is a variable, and body is a non-empty string
made up of variables and constants. Variables are 
denoted by upper-case alphabetic letters. Constants
are denoted by any character which is not a variable.

Here is an example L-System: 

   X -> F-[[X]+X]+F[+FX]-X
   F -> FF

In this program the convention is that the first rule
is taken as the starting point.

An LSystem object is constructed like so:

   rules = ['X -> F-[[X]+X]+F[+FX]-X', 'F -> FF'] 
   my_system = LSystem(rules)

That is, the LSystem constructor takes a list of strings
as its argument, where each string is a single rule.

An LSystem object doesn't do anything on its own - it must
be interpreted.

LSystem objects have a run method which takes two parameters:
   1) An non-negative integer which indicates how many times
      the rules should be iterated. 
   2) An interpreter object which implements an 'interpretTokens' 
      method.

Here is a simple example:

  class SimpleInterp(object):
     def interpretTokens(self, tokens): return tokens

  answer = my_system().run(6, SimpleInterp())

A more sophisticated interpreter is defined called Visualise
which renders the result of iterating an LSystem as turtle
graphics.

The Visualise constructor takes a dictionary mapping LSystem
variables to functions, here is an example:

   { '-': lambda _ : rollLess(rollLess_angle)
   , '+': lambda _ : right(right_angle)
   , 'F': lambda _ : forward(fwd_distance)
   , '[': lambda obj : obj.push()
   , ']': lambda obj : obj.pop()
   }

'''
import sys
from tortuga3D import *
from collections import deque

tortuga = setup()

# Configuration of graphics window
def initDisplay():
	tortuga.showturtle()
    # Codigo para depuracion
    #tracer(1,1) # Dibuja una iteracion cada segundo.
    #hideturtle() # don't draw the turtle; increase drawing speed.

def initPosition(x,y,z):

   tortuga.up() 
   tortuga.goto (x, y,z)
   tortuga.down()


class LSystem(object):
   def __init__ (self, rules):
      if len(rules) > 0:
         for r in rules:
            exec(compile(r)) in locals()
         firstRuleName,_ = decomposeRule(rules[0])
         exec('def start(n): return ' + firstRuleName + '(n)') in locals()
         self.rule = start
      else:
         self.rule = lambda _ : ''
   def run(self, maxIterations, interpreter):
      return interpreter.interpretTokens(self.rule(maxIterations))

class Visualise (object):
   def __init__(self, dict, initCommand=None):
	  self.actions = dict
	  self.initCommand = initCommand
	  self.stack_pos = deque()
	  self.stack_orient = deque()

   def interpretTokens(self, tokens):
      initDisplay()
      if self.initCommand != None: self.initCommand()
      def action_fun(token):
         return self.actions.get(token, lambda _ : None)(self)
      self.stack_pos = deque() 
      self.stack_orient = deque()
      map (action_fun, tokens)

   def push(self):
      orient = tortuga.heading()
      pos = tortuga.position()
      self.stack_pos.append(pos)
      self.stack_orient.append(orient)

   def pop(self):
      stack_pos = self.stack_pos
      stack_orient = self.stack_orient
      if len(stack_pos) == 0 or  len(stack_orient) == 0:
         raise Exception('Attempt to pop empty stack')
      pos   = stack_pos.pop()
      orient   = stack_orient.pop()
      tortuga.up()
      tortuga.goto(pos[0],pos[1],pos[2]) 
      tortuga.setheading(orient[0],orient[1],orient[2])
      tortuga.down()
      
def basic_actions (left_angle, right_angle, fwd_distance):
   return { '-': lambda _ : tortuga.roll(left_angle)
          , '+': lambda _ : tortuga.roll(-right_angle)
          , '|': lambda _ : tortuga.roll(180)
          , '^': lambda _ : tortuga.yaw(left_angle)
          , '&': lambda _ : tortuga.yaw(-right_angle)
          , '}': lambda _ : tortuga.pitch(-left_angle)
          , '{': lambda _ : tortuga.pitch(right_angle)
          , 'F': lambda _ : tortuga.forward(fwd_distance)
          , '[': lambda obj : obj.push()
          , ']': lambda obj : obj.pop()
          }
          
def basic_actions2 (left_angle, right_angle, fwd_distance):
   return { '-': lambda _ : tortuga.yaw(-left_angle)
          , '+': lambda _ : tortuga.yaw(left_angle)
          , '^': lambda _ : tortuga.pitch(-left_angle)
          , '&': lambda _ : tortuga.pitch(right_angle)
          , '>': lambda _ : tortuga.roll(-left_angle)
          , '<': lambda _ : tortuga.roll(right_angle)
          , 'F': lambda _ : tortuga.forward(fwd_distance)
          , '[': lambda obj : obj.push()
          , ']': lambda obj : obj.pop()
          }



'''
The input rule:
 
   X -> X+X+F

is compiled to:

   def X(n): 
       if n > 0:
          xn = X(n-1)
          fn = F(n-1)
          return ''.join([xn,'+',xn,'+',fn])
       else:
          return 'X'
'''

def compile(rule):
   (name, body) = decomposeRule(rule)
   (vars,listIds) = varsIds(body)
   defPart = 'def ' + name + '(n):'
   varBinds = list(map(mkVarBind,vars))
   joinListPart = "''.join([" + ','.join(listIds) + '])'
   ifHead = 'if n > 0:' 
   ifBody = varBinds + ['return ' + joinListPart]
   elsePart = 'else: return ' + quote(name)
   return '\n'.join(
      [defPart] + map(indent,
         [ifHead] + map(indent,
            ifBody) + [elsePart]))

def decomposeRule(rule):
   splitRule = rule.split('->')
   if len(splitRule) != 2:
      raise Exception("badly formed L-System rule: " + quote(str(rule)))
   name = splitRule[0].strip()
   body = splitRule[1].strip()
   if len(name) != 1 or len(body) == 0:
      raise Exception("badly formed L-System rule: " + quote(str(rule)))
   return (name, body)

def mkVarBind(var):
   return var.lower() + 'n = ' + var + '(n-1)'

def quote(str): return "'" + str + "'"

def indent(str): return '   ' + str

def varsIds(str):
   vars = set()
   list = []
   for c in str:
      if c.isupper():
         vars.add(c)
         list.append(c.lower()+'n')
      else:
         list.append(quote(c))
   return (vars, list)

