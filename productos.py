import tkinter as tk
from tkinter import ttk
from entrada import Entrada
from persona import Persona, Residente

#product - factory method
class Frame(tk.Frame):
    def __init__(self,root):
        tk.Frame.__init__(self,root)
        self.poner_espacios()
        self.poner_entry()
        self.poner_botones()
        self.dibujar_tabla()
        self.pack()
        
    def poner_espacios(self):
        pass
    def poner_entry(self):
        pass
    def poner_botones(self):
        pass
    def crear_tabla(self):
        pass
    def enable_espacios(self):
        pass
    def disable_espacios(self):
        pass
    def dibujar_tabla(self):
        pass

#concrete product A
class Frame_Visitantes(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.funcionamiento=funcionamiento_visitante()
        self.id_visitante=None
        
    def poner_espacios(self):
     #nombre
     label_nombre = tk.Label(self, text='Nombre: ')
     label_nombre.config(font= (('Arial', 12, 'bold')))
     label_nombre.grid(row = 0, column=0, padx= 10, pady=10)
     #ID
     label_id = tk.Label(self, text='ID:')
     label_id.config(font= (('Arial', 12, 'bold')))
     label_id.grid(row=1,column=0,padx=10,pady=10)
     #Hora de entrada 
     label_duracion = tk.Label(self, text='Hora de entrada: ')
     label_duracion.config(font= (('Arial', 12, 'bold')))
     label_duracion.grid(row = 2, column=0, padx= 10, pady=10)
     #Hora de salida
     label_id = tk.Label(self, text='Hora de salida: ')
     label_id.config(font= (('Arial', 12, 'bold')))
     label_id.grid(row = 3, column=0, padx= 10, pady=10)
     #Tiene vehiculo?
     self.checkbox_vehiculovar = tk.BooleanVar(self)
     self.checkbox_vehiculo = tk.Checkbutton(self,text='¿Tiene vehiculo?',variable=self.checkbox_vehiculovar,command=self.habilitar_placa,state='disabled')
     self.checkbox_vehiculo.config(font= (('Arial', 12, 'bold')))
     self.checkbox_vehiculo.grid(row=4,column=0,padx=10,pady=10)
     #Combobox
     self.espacio = ttk.Combobox(self, state='disabled', values=("1","2","3","4","5","6","7","8","9","10"))
     self.espacio.grid (row=4, column=1, padx =10, pady=10)

     #Placa del vehiculo
     label_placa=tk.Label(self, text="Placa")
     label_placa.config(font= (('Arial', 12, 'bold')))
     label_placa.grid(row=5,column=0,padx=10,pady=10)
     
    def poner_entry(self):
     self.nombre=tk.StringVar()
     self.entry_nombre = tk.Entry(self,textvariable=self.nombre)
     self.entry_nombre.config(width= 50, state= 'disabled' ,font= (('Arial', 12)))
     self.entry_nombre.grid(row = 0, column=1, padx= 10, pady=10)
     #ID
     self.id=tk.StringVar()
     self.entry_id= tk.Entry(self,textvariable=self.id)
     self.entry_id.config(width= 50, state= 'disabled' ,font= (('Arial', 12)))
     self.entry_id.grid(row = 1, column=1, padx= 10, pady=10)
     #Hora entrada
     self.horaentrada=tk.StringVar()
     self.entry_hora_entrada = tk.Entry(self, textvariable=self.horaentrada)
     self.entry_hora_entrada.config(width= 50, state= 'disabled' ,font= (('Arial', 12)))
     self.entry_hora_entrada.grid(row = 2, column=1, padx= 10, pady=10)
     #Hora salida
     self.horasalida=tk.StringVar()
     self.entry_hora_salida = tk.Entry(self,textvariable=self.horasalida)
     self.entry_hora_salida.config(width= 50, state= 'disabled' ,font= (('Arial', 12)))
     self.entry_hora_salida.grid(row = 3, column=1, padx= 10, pady=10)
     #Placa vehiculo
     self.placa=tk.StringVar()
     self.entry_placa=tk.Entry(self,textvariable=self.placa)
     self.entry_placa.config(width= 50, state= 'disabled' ,font= (('Arial', 12)))
     self.entry_placa.grid(row = 5, column=1, padx= 10, pady=10)
     
    def poner_botones(self):
     boton_nuevo = tk.Button(self, text = 'Nuevo',command=self.enable_espacios)
     boton_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_nuevo.grid(row =6, column=0, padx=10, pady=10)

     boton_guardar = tk.Button(self, text = 'Guardar',command=self.registrar_visitante)
     boton_guardar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_guardar.grid(row =6, column=1, padx=10, pady=10)
    
     boton_cancelar = tk.Button(self, text = 'Cancelar',command=self.desable_espacios)
     boton_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_cancelar.grid(row =6, column=2, padx=10, pady=10)
     
     boton_editar = tk.Button(self, text = 'Editar',command=self.editar_visitante)
     boton_editar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_editar.grid(row =8, column=1, padx=10, pady=10)
     
     boton_borrar = tk.Button(self, text = 'Eliminar',command=self.remover_visitante)
     boton_borrar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_borrar.grid(row =8, column=2, padx=10, pady=10)

    def registrar_visitante(self):
        entrada=Entrada()
        self.funcionamiento.registrar(self,entrada,self.id_visitante) 
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
         
    def editar_visitante(self):
     self.funcionamiento.editar(self)
     
    def dibujar_tabla(self):
     entrada = Entrada()    
     self.tabla_visitantes=ttk.Treeview(self,column=('Nombre','ID','Hora entrada','Hora salida','Placa'))
     self.tabla_visitantes.grid(row=7,column=0,columnspan=4,sticky='nse')
     scroll = tk.Scrollbar(self,orient='vertical',command=self.tabla_visitantes.yview)
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
    
    def remover_visitante(self):
     entrada=Entrada()
     self.funcionamiento.eliminar(self,entrada,self.id_visitante)

#concrete product B    
class FrameResidentes(Frame):
    def __init__(self, root):
           super().__init__(root)
           self.funcionamiento=funcionamiento_residente()
           self.id_residente=None
              
    def poner_espacios(self):
     #nombre
     label_nombrer = tk.Label(self, text='Nombre: ')
     label_nombrer.config(font= (('Arial', 12, 'bold')))
     label_nombrer.grid(row = 0, column=0, padx= 10, pady=10)
     #ID
     label_idr = tk.Label(self, text='ID:')
     label_idr.config(font= (('Arial', 12, 'bold')))
     label_idr.grid(row=1,column=0,padx=10,pady=10)
     #Fecha entrada 
     label_duracionr = tk.Label(self, text='Fecha de ingreso: ')
     label_duracionr.config(font= (('Arial', 12, 'bold')))
     label_duracionr.grid(row = 2, column=0, padx= 10, pady=10)
     #Tiene vehiculo?
     self.checkbox_vehiculovar = tk.BooleanVar(self)
     self.checkbox_vehiculor = tk.Checkbutton(self,text='¿Tiene vehiculo?',variable=self.checkbox_vehiculovar,command=self.habilitar_placar,state='disabled')
     self.checkbox_vehiculor.config(font= (('Arial', 12, 'bold')))
     self.checkbox_vehiculor.grid(row=3,column=0,padx=10,pady=10)
     #Placa del vehiculo
     label_placar=tk.Label(self, text="Placa")
     label_placar.config(font= (('Arial', 12, 'bold')))
     label_placar.grid(row=4,column=0,padx=10,pady=10)
     #Residencia
     label_residencia = tk.Label (self, text= "Residencia")
     label_residencia.config (font= (('Arial', 12, 'bold')))
     label_residencia.grid (row=5, column=0, padx=10, pady=10) 
    
    def poner_entry(self):
      self.nombrer=tk.StringVar()
      self.entry_nombrer = tk.Entry(self,textvariable=self.nombrer)
      self.entry_nombrer.config(width= 50, state= 'disabled' ,font= (('Arial', 12)))
      self.entry_nombrer.grid(row = 0, column=1, padx= 10, pady=10)
      #ID
      self.idr=tk.StringVar()
      self.entry_idr= tk.Entry(self,textvariable=self.idr)
      self.entry_idr.config(width= 50, state= 'disabled' ,font= (('Arial', 12)))
      self.entry_idr.grid(row = 1, column=1, padx= 10, pady=10)
      #Fecha entrada
      self.fechaentrada=tk.StringVar()
      self.entry_fecha_entrada = tk.Entry(self, textvariable=self.fechaentrada)
      self.entry_fecha_entrada.config(width= 50, state= 'disabled' ,font= (('Arial', 12)))
      self.entry_fecha_entrada.grid(row = 2, column=1, padx= 10, pady=10)
      #Placa vehiculo
      self.placar=tk.StringVar()
      self.entry_placar=tk.Entry(self,textvariable=self.placar)
      self.entry_placar.config(width= 50, state= 'disabled' ,font= (('Arial', 12)))
      self.entry_placar.grid(row = 4, column=1, padx= 10, pady=10)
      #Residencia
      self.residencia=tk.StringVar()
      self.entry_residencia=tk.Entry(self,textvariable=self.residencia)
      self.entry_residencia.config(width=50,state= 'disabled',font=(('Arial', 12)))
      self.entry_residencia.grid(row = 5, column= 1, padx=10, pady=10)
    
    def poner_botones(self):
      #Botones
     boton_nuevo = tk.Button(self, text = 'Nuevo',command=self.enable_espacios)
     boton_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_nuevo.grid(row =6, column=0, padx=10, pady=10)

     boton_guardar = tk.Button(self, text = 'Guardar',command=self.registrar_residentes)
     boton_guardar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_guardar.grid(row =6, column=1, padx=10, pady=10)
    
     boton_cancelar = tk.Button(self, text = 'Cancelar',command=self.disable_espacios)
     boton_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_cancelar.grid(row =6, column=2, padx=10, pady=10)
     
     boton_editar = tk.Button(self, text = 'Editar',command=self.editar_residente)
     boton_editar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_editar.grid(row =8, column=1, padx=10, pady=10)
     
     boton_borrar = tk.Button(self, text = 'Eliminar',command=self.remover_residente)
     boton_borrar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_borrar.grid(row =8, column=2, padx=10, pady=10)  
    
    def enable_espacios(self):
     self.checkbox_vehiculor.config(state='normal')
     self.entry_idr.config(state='normal')   
     self.entry_fecha_entrada.config(state='normal')
     self.entry_residencia.config(state='normal')
     self.entry_nombrer.config(state='normal')
    
    def disable_espacios(self):
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
    
    def registrar_residentes(self):
     entrada = Entrada()
     self.funcionamiento.registrar(self,entrada,self.id_residente)
    
    def dibujar_tabla(self):
      entrada = Entrada()    
      self.tabla_residentes=ttk.Treeview(self,column=('Nombre','ID','Fecha entrada','Placa', 'Residencia'))
      self.tabla_residentes.grid(row=7,column=0,columnspan=4,sticky='nse')
      scroll = tk.Scrollbar(self,orient='vertical',command=self.tabla_residentes.yview)
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
    
    def remover_residente(self):
       entrada = Entrada()
       self.funcionamiento.eliminar(self,entrada,self.id_residente)
    
    def habilitar_placar(self):
     if self.checkbox_vehiculovar.get():    
         self.entry_placar.config(state='normal')
     else:
         self.entry_placar.config(state='disabled')
    
    def editar_residente(self):
     self.id_residente=self.tabla_residentes.item(self.tabla_residentes.selection())['text']
     nombrev = self.tabla_residentes.item(self.tabla_residentes.selection())['values'][0]
     idv = self.tabla_residentes.item(self.tabla_residentes.selection())['values'][1] 
     fechaev = self.tabla_residentes.item(self.tabla_residentes.selection())['values'][2] 
     placav = self.tabla_residentes.item(self.tabla_residentes.selection())['values'][3]
     residenciav = self.tabla_residentes.item(self.tabla_residentes.selection())['values'][4] 
     self.enable_espacios()
     self.entry_nombrer.insert(0,nombrev)
     self.entry_idr.insert(0,idv)
     self.entry_fecha_entrada.insert(0,fechaev)
     self.entry_placar.insert(0,placav)
     self.entry_placar.config(state='normal')
     self.entry_residencia.insert(0,residenciav)       
 
#implementacion
class funcionamiento():    
    def registrar(self,frame:Frame,entrada:Entrada,id):      
        pass
    def eliminar(self,frame:Frame,entrada:Entrada,id):
        pass 
    def editar(self,frame:Frame):
        pass   
#implementacion_concreta1
class funcionamiento_visitante(funcionamiento):
    def registrar(self,frame:Frame_Visitantes,entrada:Entrada,id_visitante):
        nombre = frame.entry_nombre.get()
        identificacion = frame.entry_id.get()
        hora_entrada = frame.entry_hora_entrada.get()
        hora_salida = frame.entry_hora_salida.get()
        placa = frame.entry_placa.get()
        visitante = Persona(hora_entrada,hora_salida,identificacion,nombre,placa)
        if id_visitante==None:
           entrada.registrar_visitante(visitante)
           entrada.cerrar_db()
           frame.dibujar_tabla()
           frame.desable_espacios()
        else:
           entrada.editar_visitante(visitante,id_visitante)
           frame.dibujar_tabla()   
           frame.desable_espacios()
           id_visitante=None 
    def eliminar(self, frame: Frame_Visitantes,entrada:Entrada,id_visitante):
           id_visitante=frame.tabla_visitantes.item(frame.tabla_visitantes.selection())['text']
           entrada = Entrada()
           entrada.eliminar_visitante(id_visitante)
           entrada.resetear_contador_visitantes()
           frame.dibujar_tabla()
           frame.id_visitante=None
    def editar(self,frame:Frame_Visitantes):
           frame.id_visitante=frame.tabla_visitantes.item(frame.tabla_visitantes.selection())['text']
           nombrev = frame.tabla_visitantes.item(frame.tabla_visitantes.selection())['values'][0]
           idv = frame.tabla_visitantes.item(frame.tabla_visitantes.selection())['values'][1] 
           horaaenv = frame.tabla_visitantes.item(frame.tabla_visitantes.selection())['values'][2] 
           horasalv = frame.tabla_visitantes.item(frame.tabla_visitantes.selection())['values'][3]
           placav = frame.tabla_visitantes.item(frame.tabla_visitantes.selection())['values'][4] 
           frame.enable_espacios()
           frame.entry_nombre.insert(0,nombrev)
           frame.entry_id.insert(0,idv)
           frame.entry_hora_entrada.insert(0,horaaenv)
           frame.entry_hora_salida.insert(0,horasalv)
           frame.entry_placa.config(state='normal')
           frame.entry_placa.insert(0,placav)  

#implementacion concreta 2
class funcionamiento_residente(funcionamiento):
    def registrar(self, frame: FrameResidentes, entrada: Entrada, id_residente):
           nombre = frame.entry_nombrer.get()
           identificacion = frame.entry_idr.get()
           fecha_entrada = frame.entry_fecha_entrada.get()
           placa = frame.entry_placar.get()
           residencia = frame.entry_residencia.get()
           residente = Residente (residencia, fecha_entrada ,identificacion, nombre,placa)
           entrada = Entrada()  
           if id_residente==None:
              entrada.registrar_residente(residente)
              entrada.cerrar_db()
              frame.dibujar_tabla()
              frame.disable_espacios()
           else:
             entrada.editar_residente(residente,id_residente)
             frame.dibujar_tabla()   
             frame.disable_espacios()
             frame.id_residente=None
    def eliminar(self, frame: FrameResidentes, entrada: Entrada, id_residente):
         id_residente=frame.tabla_residentes.item(frame.tabla_residentes.selection())['text']
         entrada = Entrada()
         entrada.eliminar_residente(id_residente)
         entrada.resetear_contador_residentes()
         frame.dibujar_tabla()
         frame.id_residente=None 
    def editar(self, frame: FrameResidentes):
         frame.id_residente=frame.tabla_residentes.item(frame.tabla_residentes.selection())['text']
         nombrev = frame.tabla_residentes.item(frame.tabla_residentes.selection())['values'][0]
         idv = frame.tabla_residentes.item(frame.tabla_residentes.selection())['values'][1] 
         fechaev = frame.tabla_residentes.item(frame.tabla_residentes.selection())['values'][2] 
         placav = frame.tabla_residentes.item(frame.tabla_residentes.selection())['values'][3]
         residenciav = frame.tabla_residentes.item(frame.tabla_residentes.selection())['values'][4] 
         frame.enable_espacios()
         frame.entry_nombrer.insert(0,nombrev)
         frame.entry_idr.insert(0,idv)
         frame.entry_fecha_entrada.insert(0,fechaev)
         frame.entry_placar.insert(0,placav)
         frame.entry_placar.config(state='normal')
         frame.entry_residencia.insert(0,residenciav)       
                                
        