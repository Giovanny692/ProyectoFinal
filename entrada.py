#clase que maneja coneccion a base de datos
import sqlite3
from persona import Persona, Residente
class Entrada:
    
    def conectar_db(self):
        self.base_datos= 'Bases_de_datos/conjunto.db'
        self.conexion=sqlite3.connect(self.base_datos)
        self.cursor= self.conexion.cursor()
    def cerrar_db(self):
        self.conexion.commit()
        self.conexion.close()
    #tabla visitantes    
    def registrar_visitante(self,persona):
        self.conectar_db()
        sql = f"""INSERT INTO visitantes (Nombre, Identificacion, Hora_entrada, Hora_salida, Placa) 
        VALUES('{persona.nombre}','{persona.id}','{persona.hora_entrada}','{persona.hora_salida}','{persona.placa}')"""
        self.cursor.execute(sql)
    def listar_visitantes(self):
        self.conectar_db()
        sql = 'SELECT * FROM visitantes'  
        self.cursor.execute(sql)
        lista_visitantes = self.cursor.fetchall()
        self.cerrar_db()
        return lista_visitantes
    def editar_visitante(self,persona,id_persona):
        self.conectar_db()
        sql = f"""UPDATE visitantes SET Nombre='{persona.nombre}',Identificacion='{persona.id}',
        Hora_entrada='{persona.hora_entrada}',Hora_salida='{persona.hora_salida}',Placa='{persona.placa}'
        WHERE numero={id_persona}"""
        self.cursor.execute(sql)
        self.cerrar_db()
          