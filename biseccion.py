#!/usr/bin/python
# coding: latin-1

import Evaluar
from pylab import *
from Numeric import *

def biseccion(a, b, TOL, N):
    Evaluar.dicc_seguro['x']=a
    fa = eval(Evaluar.funcion, {"__builtins__":None}, Evaluar.dicc_seguro)
    vectorx = zeros(N, Float64)
    vectory = zeros(N, Float64)

    i = 1
    while i<=N :
        p = (a+b)/2.0
        vectorx[i-1] = p
        Evaluar.dicc_seguro['x']=p
        fp = eval(Evaluar.funcion, {"__builtins__":None}, Evaluar.dicc_seguro)
        vectory[i-1]=fp
        if (fp == 0.0) or ( (b-a)/2.0)<TOL:
            break
        i = i+1
        if (fa*fp)>0 :
            a = p
        else :
            b = p
    print "La raiz buscada es: ",p, "con", i-1,"iteraciones"
    return [vectorx, vectory]

def dibujar(a,b,TOL, N):
  x = arange(a,b,0.1)
  vectores=biseccion(a, b, TOL, N)

  subplot(211)
  plot(x, eval(Evaluar.funcion), linewidth=1.0)
  xlabel('Abcisa')
  ylabel('Ordenada')
  title('Metodo Biseccion con f(x)=' + Evaluar.funcion)
  grid(True)
  axhline(linewidth=1, color='r')
  axvline(linewidth=1, color='r')

  subplot(212)
  plot(vectores[0], vectores[1], 'k.')
  xlabel('Abcisa')
  ylabel('Ordenada')
  grid(True)
  axhline(linewidth=1, color='r')
  axvline(linewidth=1, color='r')

  show()

