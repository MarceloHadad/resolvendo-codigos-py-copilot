# Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

word = input().strip().lower()
reversed_word = word[::-1]

if word == reversed_word:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")