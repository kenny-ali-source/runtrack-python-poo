class Operation: 
    def __init__(self, nombre1=12, nombre2 =3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    
operation_instance = Operation()
print(f"le nombre1 est {operation_instance.nombre1}")
print(f"le nombre2 est {operation_instance.nombre2}")