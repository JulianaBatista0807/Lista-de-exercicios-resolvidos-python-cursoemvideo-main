produto = float(input("Digite o preço do produto: "))
aplicando_desconto = (produto * 5/100)
novo_preco = produto - aplicando_desconto
print("O produto com o desconto de 5% é: {:.2f}".format(novo_preco))
