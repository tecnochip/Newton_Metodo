
#!/usr/bin/python
# coding: latin-1

import Evaluar
from pylab import *
from Numeric import *

def newton(df, po, TOL, N):

    i = 1
    vectorx = zeros(N, Float64)
    vectory = zeros(N, Float64)

    while i<=N:

        vectorx[i-1] = po
        Evaluar.dicc_seguro['x'] = po
        f  = eval(Evaluar.funcion, {"__builtins__":None}, Evaluar.dicc_seguro)
        df_val = eval(df, {"__builtins__":None}, Evaluar.dicc_seguro)

        vectory[i-1] = f

        if df_val == 0:
            print "La evaluacion de la derivada de la funcion dio 0"
            break

        p1 = po - (f/df_val)

        if fabs(po-p1) < TOL:
            print "La raiz buscada es: ",po, "con", i-1,"iteraciones"
            break

        i += 1
        po = p1

    return [vectorx, vectory]

def dibujar(df, po, TOL, N):

  x = arange(po-2,po+2,0.1)
  vectores = newton(df, po, TOL, N)

  subplot(211)
  plot(x, eval(Evaluar.funcion), linewidth=1.0)
  xlabel('Abcisa')
  ylabel('Ordenada')
  title('Metodo Newton con f(x)=' + Evaluar.funcion)
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
