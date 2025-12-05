previsoes = ['Ensolarado', 'Nublado', 'Chuvoso', 'Tempestade', 'Ensolarado']
print(previsoes)

previsao_feliz = 'Ensolarado'

for p in previsoes:
    #print(p)
    if p == previsao_feliz:
        print('Dia bom! Aproveite pra passear.')
    else:
        print('Dia ruim! Leve um guarda-chuva.')