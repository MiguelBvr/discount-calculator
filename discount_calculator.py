print("CAUCULADORA DE DESCONTO\n")


try:
    idade = float(input('Quantos anos você tem? '))
except ValueError:
    print('Escreva sua idade apenas com numeros.')



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

verif_student = input('você é estudante? (sim/não) ').lower()
if verif_student not in ['sim', 's', 'não', 'n']:
        print('Apenas sim e não')
else:

    verif_cumpom = input('você tem desconto? (sim/não) ').lower()
    if verif_cumpom not in ['sim', 's', 'não', 'n']:
            print('Apenas sim e não')
    else:

        preco_com_desconto = preco

        if verif_student in ['sim', 's']:
                preco_com_desconto = preco * (1 - 0.50)

        if verif_cumpom in ['sim', 's']:
                preco_com_desconto = preco_com_desconto * (1 - 0.20)

        preco_final = round(preco_com_desconto, 2)

        print(f'valor final do ingresso é de R${preco_final}')

