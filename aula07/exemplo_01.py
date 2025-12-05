#Listas
#Sâo variáveis compostas para armazenamento de mais de uma informação por vez.
#É caracterizada no Python por []
#Por convenção, usamos o nome das listas no PLURAL. É opcional o prefixo "list", "lst"

list_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho']

print(list_meses[0]) # primeiro
print(list_meses[-1]) # último
print(list_meses[1:4]) # Imprime a partir do indice 1 até o indice 3(4-1)
print(list_meses[2:]) #Imprime a partir do indice 2 até o final!
print(list_meses[:5]) #Imprime do inicio até o indice 5-1
print(list_meses[0:6:2]) #Imprime do indice 0 até o indice 6-1 pulando 2