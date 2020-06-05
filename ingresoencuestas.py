class Encuesta:

    def __init__(self, titulo, listadepreguntas):
        self.titulo = titulo #titulo de la encuesta#
        self.listadepreguntas = listadepreguntas #lista de preguntas con sus respectivas respuestas#

    def imprimirencuesta(self):
        print(self.titulo , self.listadepreguntas)
    
class preguntayrespuestas:
    def __init__(self, pregunta, respuestas):
      self.pregunta = pregunta
      self.respuestas = respuestas
    def agregarpregunta(self):
        input("agregar")




class lista:
    def __init__(self):
        self.pregunta = pregunta
        self.respuestas = respuestas
        listado = []
        pregunta = input("Ingresa tu pregunta:")
        respuestas = []
        contador = 0
        while contador < 4:
            respuesta = input("ingresa tu respuesta:")
            respuestas.append(respuesta)
            contador = contador + 1

        else:
            print("Alcanzaste el maximo de respuestas")
            listado.append(pregunta)
            listado.append(respuestas)
            continuar = "si"
            while input("Desea continuar con otra pregunta?:") == continuar:
                contador = 0
                pregunta = input("ingresa otra pregunta:")
                respuestas = []
                while contador < 4:
                    respuesta = input("ingresa tu respuesta:")
                    respuestas.append(respuesta)
                    contador = contador + 1
                else:
                    listado.append(pregunta)
                    listado.append(respuestas)


