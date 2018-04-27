
# coding: utf-8

# In[29]:

n1 = int(input("Digite o n1: "))
n2 = int(input("Digite o n2: "))
n3 = int(input("Digite o n3: "))

if (n1 > n2) and (n1 > n3):
    if (n2 > n3):
        print(n3, n2, n1)
    else:
        print(n2, n3, n1)
elif (n2 > n1) and (n2 > n3):
    if (n1 > n3):
        print(n3, n1, n2)
    else:
        print(n1, n3, n2)
elif (n3 > n1) and (n3 > n2):
    if (n1 > n2):
        print(n2, n1, n3)
    else:
        print(n1, n2, n3)


# In[30]:

a = 10
while a == 10:
    print(a)
    a = 11


# In[31]:

lista = [1,2,3]
n = len(lista)-1
while (n != -1):
    print(lista[n])
    n=n-1


# In[32]:

produtos = ['ipad','celular','notebook', 'tv']
for item in produtos:
    print(item)


# In[36]:

produtos = ['ipad','celular','notebook', 'tv', 10]
for item in produtos:
    print(item)


# In[37]:

produtos.append([True, False])
for item in produtos:
    print(item)


# In[38]:

for i in range(5):
    print(i)


# In[39]:

for i in range(len(produtos)):
    print(i)


# In[40]:

for i in range(len(produtos)):
    print(produtos[i])


# In[44]:

for i in range(len(produtos)):
    print(i)
    print(produtos[i])


# In[50]:

texto = "Estou programando em Python"
for i in range(len(texto)):
    print(texto[i])


# In[48]:

for i in range(len(texto)):
    print(i, end=' ')


# In[51]:

for i in range(len(texto)):
    print(i, texto[i])


# In[52]:

list(range(5))


# In[53]:

list(range(1,5))


# In[62]:

list(range(1,40,2))


# In[72]:

list(range(1,60,3))


# In[75]:

list(range(1,70,4))


# In[76]:

list(range(1,90,5))


# In[81]:

print("Exercicio #1")
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
anoAtual = 2018
anoNascimento = anoAtual - idade
calculoIdade = anoNascimento + 100
print(nome + ", você irá fazer 100 anos em ", calculoIdade)


# In[84]:

print("Exercicio #2")
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
qtd = int(input("Quantas vezes você gostaria de imprimir a mensagem? "))
anoAtual = 2018
anoNascimento = anoAtual - idade
calculoIdade = anoNascimento + 100
while (qtd !=0):
    print(nome + ", você irá fazer 100 anos em ", calculoIdade)
    qtd = qtd -1


# In[92]:

print("Exercicio #3")
n = int(input("Digite um numero: "))
if (n%2 == 0):
    print("Numero Par")
else:
    print("Numero Impar")


# In[117]:

print("Exercicio #4")
numeros = [4,5,6,7,8,-3,9,-4]
for i in range(len(numeros)):
    if (numeros[i] < 0):
        print(numeros[i])


# In[110]:

print("Exercicio #5")
list(range(0,101,2))


# In[109]:

print("Exercicio #5")
for i in range(101):
    if (i%2 == 0):
        print(i)


# In[176]:

print("Exercicio #6-a")
lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in range(len(lst)):
    if (lst[i] < 6):
        print(lst[i])


# In[2]:

print("Exercicio #6-a")
lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for item in lst:
    if item <= 5:
        print(item)


# In[66]:

print("Exercicio #6-b")
lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
novaLst = []
for item in lst:
    if item <= 5:
        novaLst.append(item)
print(novaLst)


# In[70]:

lista1 = [1, 2, 3]
lista1.append([4, 5])
print ("append: ",lista1)
# resultado: [1, 2, 3, [4, 5]]

lista2 = [1, 2, 3]
lista2.extend([4, 5])
print ("extend: ", lista2)
# resultado: [1, 2, 3, 4, 5]

lista3 = [1, 2, 3]
lista3.append(4)
print (lista3)


# In[71]:

print("Exercicio #6-c")
n = int(input("Digite um numero: "))
lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
novaLst = []
for item in lst:
    if item <= n:
        novaLst.append(item)
print(novaLst)


# In[5]:

print("Exercicio #7")
aparelhos = ['iphone', 'pc', 'notebook', 'monitor', 'impressora']       
for i, item in enumerate(aparelhos):
    print(i+1, item)
    print(' ')


# In[232]:

print("Exercicio #7")
aparelhos = ['iphone', 'pc', 'notebook', 'monitor', 'impressora']       
for i in range(len(aparelhos)):
    print(i+1, aparelhos[i])
    print(' ')


# In[98]:

print("Exercicio #8-a")
l1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
novaLst = []
for i in range(len(l1)):
    for j in range(len(l2)):
        if (l1[i] == l2[j]) and (l1[i] != l1[i-1]) and (l2[j] != l2[j-1]):
                novaLst.append(l1[i])
print(novaLst)


# In[99]:

print("Exercicio #8-b")
l1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 101, 121, 130, 150]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 34, 55, 89, 121, 150, 190, 300, 555, 999]
novaLst = []
for item in (l2):
        if item in (l1) and item not in novaLst:
            novaLst.append(item)
print(novaLst)


# In[82]:

print("Exercicio #9")
frase = input("Digite uma frase: ")
dict = {'MAIUSCULA': 0, 'minusculas': 0}
for i in range(len(frase)):
    str = frase[i]
    if (str.isupper()):
        dict['MAIUSCULA'] = dict['MAIUSCULA'] + 1
    elif (str.islower()):
        dict['minusculas'] = dict['minusculas'] + 1
print("Quantidade de letras MAIÚSCULA: ", dict['MAIUSCULA'])
print("Quantidade de letras minúsculas: ", dict['minusculas'])


# In[12]:

palavras = {
    'big' : 182,
    'data' : 342,
    'python' : 423
}
print("A palavra python apareceu", palavras['python'], "vezes")

print("As palavras big, data e python apareceram", palavras['big'] + palavras['data'] + palavras['python'], "vezes")


# In[298]:

print("Exercicio #EP0")
n = (input("Digite um numero inteiro (entre 0 e 10000): "))
num = int(n)
if (num > 10000):
    n = (input("Digite um numero inteiro menor que 10000): "))
    num = int(n)
if (num < 0):
    n = (input("Digite um numero inteiro maior que -1): "))
    num = int(n)
if (num > -1) and (num < 10001):    
    if n == '0':
        print('o número zero possui 0 dígito')
    else: 
        digito = len(n)
        print('o número ', n ,' possui ', digito , ' dígitos')


# In[300]:

print("Cálculo dos quadrados de uma sequencia de números.")
print("A sequencia termina com um 0 (zero).\n")

num = int(input("Digite um número: "))
while num != 0:
    quadrado = num * num
    print(num, "ao quadrado é", quadrado)
    num = int(input("Digite um número: "))


# In[ ]:



