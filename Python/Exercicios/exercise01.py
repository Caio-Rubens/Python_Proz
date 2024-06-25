print('-=-=-=-=-=-=Calcular Tributo=-=-=-=-=-')
print('-=-=-=-=-=-=-=Tabela INSS=-=-=-=-=-=-=')
print('Salário --------------------- Aliquota')
print('Até R$ 1412.00 ------------------ 7.5%')
print('De R$ 1412.01 até R$ 2666.68 ---- 9  %')
print('De R$ 2666.69 até R$ 4000.03 ---- 12 %')
print('De R$ 4000.04 até R$ 7786.02 ---- 14 %')
print('')
print('-=-=-=-=-=-=-=-Tabela IR-=-=-=-=-=-=-=')
print('Salário --------------------- Aliquota')
print('Até R$ 2259.20 ------------------   ==')
print('De R$ 2259.21 até R$ 2826.65 --- 7.5 %')
print('De R$ 2826.66 até R$ 3751.05 --- 15  %')
print('De R$ 3751.06 até R$ 4664.68 --- 22.5%')
print('Acima de R$ 4664.68 ------------ 27.5%')
print('')
ValHoras = float(input('Valor recebido por Hora: '))
Horas = int(input('Horas trabalhadas: '))
print("-=" * 20)
print('')

Sal =  ValHoras * Horas
Fgts = 8

if Sal < 2259.20:
    Ir = 0
    IrP = 0

    if Sal <= 1412:
        Inss = Sal / 7.5 
        InssP = 7.5
            
    elif Sal > 1412 and Sal <= 2666.68:
        Inss = Sal / 9 
        InssP = 9

    elif Sal > 2666.68 and Sal <= 4000.03:
        Inss = Sal / 12
        InssP = 12

elif Sal > 2259.20 and Sal <= 2826.65:
    Ir = Sal / 7.5
    IrP = 7.5

    if Sal > 1412 and Sal <= 2666.68:
        Inss = Sal / 9 
        InssP = 9

    elif Sal > 2666.68 and Sal <= 4000.03:
        Inss = Sal / 12
        InssP = 12

elif Sal > 2826.65 and Sal <= 3751.05:
    Ir = Sal / 15
    IrP = 15

    if Sal > 2666.68 and Sal <= 4000.03:
        Inss = Sal / 12
        InssP = 12

elif Sal > 3751.05 and Sal <= 4664.68:
    Ir = Sal / 22.5
    IrP = 22.5

    if Sal > 2666.68 and Sal <= 4000.03:
        Inss = Sal / 12
        InssP = 12
        
    elif Sal > 4000.03 and Sal <= 7786.02:
        Inss = 14
        InssP = 14

elif Sal > 4664.68:
    Ir = Sal / 27.5
    IrP = 27.5

    if Sal > 4000.03 and Sal <= 7786.02:
        Inss = Sal / 14
        InssP = 14

    elif Sal > 7786.02:
        Inss = 0
        InssP = 0
TotImposto = Sal / Fgts + Inss + Ir

print(f'Salario Bruto ({Horas}hrs x R${ValHoras:.2f}): R${Sal:.2f}')
print(f'FGTS ({Fgts}%): R${Sal / Fgts:.2f}')
print(f'INSS ({InssP}%): R${Inss:.2f}')
print(f'IR ({IrP}%): R${Ir:.2f}')
print(f'Total Tributo: R${TotImposto:.2f}')
print(f'Valor Liquido: R${Sal - TotImposto:.2f}')