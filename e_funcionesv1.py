print("manejo de funciones V1")
def hola_mundo():
    print("hola aqui estoy dentro de la funcion")

def mensa(msg):
    print(msg )  
def escribeNC(nombre,apellido):
    print(nombre,apellido)
    print(f"tu nombre completo es  {nombre}{apellido}")
def suma2numeros(n1,n2):
    s= n1 + n2
    return f"la suma de {n1} y de {n2} es de:",s
    print(f"la suma de {n1} + {n2} es {s}") 
# llamando a la función
hola_mundo()
mensa("hola WhatsAPP")  #llama a mensa con 1 parametro
mensa("el profe me sorprendio enviando mensajes") #llama a la mensa con 1p
escribeNC("johana","moras martinez")
print("funciones que regresan valores")
print(suma2numeros(7,3))
print(suma2numeros(15,45))


