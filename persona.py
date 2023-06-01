#este archivo maneja empleados y personas

class Persona():
  def __init__(self,hora_entrada,hora_salida,id,nombre,placa):
    self.hora_entrada = hora_entrada
    self.hora_salida=hora_salida
    self.id = id
    self.nombre = nombre
    self.placa = placa

class Residente(Persona):
  def __init__(self,residencia,fecha_entrada,id,nombre,placa):
    self.fecha_entrada = fecha_entrada
    self.id = id
    self.nombre = nombre
    self.placa = placa
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


    