print("Aula inicial")

"""
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos que estão dentro de aspas
Strings colocados em aspas simples/duplas/escape
Simple: 
print('Texto escrito')

Duplas:
print("Texto escrito")

Escape: Interpretador pula o proximo carater e le oque esta na frente
print("Texto \" escrito")

r: para apararecer o carater de escape
print(r"Texto \" escrito"")

Texto com aspas simplex e duplas:
print(2,'Texto "escrito"')
"""

print("Aula Sobre int e float")

"""
Tipos int e float
#Int são numeros inteiros, sem virgula ou ponto
print(11)
print(-11)
print(0)

#Float são numeros com casas decimais;
print(11.10, 1.1)
print(-11.10)
print(0.90, -0.90)

#A função type mostra o tipo que o Python inferiu ao valor:
Ex:
print(type())
"""

"""
print(type(-1))
print(type(0.90))
print(type('batman'))
"""

"""
Tipo boolean só possui dois valores True or False;
Existe vários operadores para "questionar", dentre eles temos
0 ==, que é um operador lógico que questiona se um valor é igual a outro;
"""
"""
Ex:
print(10 == 10)
print(10 == 11)
"""
print("Conversão, coerção, convertion, typecasting, coercion")

"""
Conversão de tipos de dados ou coerção;
Tipos imutáveis e primitivos;
Str, int, float, bool
Ex:
print(int('1') + 1)
print(float('1.1') + 1)
print(str('1') + 'a')
print(str('1') =='a')
print(bool(''))
"""

print("Variaveis")

"""
Váriaveis são usadas para salvar algo na memória do computador;
Incie as variaveis com letra minusculas, pode usar
numero e ubderline _;
O sinal de = é o operador de atribuição;
Usado para atribuir um valor a uma váriavel;
Ex:
nome_completo = 'Bruce Wayne';
soma_dois_mais_dois = 2 + 2;
int_um = int('1')
print(int_um, type(int_um), nome_completo, soma_dois_mais_dois)

nome = 'Bruce'
idade = 30
maior_de_idades = idade >= 18
print("Nome:", nome, "Idade:", idade)
print("É maior?", maior_de_idade)
"""

print("Operadores aritméticos")
"""
adicao = 10 + 10
print('Adição', adicao)

subtracao = 10.5 - 5.4
print("Subtração", subtracao)

multiplicacao = 15 * 10.5
print("multiplicação", multiplicacao)

divisao = 10 / 2.2
print("Divisão", divisao)

divisao_inteira = 10 // 2.5
retira as casas decimais
print("Divisao_Inteira", divisao_inteira)

exponenciacao = 2 ** 10
print("Exponenciação", exponenciacao)

modulo = 25 % 5
print("Modulo", modulo)
"""

"""
concatenacao = 'A' + 'B' + 'C'
print(concatenacao)

a_dez_vezes = 'A' * 10
tres_vezes_luiz = 3 * 'Luiz'
print(a_dez_vezes)
print(tres_vezes_luiz)
"""

"""
Precendencia ordem:
1.(n+n)
2. **
3. * / // %
4. + -
"""
"""
print("Exercicio IMC")
nome = 'Vinicius'
altura = 1.83
peso = 70
imc = peso / (altura * altura)
print(nome)
print("Imc", imc)
"""

"""
Formatação de String
linha_' = f'{nome} tem {altura:.2f} de altura';
Utilizando o format;
.format();
Ex:
formato = 'a={} b={}'.formay(a, b, c)
Python trata tudo como objetos
"""

"""
Utilizando o input para coletar dados
Ex:
nome = input('Qual o seu nome')
numero_1 = int(input('Digite um numero: '))
int_numero_1 = int(numero_1)
"""

"""
# if / elif / else
#se / se não se / se não

entrada = input('Vocer quer "entrar" ou "sair"?')

if entrada == 'entrar':
    print('Voce entrou no sistema')
elif entrada == 'sair':
    print('Voce saiu')
else:
    print('Não digitou nada)

elif e else depende do if, depois do if utiliza o elif e apos usar o elif, utiliza o else
"""


"""
Operadores de comparação:
>    Maior   2 > 1
>=   Maior ou igual   2 >= 2
<    Menor             1 < 2
<=   Menor ou igual    2 <=
==   Igual             'a' == 'a'
!=   Diferente         'a' != 'b'
"""
"""
print('Exercicio')

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor} é maior que {segundo_valor}')
elif segundo_valor > primeiro_valor:
    print(f'{segundo_valor} é maior que {primeiro_valor}')
else:
    print('Os valores são iguais')

"""
"""
Operadores lógicos

and(e) or (ou) not (não);

and: Todas as condições precisam ser verdadeiras
Se qualquer valor for considerado falso,
a expressão inteira será avaliada naquele valor;
São considerados falsy
0 0. 0 '' False
Tambem existe o tipo None que é
usado para representar um não valor

or: Caso a primeira condição seja verdadeira
ela avalia toda a função como verdadeira;

not: é usado para inverter expressões
not True = False
not False = True

Operadores in e not in
String são iteráveis
0 1 2 3 4 5
O t á v i o
-6-5-4-3-2-1
"""

"""
Interpolação entre String
s - String
d e i - int
x e x - Hexadecimal (ABCDEF0123456789)
f - float
Ex:
nome = 'Luiz'
preco = 1000.95789
variavel = '%s, o preço é R$%f' % (nome, preco)
print(variavel)
"""

"""
F-String
s -  string
d - int;
f - float;
x ou X hexadecimal
(Caractere)(><) (quantidade);
> esquerda;
< direita
 centro;
 Sinal - + ou -
 Ex.: 0 > -100, .1f;
 Conversion Flags - !r !s !a
 variavel = 'ABC'
 print(f'{variavel}');
print(f'{variavel: > 10}')
print(f'{variavel: < 10}')
print(f'{variavel}')
print(f'{1000.4874656347:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
"""

"""
Fatiamento de Strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd
de caracteres da str
variavel = 'Ola mundo'
print(variavel[4:8])
"""
"""
nome_nome = input('Digite seu nome:')
idade_idade = input('Digite a idade:')
if nome_nome and idade_idade :
    print('Seu nome eh: %s' % (nome_nome))
    print(nome_nome[::-1])
    print(nome_nome[0:1])
    print(nome_nome[7:8])
    if ' ' in nome_nome:
    print('Contem espaços')
    else:
    print('Não contem')
    print(f'Seu nome tem {len(nome)} letras')
else:
    print('Desculpe, você deixou os campos vazios')
"""

"""
Try/Except;
try -> tenta executar o código;
except -> ocorreu algum erro ao tentar executar;

try:
    numero_float = float(numero_str)
    print('Float:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f})
    print(f'O dobrp de {numero_str} é {numero_float * 2:.2f})
except:
print('Isso não é um número')
"""

"""
Constante = "Variáveis" que não mudam
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)

velocidade = 61;
local_carro = 90;
Constantes escrever em maisuculo:
RADAR_1 = 60;
LOCAL_1 = 100;
RADAR_RANGE = 1;

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 + RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_multado_radar_1 and velocidade > RADAR_1

if vel_carro_pass_radar_1:
    print('Velocidade passou do radar 1')

if carro_passou_radar 1:
    print('Carro passou radar 1')

if carro_multado_radar_1: 
    print('Carro multado em radar 1')
"""

"""
id - identidade
Localizar o valor que esta na memoria
v1 = 'a'
print(id(v1))
"""

"""
Flags, is, is not e None:
Saber se o interpretador passou em um determinado local
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade

condicao  = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
"""
"""
print('Exercicio')
#Utilizando isDigit tambem
entrada = input('Digite um numero: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
         par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')

else:
    print('Você não digitou um número inteiro')
"""



"""
numero_int = input('Digite um numero: ')
try:
    valor = int(numero_int)
    print("Numero é inteiro")
    if valor % 2 == 0:
        print('Numero é par')
    else:
        print('Numero não é par')
except:
    print('Numero não é inteiro')
"""

"""
print('Exercicio dois')
horario = input('Horario:')
try:
    relogio = int(horario)
    if relogio >= 0 and relogio <= 11:
        print('Bom dia')
    elif relogio >= 12 and relogio <= 17:
        print('Boa tarde')
    elif relogio >= 18 and relogio <= 23:
        print('Boa noite')
except:
    print('Digite numeros inteiros')

print('Exercicio')
nome = input('Digite seu nome:')
tamanho_nome = len(nome)
if tamanho_nome <= 4 and tamanho_nome > 1:
    print('Seu nome é curto')
elif tamanho_nome <= 5 and tamanho_nome >= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
"""

"""
Repetições com while;
Executa uma ação enquanto uma condição é verdadeira
Operadores de atribuição:
= += -= *= /= //= **= %=

contador = 0

while contador < 10:
    nome = input('Qual seu nome:')
    print(f'Seu nome é:{nome}')
    contador += 1
    if contador == 6:
        print('Não vou mostrar o 6')
        continue
    print(contadaor)

Continue serve para pular uma etapa do laço da repetição



qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while continua <= qtd_colunas:
    print(f'{linha=}{coluna=}')
        coluna += 1
    linha += 1

print('Acabou')
"""
"""
print('Exercicio while')
nome = 'Vinicius' #iteráveis
indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1   
print(novo_nome) 
""" 
"""   
print('Calculadora com while')
while True:
    primeiro_numero = input("Digite o numero: ")
    segundo_numero = input("Digite o segundo: ")
    operador = input('Digite o Operador:')
    operador_permitido = '+-/*'
    numero_validos = None
    numero_1_float = 0
    numero_2_float = 0
    try:
        numero_1_float = float(primeiro_numero)
        numero_2_float = float(segundo_numero)
        numero_validos = True
    except:
        numero_validos = None

        if numero_validos is None:
            print('Um ou ambos não são validos')
            continue
    
    if operador not in operador_permitido:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um')
        continue

    if operador == '+':
            print(f'Resultado é: {numero_1_float + numero_2_float}')
    elif operador == '-':
            print(f'Resultado é: {numero_1_float - numero_2_float}')
    elif operador == '/':
            print(f'Resultado é: {numero_1_float / numero_2_float}')
    elif operador == '*':
            print(f'Resultado é: {numero_1_float * numero_2_float}')
    
    sair = input("Quer sair? [s]im:").lower().startswith('s')
    if sair is True:
        break
"""
"""
while/else
Especifico para python
string = 'valor qualquer'
i = 0
while i < len(string):
    letra = string[i]
    print(letra)
    i += 1
else:
    print('O else foi executado')
print('Fora do while')
"""
"""
Utiliza o while quando não sabemos quantas repitoções o codigo vai ter, assim utilizamos o for 
quando sabemos quantas repetições vão acontecer.
"""
"""
texto = 'Python'
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto)
"""
"""
For + Range
range -> range(start, stop, step)
Ela não depende do for e o for não depende dela
"""
#exemplo tenho numeros que iniciam em 5 vão ate 10 e pulam de 2 em 2
#numeros = range(5,10, 2)
#O while tinha pegar o indice para entrar dentro da variavel numeros e atraves do indice procurar o valor, ja o for ja faz isso, pegando o valor
#especificamente
"""
numeros = range(0, -10, -3)

for numero in numeros:
    print(numero)
"""

"""
import os

palavra_secreta = 'batman'
letras_acertadas = ''
numero_de_tentativas = 0
while True:
    letra_digitada = input('Digite uma letra:')
    numero_de_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('Você ganhou parabens')
        print('a palavra era:', palavra_formada)
        print('Tentativas:', numero_de_tentativas)
        letras_acertadas = ''
        numero_de_tentativas = 0
"""

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - índices e fatiamento
Métodos úteis: 
append - Adiciona um item ao final
insert - Adiciona um item no índice ecolhido
pop - Remove do final ou do índice ecolhido
del - Apaga um índice
clear - limpa a lista
extend - estende a lista
+ - concatena listas
Create Read Update Delete

A sua declaração é o nome = list()
lista = list()
ou
lista = [123, True, 'Luiz Otávio, 1.2, []]
lista[2] = False
del lista[2]
lista.append(50)
lista.pop()
ou
lista.pop(2)
del lista[4]
lista.clear()
lista.insert(0, 20)
print(lista[2])
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
"""

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

""""
for in com listas
lista = ['Maria', 'Helena', 'Luiz']

for nome in lista:
print(nome, type(nome))
"""
"""
print("Exercicio de lista")

lista = ['Maria', 'Helena', 'Luiz']
for nome in lista:
    print(lista.index(nome))

print('Outra resolução')
lista = ['Maria', 'Helena', 'Luiz']
indices = range(len(lista))
for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
"""

"""
Introdução ao desempacotamento + tuples (tuplas)
Todos os iteraveis é possivel fazer o desempacotamento, retirar os valores com váriaveis.
Colocar virgula dos lados das váreis, como no exemplo:
nomes: ['Batman', 'Superman', 'WW']
nome1, nome2, nome3 = nomes
Caso queira pegar apenas um valor, é necesário criar uma variável de 
empacotamento, para os restos dos valores, exemplo
nome1, *resto = ['batman', 'Superman', 'WW']
print(nome1, resto)
Quando não se utiliza o resto, nomeia a variavel como *-
"""

"""
Tuplas são listas imutáveis
Utilizamos quando não queremos alterar a lista, sem remover ou adicionar
ou seja se manter.
A lista carrega métodos que permitem alterações.
Para criar uma tupla tem duas formas, uma delas é não colocar []
ou pode se utilizar o ();
Para converter, pode se utilizar
nomes = tuple(nomes)
O mesmo vale para mudar pra lista
nomes = list(nomes)
"""

"""
Enumarate - enumera iteráveis (índices)
Pode se criar uma lista enumerada:
lista_enumerada = enumare(lista)
Pode se receber qualquer iterável, chamador de iterator
print(next(lista_enumerada))
list_enumerada = list(enumerate(lista))
for tupla_enumerada in enumerate(lista):
    for valor in tupla_enumerada:
        print(valor)

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])
"""
"""
import os

print('Exercicio sobre listas')

lista_compras = []
valor = ''
indice = 0
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar:')
    if opcao == 'i':
        os.systtem('clear')
        valor = input('Digite oque vai ser adicionado:')
        lista_compras.append(valor)

    elif opcao == 'l':
        if len(lista_compras) == 0:
            print('Nada a listar')
        for i, valor in enumerate(lista_compras):
             print(i, valor)

    elif opcao == 'a':  
        try:
            indice = int(input('Escolha o indice para apagar:'))
            del lista_compras[indice]  
        except ValueError:
            print('Não foi possivel apagar esse indice')  
        except IndexError:
            print('Indice não existe na lita')           
"""
"""
Imprecisão de ponto flutuante
import decimal (usar uma classe interna chamada Decimal)

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 3))
"""

"""
Métodos de str para utilizar em textos e envolve listas tambem;

split e join com list e str
split - divide uma string
join - une uma string

frase = 'Olha só que, coisa interessante'
lista_frases_cruas = frase.split(',')
lista_frases=[]
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

frase_unidas = '-'.join(lista_frases)
print(frases_unidas)
"""

"""
Listas de listas e seus índices;

salas = [['Maria', 'Helena',],
        ['Elaine',],
        ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)]
]
print(salaas[1][0])
print(salas[2][3][2])
for sala in salas:
    print(f'A sala é{sala}')
    for aluno in sala:
        print(aluno)     
"""
"""
Desempacotamento em chamadas 
de métodos e funções
É possivel pegar o primeiro e o ultimo elemento de uma lista 
ou o antepenultimo da seguinte fonma
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3 'Eduarda']
tuplas = 'Python', 'é', 'legal'
salas = [['Maria', 'Helena',],
        ['Elaine',],
        ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)]
]
p, b, *_, ap, u = lista
print(p, u, ap)

print(nome, end=' ', sep=' ')
print(*lista)
print(*string)
print(*slas, end='\n')
print(*slas, sep='\n')
"""

"""
Operação ternária (Condicional de uma linha)
<valor> if <condicao> else <outro valor>
Operadores ou operação ternária significa basicamente um if else em 
uma linha só;
condicao = 10 == 10
variavel = 'Valor' if condicao else 'Outro valor'
print(varivavel)

digito = 9
novo_digito = digito if digito <= 9 else 0
novo_digito_dois = 0 if digito > 9 else digito
"""


