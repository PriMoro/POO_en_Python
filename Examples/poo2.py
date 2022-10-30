class Ascensor:
    # CARGAMOS LOS ATRIBUTOS COMUNES A TODOS LOS ASCENSORES DEL EDIFICIO
    pesoMax = 400
    pisoMin = -1
    pisoMax = 18

    # CARGAMOS LOS ATRIBUTOS ESPECÍFICOS POR MÉTODO CONSTRUCTOR
    def __init__(self, d, u, c):
        self.denominacion = d
        self.ubicacion = u
        self.cargaActual = c

    def chequear(self):
        if self.cargaActual <= self.pesoMax:
            habilitado = True
        else:
            habilitado = False
            print(self.denominacion, 'con sobrecarga de',
                  self.cargaActual - self.pesoMax, 'kg!')
        print(habilitado)
        return habilitado

    def modificarCarga(self, peso):
        self.cargaActual += peso
        print('Carga actual de', self.denominacion,
              ':', self.cargaActual, 'kg.')

    def moverse(self, piso):
        if self.chequear():
            print(self.denominacion, 'inicia recorrido en el piso', self.ubicacion)
            self.ubicacion = piso
            print(self.denominacion,
                  'detiene su recorrido en el piso', self.ubicacion)


ascensor1 = Ascensor("ascensor1", 0, 0)
ascensor1.chequear()
ascensor1.moverse(3)
ascensor1.modificarCarga(70)
ascensor1.chequear()

print("--------")

ascensor2 = Ascensor("ascensor2", 10, 150)
ascensor2.chequear()
ascensor2.moverse(2)
ascensor2.modificarCarga(80)
ascensor2.chequear()

print("--------")

ascensor3 = Ascensor("ascensor3", 5, 200)
ascensor3.chequear()
ascensor3.moverse(2)
ascensor3.modificarCarga(300)
ascensor3.chequear()

#a1 = Ascensor('Unidad A', 10, 230)
#a2 = Ascensor('Unidad B', 0, 455)
#a3 = Ascensor('Unidad C', 5, 198)
# a1.moverse(13)
# a2.moverse(10)
# a2.modificarCarga(-90)
# a2.moverse(10)
# a3.moverse(-1)
