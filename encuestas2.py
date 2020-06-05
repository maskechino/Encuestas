

class Encuesta:

    def __init__(self):
        pass


    def nuevaencuesta(self, titulo, listado):
        self.titulo = titulo
        self.listado = listado #listado de preguntas con sus respuestas

    def imprimirtitulo(self):
        print(self.titulo)


encuesta = Encuesta()


encuesta.titulo = input("Ingresar titulo:\n")

ingresarPregunta = input("Desesa ingresar una pregunta?:")

while ingresarPregunta == "si":
    pregunta = input("Ingrese pregunta:\n")
    continuar = "si"
    indice = 0

    while indice < 4 and continuar == "si":
        respuesta = input("Ingrese respuesta:\n")
        continuar = input("Desea ingresar otra respuesta:\n")
        indice = indice + 1
    ingresarPregunta = input("Desea agregar otra pregunta?\n")

encuesta.imprimirtitulo()




if __name__ == "__main__":
    print("ok")
    pass



