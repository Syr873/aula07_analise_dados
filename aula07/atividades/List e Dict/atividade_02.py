# Dicionário de amigos
# amigos = {}
# amigos['João'] = 20 
# amigos['Maria'] = 22
# amigos['Carlos'] = 19

# print(f'A idade de Maria é: \n {amigos['Maria']}')

# amigos['Carlos'] = 20

# amigos['Ana'] = 21
# del amigos['João']
# print(amigos)


# Dicionário de Compras

# produtos = {}
# produtos['Arroz'] = 25.90
# produtos['Feijão'] = 8.50
# produtos['Leite'] = 5.80

# print(f'Preço do arroz é :\n{produtos['Arroz']:.2f}')

# produtos['Leite'] = 4.00
# produtos['Açúcar'] = 6.30
# del produtos['Feijão']

# print(produtos)


# Dicionário candidatos

# candidatos = []
# info_cadidatos = {}

# for i in range(5):
#     print(30*'=')
#     print(f'Candidato {i+1}:')
#     nome = input('\nInforme o nome do candidato: ')
#     idade = int(input('\nInforme a idade: '))
#     tel = int(input('\nInforme o telefone: '))
#     email = input('\nInforme o email: ')
#     formacao = input('\nInforme a formação acadêmica: ')

#     info_cadidatos = {
#         'Nome' : nome,
#         'Idade' : idade,
#         'Telefone' : tel,
#         'E-mail' : email,
#         'Formação Acadêmica' : formacao
#     }

#     candidatos.append(info_cadidatos)

# print(candidatos)


# Seleção de Atletas
classificados = []
atleta = {}
for i in range(5):
    print(50*'-')

    print(f'Atleta {i+1}: ')
    
    nome = input('\nInforme o nome do atleta: ')
    tempo = int(input('\nInforme o tempo: '))
    categoria = input('\nInforme a categoria: ')

    atleta = {
        'Nome do atleta' : nome,
        'Tempo nos 100 metros(segundos)' : tempo,
        'Categoria' : categoria
    }
    if tempo <= 12:
        print(f'Atleta: {nome} \nClassificado!')
        classificados.append(atleta)
    else:
        print(f'Atleta: {nome} \nDesclassificado!!')

print(f'Atletas classificados: \n {classificados}')
    






