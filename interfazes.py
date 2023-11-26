import tkinter as tk
from productos import Frame,FrameResidentes,Frame_Visitantes
from fabricasproductos import factory,factory_residentes,factory_visitantes

class Hoja(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registro")
        self.geometry("1300x650")
        self.frame=None
        self.crear_barra_menu()
        self.mostrar_visitantes()
        self.mainloop()
    
    def crear_barra_menu(self):
        barra_menu = tk.Menu(self)
        menu_inicio = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label = "Inicio",menu =menu_inicio)
        self.config(menu= barra_menu,width=300,height=300)
        menu_inicio.add_command(label = "Visitantes",command=self.mostrar_visitantes)
        menu_inicio.add_command(label= 'Residentes',command=self.mostrar_residentes)    
        
    def mostrar_visitantes(self):
        self.frame = self.obtener_frame()
        f_visitantes=factory_visitantes()
        self.frame=f_visitantes.retornar_producto(self)
        self.frame.pack()
    
    def mostrar_residentes(self):
        self.frame=self.obtener_frame()
        f_residentes=factory_residentes()
        self.frame=f_residentes.retornar_producto(self)
        self.frame.pack()       
    
    #singleton para que solo haya un frame
    def obtener_frame(self):
        if(self.frame==None):
            self.frame=Frame(self)
        else:
            self.frame.destroy()    
        return    


