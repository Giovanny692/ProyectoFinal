#este archivo maneja empleados y personas

class Persona():
  def __init__(self,horas,id,nombre):
    self.horas = horas
    self.id = id
    self.nombre = nombre

  def getnombre(self):
    return self.nombre
  def getid(self):
    return self.id
  def gethoras(self):
    return self.horas

class Residente(Persona):
  def __init__(self,residencia,horas,id,nombre):
    super().__init__(horas,id,nombre)
    self.residencia = residencia

class Trabajador(Persona):
  def __init__(self,turno,horas,id,nombre,t_aseo):
    super().__init__(horas,id,nombre)
    self.turno = turno
    self.t_aseo=t_aseo