print("CAUCULADOR DE DESCONTO\n")


try:
    idade = float(input('Quantos anos você tem? '))
except ValueError:
    print('Escreva sua idade apenas com numeros.')

else:

    verif_student = input('você é estudante? (sim/não) ').lower()
    verif_cumpom = input('você tem desconto? (sim/não) ').lower()

if idade <= 12:
    preco = 10.00

elif idade <= 17:
    preco = 15.00

elif idade <= 59:
    preco = 30.00

elif idade <= 110:
    preco = 12.00

else:
    print('Essa idade não existe.')

preco_com_desconto = preco


if verif_student in ['sim', 's']:
    preco_com_desconto = preco * (1 - 0.50)
    print('linha 34', preco_com_desconto)

if verif_cumpom in ['sim', 's']:
    preco_com_desconto = preco_com_desconto * (1 - 0.20)
    print('linha 38', preco_com_desconto)

preco_final = round(preco_com_desconto, 2)


print(f'valor final do ingresso é de R${preco_final}')


print(f'valor final do ingresso é de R${preco_final}')
