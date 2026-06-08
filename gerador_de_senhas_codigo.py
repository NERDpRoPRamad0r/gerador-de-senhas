import random
legal =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

senha1 = ""

digitar = int(input("POR FAVOR, DIGITE COMO VAI SER O TAMANHO DA SUA SENHA"))

for i in range(digitar):
    senha1 += random.choice(legal)

print("senha criada:", senha1)
