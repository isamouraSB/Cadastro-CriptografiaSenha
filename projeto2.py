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
16 = G
17 = H
18 = I
19 = J
20 = L
21 = M
22 = N
23 = O
24 = P
25 = Q
26 = R
27 = S
28 = T
29 = U
30 = V
31 = X
32 = Y
33 = Z

"""

chave = input("Digite a base da sua senha: ")

senha = ""
for letra in chave:
    if letra in "Aa": senha = senha + "!"
    elif letra in "Bb": senha = senha + "&"
    elif letra in "Cc": senha = senha + "12"
    elif letra in "Dd": senha = senha + "13"
    elif letra in "Ee": senha = senha + "4"
    elif letra in "Ff": senha = senha + "1"
    elif letra in "Gg": senha = senha + "6"
    elif letra in "Hh": senha = senha + "17"
    elif letra in "Ii": senha = senha + "18"
    elif letra in "Jj": senha = senha + "19"
    elif letra in "Ll": senha = senha + "20"
    elif letra in "Mm": senha = senha + "%"
    elif letra in "Nn": senha = senha + "¢"
    elif letra in "Oo": senha = senha + "23"
    elif letra in "Pp": senha = senha + "24"
    elif letra in "Qq": senha = senha + "2"
    elif letra in "Rr": senha = senha + "@"
    elif letra in "Ss": senha = senha + "7"
    elif letra in "Tt": senha = senha + "8"
    elif letra in "Uu": senha = senha + "5"
    elif letra in "Vv": senha = senha + "?"
    elif letra in "Xx": senha = senha + "§"
    elif letra in "Yy": senha = senha + "&"
    elif letra in "Zz": senha = senha + "3"
    else: senha = senha + letra
print(senha)
