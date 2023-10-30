#O cardápio de uma casa de lanches, especializada em sanduíches, é dado abaixo.
#CÓDIGO  PRODUTO         PREÇO (R$)
#H       Hamburger       5.50
#C       Cheeseburger    6.80
#M       Misto Quente    4.50
#A       Americano       7.00
#Q       Queijo Prato    4.00
#X       PARA TOTAL DA CONTA
#Escreva um programa que leia o código e a quantidade de cada item comprado por um freguês, calcule e exiba o total a pagar. 
# Obs: A leitura do código 'X' indica o fim dos itens.


valor_total = 0.0
while True:
    print('CÓDIGO  PRODUTO         PREÇO (R$)')
    print('H       Hamburger       5,50')
    print('C       Cheeseburger    6,80')
    print('M       Misto Quente    4,50')
    print('A       Americano       7,00')
    print('Q       Queijo Prato    4,00')
    print('X       PARA TOTAL DA CONTA')

    codigo = input().upper().strip()
    if codigo == 'X':
        break  
    if codigo == 'H':
        valor_total += 5.50
    if codigo == 'C':
        valor_total += 6.80
    if codigo == 'M':
        valor_total += 4.50
    if codigo == 'A':
        valor_total += 7.00
    if codigo == 'Q':
        valor_total += 4.00

print(f'{valor_total:.2f}')
