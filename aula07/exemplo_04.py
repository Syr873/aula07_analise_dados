# Dicionario
# Estrutura chave e valor
# Símbolo {}

# notas = {} # Dicionário vazio
# notas ['Matemática'] = 8.5
# notas['Português'] = 7.0
# notas['História'] = 9.2


# notas['Geografia'] = 9.9 # Adicionar ['Novo item'] = valor do item
# notas('Matemática') = 8.0 # Alterar ['Item existente'] = novo valor
# del notas['História'] # Deleta um item do dicionário
# print(notas)


# Criando cadastro em dicionários
livros = {}
lista_cadastro = []

for i in range(3):
    print(30*'=')
    titulo = input('\nInforme o título do livro: ')
    autor = input('\nInforme o nome do autor: ')
    ano = int(input('\nInforme o ano: '))
    genero = input('\nInforme o gênero do livro: ')

    livros = {
        'Título':titulo, 
        'Autor': autor,
        'Ano': ano,
        'Gênero': genero
    }

    lista_cadastro.append(livros)
    print(f'\nLivro {i + 1} Cadastrado!')



