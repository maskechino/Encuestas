class Encuesta:

    def __init__(self, titulo, listadepreguntas):
        self.titulo = titulo #titulo de la encuesta#
        self.listado = listado #lista de preguntas con sus respectivas respuestas#

    def imprimirencuesta(self):
        print(self.listado)
    
class Preguntayrespuestas:
    def __init__(self, pregunta, respuestas):
      self.pregunta = pregunta
      self.respuestas = respuestas

class Listado:
    def  __init__ (self, listado):
        self.listado = listado

titulo = input("ingresa el titulo:\n")


pregunta = input("Ingresa tu pregunta:")
respuestas = []
listado = []
contador = 0

preguntayrespuestas = Preguntayrespuestas(pregunta, respuestas)


for i in range(1, 5):
    print("ingresa respuesta")
    respuesta = input()
    respuestas.append(respuesta)
    contador = contador + 1

else:
    print("Alcanzaste el maximo de respuestas")
    listado.append(preguntayrespuestas)
    continuar = "si"
    while input("Desea continuar con otra pregunta?:") == continuar:
        contador = 0
        pregunta = input("ingresa otra pregunta:")
        respuestas = []
        for i in range(1, 5):
            print("ingresa respuesta")
            respuesta = input()
            respuestas.append(respuesta)
            contador = contador + 1
        else:
            listado.append(preguntayrespuestas)

listado = Listado(listado)




encuestanueva = Encuesta(titulo, listado)



print(listado)