#este archivo maneja la interfaz
import tkinter as tk

class Hoja():
  def __init__(self,root = None):
    root = tk.Tk()
    root.title("Registro")
    root.geometry("800x480")
    self.crear_fmenu(root)
    self.crear_barramenu(root)
    self.poner_campos()
    root.mainloop()


  def crear_fmenu(self,root):
    self.frame = tk.Frame(root)
    self.frame.pack()

  def crear_barramenu(self,root):
    barra_menu = tk.Menu(root)
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    root.config(menu= barra_menu,width=300,height=300)
    barra_menu.add_cascade(label = "Inicio",menu =menu_inicio)
    menu_inicio.add_command(label = "Hacer algo")

  def poner_campos(self):
     #nombre
     label_nombre = tk.Label(self.frame, text='Nombre: ')
     label_nombre.config(font= (('Arial', 12, 'bold')))
     label_nombre.grid(row = 0, column=0, padx= 10, pady=10)
     #Duracion
     label_duracion = tk.Label(self.frame, text='Id: ')
     label_duracion.config(font= (('Arial', 12, 'bold')))
     label_duracion.grid(row = 1, column=0, padx= 10, pady=10)
     #Genero
     label_genero = tk.Label(self.frame, text='Hora: ')
     label_genero.config(font= (('Arial', 12, 'bold')))
     label_genero.grid(row = 2, column=0, padx= 10, pady=10)

     #Entrada de cada campo
     #Nombre
     entry_nombre = tk.Entry(self.frame)
     entry_nombre.config(width= 25, state= 'disabled' ,font= (('Arial', 12)))
     entry_nombre.grid(row = 0, column=1, padx= 10, pady=10)

     #Duracion
     entry_duracion = tk.Entry(self.frame)
     entry_duracion.config(width= 25, state= 'disabled' ,font= (('Arial', 12)))
     entry_duracion.grid(row = 1, column=1, padx= 10, pady=10)
     #Genero
     entry_genero = tk.Entry(self.frame)
     entry_genero.config(width= 25, state= 'disabled' ,font= (('Arial', 12)))
     entry_genero.grid(row = 2, column=1, padx= 10, pady=10)
        
        
     #Botones
     boton_nuevo = tk.Button(self.frame, text = 'Nuevo')
     boton_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_nuevo.grid(row =4, column=0, padx=10, pady=10)

     boton_guardar = tk.Button(self.frame, text = 'Guardar')
     boton_guardar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_guardar.grid(row =4, column=1, padx=10, pady=10)
    
     boton_cancelar = tk.Button(self.frame, text = 'Cancelar')
     boton_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
     boton_cancelar.grid(row =4, column=2, padx=10, pady=10)

    

  