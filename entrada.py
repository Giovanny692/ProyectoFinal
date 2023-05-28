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
        