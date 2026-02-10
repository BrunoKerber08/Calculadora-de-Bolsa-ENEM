nota = int(input('Qual foi sua nota do ENEM?: '))
valor_curso = int(input('Qual o valor integral do curso desejado? : '))
valor60 = valor_curso * 40 / 100
valor80 = valor_curso * 20 / 100

if nota >= 800:
    print('Meus parabéns, você conseguiu bolsa integral')
elif nota >= 600:
    print(f'Parabéns, aluno, você conseguiu 80% de bolsa, de R${valor_curso} por R${valor80}')
elif nota >= 400:
    print(f'Parabéns, você conseguiu 60% de bolsa, de R${valor_curso} por R${valor60}')
else:
    print('Você não foi pré-selecionado')