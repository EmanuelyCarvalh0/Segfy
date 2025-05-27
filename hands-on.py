# 1 atividade - Retorne os números impares

def numeros_impares(n):          # Chamada para definir os números impares
    return n // 2          # Vai realizar a divisão por 2, assim vai encontrar os números impares
print(numeros_impares(7))  # Vai contar os números impares até 7
print(numeros_impares(15))  # Vai contar os números impares até 15

print()

# 2 atividade - Determinar quais palavras são palíndromo:
def palindromo(s): # Compara se as palavras é igual de trás pra frente
    return s == s[::-1] #  Verifique se a palavra tem o mesmo significado de tras pra frente

# Definindo as palavras que quero utilizar no teste:
print(palindromo("setor"))  # Saída: False
print(palindromo("osso"))   # Saída: True

print()

# 3 atividade - Retorne os valores mínimos e máximos
def valormm(lst): # Para listar os números
    return max(lst), min(lst) # Chamada para verificar o valor minimo e máximo
maior, menor = valormm([4,6,2,1,9,63,-134,566]) # Listagem de números
print("Maior:", maior)
print("Menor:", menor)

print()

    # 4 atividade - Concatenando números
def concatenando(num):
    resultado = "" # Aqui criamos uma variavel para os resultados
    for d in str(num): # Transformando os números em texto
        resultado += str(int(d) ** 2) # Solicitando que os resultados fique ao quadrado
    return int(resultado)

# Informando números e resultado:
print(concatenando(9119))

print()

# 5 atividade - Filtrando amigos
def amigo_ou_inimigo(lst): # Chamada para listar os amigos
    return [name for name in lst if len(name) == 4] # Informando que temos amigos tem somente 4 letras no nome

# Teste e lista de nomes:
print(amigo_ou_inimigo(["João", "Augusto", "Pedro", "José"]))

print()

#  6 atividade - Criando as torres - revisar

def construir_torre(andares): # Chamada para contruir as estrelas
    torre = []  # Para guardar as linhas da torre
    for i in range(andares):
        espacos = ' ' * (andares - i - 1)  # Espaços antes e depois das estrelas
        estrelas = '*' * (2 * i + 1)       # Estrelas no meio
        linha = espacos + estrelas + espacos  # Monta a linha completa
        torre.append(linha)  # Adiciona a linha na torre
    return torre  # Retorna a torre completa (lista de linhas)

# Função que mostra e salva a torre em um arquivo
def salvar_torre(andares):
    torre = construir_torre(andares)  # Constrói a torre
    with open('torre.txt', 'w') as arquivo:  # Abre o arquivo para escrita
        for linha in torre:
            print(linha)  # Mostra a linha no terminal
            arquivo.write(linha + '\n')  # Salva a linha no arquivo

# Teste: cria uma torre com 6 andares
salvar_torre(3)
