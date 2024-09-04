arquivo = open('arqtext.txt', 'w')

arquivo.write('curso Python \n')
arquivo.write('Aula Pratica')
arquivo.close()

#leitura do arquivo texto

leitura=open('arqText.txt', 'r')
print(leitura.read()) 
leitura.close()