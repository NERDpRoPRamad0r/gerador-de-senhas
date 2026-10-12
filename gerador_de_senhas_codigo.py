import random
import pyttsx3 as pyt

engine = pyt.init()
legal =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

senha1 = ""

engine.say("POR FAVOR, DIGITE O TAMANHO DA SUA SENHA")
engine.runAndWait()
digitar = int(input("DIGITAR"))

for i in range(digitar):
    senha1 += random.choice(legal)

print("senha criada:", senha1)
