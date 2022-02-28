print('=' * 30)
print('{:^33}'.format('Banco Python'))
print('=' * 30)
valor = int(input('Qual valor você quer sacar? R$'))
total = valor
cédula = 50
totalcédula = 0
while True:
    if total >= cédula:
        total -= cédula
        totalcédula += 1
    else:
        if totalcédula > 0:
            print(f'Total de{totalcédula} cédulas de R$ {cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
             cédula = 2
             totalcédula = 0
             if total == 0:
                break
