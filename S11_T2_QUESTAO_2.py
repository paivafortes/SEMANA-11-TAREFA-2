#Escreva um programa que, para um número indeterminado de pessoas:
#leia a idade de cada pessoa, sendo que a leitura da idade 0 (zero) indica o fim dos dados (flag) e não deve ser considerada;
# calcule e escreva o número de pessoas;
# calcule e escreva a idade média do grupo;
# calcule e escreva a menor idade e a maior idade.
pessoas = 0
m_idade = 0
maior_idade = -1
menor_idade = float('inf')
while True:
    idade= int(input())
    if idade == 0:
        break
    pessoas += 1
    m_idade += idade
    
    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade

media= m_idade / pessoas
print(f'{pessoas}')
print(f'{media:.2f}')
print(f'{menor_idade}')
print(f'{maior_idade}')

