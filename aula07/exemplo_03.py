lista_numeros = []

for n in range(5):
    num = float(input('Informe o número: '))
    lista_numeros.append(num)

print(lista_numeros[0]) #Imprime o item da posição 0
lista_numeros[0] = 22 #Altera a posição zero
lista_numeros.pop() #Deleta o ultimo valor
# lista_numeros.pop(-2) #Deleta o penultimo valor
lista_numeros.remove(30) #Deleta pelo valor
# del lista_numeros[0] #Remove o item da posição informada -- se o indice nao for informado, del irá deletar a variável lista!!
lista_numeros.clear()
print(lista_numeros)

