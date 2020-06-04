class Encuesta:

    def __init__(self, titulo, preguntas, respuestas):
        self.titulo = titulo
        self.preguntas = preguntas
        self.respuestas = respuestas
        pass
    
    def header(self):

        tituloin = input("Ingrese el Titulo:\n")

    def preguntas(self):

        listapreguntas = []
        preguntain = input("pregunta:\n")
        listapreguntas.append(preguntain)
        Encuesta.respuestas(input)

    def respuestas(self):

        listarespuestas = []
        respuestain = input("Respuesta:\n")
        listarespuestas.append(respuestain)
        continuar = input("Desea agregar otra respuesta?")

        if continuar == "si":
            Encuesta.respuestas(input)
        
        else:
            pass


    

print("Desea crear una encuesta?")

ingreso = input()

if ingreso.lower() == "si":
    Encuesta.header(input)
else:
    print("Adios!")

print("Comenzamos")

Encuesta.preguntas(input)














