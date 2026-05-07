#nombre/identificador de la clase
#class es palabra reservada
class Coche:
    """Docstring: Esta clase define el estado y el comportamiento de un coche"""
    #atributos de clase
    ruedas=4
    #constructor
    def __init__(self,color,aceleracion):
        #atributos de instancia
        self.color= color
        self.aceleracion=aceleracion
        self.velocidad=0
    #métodos
    def acelera(self):
        self.velocidad=self.velocidad+self.aceleracion
    def frena(self):
        v=self.velocidad - self.aceleracion
        if v<0:
            v=0
        self.velocidad=v

        # crear objeto
mi_coche = Coche("rojo", 10)

# acelerar
mi_coche.acelera()
print(mi_coche.velocidad)  # 10

# volver a acelerar
mi_coche.acelera()
print(mi_coche.velocidad)  # 20

# frenar
mi_coche.frena()
print(mi_coche.velocidad)  # 10

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#la clase CocheVolador hereda de la clase Coche
class CocheVolador(Coche):
    ruedas = 6
    def __init__(self, color, aceleracion, esta_volando=False):
        # la función super(). Esta función devuelve un objeto temporal de la superclase que permite invocar a los métodos definidos en la misma.
        super().__init__(color, aceleracion)
        #se crea el atributo de instancia esta_volando solo para objetos de la clase CocheVolador.
        self.esta_volando = esta_volando

    def vuela(self):
        self.esta_volando = True

    def aterriza(self):
        self.esta_volando = False

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

class A:
    def __init__(self):
        self._contador = 0  # Este atributo es privado
    def incrementa(self):
        self._contador += 1
    def cuenta(self):
        return self._contador

class B(object):
    def __init__(self):
        self.__contador = 0  # Este atributo es privado
    def incrementa(self):
        self.__contador += 1
    def cuenta(self):
        return self.__contador
a = A()
a.incrementa()
a.incrementa()
a.incrementa()
print(a.cuenta()) #3
print(a._contador) #3

b = B()
b.incrementa()
b.incrementa()
print(b.cuenta())
print(b._B__contador)