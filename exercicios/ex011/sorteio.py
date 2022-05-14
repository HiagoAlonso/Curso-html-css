from random import randint

numero = randint(1, 3)

if numero == 1:
    escolhido = "Daniel"
elif numero == 2:
    escolhido = "Débora"
elif numero == 3:
    escolhido = "Matheus"

print(f' O número sorteado foi {numero} e o escolhido(a) foi {escolhido}')
