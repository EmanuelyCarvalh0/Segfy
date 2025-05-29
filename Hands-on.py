def oddCount(n):
    return n//2
print('A quantidade de números impares até 7, é:', oddCount(7))
print('A quantidade de números impares até 15 é:', oddCount(15))

print()

def isPalindrome(s):
    return s == s[::-1]
print('A palavra setor é um palíndromo?', isPalindrome('setor'))
print('A palavra osso é um palíndromo?', isPalindrome('osso'))

print()

def mm(lst):
    return max(lst), min(lst)
num= [
    [4, 6, 2, 1, 9, 63, -134, 566],
    [-52, 56, 30, 29, -54, 0, -110],
    [42, 54, 65, 87, 0],
    [5]
]
for l in num:
    maior, menor = mm(l)
    print(f'O maior número é {maior} e o menor é: {menor}')

print()

def squase(num):
    resultado = ''
    for i in str(num):
        resultado += str(int(i)**2)
    return resultado
print('O resultado é:',(squase(1212)))
print('O resultado é',(squase(2345)))

print()

def friendOrFoe(lst):
    return','.join([name for name in lst if len(name) == 4])
print(friendOrFoe(['João', 'Augusto', 'Pedro', 'José']))
print(friendOrFoe(['Augusto', 'Pedro', 'Gustavo', 'Raí']))
print(friendOrFoe(['Mari']))

print()


def torre(andares):
    largura_base = andares * 2 - 1

    with open('torre.txt', 'w') as arquivo:
        for i in range(1, andares * 2, 2):
            linha = '*' * i
            linha = linha.center(largura_base)
            print(linha)
            arquivo.write(linha + '\n')

torre(3)
print()
torre(6)
