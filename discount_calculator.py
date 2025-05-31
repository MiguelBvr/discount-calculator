print("CAUCULADOR DE DESCONTO\n")


try:
    idade = float(input('Quantos anos você tem? '))
except ValueError:
    print('Escreva sua idade apenas com numeros.')

else:

    verif_student = input('você é estudante? ').lower()
    verif_cumpom = input('você tem desconto? ').lower()

if idade <= 12:
    preco = 10.00

elif idade <= 17:
    preco = 15.00

elif idade <= 59:
    preco = 30.00

else:
    preco = 12.00

preco_com_desconto = preco

if verif_student in ['sim', 'Sim', "SIM"]:
    preco_com_desconto = preco * (1 - 0.50)

    if verif_cumpom in ['sim', 'Sim', "SIM"]:
        preco_com_desconto = preco * (1 - 0.20)

    if verif_student and verif_cumpom in ['sim', 'Sim', "SIM"]:
        preco_com_desconto = preco * (1 - 0.70)

preco_final = round(preco_com_desconto, 2)


print(f'valor final do ingresso é de R${preco_final}')
