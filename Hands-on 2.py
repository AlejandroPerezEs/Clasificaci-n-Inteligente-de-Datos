#Pérez Escobar Alejandro



class RegresionLineal:
    def __init__(self):
        self.y = [2, 4, 6, 8, 10, 12, 14, 16, 18] # Valores de y
        self.x = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Valores de x
        self.b0 = None  # Beta 0
        self.b1 = None  # Beta 1

    def calcular_regresion(self): #Calcular los valores de beta 1 y beta 0
    
        n = len(self.x) # Calcular la longitud de x

        #Calcular las sumatoria
        sumatoriaXcuadrada = sum(x**2 for x in self.x)
        sumatoriaY = sum(self.y)
        sumatoriaX = sum(self.x)
        sumatoriaXY = sum(x * y for x, y in zip(self.x, self.y))
        
        divisor = (n * sumatoriaXcuadrada - pow(sumatoriaX,2))
        self.b0 = (sumatoriaXcuadrada * sumatoriaY - sumatoriaX * sumatoriaXY) / divisor
        self.b1 = (n * sumatoriaXY - sumatoriaX * sumatoriaY) / divisor

        return self.b0 , self.b1
    

    def predecir(self):
        if self.b0 is None or self.b1 is None:
            raise ValueError("Primero debes calcular la regresión.")
        else:
            valor = int(input('Ingresa el valor a predecir: '))
            prediccion = (self.b0 + self.b1 * valor)
            print(f'Y = β\u2080 + β\u2081x\u2081 \nY = {self.b0:.2f} + {self.b1:.2f}({valor})\nY = {prediccion:.2f}')



# Crear la instancia de la clase
modelo = RegresionLineal()
modelo.calcular_regresion()
modelo.predecir()
