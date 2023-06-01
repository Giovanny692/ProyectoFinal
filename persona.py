#este archivo maneja empleados y personas

class Persona():
  def __init__(self,hora_entrada,hora_salida,id,nombre,placa):
    self.hora_entrada = hora_entrada
    self.hora_salida=hora_salida
    self.id = id
    self.nombre = nombre
    self.placa = placa

class Residente(Persona):
  def __init__(self,residencia,horas,id,nombre,placa):
    super().__init__(horas,id,nombre,placa)
    self.residencia = residencia

class Trabajador(Persona):
  def __init__(self,turno,horas,id,nombre,t_aseo):
    super().__init__(horas,id,nombre)
    self.turno = turno
    self.t_aseo=t_aseo

class Parqueadero():
  def init(self):
    self.cupo_disponible = 50 #Cupo parqueadero
    self.parqueaderos = []

  def  ingresar_persona(self, persona):
    if self.cupo_disponible > 0:
      self.parqueaderos.append(persona)
      self.cupo_disponible -= 1
      print(f"{persona.nombre} ha ingresado al parqueadero. Cupo disponible: {self.cupo_disponible}")
    else:
      print("No hay cupo disponible en el parqueadero.")

  def retirar_persona(self, persona):
      if persona in self.parqueaderos:
        self.parqueados.remove(persona)
        self.cupo_disponible += 1
        print(f"{persona.nombre} ha salido del parqueadero. Cupo disponible: {self.cupo_disponible}")
      else:
        print(f"{persona.nombre} no se encuentra en el parqueadero.")

  def imprimir_parqueadero(self):
        print("Personas en el parqueadero:")
        for persona in self.parqueaderos:
            print(f"ID: {persona.id}, Nombre: {persona.nombre}, Placa: {persona.placa}")

    