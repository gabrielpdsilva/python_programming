import random

#funcao que retorna a string gerada aleatoriamente
def randomString(tamanhoString):
    #caracteres possiveis utilizados para a gerar a senha
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#@%"
    return ''.join(random.choice(letras) for i in range(tamanhoString))

print(
"""
    **********************************
    ******GERADOR DE SENHA FORTE******
    **********************************

> Defina o tamanho da sua senha. Um arquivo .txt sera criado, junto com a senha gerada.
>Tamanho min. predefinido: 6 caracteres.
> Tamanho max. predefinido: 100 caracteres.
"""
)

tamanhoString = 0
try:
    while (tamanhoString > 100 or tamanhoString < 6):
        tamanhoString = int(input("Digite aqui o tamanho: "))

        if(tamanhoString > 100):
            print("O valor nao pode ser maior que 100.")
        elif(tamanhoString < 6):
            print("O valor nao pode ser menor que 6.")

    nova_senha = open('senhaGerada.txt', 'w') # 'w' permite que, caso nao exista um arquivo.txt, um novo será criado
    nova_senha.write(randomString(tamanhoString))
    nova_senha.close()

    print("""
    ==============================
    ===SENHA GERADA COM SUCESSO===
    ==============================
    """)

except Exception as erro:
    print("\nNao foi possivel gerar uma senha pelo seguinte erro:\n", erro,"\n")

input("Aperte ENTER para sair.")
