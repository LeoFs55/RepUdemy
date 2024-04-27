num = int(input("Verificar numeros primos ate: "))
multiplos=0
for count in range(2,num):
    if (num % count == 0):
        multiplos += 1
if (num == 1):
    print("Não é primo")
else:
    if(multiplos==0):
        print("É primo")
    else:
        print("Não é primo")