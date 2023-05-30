#este archivo maneja la interfaz
import tkinter as tk
from tkinter import ttk
from persona import Persona
from entrada import Entrada
from novedad import Novedad

class Hoja():
  def __init__(self,root = None):
    self.root = tk.Tk()
    self.root.title("Registro")
    self.root.iconbitmap('img/lArrow.ico')
    self.root.geometry("1300x650")
    self.frame=None
    self.framenovedades=None
    self.id_visitante=None
    self.crear_fmenu()
    self.crear_barramenu(root)
    self.root.mainloop() 
    self.frameresidentes = None
    


  def crear_fmenu(self):  
    if (self.frame==None and self.framenovedades==None):      
     self.frame = tk.Frame(self.root)
     self.poner_campos()
     self.dibujar_tabla_visitantes()
     self.frame.pack()
    else:
     if (self.framenovedades!=None):     
      self.framenovedades.borrar_frame_novedad()
      self.framenovedades=None
      self.frame = tk.Frame(self.root)
      self.poner_campos()
      self.dibujar_tabla_visitantes()
      self.frame.pack()

    
  def crear_novedades(self): 
    if (self.framenovedades==None): 
     self.frame.destroy() 
     self.framenovedades = Novedad(self.root)
     self.frame=None

  def crear_barramenu(self,root):
    barra_menu = tk.Menu(root)
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    self.root.config(menu= barra_menu,width=300,height=300)
    barra_menu.add_cascade(label = "Inicio",menu =menu_inicio)
    menu_inicio.add_command(label = "Registrar persona",command=self.crear_fmenu)
    menu_inicio.add_command(label="Crear Novedad",command=self.crear_novedades)

  def poner_campos(self):
     #nombre
     label_nombre = tk.Label(self.frame, text='Nombre: ')
     label_nombre.config(font= (('Arial', 12, 'bold')))
     label_nombre.grid(row = 0, column=0, padx= 10, pady=10)
     #ID
     label_id = tk.Label(self.frame, text='ID:')
     label_id.config(font= (('Arial', 12, 'bold')))
     label_id.grid(row=1,column=0,padx=10,pady=10)
     #Hora de entrada 
     label_duracion = tk.Label(self.frame, text='Hora de entrada: ')
     label_duracion.config(font= (('Arial', 12, 'bold')))
     label_duracion.grid(row = 2, column=0, padx= 10, pady=10)
     #Hora de salida
     label_id = tk.Label(self.frame, text='Hora de salida: ')
     label_id.config(font= (('Arial', 12, 'bold')))
     label_id.grid(row = 3, column=0, padx= 10, pady=10)
     #Tiene vehiculo?
     self.checkbox_vehiculovar = tk.BooleanVar(self.frame)
     self.checkbox_vehiculo = tk.Checkbutton(self.frame,text='¿tiene vehiculo?',variable=self.checkbox_vehiculovar,command=self.habilitar_placa,state='disabled')
     self.checkbox_vehiculo.config(font= (('Arial', 12, 'bold')))
     self.checkbox_vehiculo.grid(row=4,column=0,padx=10,pady=10)
     #Placa del vehiculo
     label_placa=tk.Label(self.frame, text="Placa")
     label_placa.config(font= (('Arial', 12, 'bold')))
     label_placa.grid(row=5,column=0,padx=10,pady=10)
     
     #Entrada de cada campo
     #Nombre
     self.nombre=tk.StringVar()
     self.entry_nombre = tk.Entry(self.frame,textvariable=self.nombre)
     self.entry_nombre.config(width= 50, state= 'disabled' ,font= (('Arial', 12)))
     self.entry_nombre.grid(row = 0, column=1, padx= 10, pady=10)
     #ID
     self.id=tk.StringVar()
     self.entry_id= tk.Entry(self.frame,textvariable=self.id)
     self.entry_id.config(width= 50, state= 'disabled' ,font= (('Arial', 12)))
     self.entry_id.grid(row = 1, column=1, padx= 10, pady=10)
     #Hora entrada
     self.horaentrada=tk.StringVar()
     self.entry_hora_entrada = tk.Entry(self.frame , textvariable=self.horaentrada)
     self.entry_hora_entrada.config(width= 50, state= 'disabled' ,font= (('Arial', 12)))
     self.entry_hora_entrada.grid(row = 2, column=1, padx= 10, pady=10)
     #Hora salida
     self.horasalida=tk.StringVar()
     self.entry_hora_salida = tk.Entry(self.frame,textvariable=self.horasalida)
     self.entry_hora_salida.config(width= 50, state= 'disabled' ,font= (('Arial', 12)))
     self.entry_hora_salida.grid(row = 3, column=1, padx= 10, pady=10)
     #Placa vehiculo
     self.placa=tk.StringVar()
     self.entry_placa=tk.Entry(self.frame,textvariable=self.placa)
     self.entry_placa.config(width= 50, state= 'disabled' ,font= (('Arial', 12)))
     self.entry_placa.grid(row = 5, column=1, padx= 10, pady=10)
        
        
     #Botones
     boton_nuevo = tk.Button(self.frame, text = 'Nuevo',command=self.enable_espacios)
     boton_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_nuevo.grid(row =6, column=0, padx=10, pady=10)

     boton_guardar = tk.Button(self.frame, text = 'Guardar',command=self.registrar_visitante)
     boton_guardar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_guardar.grid(row =6, column=1, padx=10, pady=10)
    
     boton_cancelar = tk.Button(self.frame, text = 'Cancelar',command=self.desable_espacios)
     boton_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_cancelar.grid(row =6, column=2, padx=10, pady=10)
     
     boton_editar = tk.Button(self.frame, text = 'Editar',command=self.editar_visitante)
     boton_editar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_editar.grid(row =8, column=1, padx=10, pady=10)
     
     boton_borrar = tk.Button(self.frame, text = 'Eliminar',command=self.remover_visitante)
     boton_borrar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_borrar.grid(row =8, column=2, padx=10, pady=10)

     boton_parquedero = tk.Button(self.frame, text = 'Parquedero',command=self.remover_visitante)
     boton_parquedero.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_parquedero.grid(row =8, column=0, padx=10, pady=10)
  
  
  def enable_espacios(self):
    self.checkbox_vehiculo.config(state='normal')
    self.entry_id.config(state='normal')   
    self.entry_hora_entrada.config(state='normal')
    self.entry_hora_salida.config(state='normal')
    self.entry_nombre.config(state='normal')
  def habilitar_placa(self):
    if self.checkbox_vehiculovar.get():    
     self.entry_placa.config(state='normal')
    else:
      self.entry_placa.config(state='disabled')
  def desable_espacios(self):
    self.checkbox_vehiculo.config(state='disabled') 
    self.entry_id.config(state='disabled')       
    self.entry_hora_entrada.config(state='disabled')
    self.entry_hora_salida.config(state='disable')
    self.entry_nombre.config(state='disabled')
    self.entry_placa.config(state='disabled')
    self.checkbox_vehiculovar.set(False)
    self.nombre.set('')
    self.placa.set('')
    self.id.set('')
    self.horaentrada.set('')
    self.horasalida.set('')
  
  #tabla de visitantes  
  def dibujar_tabla_visitantes(self):
    entrada = Entrada()    
    self.tabla_visitantes=ttk.Treeview(self.frame,column=('Nombre','ID','Hora entrada','Hora salida','Placa'))
    self.tabla_visitantes.grid(row=7,column=0,columnspan=4,sticky='nse')
    scroll = tk.Scrollbar(self.frame,orient='vertical',command=self.tabla_visitantes.yview)
    scroll.grid(row=7,column=5,sticky='nse')
    self.tabla_visitantes.configure(yscrollcommand=scroll.set)
    self.tabla_visitantes.heading('#0',text='Numero')
    self.tabla_visitantes.heading('#1',text='Nombre')
    self.tabla_visitantes.heading('#2',text='Identificacion')
    self.tabla_visitantes.heading('#3',text='Hora entrada')
    self.tabla_visitantes.heading('#4',text='Hora salida')
    self.tabla_visitantes.heading('#5',text='Placa')
    lista_visitantes = entrada.listar_visitantes()
    lista_visitantes.reverse()
    for visitante in lista_visitantes:
          self.tabla_visitantes.insert('',0,text=visitante[0],values=(visitante[1],visitante[2],visitante[3],visitante[4],visitante[5]))
          
  
  def registrar_visitante(self):
      nombre = self.entry_nombre.get()
      identiciacion = self.entry_id.get()
      hora_entrada = self.entry_hora_entrada.get()
      hora_salida = self.entry_hora_salida.get()
      placa = self.entry_placa.get()
      visitante = Persona(hora_entrada,hora_salida,identiciacion,nombre,placa)
      entrada = Entrada()
      if self.id_visitante==None:
       entrada.registrar_visitante(visitante)
       entrada.cerrar_db()
       self.dibujar_tabla_visitantes()
       self.desable_espacios()
      else:
       entrada.editar_visitante(visitante,self.id_visitante)
       self.dibujar_tabla_visitantes()   
       self.desable_espacios()
       self.id_visitante=None   
      
  def editar_visitante(self):
    self.id_visitante=self.tabla_visitantes.item(self.tabla_visitantes.selection())['text']
    nombrev = self.tabla_visitantes.item(self.tabla_visitantes.selection())['values'][0]
    idv = self.tabla_visitantes.item(self.tabla_visitantes.selection())['values'][1] 
    horaaenv = self.tabla_visitantes.item(self.tabla_visitantes.selection())['values'][2] 
    horasalv = self.tabla_visitantes.item(self.tabla_visitantes.selection())['values'][3]
    placav = self.tabla_visitantes.item(self.tabla_visitantes.selection())['values'][4] 
    self.enable_espacios()
    self.entry_nombre.insert(0,nombrev)
    self.entry_id.insert(0,idv)
    self.entry_hora_entrada.insert(0,horaaenv)
    self.entry_hora_salida.insert(0,horasalv)
    self.entry_placa.config(state='normal')
    self.entry_placa.insert(0,placav)  
  
  def remover_visitante(self):
    self.id_visitante=self.tabla_visitantes.item(self.tabla_visitantes.selection())['text']
    entrada = Entrada()
    entrada.eliminar_visitante(self.id_visitante)
    entrada.resetear_contador_visitantes()
    self.dibujar_tabla_visitantes()
    self.id_visitante=None     