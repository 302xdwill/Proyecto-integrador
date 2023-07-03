class Persona:
    """clase que implementa persona"""
    def _init_(self, dni, nombres, apellidos, edad, saldo, correo_electronico, direccion, telefono):
        self.dni= dni
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad 
        self.saldo = saldo
        self.correo_electronico = correo_electronico
        self.direccion = direccion 
        self.telefono = telefono
    
    def convertir_a_string(self):
        return "| {} | {} | {} | {} | {} | {} | {} | {} |".format(self.dni, 
                                                            self.nombres,
                                                            self.apellidos,
                                                            self.edad,
                                                            self.saldo,
                                                            self.correo_electronico,
                                                            self.direccion,
                                                            self.telefono)