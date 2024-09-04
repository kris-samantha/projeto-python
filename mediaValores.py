def lernotas():
    n=float(input("digite uma nota para o aluno(a):"))
    return n 


def resultado(n1, n2):
    media=(n1+n2)/2
    print("Nota 1: ", n1)
    print("Nota 2:", n2)
    print("Media: ", media, "resultado:", end="")
    if media >=7:
        print("Aprovado")
    else:
        print("reprovado")


a= lernotas()
b= lernotas()
resultado(a,b)