notas = []
for n in range(10):
    nota = float(input('Informe a nota: '))
    notas.append(nota)

print(notas)

for i in notas:
    if i >= 7:
        print(f'Nota: {i} \nAprovado!!')
    elif 5 <= i < 7:
        print(f'Nota: {i} \nRecuperação!!')
    else:
        print(f'Nota: {i} \nReprovado...')