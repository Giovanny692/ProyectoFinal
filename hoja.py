#este archivo maneja la interfaz
import tkinter as tk

class Hoja():
  def __init__(self):
    root = tk.Tk()
    root.title("Registro")
    self.crear_fmenu(root)
    self.crear_barramenu(root)
    root.mainloop()


  def crear_fmenu(self,root):
    frame = tk.Frame(root)
    frame.config(width=480,height =320)
    frame.pack()

  def crear_barramenu(self,root):
    barra_menu = tk.Menu(root)
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    root.config(menu= barra_menu,width=300,height=300)
    barra_menu.add_cascade(label = "Inicio",menu =menu_inicio)
    menu_inicio.add_command(label = "Hacer algo")