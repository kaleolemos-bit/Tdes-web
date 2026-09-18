#1
"""
num_por_ext = (
    'zero', 'um', 'dois', 'três', 'quatro',
    'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'quatorze',
    'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
    'vinte'
)

numero = int(input('Digite um numero entre 0 e 20: '))
if 0 <= numero <= 20:
    print(f'O nimero {numero} por extenso é: {num_por_ext[numero]}')
else:
    print('Digite um numero entre 0 e 20')
"""
#2
"""
lista = []
for i in range(10):
    valor = int(input("Digite um valor: "))
    lista.append(valor)

dif = set(lista)
print("Quantidade de valores diferentes: ", len(dif))
"""
#3
"""
lista = []
for i in range(4):
    valor = int(input("Digite um valor: "))
    lista.append(valor)

print("O valor 9 aparece", lista.count(9), "vezes.")

if 3 in lista:
    print("O primeiro 3 está na posição", lista.index(3))
else:
    print("O valor 3 não foi digitado.")

print("Numeros pares: ")

for valor in lista:
    if valor % 2 == 0:
        print(valor)
"""
#4
"""
import random

lista = []
for i in range(50):
    dado = random.randint(1, 6)
    lista.append(dado)

qtd_6 = lista.count(6)
perc = (qtd_6 / 50) * 100

print("Quantidade 6: ", qtd_6)
print("Percentual de 6: ", perc, "%")
"""
#5
"""
tradutor = {
    "casa": "house",
    "mesa": "table",
    "cachorro": "dog",
    "gato": "cat",
    "livro": "book",
    "água": "water"
}

palavra = input("Digite uma palavra: ").lower()
if palavra in tradutor:
    print("Tradução:", tradutor[palavra])
else:
    print("Que?")
"""
#6
"""
estoque = {}

while True:
    print("\n1 - Adicionar produto")
    print("2 - Atualizar quantidade")
    print("3 - Exibir estoque")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        produto = input("Digite o nome do produto: ")
        qtd = int(input("Digite a quantidade: "))

        estoque[produto] = qtd

    elif opcao == 2:
        produto = input("Digite o nome do produto: ")

        if produto in estoque:
            qtd = int(input("Digite a nova quantidade: "))
            estoque[produto] = qtd
        else:
            print("Produto não encontrado.")

    elif opcao == 3:
        print("\nEstoque:")

        for produto, qtd in estoque.items():
            print(produto, ":", qtd)

    elif opcao == 4:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
"""
#7
"""
idades = []
alturas = []

for i in range(5):
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))
    idades.append(idade)
    alturas.append(altura)
print("\nDados na ordem inversa:")

for i in range(4, -1, -1):
    print("Idade:", idades[i])
    print("Altura:", alturas[i])
"""
#8
"""
texto = input("Digite uma frase: ").lower()
alfabeto = {}

for letra in "abcdefghijklmnopqrstuvwxyz":
    alfabeto[letra] = 0

for letra in texto:
    if letra in alfabeto:
        alfabeto[letra] += 1

print(alfabeto)
"""
#9
"""
def cal_media(alunos):
    soma = 0

    for nota in alunos.values():
        soma += nota
    media = soma / len(alunos)
    return {"média": media}

alunos = {
    "Daniel": 8,
    "Kaleo": 7,
    "Pedro": 9,
    "Ana": 6
}

resultado = calcular_media(alunos)
print(resultado)
"""
#10
"""
texto = input("Digite uma frase: ").lower()
palavras = texto.split()

contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(contagem)
"""
#11
"""
def pos_neg(n):

    if n >= 0:
        print("Positivo")
    else:
        print("Negativo")

numero = int(input("Digite um número: "))
pos_neg(numero)
"""
#12
"""
def valor_abso(numero):

    if numero < 0:
        numero = numero * -1

    print(numero)

numero = float(input("Digite um número: "))
valor_abso(numero)
"""
#13
"""
def soma_maior(a, b, limite):

    if a + b > limite:
        return True
    else:
        return False

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
limite = int(input("Digite o limite: "))

resultado = soma_maior(a, b, limite)
print(resultado)
"""
#14
"""
def somaImp(taxaImp, custo):

    imposto = custo * (taxaImp / 100)

    custo = custo + imposto

    return custo

taxa = float(input("Digite a taxa de imposto (%): "))
custo = float(input("Digite o custo do produto: "))

novo_custo = somaImp(taxa, custo)
print("Custo com imposto:", novo_custo)
"""
#15
"""
def qtd_digitos(numero):

    numero = abs(numero)

    return len(str(numero))

numero = int(input("Digite um numero inteiro: "))
resultado = qtd_digitos(numero)
print("Quantidade de dígitos:", resultado)
"""
