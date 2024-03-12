# Crear clase 
class Personaje():
    # Metodo constructor, considera parametros y valores a atributos de instancia
    def __init__(self, nombre): 
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0
    
    # definir getter para que me muestre los resultados de nombre, nivel y experiencia     
    @property
    def estado(self):
        return f"NOMBRE: {self.nombre} \
        NIVEL: {self.nivel} \
        EXP: {self.experiencia}"
        
    # definir Setter de estado para recibir la experiencia como si fuese un parametro (variable temporal que almacenara la experiencia)
    @estado.setter
    def estado(self, exp):
        # experiencia que tiene más la que le demos 
        tmp_exp = self.experiencia + exp
        #mientras la variable temporal tmp_exp sea mayor igual a 100 le sumamos 1 al nivel
        while tmp_exp >= 100:
            self.nivel += 1
            tmp_exp -= 100
        # si la variable tmp_exp es negativa le restamos 
        while tmp_exp < 0:
            if self.nivel > 1:
                tmp_exp = 100 + tmp_exp
                self.nivel -= 1
            else:
                tmp_exp = 0
        self.experiencia = tmp_exp
        
    #metodo para comprobar si el menor que. (__lt__)("simular sobrecarga")
    def __lt__(self, other):
        return self.nivel < other.nivel
    
    #metodo para comprobar si es mayor que. (__gt__)
    def __gt__(self, other):
        return self.nivel > other.nivel
    
    #metodo para comprobar que sea igual que.
    def __eq__(self, other):
        return self.nivel == other.nivel

    #probabilidad de ganar frente al orco
    def get_probabilidad_ganar(self, other):
        if self < other:
            return 0.33
        elif self > other:
            return 0.66
        else:
            return 0.5

    @staticmethod
    def mostrar_dialogo_opcion(probabilidad_ganar):
        return int(input(
            f"\nCon tu nivel actual, tienes {probabilidad_ganar * 100}% "
            "de probabilidades de ganarle al Orco.\n"
            "\nSi ganas, ganarás 50 puntos de experiencia y el orco perderá 30. \n"
            "Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.\n"
            "\n¿Qué deseas hacer?\n"
            "1. Atacar\n"
            "2. Huir\n"
        ))        