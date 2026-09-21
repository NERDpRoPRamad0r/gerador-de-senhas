import random
legal =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
senhas = []
senha1 = ""
quantidade = 0
print("bem vindo ao gerador de senhas")

while quantidade <= 5:
    digite = input("digite 1 para criar e escolher o tamanho de sua senha, digite 2 para ver todas as suas senhas")
    if digite.lower() == "1":
        digitar = int(input("POR FAVOR, DIGITE COMO VAI SER O TAMANHO DA SUA SENHA"))
        for i in range(digitar):
            senha1 += random.choice(legal)
        
        senhas.append(senha1)
        print("senha criada:", senha1)
        quantidade += 1
    elif digite.lower() == "2":
        print(f"suas senhas:{senhas}")
