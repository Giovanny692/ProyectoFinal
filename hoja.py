#este archivo maneja la interfaz
import tkinter as tk

class Hoja():
  def __init__(self,root = None):
    self.root = tk.Tk()
    self.root.title("Registro")
    self.root.geometry("800x600")
    self.frame=None
    self.frameresidentes=None
    self.crear_fmenu()
    self.crear_barramenu(root)
    self.root.mainloop()


  def crear_fmenu(self):  
    if (self.frame==None and self.frameresidentes==None):      
     self.frame = tk.Frame(self.root)
     self.poner_campos()
     self.frame.pack()
    else:
     if (self.frameresidentes!=None):     
      self.frameresidentes.destroy()
      self.frameresidentes=None
      self.frame = tk.Frame(self.root)
      self.poner_campos()
      self.frame.pack()

    
  def crear_listaresidentes(self): 
    if (self.frameresidentes==None): 
     self.frame.destroy()  
     self.frameresidentes = tk.Frame(self.root) 
     label_ejemplo=tk.Label(self.frameresidentes,text='Algo')
     label_ejemplo.config(font= (('Arial', 12, 'bold')))
     label_ejemplo.grid(row = 0, column=0, padx= 10, pady=10)
     self.frameresidentes.pack()
     self.frame=None

  def crear_barramenu(self,root):
    barra_menu = tk.Menu(root)
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    self.root.config(menu= barra_menu,width=300,height=300)
    barra_menu.add_cascade(label = "Inicio",menu =menu_inicio)
    menu_inicio.add_command(label = "Registrar persona",command=self.crear_fmenu)
    menu_inicio.add_command(label="ver lista de residentes",command=self.crear_listaresidentes)

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
     self.entry_nombre = tk.Entry(self.frame)
     self.entry_nombre.config(width= 25, state= 'disabled' ,font= (('Arial', 12)))
     self.entry_nombre.grid(row = 0, column=1, padx= 10, pady=10)
     #ID
     self.entry_id= tk.Entry(self.frame)
     self.entry_id.config(width= 25, state= 'disabled' ,font= (('Arial', 12)))
     self.entry_id.grid(row = 1, column=1, padx= 10, pady=10)
     #Hora entrada
     self.entry_hora_entrada = tk.Entry(self.frame)
     self.entry_hora_entrada.config(width= 25, state= 'disabled' ,font= (('Arial', 12)))
     self.entry_hora_entrada.grid(row = 2, column=1, padx= 10, pady=10)
     #Hora salida
     self.entry_hora_salida = tk.Entry(self.frame)
     self.entry_hora_salida.config(width= 25, state= 'disabled' ,font= (('Arial', 12)))
     self.entry_hora_salida.grid(row = 3, column=1, padx= 10, pady=10)
     #Placa vehiculo
     self.entry_placa=tk.Entry(self.frame)
     self.entry_placa.config(width= 25, state= 'disabled' ,font= (('Arial', 12)))
     self.entry_placa.grid(row = 5, column=1, padx= 10, pady=10)
        
        
     #Botones
     boton_nuevo = tk.Button(self.frame, text = 'Nuevo',command=self.enable_espacios)
     boton_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_nuevo.grid(row =6, column=0, padx=10, pady=10)

     boton_guardar = tk.Button(self.frame, text = 'Guardar')
     boton_guardar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_guardar.grid(row =6, column=1, padx=10, pady=10)
    
     boton_cancelar = tk.Button(self.frame, text = 'Cancelar')
     boton_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_cancelar.grid(row =6, column=2, padx=10, pady=10)
  
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
      

    

  