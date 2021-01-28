#!/usr/bin/python
# coding: latin-1

import Evaluar
from pylab import *
from Numeric import *

def secante(po, p1, TOL, N):
    Evaluar.dicc_seguro['x']=po
    qo = eval(Evaluar.funcion, {"__builtins__":None}, Evaluar.dicc_seguro)
    Evaluar.dicc_seguro['x']=p1
    q1 = eval(Evaluar.funcion, {"__builtins__":None}, Evaluar.dicc_seguro)
    vectorx = zeros(N, Float64)
    vectorx1 = zeros(N, Float64)
    vectory = zeros(N, Float64)
    vectory1 = zeros(N, Float64)

    i = 2
    while i<=N :
        p = p1-(q1*(p1-po)/(q1-qo))
        vectorx[i-2] = po
        vectorx1[i-2] = p1
        Evaluar.dicc_seguro['x']=p
        fp = eval(Evaluar.funcion, {"__builtins__":None}, Evaluar.dicc_seguro)
        vectory[i-2]=qo
        vectory1[i-2]=q1
        if fabs(po-p1)<TOL :
            print "La raiz buscada es: ",p, "con", i-2,"iteraciones"
            break

        i = i+1
        po = p1
        qo = q1
        p1 = p
        q1 = fp

    return [vectorx, vectory, vectorx1, vectory1]

def dibujar(po, p1, TOL, N):
  x = arange(po-2,po+2,0.1)
  vectores=secante(po, p1, TOL, N)

  subplot(211)
  plot(x, eval(Evaluar.funcion), linewidth=1.0)
  xlabel('Abcisa')
  ylabel('Ordenada')
  title('Metodo Secante con f(x)= ' + Evaluar.funcion)
  grid(True)
  axhline(linewidth=1, color='r')
  axvline(linewidth=1, color='r')

  subplot(212)
  plot(vectores[0], vectores[1], 'r.', vectores[2], vectores[3], 'b.')
  xlabel('Abcisa')
  ylabel('Ordenada')
  grid(True)
  axhline(linewidth=1, color='r')
  axvline(linewidth=1, color='r')

  show()

