from statistics import median


class Persona:

    # MÉTODO DE INICIALIZACIÓN
    def __init__(self, nom, fn, dom, dni, tel):
        self.nombre = nom
        self.fecha_nacim = fn
        self.domicilio = dom
        self.dni = dni
        self.telefono = tel

    def modificarDomicilio(self, nuevodom):
        pass

    def modificarTelefono(self, nuevotel):
        pass


class Empleado(Persona):
    sueldoBase = 70000

    def __init__(self, nom, fn, dom, dni, tel, cat, leg, cargo, antig):
        super().__init__(nom, fn, dom, dni, tel)
        self.categoría = cat
        self.legajo = leg
        self.extraCargo = cargo
        self.extraAntig = antig

    def calculaSueldo(self):
        print('El sueldo de', self.nombre, 'es de $',
              self.sueldoBase + self.extraAntig + self.extraCargo)


class Paciente(Persona):
    gastoBase = 1000

    def __init__(self, nom, fn, dom, dni, tel, med):
        super().__init__(nom, fn, dom, dni, tel)
        self.especialidad = med

    def calcularGasto(self):
        if self.especialidad == 'odontologia':
            self.gastoBase += 5000
        elif self.especialidad == 'traumatologia':
            self.gastoBase += 10000
        elif self.especialidad == 'oftalmologia':
            self.gastoBase += 7500
        else:
            self.gastoBase += 4000
        return self.gastoBase

    def gastoTotal(self):
        print('el gasto total del paciente',
              self.nombre, 'es: ', self.calcularGasto())


paciente1 = Paciente("pedro", "02/04/1999", "ni idea",
                     "444444", "147258369", 'odontologia')
paciente1.gastoTotal()

paciente2 = Paciente("juan", "02/02/1979", "ni idea",
                     "444444", "3456789", 'psicologia')
paciente2.gastoTotal()

paciente3 = Paciente("marta", "07/05/2009", "ni idea",
                     "445544", "3565164+", 'oftalmologia')
paciente3.gastoTotal()

e1 = Empleado('Juan Pérez', '20/12/1968', 'Aráoz 234 - CABA', '20565412',
              '(011) 4555-5874', 'Ordenanza', 'L-452258', 25000, 65000)
e1.calculaSueldo()

e2 = Empleado('Marta Perz', '01/01/2000', 'por ahi', '12345678',
              '12345', 'ingeniaria', 'L-445566', 20000, 50000)
e2.calculaSueldo()

e3 = Empleado('Fulanito', '12/10/2000', 'en algun lugar', '12345',
              '123456', 'marketing', 'L-22334', 30000, 60000)
e3.calculaSueldo()
