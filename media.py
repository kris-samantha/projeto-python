notaA=float(input("informe a primeira nota: "))
notaB=float(input("informe a segunda nota: "))

#cacular media
mediafinal= (notaA + notaB) /2

#Verificação
if mediafinal >=7.0:
    print("A media: %.1f - Apovado "% mediafinal)
else:
    print("A media: %.1f - Reprovado " % mediafinal)