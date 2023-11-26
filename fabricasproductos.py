from productos import Frame,Frame_Visitantes,FrameResidentes

class factory():
    def retornar_producto(root):
        pass
    
class factory_visitantes(factory):
    def retornar_producto(self,root):
        return Frame_Visitantes(root)    


class factory_residentes(factory):
    def retornar_producto(self,root):
        return FrameResidentes(root)