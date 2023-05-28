#esta clase generar las novedades en forma de txt
import tkinter as tk
class Novedad():
    def __init__(self,root):
        self.crear_frame_novedad(root)
    
    def crear_frame_novedad(self,root):
        self.frame_novedad = tk.Frame(root)
        self.poner_espacios()
        self.frame_novedad.pack()   
    def poner_espacios(self):
        label_titulo=tk.Label(self.frame_novedad,text='Hacer novedad') 
        label_titulo.config(font= (('Arial', 12, 'bold')))
        label_titulo.grid(row = 0, column=0, padx= 10, pady=10)
        self.entry_novedad=tk.Text(self.frame_novedad,width=100,height=25)
        scroll = tk.Scrollbar(self.frame_novedad,orient='vertical',command=self.entry_novedad.yview)
        self.entry_novedad.configure(yscrollcommand=scroll.set)
        self.entry_novedad.grid(row=1,column=0,padx=10,pady=10,sticky='nse')
        scroll.grid(row=1,column=5,sticky='nse')
        
        
    def borrar_frame_novedad(self):
        self.frame_novedad.destroy()    