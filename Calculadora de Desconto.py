preco = float(input())  # recebe o preço do produto

desconto = float(input())  # recebe o percentual de desconto

valor_desconto = preco * (desconto / 100)  # calcula quanto será descontado

preco_final = preco - valor_desconto  # tira o desconto do preço original

print(f"{preco_final:.2f}")  # mostra o preço final com duas casas decimais