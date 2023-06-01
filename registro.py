#este archivo maneja la interfaz
import tkinter as tk
from tkinter import ttk
from persona import Persona
from entrada import Entrada
from novedad import Novedad
from persona import Residente, Parqueadero

class Hoja():
  def __init__(self,root = None):
    self.root = tk.Tk()
    self.root.title("Registro")
    self.root.iconbitmap('img/lArrow.ico')
    self.root.geometry("1300x650")
    self.frame=None
    self.framenovedades=None
    self.id_visitante=None
    self.id_residente=None
    self.frameresidentes = None
    self.fparqueadero = None 
    self.crear_fmenu()
    self.crear_barramenu(root)
    self.root.mainloop() 
      
  def crear_fmenu(self):  
    if (self.frame==None and self.framenovedades==None and self.frameresidentes==None and self.fparqueadero == None):      
     self.frame = tk.Frame(self.root)
     self.poner_camposvisitante()
     self.dibujar_tabla_visitantes()
     self.frame.pack()
    else:
     if (self.framenovedades!=None):     
      self.framenovedades.borrar_frame_novedad()
      self.framenovedades=None
      self.frame = tk.Frame(self.root)
      self.poner_camposvisitante()
      self.dibujar_tabla_visitantes()
      self.frame.pack()

     elif (self.frameresidentes != None):
       self.frameresidentes.destroy()
       self.frameresidentes=None
       self.frame = tk.Frame(self.root)
       self.poner_camposvisitante()
       self.dibujar_tabla_visitantes()
       self.frame.pack()       
       
     elif (self.fparqueadero != None):
       self.fparqueadero.destroy ()
       self.fparqueadero = None
       self.frame = tk.Frame(self.root)
       self.poner_camposvisitante()
       self.dibujar_tabla_visitantes()
       self.frame.pack()

  def crear_fresidentes(self):
    if (self.frame != None):
      self.frame.destroy()
      self.frameresidentes = tk.Frame (self.root)
      self.poner_camposresidente ()
      self.dibujar_tabla_residentes ()
      self.frameresidentes.pack()
      self.frame=None
    if (self.framenovedades != None):
      self.framenovedades.borrar_frame_novedad()
      self.frameresidentes = tk.Frame (self.root)
      self.poner_camposresidente ()
      self.dibujar_tabla_residentes ()
      self.frameresidentes.pack()
      self.framenovedades=None

  def crear_novedades(self): 
    if (self.framenovedades==None):
     if (self.frame != None): 
      self.frame.destroy()
      self.frame = None
      self.framenovedades = Novedad(self.root) 
      
    if (self.frameresidentes != None):
      self.frameresidentes.destroy()
      self.frameresidentes=None  
      self.framenovedades = Novedad(self.root)

  def crear_barramenu(self,root):
    barra_menu = tk.Menu(root)
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    self.root.config(menu= barra_menu,width=300,height=300)
    barra_menu.add_cascade(label = "Inicio",menu =menu_inicio)
    menu_inicio.add_command(label = "Visitantes",command=self.crear_fmenu)
    menu_inicio.add_command(label="Crear Novedad",command=self.crear_novedades)
    menu_inicio.add_command(label= 'Residentes', command= self.crear_fresidentes)

  def poner_camposvisitante(self):
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
     self.checkbox_vehiculo = tk.Checkbutton(self.frame,text='¿Tiene vehiculo?',variable=self.checkbox_vehiculovar,command=self.habilitar_placa,state='disabled')
     self.checkbox_vehiculo.config(font= (('Arial', 12, 'bold')))
     self.checkbox_vehiculo.grid(row=4,column=0,padx=10,pady=10)
     #Combobox
     self.espacio = ttk.Combobox(self.frame, state='disabled', values=("1","2","3","4","5","6","7","8","9","10"))
     self.espacio.grid (row=4, column=1, padx =10, pady=10)

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

     boton_parquedero = tk.Button(self.frame, text = 'Parquedero',command=self.frameparqueadero)
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
     self.espacio.config (state= 'readonly')
    else:
      self.entry_placa.config(state='disabled')
      self.espacio.config (state= 'disabled')

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
  
  #Tabla de visitantes  
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
      self.parquedaero_prueba = Parqueadero()
      nombre = self.entry_nombre.get()
      identificacion = self.entry_id.get()
      hora_entrada = self.entry_hora_entrada.get()
      hora_salida = self.entry_hora_salida.get()
      placa = self.entry_placa.get()
      visitante = Persona(hora_entrada,hora_salida,identificacion,nombre,placa)
      entrada = Entrada()
      if placa != "":
        entrada.registrar_parqueadero (visitante, self.espacio.get())

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

  def poner_camposresidente (self):
     #nombre
     label_nombrer = tk.Label(self.frameresidentes, text='Nombre: ')
     label_nombrer.config(font= (('Arial', 12, 'bold')))
     label_nombrer.grid(row = 0, column=0, padx= 10, pady=10)
     #ID
     label_idr = tk.Label(self.frameresidentes, text='ID:')
     label_idr.config(font= (('Arial', 12, 'bold')))
     label_idr.grid(row=1,column=0,padx=10,pady=10)
     #Fecha entrada 
     label_duracionr = tk.Label(self.frameresidentes, text='Fecha de ingreso: ')
     label_duracionr.config(font= (('Arial', 12, 'bold')))
     label_duracionr.grid(row = 2, column=0, padx= 10, pady=10)
     #Tiene vehiculo?
     self.checkbox_vehiculovarr = tk.BooleanVar(self.frameresidentes)
     self.checkbox_vehiculor = tk.Checkbutton(self.frameresidentes,text='¿Tiene vehiculo?',variable=self.checkbox_vehiculovarr,command=self.habilitar_placar,state='disabled')
     self.checkbox_vehiculor.config(font= (('Arial', 12, 'bold')))
     self.checkbox_vehiculor.grid(row=3,column=0,padx=10,pady=10)
     #Placa del vehiculo
     label_placar=tk.Label(self.frameresidentes, text="Placa")
     label_placar.config(font= (('Arial', 12, 'bold')))
     label_placar.grid(row=4,column=0,padx=10,pady=10)
     #Residencia
     label_residencia = tk.Label (self.frameresidentes, text= "Residencia")
     label_residencia.config (font= (('Arial', 12, 'bold')))
     label_residencia.grid (row=5, column=0, padx=10, pady=10)
     
     #Entrada de cada campo
     #Nombre
     self.nombrer=tk.StringVar()
     self.entry_nombrer = tk.Entry(self.frameresidentes,textvariable=self.nombrer)
     self.entry_nombrer.config(width= 50, state= 'disabled' ,font= (('Arial', 12)))
     self.entry_nombrer.grid(row = 0, column=1, padx= 10, pady=10)
     #ID
     self.idr=tk.StringVar()
     self.entry_idr= tk.Entry(self.frameresidentes,textvariable=self.idr)
     self.entry_idr.config(width= 50, state= 'disabled' ,font= (('Arial', 12)))
     self.entry_idr.grid(row = 1, column=1, padx= 10, pady=10)
     #Fecha entrada
     self.fechaentrada=tk.StringVar()
     self.entry_fecha_entrada = tk.Entry(self.frameresidentes , textvariable=self.fechaentrada)
     self.entry_fecha_entrada.config(width= 50, state= 'disabled' ,font= (('Arial', 12)))
     self.entry_fecha_entrada.grid(row = 2, column=1, padx= 10, pady=10)
     #Placa vehiculo
     self.placar=tk.StringVar()
     self.entry_placar=tk.Entry(self.frameresidentes,textvariable=self.placar)
     self.entry_placar.config(width= 50, state= 'disabled' ,font= (('Arial', 12)))
     self.entry_placar.grid(row = 4, column=1, padx= 10, pady=10)
     #Residencia
     self.residencia=tk.StringVar()
     self.entry_residencia=tk.Entry(self.frameresidentes,textvariable=self.residencia)
     self.entry_residencia.config(width=50,state= 'disabled',font=(('Arial', 12)))
     self.entry_residencia.grid(row = 5, column= 1, padx=10, pady=10)

     #Botones
     boton_nuevo = tk.Button(self.frameresidentes, text = 'Nuevo',command=self.enable_espaciosresidente)
     boton_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_nuevo.grid(row =6, column=0, padx=10, pady=10)

     boton_guardar = tk.Button(self.frameresidentes, text = 'Guardar',command=self.registrar_residentes)
     boton_guardar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_guardar.grid(row =6, column=1, padx=10, pady=10)
    
     boton_cancelar = tk.Button(self.frameresidentes, text = 'Cancelar',command=self.desable_espaciosr)
     boton_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_cancelar.grid(row =6, column=2, padx=10, pady=10)
     
     boton_editar = tk.Button(self.frameresidentes, text = 'Editar',command=self.editar_residente)
     boton_editar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_editar.grid(row =8, column=1, padx=10, pady=10)
     
     boton_borrar = tk.Button(self.frameresidentes, text = 'Eliminar',command=self.remover_residente)
     boton_borrar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_borrar.grid(row =8, column=2, padx=10, pady=10)

     boton_parquedero = tk.Button(self.frameresidentes, text = 'Parquedero',command=self.frameparqueadero)
     boton_parquedero.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_parquedero.grid(row =8, column=0, padx=10, pady=10)

  def enable_espaciosresidente(self):
    self.checkbox_vehiculor.config(state='normal')
    self.entry_idr.config(state='normal')   
    self.entry_fecha_entrada.config(state='normal')
    self.entry_residencia.config(state='normal')
    self.entry_nombrer.config(state='normal')

  def habilitar_placar(self):
    if self.checkbox_vehiculovarr.get():    
     self.entry_placar.config(state='normal')
    else:
      self.entry_placar.config(state='disabled')

  def desable_espaciosr(self):
    self.checkbox_vehiculor.config(state='disabled') 
    self.entry_idr.config(state='disabled')       
    self.entry_fecha_entrada.config(state='disabled')
    self.entry_nombrer.config(state='disabled')
    self.entry_placar.config(state='disabled')
    self.entry_residencia.config(state='disabled')
    self.checkbox_vehiculovar.set(False)
    self.nombrer.set('')
    self.placar.set('')
    self.idr.set('')
    self.fechaentrada.set('')
    self.residencia.set('')

  #Tabla de residenets  
  def dibujar_tabla_residentes(self):
    entrada = Entrada()    
    self.tabla_residentes=ttk.Treeview(self.frameresidentes,column=('Nombre','ID','Fecha entrada','Placa', 'Residencia'))
    self.tabla_residentes.grid(row=7,column=0,columnspan=4,sticky='nse')
    scroll = tk.Scrollbar(self.frameresidentes,orient='vertical',command=self.tabla_residentes.yview)
    scroll.grid(row=8,column=5,sticky='nse')
    self.tabla_residentes.configure(yscrollcommand=scroll.set)
    self.tabla_residentes.heading('#0',text='Numero')
    self.tabla_residentes.heading('#1',text='Nombre')
    self.tabla_residentes.heading('#2',text='Identificacion')
    self.tabla_residentes.heading('#3',text='Fecha entrada')
    self.tabla_residentes.heading('#4',text='Placa')
    self.tabla_residentes.heading('#5',text='Residencia')
    lista_residentes = entrada.listar_residentes()
    lista_residentes.reverse()
    for residente in lista_residentes:
          self.tabla_residentes.insert('',0,text=residente[0],values=(residente[1],residente[2],residente[3],residente[4],residente[5]))

  def registrar_residentes(self):
      self.parquedaero_prueba = Parqueadero()
      nombre = self.entry_nombrer.get()
      identificacion = self.entry_idr.get()
      fecha_entrada = self.entry_fecha_entrada.get()
      placa = self.entry_placar.get()
      residencia = self.entry_residencia.get()
      residente = Residente (residencia, fecha_entrada ,identificacion, nombre,placa)
      entrada = Entrada()
      if placa != "":
        pass 

      if self.id_residente==None:
       entrada.registrar_residente(residente)
       entrada.cerrar_db()
       self.dibujar_tabla_residentes()
       self.desable_espaciosr()
      else:
       entrada.editar_residente(residente,self.id_residente)
       self.dibujar_tabla_residentes()   
       self.desable_espaciosr()
       self.id_visitante=None   
      
  def editar_residente(self):
    self.id_residente=self.tabla_residentes.item(self.tabla_residentes.selection())['text']
    nombrev = self.tabla_residentes.item(self.tabla_residentes.selection())['values'][0]
    idv = self.tabla_residentes.item(self.tabla_residentes.selection())['values'][1] 
    fechaev = self.tabla_residentes.item(self.tabla_residentes.selection())['values'][2] 
    placav = self.tabla_residentes.item(self.tabla_residentes.selection())['values'][3]
    residenciav = self.tabla_residentes.item(self.tabla_residentes.selection())['values'][4] 
    self.enable_espaciosresidente()
    self.entry_nombrer.insert(0,nombrev)
    self.entry_idr.insert(0,idv)
    self.entry_fecha_entrada.insert(0,fechaev)
    self.entry_placar.insert(0,placav)
    self.entry_placar.config(state='normal')
    self.entry_residencia.insert(0,residenciav)  
  
  def remover_residente(self):
    self.id_residente=self.tabla_residentes.item(self.tabla_residentes.selection())['text']
    entrada = Entrada()
    entrada.eliminar_residente(self.id_residente)
    entrada.resetear_contador_residentes()
    self.dibujar_tabla_residentes()
    self.id_residente=None

  def dibujar_tablaparqueadero(self):
    entrada = Entrada()    
    self.tabla_parqueadero=ttk.Treeview(self.fparqueadero,column=('Nombre','Placa','Estado'))
    self.tabla_parqueadero.grid(row=0,column=0,columnspan=4,sticky='nse')
    scroll = tk.Scrollbar(self.fparqueadero,orient='vertical',command=self.tabla_parqueadero.yview)
    scroll.grid(row=0,column=5,sticky='nse')
    self.tabla_parqueadero.configure(yscrollcommand=scroll.set)
    self.tabla_parqueadero.heading('#0',text='Numero')
    self.tabla_parqueadero.heading('#1',text='Nombre')
    self.tabla_parqueadero.heading('#2',text='Placa')
    self.tabla_parqueadero.heading('#3',text='Estado')
    lista_parqueadero = entrada.listar_parqueadero()
    lista_parqueadero.reverse()
    for parqueadero in lista_parqueadero:
          self.tabla_parqueadero.insert('',0,text=parqueadero[0],values=(parqueadero[1],parqueadero[2],parqueadero[3]))

  def frameparqueadero (self):
    self.frame.destroy ()
    self.frame = None
    self.fparqueadero = tk.Frame (self.root)
    self.dibujar_tablaparqueadero ()
    self.fparqueadero.pack ()