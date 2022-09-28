salario = 0
salario = float(input("Qual o salário?"))
if salario <= 1900:
  print(f"Você terá que pagar 489.20 de imposto")
  print(f"Seu salário será {salario - 489.20}")
else:
  print("Erro!!!")