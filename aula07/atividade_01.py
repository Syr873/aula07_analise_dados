lista_nota = []

for notas in range(5):
    nota = float(input('Informe a nota: '))
    lista_nota.append(nota)

print(f'As notas são: \n{lista_nota}')

for n in lista_nota:
    if n >= 7:
        print(f'Nota: {n} \nAprovado!')
    else:
        print(f'Nota: {n} \nReprovado!')

