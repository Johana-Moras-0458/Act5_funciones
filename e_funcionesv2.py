print("funciones creadas por el usuario")
#las funciones 
def mi_lista():
    print("--amigos de navita con lista--")
    amigos=["homero","paty","lety"]
    for nava in amigos:
        print(nava)
#tupla
def mi_tupla():
    print("--amigos de navita con tupla--")
    amigos=["homero","lety","paty"]
    for navitaa in amigos:
        print(navitaa)
#conjunto
def mi_conjunto():
    print("--amigos de navita con conjunto--")
    amigos={"homero","paty","lety"}
    for NAVA in amigos:
        print(NAVA)
#diccionario
def mi_diccionario():
    print("--amigos de navita con diccionario--")
    amigos={
        "amigo_1": "lety",
        "amigo_2": "paty",
        "amigo_3": "homero"
    }
    for navita in amigos:
        print(amigos[navita])
#llamadas a funciones
mi_lista()
mi_tupla()
mi_conjunto()
mi_diccionario()