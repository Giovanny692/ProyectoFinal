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