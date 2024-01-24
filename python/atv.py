def class_produto(produto, preco):
    if preco < 50:
        clas = 1
    elif preco >= 50 and preco <= 100:
        clas = 2
    elif preco  > 100:
        clas = 3
    else:
        print("Digite um valor valido")
        clas = 0     

    if clas == 1:
        tipo = "Baixo"
        print(f"A classificação do produto: {produto} com valor de {preco} é de {tipo}")
        
    elif clas == 2:
        tipo = "Médio"
        print(f"A classificação do produto: {produto} com valor de {preco} é de {tipo}")

    elif clas == 3:
        tipo = "Alto"
        print(f"A classificação do produto: {produto} com valor de {preco} é de {tipo}")


produto = str(input("Qual o seu produto? "))
preco = int(input("Qual o preço do seu produto? "))

class_produto(produto, preco)