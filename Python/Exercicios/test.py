nota = int(input("VALOR DA NOTA> "))

if nota >= 0 and nota <= 10:
    print(f"A NOTA FOI {nota}")
    
else:
    n = 1 
    while n > 0:
        print("VALOR INVALIDO. TENTE NOVAMENTE.")
        nota = int(input("VALOR DA NOTA> "))
        if nota >= 0 and nota <= 10:
            print(f"A NOTA FOI {nota}")
            n = 0
