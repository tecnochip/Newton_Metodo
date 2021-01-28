#!/usr/bin/python
# coding: latin-1

import Evaluar
from pylab import *
from Numeric import *

def puntofijo(po,TOL, N):
    vectorx = zeros(N, Float64)
    vectory = zeros(N, Float64)

    i = 1
    while i<=N :
        vectorx[i-1] = po
        Evaluar.dicc_seguro['x']=po
        fp = eval(Evaluar.funcion, {"__builtins__":None}, Evaluar.dicc_seguro)
        vectory[i-1]=fp
        if fabs(po-fp)<TOL:
            print "La raiz buscada es: ",po, "con", i-1, "iteraciones"
            break
        i = i+1
        po = fp
    return [vectorx, vectory]

def dibujar(po,TOL, N):
  x = arange(po-2,po+2,0.1)
  vectores=puntofijo(po, TOL, N)

  subplot(211)
  plot(x, eval(Evaluar.funcion), linewidth=1.0)
  xlabel('Abcisa')
  ylabel('Ordenada')
  title('Metodo Punto Fijo con f(x)= x - ' + Evaluar.funcion)
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

