from generar import *

class Dato:
  def __init__(self):
    dato = generarNombreSexoEdad()
    self.nombre = dato['Nombre']
    self.sexo = dato['Sexo']
    self.edad = dato['Edad']
    self.cursos = dato['Cursos']
    self.departamento = dato["Departamento"]
    self.prob_aprob = dato["Probabilidad Aprobar"]
    self.prob_perd = dato["Probabilidad Perder"]
    self.prob_dese = dato["Probabilidad Desertar"]
  
  #==
  def __eq__ (self, __o: object) -> bool:
    return (self.departamento == __o.departamento) #and (self.sexo == __o.sexo)

  #<
  def __lt__ (self, __o: object) -> bool:
    return (self.departamento< __o.departamento) #and (self.sexo == __o.sexo)
  
  #<=
  def __le__ (self, __o: object) -> bool:
    return (self.departamento <= __o.departamento) #and (self.sexo == __o.sexo)
  
  #>
  def __gt__ (self, __o: object) -> bool:
    return (self.departamento > __o.departamento) #and (self.sexo == __o.sexo)
  
  #>=
  def __ge__ (self, __o: object) -> bool:
    return (self.departamento >= __o.departamento) #and (self.sexo == __o.sexo)
  
  #!=
  def __ne__ (self, __o: object) -> bool:
    return (self.departamento != __o.departamento) #or (self.sexo != __o.sexo)

  def __str__(self):
    return f'OD=[Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {self.sexo}, Cursos: {self.cursos}, Departamento: {self.departamento}, Probabilidad Aprobar: {self.prob_aprob}, Probabilidad Perder: {self.prob_perd}, Probabilidad Desertar: {self.prob_dese}]'