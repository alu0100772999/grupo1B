#! /usr/bin/python
import matplotlib.pyplot as pl
import numpy as np
from math import *


def funcion():
   fuction = np.log1p(6*x1)
   return fuction
   
def lagrange(a,b):
   aux = 0
   aux = float((b-a)/(log1p(b)-log1p(a)))
   return aux 



if __name__ =='__main__':
   print '\n\nCalculo de los puntos vaticinados en el teorema de Larange \n'
   print '  ->TEOREMA: \n'
   print '  Sea f una funcion continua en [a,b] y derivable en (a,b), \n entonces existe un punto c contenido en (a,b) tal que: \n\n f`(c)=(f(b)-f(a))/(b-a)\n'
   print ' *Consideremos la funcion f(x)=ln(6x), estudiemos los puntos vaticinados en el teorema\n para un intervalo I = [a,b]: '
   print ' \nSi f(x)=ln(6x), entonces f`(x) = 1/x ' 
   print ' Evaluamos (f(b)-f(a))/(b-a) en I, y obtenemos que'
   
   a = int(raw_input('Introduzca un valor de a : '))
   b = int(raw_input('Introduzca un valor de b : '))
   
   c = lagrange(a,b)
   print 'El punto vaticinado en el Teorema para un intervalo [{0},{1}], de la funcion es c = {2} \n\n'.format(a,b, lagrange(a,b))
   
   
   opc = int(raw_input(' Desea un grafico ? \n 1 = Si\n 0 =No\n'))
   if(opc==1):
     if(a<b):
       x1 = np.arange(a,b,0.1)
       y1 = funcion()
       x2 = c
       y2 = np.log1p(6*x2)
       pl.plot(x1,y1,'r')
       pl.plot(x2,y2,'d')
       pl.show()
     else:
       print'El valor de a debe ser menor que b'
   else:
     print' Adios '