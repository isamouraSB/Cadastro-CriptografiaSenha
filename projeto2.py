# projeto 2 ("Gerador de senhas Python")
#maiúscula e minuscula
#símbolod e espeços

"""
Security = chave
5ecur1ty = senha

hex 
1 = 1
2 = 2
até 9 = 9
10 = A
11 = B
12 = C
13 = D
14 = E
15 = F
16 = I
17 = M
18 = R
19 = S
20 = U

"""

chave = input("Digite a sua senha: ")

senha = ""
for letra in chave:
    if letra in "Aa": senha = senha + "!"
    elif letra in "Bb": senha = senha + "&"
    elif letra in "Cc": senha = senha + "3"
    elif letra in "Dd": senha = senha + "¢"
    elif letra in "Ee": senha = senha + "?"
    elif letra in "Ff": senha = senha + "1"
    elif letra in "Ii": senha = senha + "&"
    elif letra in "Mm": senha = senha + "%"
    elif letra in "Rr": senha = senha + "@"
    elif letra in "Ss": senha = senha + "7"
    elif letra in "Uu": senha = senha + "5"
    else: senha = senha + letra
print(senha)
