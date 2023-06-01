#clase que maneja coneccion a base de datos
import sqlite3
from persona import Persona, Residente
from tkinter import messagebox
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
    def eliminar_visitante(self,id_visitante):
        self.conectar_db()
        try:
         sql = f'DELETE FROM visitantes WHERE numero= {id_visitante}'
         self.cursor.execute(sql)
        except:
         titulo = 'error'
         message = 'Seleccione una entrada para eliminarla' 
         messagebox.showinfo(titulo,message)   
        self.cerrar_db()  
    def resetear_contador_visitantes(self):
        self.conectar_db()
        sql=f'UPDATE sqlite_sequence SET seq=1 WHERE name="visitantes"'
        self.cursor.execute(sql)  
        self.cerrar_db()
    
    #tabla residentes
    def registrar_residente(self,persona):
        self.conectar_db()
        sql = f"""INSERT INTO residentes (Nombre, Identificacion, Fecha_ingreso, Fecha_salida, Placa, Residencia) 
        VALUES('{persona.nombre}','{persona.id}','{persona.hora_entrada}','{persona.hora_salida}','{persona.placa}','{Residente.residencia}')"""
        self.cursor.execute(sql)
    def listar_residentes(self):
        self.conectar_db()
        sql = 'SELECT * FROM residentes'  
        self.cursor.execute(sql)
        lista_residentes = self.cursor.fetchall()
        self.cerrar_db()
        return lista_residentes
    def editar_residente(self,persona,id_persona):
        self.conectar_db()
        sql = f"""UPDATE residentes SET Nombre='{persona.nombre}',Identificacion='{persona.id}',
        Fecha_infreso='{persona.hora_entrada}',Fecha_salida='{persona.hora_salida}',Placa='{persona.placa}'
        WHERE numero={id_persona}"""
        self.cursor.execute(sql)
        self.cerrar_db()
    def eliminar_residente(self,id_residente):
        self.conectar_db()
        try:
         sql = f'DELETE FROM residentes WHERE numero= {id_residente}'
         self.cursor.execute(sql)
        except:
         titulo = 'error'
         message = 'Seleccione una entrada para eliminarla' 
         messagebox.showinfo(titulo,message)   
        self.cerrar_db()  