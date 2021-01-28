import wpf

from math import *

from System.Windows import Application, Window

lista_segura = ['math','acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh', 'de grees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh']
dicc_seguro = dict([ (k, locals().get(k, None)) for k in lista_segura ])

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'Newton_Metodo.xaml')
    

if __name__ == '__main__':
    Application().Run(MyWindow())
