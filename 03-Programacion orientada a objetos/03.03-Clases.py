import datetime

class Alumno:
    """Comentario de uso de la clase"""
    #Variable o propiedades de la clase
    Nombre = None
    Apellido1 = None
    Apellido2 = None
    FechaNacimiento = None

    #Funcion constructura que se ejecuta al crear (instanciar) el objeto
    #self, es una variable que representa al mismo objeto
    def __init__(self, nombre, apellido1, apellido2 = "") -> None:
       self.Nombre = nombre
       self.Apellido1 = apellido1
       self.Apellido2 = apellido2

    #Otras funciones del objeto
    def getNombreCompleto(self) -> str:
        return f"{self.Nombre} {self.Apellido1} {self.Apellido2}"
    
    def setFechaNacimiento(self,fecha) -> bool:
        try:
            if(len(fecha) == 10):
                self.FechaNacimiento = datetime.strptime(fecha,"%d-%m-%Y").date()
            else:
                self.FechaNacimiento = datetime.strptime(fecha,"%d-%m-%y").date()
            return True
        
        except:
            return False
        
    def getEdad(self) -> int:
        if (self.FechaNacimiento == None):
            return -1
        else:
            return datetime.now().year - self.FechaNacimiento
        
# Creamos objetos
alumno = Alumno("Borja", "Cabeza", "Rozas")
alumno2 = Alumno("Luis","Echeverry")

print(f"Me llamo: {alumno.Nombre} {alumno.Apellido1} {alumno.Apellido2}")
print(f"Me llamo: {alumno.getNombreCompleto()}")

resultado = alumno.setFechaNacimiento ("01-01-00")
print(alumno.setFechaNacimiento ("01-01-00"))
resultado = alumno.setFechaNacimiento ("01-01-00")

