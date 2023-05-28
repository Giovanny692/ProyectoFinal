#esta clase generar las novedades en forma de txt
import tkinter as tk
import random
class Novedad():
    def __init__(self,root):
        self.contador_archivos=0
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
        boton_crear = tk.Button(self.frame_novedad, text = 'Crear Novedad',command=self.crear_novedad)
        boton_crear.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#FF5733', cursor='hand2', activebackground='#35BD6F')
        boton_crear.grid(row =2, column=0, padx=10, pady=10)
    
    def crear_novedad(self):
         self.contador_archivos=self.contador_archivos+1
         nombre_archivo='novedades/novedad'+str(self.contador_archivos)+'.txt'
         try:   
          archivo = open(nombre_archivo,'x')
          archivo.write(self.entry_novedad.get("1.0","end-1c"))
          archivo.close
         except: 
          nombre_archivo='novedades/novedad'+str(random.randint(self.contador_archivos,100))+'.txt' 
          archivo = open(nombre_archivo,'x')
          archivo.write(self.entry_novedad.get("1.0","end-1c"))
          archivo.close  
        
        
    def borrar_frame_novedad(self):
        self.frame_novedad.destroy()    