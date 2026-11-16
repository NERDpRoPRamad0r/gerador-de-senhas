# Bibliotecas
import random
import pyttsx3 as pyt

# Variavel que vai ser o pyttsx3
engine = pyt.init()

# Caracteres para a senha
SENHA_CARACTERES =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" 

# Aonde vai ser armazenado a senha
propria_senha = ""

# Para o computador falar pros necessitados
engine.say("POR FAVOR, DIGITE O TAMANHO DA SUA SENHA")
engine.runAndWait()

# Local para digitar ocomprimento da senha
digitar = int(input("DIGITAR"))

# Looping for para fazer o comprimento da senha que o cliente quer
for i in range(digitar):
    propria_senha += random.choice(SENHA_CARACTERES)

# Print para mostrar como ficou a senha
print("senha criada:", propria_senha)
