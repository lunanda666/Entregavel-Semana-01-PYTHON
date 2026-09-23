valor_compra = float(input("Digite o valor da compra: "))   # recebe o valor da compra e transforma para número decimal
valor_pago = float(input("Digite o valor pago: "))  # recebe o valor que o cliente pagou

troco = valor_pago - valor_compra   # calcula o troco subtraindo o valor da compra do valor pago

print(f"Troco: R$ {troco:.2f}")     # mostra o troco com duas casas decimais