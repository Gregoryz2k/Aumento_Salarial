salario = float(input("Digite seu salario: "))
porcentagem = float(input("Qual a porcentagem do aumento: "))

aumento = (salario * porcentagem / 100)
novo_salario = salario + aumento

print(f"O seu aumento foi de R${aumento:5.2f} e o seu novo salario é de R${novo_salario:5.2f}.")


